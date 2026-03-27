# 🔐 Smart File Vault — AWS Serverless File Management System

## 📌 Problem Statement
Organizations struggle with untracked file uploads, no audit trails, and high server costs for storage systems.

## ✅ Solution
A fully serverless file management system that automatically logs, validates, and alerts on every file upload — with zero server management.

## 🏗️ Architecture
S3 → Lambda → DynamoDB + SNS + CloudWatch

## ⚙️ AWS Services Used
| Service | Purpose |
|---------|---------|
| Amazon S3 | File storage with versioning |
| AWS Lambda | Auto-triggered file processor (Python) |
| Amazon DynamoDB | Audit log of every upload |
| Amazon SNS | Real-time email alerts |
| Amazon CloudWatch | Execution logs & monitoring |

## 🚀 How It Works
1. User uploads a file to S3 `uploads/` folder
2. Lambda function triggers automatically
3. File metadata is logged to DynamoDB
4. Email alert sent via SNS
5. All logs stored in CloudWatch

## 📊 File Types Supported
PDF, PNG, JPG, JPEG, TXT, CSV, DOCX

## 👨‍💻 Author
Dnyanesh Kamdi — Cloud Computing Enthusiast
AWS Certified | Walchand College of Engineering, Sangli
