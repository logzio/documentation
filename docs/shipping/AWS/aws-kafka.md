---
id: AWS-Kafka
title: Amazon Managed Streaming for Apache Kafka (MSK)
overview: Send your Amazon Managed Streaming for Apache Kafka (MSK) metrics to Logz.io.
product: ['metrics']
os: ['windows', 'linux']
filters: ['AWS', 'Distributed Messaging']
logo: https://dytvr9ot2sszz.cloudfront.net/logz-docs/shipper-logos/aws-msk.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['7bHNddlAK5q8Iya7xIhbbU']
metrics_alerts: []
drop_filter: []
---


:::note
For a much easier and more efficient way to collect and send metrics, consider using the [Logz.io telemetry collector](https://app.logz.io/#/dashboard/integrations/collectors?tags=Quick%20Setup).
:::



Deploy this integration to send your Amazon Managed Streaming for Apache Kafka (MSK) metrics to Logz.io.

This integration creates a Kinesis Data Firehose delivery stream that links to your Amazon Managed Streaming for Apache Kafka (MSK) metrics stream and then sends the metrics to your Logz.io account. It also creates a Lambda function that adds AWS namespaces to the metric stream, and a Lambda function that collects and ships the resources' tags.

Install the pre-built dashboard to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["7bHNddlAK5q8Iya7xIhbbU"] -->

{@include: ../../_include/metric-shipping/generic-dashboard.html}



{@include: ../../_include/metric-shipping/aws-metrics-new.md}

Install the pre-built dashboard to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["7bHNddlAK5q8Iya7xIhbbU"] -->

{@include: ../../_include/metric-shipping/generic-dashboard.html}

