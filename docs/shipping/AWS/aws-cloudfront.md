---
id: AWS-CloudFront
title: AWS CloudFront
overview: Send your Amazon CloudFront metrics to Logz.io.
product: ['logs' , 'metrics']
os: []
filters: ['AWS', 'Network']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/aws-cloudfront.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['3MJWDTivgQCNz3DQIj3Kry']
metrics_alerts: []
drop_filter: []
---



:::note
For a much easier and more efficient way to collect and send metrics, consider using the [Logz.io telemetry collector](https://app.logz.io/#/dashboard/integrations/collectors?tags=Quick%20Setup).
:::


## Logs


When you set Logz.io to fetch CloudFront logs, Logz.io will periodically read logs from the configured S3 bucket.
CloudFront logs are useful for auditing/security monitoring and business intelligence.

{@include: ../../_include/log-shipping/s3-bucket.md}


**Before you begin, you'll need**:

* `s3:ListBucket` and `s3:GetObject` [permissions](https://docs.logz.io/docs/user-guide/admin/give-aws-access-with-iam-roles/) for the required S3 bucket

* {@include: ../../_include/log-shipping/s3-bucket-file-order.md}

 

### Send your logs to an S3 bucket

Logz.io fetches your CloudFront logs from an S3 bucket.
CloudFront access logs are not enabled by default, so you'll need to set this up.

For help with this, see [Configuring and Using CloudFront Access Logs](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/AccessLogs.html) from AWS.

### Add a new S3 bucket using the dedicated Logz.io configuration wizard

Log into the app to use the dedicated Logz.io [configuration wizard](https://app.logz.io/#/dashboard/send-your-data/log-sources/cloudfront) and add a new S3 bucket.

<!-- logzio-inject:aws:cloudfront -->

{@include: ../../_include/log-shipping/add-s3-bucket.md}

### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [log shipping troubleshooting](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/log-shipping-troubleshooting/).

 
## Metrics


Deploy this integration to send your Amazon CloudFront metrics to Logz.io.

This integration creates a Kinesis Data Firehose delivery stream that links to your Amazon CloudFront metrics stream and then sends the metrics to your Logz.io account. It also creates a Lambda function that adds AWS namespaces to the metric stream, and a Lambda function that collects and ships the resources' tags.

Install the pre-built dashboard to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["3MJWDTivgQCNz3DQIj3Kry"] -->

{@include: ../../_include/metric-shipping/generic-dashboard.html}


{@include: ../../_include/metric-shipping/aws-metrics-new.md}


Install the pre-built dashboard to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["3MJWDTivgQCNz3DQIj3Kry"] -->

{@include: ../../_include/metric-shipping/generic-dashboard.html}
