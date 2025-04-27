---
id: AWS-Redshift
title: AWS Redshift
overview: This integration creates a Kinesis Data Firehose delivery stream that links to your Amazon Redshift metrics stream and then sends the metrics to your Logz.io account. It also creates a Lambda function that adds AWS namespaces to the metric stream, and a Lambda function that collects and ships the resources' tags.
product: ['metrics']
os: ['windows', 'linux']
filters: ['AWS', 'Data Store']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/Amazon-Redshift.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: ['3emd5myHx9uqY4U272loav']
drop_filter: []
---



:::note
For a much easier and more efficient way to collect and send metrics, consider using the [Logz.io telemetry collector](https://app.logz.io/#/dashboard/integrations/collectors?tags=Quick%20Setup).
:::
 



Deploy this integration to send your Amazon Redshift metrics to Logz.io.

This integration creates a Kinesis Data Firehose delivery stream that links to your Amazon Redshift metrics stream and then sends the metrics to your Logz.io account. It also creates a Lambda function that adds AWS namespaces to the metric stream, and a Lambda function that collects and ships the resources' tags.


{@include: ../../_include/metric-shipping/aws-metrics-new.md}

