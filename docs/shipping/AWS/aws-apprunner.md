---
id: AWS-AppRunner
title: AWS AppRunner
overview: Send your Amazon AppRunner metrics to Logz.io
product: ['metrics']
os: []
filters: ['AWS', 'Compute']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/aws-fusion.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---

:::note
For a much easier and more efficient way to collect and send metrics, consider using the [Logz.io telemetry collector](https://app.logz.io/#/dashboard/integrations/collectors?tags=Quick%20Setup).
:::
 



Deploy this integration to send your Amazon AppRunner metrics to Logz.io.

This integration creates a Kinesis Data Firehose delivery stream that links to your Amazon AppRunner metrics stream and then sends the metrics to your Logz.io account. It also creates a Lambda function that adds AWS namespaces to the metric stream, and a Lambda function that collects and ships the resources' tags.

{@include: ../../_include/metric-shipping/aws-metrics-new.md}
