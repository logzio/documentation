---
sidebar_position: 11
title: Copy archived logs to Cold Tier
description: Copy archived logs from an external S3 bucket archive to a Coldn Tier S3 bucket using AWS services.
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logz.io, cold tier, storage, archive, opensearch dashboards, log analysis, observability]
---


Here's a detailed, step-by-step guide for Logz.io customers on how to copy archived logs from an external-archive S3 bucket to a cold-tier S3 bucket using AWS services. This process requires using S3 Batch Operations and AWS Lambda to manage the copying and renaming of files, as file naming conventions differ between the two storage tiers.

**Before you begin, you'll need**: AWS CLI

## Generate a Manifest File

You need a list of keys (files) in your external-archive bucket to copy. To do this, generate a manifest file.

### Fetch keys in a specific range

```shell
aws s3api list-objects-v2 \
    --bucket EXTERNAL_ARCHIVE_BUCKET_NAME \
    --query "Contents[?LastModified>='DATE_FROM' && LastModified<'DATE_TO'].{Key: Key}" \
    --output json | jq -r '.[] | "EXTERNAL_ARCHIVE_BUCKET_NAME, \(.Key)"' > output.csv
```

Replace `EXTERNAL_ARCHIVE_BUCKET_NAME` with your bucket name, and `DATE_FROM` and `DATE_TO` with your specific date range.

### Fetch all keys

```shell
aws s3api list-objects-v2 \  
    --bucket EXTERNAL_ARCHIVE_BUCKET_NAME     
    --output json | jq -r '"EXTERNAL_ARCHIVE_BUCKET_NAME," + .Contents[].Key' > output.csv
```

Replace `EXTERNAL_ARCHIVE_BUCKET_NAME` with your bucket name.

## Enable S3 Inventory report

Enable the S3 inventory report for your external-archive bucket. This will generate a report of files that should be moved, simplifying the process. To this on the AWS Console:

1. Navigate to S3 > Your External Archive Bucket > Management tab.
2. Scroll to "Inventory configurations" and click "Create inventory configuration".
3. Fill in the necessary details, ensuring the report details are set to a different account (use Logz.io Prod Account ID: `406095609952`) and the destination bucket is correctly set (follow instructions on the format).

## Update bucket policy

Allow Logz.io's AWS Lambda to read files from your external-archive bucket by updating the bucket policy. This policy allows specific actions like GetObject and ListBucket, ensuring that the necessary permissions are in place for the copying process.

Use the AWS Console or CLI to update the policy, ensuring to replace placeholders with your specific bucket names and ensuring the Logz.io Prod Account ID is correctly set.


## Wait for Inventory report

After enabling the inventory report, wait for it to appear in the designated output bucket. This might take up to 48 hours.

## Create and run S3 batch operations job

With the inventory report ready, create an S3 Batch Operations job. This job will invoke an AWS Lambda function for each file that needs to be copied, managing the process efficiently.

Use the AWS Console or CLI to create the job, ensuring to specify the correct source bucket, destination bucket, and Lambda function details. Remember to set the permissions correctly by including the `BatchOperationsDestinationRoleCOPY`.

## Disable Inventory report and remove bucket policy

Once the copy process is complete, it's important to disable the inventory report and remove the updated bucket policy to clean up and secure your environment.
