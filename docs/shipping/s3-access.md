---
id: Amazon-S3
title: Amazon S3
sidebar_position: 1
overview: This integration creates a Kinesis Data Firehose delivery stream that links to your Amazon S3 metrics stream and then sends the metrics to your Logz.io account. It also creates a Lambda function that adds AWS namespaces to the metric stream, and a Lambda function that collects and ships the resources' tags.
product: ['metrics']
os: ['windows', 'linux']
filters: ['gcp', 'cloud']
logo: https://docs.logz.io/images/logo/logz-symbol.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['1Pm3OYbu1MRGoELc2qhxQ1']
metrics_alerts: []
---


Amazon S3 Access Logs provide detailed records about requests that are made to your S3 bucket. This integration allows you to send these logs to your Logz.io account.

#### Configuration

**Before you begin, you'll need**:

* `s3:ListBucket` and `s3:GetObject` [permissions](https://docs.logz.io/user-guide/give-aws-access-with-iam-roles/) for the required S3 bucket

* {@include: ../_include/log-shipping/s3-bucket-file-order.md}

 

##### Send your logs to an S3 bucket

Logz.io fetches your S3 access logs from a separate S3 bucket.
By default, S3 access logs are not enabled, so you'll need to set this up.

For help with this, see [Amazon S3 Server Access Logging](https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerLogs.html) from AWS.


##### Add a new S3 bucket using the dedicated Logz.io configuration wizard

{@include: ../_include/log-shipping/app_login.html}


<!-- logzio-inject:aws:s3-access -->


{@include: ../_include/log-shipping/add-s3-bucket.md}


##### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [log shipping troubleshooting]({{site.baseurl}}/user-guide/log-shipping/log-shipping-troubleshooting.html).

 
