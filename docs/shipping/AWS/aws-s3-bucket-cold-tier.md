---
id: AWS-S3-Bucket-cold-tier
title: AWS S3 Bucket (cold tier)
overview: This integration transfers archived logs from an "external-archive" S3 bucket to a "cold-tier" S3 bucket using S3 Batch Operations for management and AWS Lambda for renaming due to differing naming conventions.
product: ['logs']
os: ['windows', 'linux']
filters: ['AWS', 'Data Store', 'Other', 'Most Popular']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/aws-s3.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---

This integration transfers archived logs from the "external-archive" S3 bucket to the "cold-tier" S3 bucket. It recommends using S3 Batch Operations for efficient management of the copy process, including features like retries and copy reports. Additionally, it suggests employing AWS Lambda for dynamic file renaming, addressing the differing naming conventions between the two storage tiers.

## Logz.io side (Cold-Tier side)

### Prepare AWS Lambda

Ensure AWS Lambda is set up in every region used.

:::importnat
S3 Batch Operations can only be created in the same region as the destination bucket and can only call AWS Lambda in the same region.

Example Lambda for reference: `arn:aws:lambda:eu-west-2:<YOUR-ACCOUNT-ID>:function:RenameS3ObjectFromArchiveToColdTierFormat`

Create IAM Policy similar to `LambdaBatchOperationPermissions`.
:::

### Create or edit IAM role

Modify or create the IAM role `BatchOperationsDestinationRoleCOPY`. Base this on the S3 Batch Operations trust policy, which includes permissions for various S3 and Lambda actions:

```json
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Sid": "BatchOperationsLambdaPolicy",
			"Effect": "Allow",
			"Action": [
				"s3:PutObject",
				"s3:PutObjectVersionAcl",
				"s3:PutObjectAcl",
				"s3:PutObjectVersionTagging",
				"s3:PutObjectTagging",
				"s3:GetObject",
				"s3:GetObjectVersion",
				"s3:GetObjectAcl",
				"s3:GetObjectTagging",
				"s3:GetObjectVersionAcl",
				"s3:GetObjectVersionTagging",
				"s3:ListBucket",
				"lambda:InvokeFunction"
			],
			"Resource": "*"
		}
	]
}
```

### Obtain the manifest file

Get the manifest file with the list of files to be transferred.

### Create S3 Batch operations job

Create the S3 Batch Operations Job:
- In the **Operation type**, select **Invoke AWS Lambda function**. 
- In the **Permissions** section, include `BatchOperationsDestinationRoleCOPY`.

After creation, run the job.

## Your side (external archive side)

```note
The file copying procedure may exhibit variations based on several aspects, including the utilization of CSV files or inventory reports, and the specific locations of these files.

To streamline the process, it is advisable to store either the CSV file or the inventory report within the external archive bucket.
```

### File Preparation

Store a CSV file or inventory report in the external archive bucket.

Prepare the manifest with a list of files to move, either as a CSV file or an S3 inventory report.

#### CSV file

The CSV file can be strctured as follows:

```csv
archive,221101/1_221101T000103_8Uqyy3qeU6Xj3unh.log.gz
archive,221102/1_221102T000109_XQIBEH1OlPjjuQe7.log.gz
archive,221103/1_221103T000816_P4jGW9wFSK84IjBG.log.gz
```

#### S3 inventory report

Prepare an S3 inventory report listing the files to be transferred from the external-archive bucket to the cold-tier bucket. Detailed guidance on this process is available [here](https://docs.aws.amazon.com/AmazonS3/latest/userguide/configure-inventory.html). We recommend a straightforward approach to avoid encryption and use only CSV or JSON formats. For an overview of the report's purpose and its application, refer to the information provided [here](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-create-job.html#specify-batchjob-manifest).

### Send the manifest file

Send the manifest file to Logz.io, for example, using a download link. This avoids the need to create additional users and set more IAM policies.

### Set bucket policy

Go to **S3 > Buckets > `<YOUR-BUCKET-NAME>` > Permissions > Bucket Policy** and specify a bucket policy for the external archive bucket, allowing AWS Lambda to read and rename files:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowBatchOperationsSourceObjectCOPY",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::<YOUR-LOGZIO-ACCOUNT>:role/service-role/LambdaBatchOperationPermissions"
            },
            "Action": [
                "s3:GetObject",
                "s3:GetObjectVersion",
                "s3:GetObjectAcl",
                "s3:GetObjectTagging",
                "s3:GetObjectVersionAcl",
                "s3:GetObjectVersionTagging",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::<Customers External Archive Bucket Name>/*",
                "arn:aws:s3:::<Customers External Archive Bucket Name>"
            ]
        }
    ]
}
```

Replace `<YOUR-LOGZIO-ACCOUNT>` with your Logz.io accound ID.
