---
id: Amazon-ElastiCache
title: AWS ElastiCache
overview: Send your Amazon ElastiCache metrics to Logz.io.
product: ['metrics']
os: ['windows', 'linux']
filters: ['AWS', 'Memory Caching']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/Amazon-ElastiCache.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---


:::note
For a much easier and more efficient way to collect and send metrics, consider using the [Logz.io telemetry collector](https://app.logz.io/#/dashboard/send-your-data/agent/new).
:::
 



Deploy this integration to send your Amazon ElastiCache metrics to Logz.io.

This integration creates a Kinesis Data Firehose delivery stream that links to your Amazon ElastiCache metrics stream and then sends the metrics to your Logz.io account. It also creates a Lambda function that adds AWS namespaces to the metric stream, and a Lambda function that collects and ships the resources' tags.


{@include: ../../_include/metric-shipping/aws-metrics.md}


