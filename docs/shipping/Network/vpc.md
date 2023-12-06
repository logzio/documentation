---
id: VPC-network
title: VPC
overview: VPC Flow Logs is a feature that enables you to capture information about the IP traffic going to and from network interfaces in your VPC. This integration allows you to send these logs to your Logz.io account. 
product: ['logs']
os: []
filters: ['Network']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/vpc.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---


VPC Flow Logs is a feature that enables you to capture information about the IP traffic going to and from network interfaces in your VPC. This integration allows you to send these logs to your Logz.io account. 

**Before you begin, you'll need**:

* `s3:ListBucket` and `s3:GetObject` [permissions](/docs/user-guide/admin/give-aws-access-with-iam-roles) for the required S3 bucket

* {@include: ../../_include/log-shipping/s3-bucket-file-order.md}

 

### Send your logs to an S3 bucket

Logz.io fetches your VPC Flow logs from an S3 bucket.
VPC Flow logs are not stored in S3 by default, so you'll need to set up AWS to send your Flow logs to S3.

For help with this, see [Publishing Flow Logs to Amazon S3](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs-s3.html) from AWS.

### Add a new S3 bucket using the dedicated Logz.io configuration wizard

Log into the app to use the dedicated Logz.io [configuration wizard](https://app.logz.io/#/dashboard/send-your-data/log-sources/vpc) and add a new S3 bucket.


<!-- logzio-inject:aws:vpc-flow -->


{@include: ../../_include/log-shipping/add-s3-bucket.md}



### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [log shipping troubleshooting](/docs/user-guide/log-management/troubleshooting/log-shipping-troubleshooting/).

 
