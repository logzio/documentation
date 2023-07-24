---
id: Amazon-CloudFront
title: AWS CloudFront
sidebar_position: 1
overview: Amazon CloudFront is a content delivery network operated by Amazon Web Services. When you set Logz.io to fetch CloudFront logs, Logz.io will periodically read logs from the configured S3 bucket.
product: ['metrics']
os: ['windows', 'linux']
filters: ['gcp', 'cloud']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/aiven-logo.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
---


Amazon CloudFront is a content delivery network operated by Amazon Web Services. When you set Logz.io to fetch CloudFront logs, Logz.io will periodically read logs from the configured S3 bucket. 

When you set Logz.io to fetch CloudFront logs, Logz.io will periodically read logs from the configured S3 bucket.
CloudFront logs are useful for auditing/security monitoring and business intelligence.

{@include: ../_include/log-shipping/s3-bucket.md service="CloudFront" %}

#### Configuration

**Before you begin, you'll need**:

* `s3:ListBucket` and `s3:GetObject` [permissions](https://docs.logz.io/user-guide/give-aws-access-with-iam-roles/) for the required S3 bucket

* {@include: ../_include/log-shipping/s3-bucket-file-order.md}

 

##### Send your logs to an S3 bucket

Logz.io fetches your CloudFront logs from an S3 bucket.
CloudFront access logs are not enabled by default, so you'll need to set this up.

For help with this, see [Configuring and Using CloudFront Access Logs](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/AccessLogs.html) from AWS.

##### Add a new S3 bucket using the dedicated Logz.io configuration wizard

Log into the app to use the dedicated Logz.io [configuration wizard](https://app.logz.io/#/dashboard/send-your-data/log-sources/cloudfront) and add a new S3 bucket.

<!-- logzio-inject:aws:cloudfront -->

{@include: ../_include/log-shipping/add-s3-bucket.md}

##### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [log shipping troubleshooting]({{site.baseurl}}/user-guide/log-shipping/log-shipping-troubleshooting.html).

 
