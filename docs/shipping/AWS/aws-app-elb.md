---
id: AWS-App-ELB
title: AWS App ELB
overview: Send your AWS Application ELB logs and metrics to Logz.io.
product: ['logs', 'metrics']
os: []
filters: ['AWS', 'Load Balancer']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/aws-app-elb.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['5BZ6El3juQkCKCIuGm1oyC']
metrics_alerts: []
drop_filter: []
---

## Configure AWS to forward logs to Logz.io

When you set Logz.io to fetch Elastic Load Balancing (ELB) logs, Logz.io will periodically read logs from the configured S3 bucket. Elastic Load Balancing logs are useful for application usage intelligence and monitoring.

{@include: ../../_include/log-shipping/s3-bucket.md}



**Before you begin, you'll need**:
`s3:ListBucket` and `s3:GetObject` [permissions](https://docs.logz.io/docs/user-guide/admin/give-aws-access-with-iam-roles) for the required S3 bucket (one bucket per region)

 

### Send your logs to an S3 bucket

Logz.io fetches your Elastic Load Balancing logs from an S3 bucket.

For help with setting this up, see [these AWS doce](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html)



### Add a new S3 bucket using the dedicated Logz.io configuration wizard

Log into the app to use the dedicated Logz.io [configuration wizard](https://app.logz.io/#/dashboard/send-your-data/log-sources/elastic-load-balancing) and add a new S3 bucket.


<!-- logzio-inject:aws:elb -->

{@include: ../../_include/log-shipping/add-s3-bucket.md}


### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [log shipping troubleshooting](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/log-shipping-troubleshooting/).


## Configure AWS to forward metrics to Logz.io

Deploy this integration to send your Amazon App ELB metrics to Logz.io.

This integration creates a Kinesis Data Firehose delivery stream that links to your Amazon App ELB metrics stream and then sends the metrics to your Logz.io account. It also creates a Lambda function that adds AWS namespaces to the metric stream, and a Lambda function that collects and ships the resources' tags.

{@include: ../../_include/metric-shipping/custom-dashboard.html} Install the pre-built dashboard to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["5BZ6El3juQkCKCIuGm1oyC"] -->

{@include: ../../_include/metric-shipping/generic-dashboard.html}

{@include: ../../_include/metric-shipping/aws-metrics.md}

{@include: ../../_include/metric-shipping/custom-dashboard.html} Install the pre-built dashboard to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["5BZ6El3juQkCKCIuGm1oyC"] -->

{@include: ../../_include/metric-shipping/generic-dashboard.html}
