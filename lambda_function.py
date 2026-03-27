import json
import boto3
import urllib.parse
from datetime import datetime

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
sns = boto3.client('sns')

SNS_TOPIC_ARN = 'arn:aws:sns:ap-south-1:720472223406:SmartFileVaultAlerts'
DYNAMODB_TABLE = 'FileUploadLogs'

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
    size = event['Records'][0]['s3']['object']['size']

    file_extension = key.split('.')[-1].upper() if '.' in key else 'UNKNOWN'
    allowed_types = ['PDF', 'PNG', 'JPG', 'JPEG', 'TXT', 'CSV', 'DOCX']
    status = 'ALLOWED' if file_extension in allowed_types else 'FLAGGED'
    timestamp = datetime.utcnow().isoformat()

    print(f'File: {key} | Size: {size} bytes | Type: {file_extension} | Status: {status}')

    table = dynamodb.Table(DYNAMODB_TABLE)
    table.put_item(Item={
        'file_name': key,
        'bucket': bucket,
        'size_bytes': size,
        'file_type': file_extension,
        'status': status,
        'timestamp': timestamp
    })

    message = f'''
Smart File Vault Alert
======================
File Name : {key}
Bucket    : {bucket}
Size      : {size} bytes ({round(size/1024, 2)} KB)
Type      : {file_extension}
Status    : {status}
Time      : {timestamp} UTC
'''

    sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Subject=f'[Smart File Vault] New Upload: {key}',
        Message=message
    )

    return {'statusCode': 200, 'body': json.dumps('Processed successfully')}
