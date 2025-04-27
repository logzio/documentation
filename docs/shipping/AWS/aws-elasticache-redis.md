---
id: AWS-ElastiCache-Redis
title: AWS ElastiCache for Redis
overview: Send your Amazon ElastiCache for Redis metrics to Logz.io.
product: ['metrics']
os: ['windows', 'linux']
filters: ['AWS', 'Memory Caching']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/aws-redis-logo.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['2iTJV7AkvtHDJauaEzYobs']
metrics_alerts: []
drop_filter: []
---


:::note
For a much easier and more efficient way to collect and send metrics, consider using the [Logz.io telemetry collector](https://app.logz.io/#/dashboard/integrations/collectors?tags=Quick%20Setup).
:::




Deploy this integration to send your Amazon ElastiCache for Redis metrics to Logz.io.

This integration creates a Kinesis Data Firehose delivery stream that links to your Amazon ElastiCache for Redis metrics stream and then sends the metrics to your Logz.io account. It also creates a Lambda function that adds AWS namespaces to the metric stream, and a Lambda function that collects and ships the resources' tags.

Install the pre-built dashboard to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["2iTJV7AkvtHDJauaEzYobs"] -->

{@include: ../../_include/metric-shipping/generic-dashboard.html}


{@include: ../../_include/metric-shipping/aws-metrics-new.md}



Install the pre-built dashboard to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["2iTJV7AkvtHDJauaEzYobs"] -->

{@include: ../../_include/metric-shipping/generic-dashboard.html}
