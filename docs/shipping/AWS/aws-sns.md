---
id: AWS-SNS
title: AWS SNS
overview: This integration creates a Kinesis Data Firehose delivery stream that links to your Amazon SNS metrics stream and then sends the metrics to your Logz.io account. It also creates a Lambda function that adds AWS namespaces to the metric stream, and a Lambda function that collects and ships the resources' tags.
product: ['metrics']
os: ['windows', 'linux']
filters: ['AWS', 'Distributed Messaging']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/aws-sns.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['3G7HxOI10AvzpqGXQNfawA']
metrics_alerts: []
drop_filter: []
---



:::note
For a much easier and more efficient way to collect and send metrics, consider using the [Logz.io telemetry collector](https://app.logz.io/#/dashboard/integrations/collectors?tags=Quick%20Setup).
:::




Deploy this integration to send your Amazon SNS metrics to Logz.io.

This integration creates a Kinesis Data Firehose delivery stream that links to your Amazon SNS metrics stream and then sends the metrics to your Logz.io account. It also creates a Lambda function that adds AWS namespaces to the metric stream, and a Lambda function that collects and ships the resources' tags.

{@include: ../../_include/metric-shipping/custom-dashboard.html} Install the pre-built dashboard to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["3G7HxOI10AvzpqGXQNfawA"] -->

{@include: ../../_include/metric-shipping/generic-dashboard.html}


{@include: ../../_include/metric-shipping/aws-metrics.md}


{@include: ../../_include/metric-shipping/custom-dashboard.html} Install the pre-built dashboard to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["3G7HxOI10AvzpqGXQNfawA"] -->

{@include: ../../_include/metric-shipping/generic-dashboard.html}
