---
id: AWS-EFS
title: AWS EFS
overview: Send your Amazon EFS metrics to Logz.io.
product: ['metrics']
os: ['windows', 'linux']
filters: ['AWS', 'Data Store']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/aws-efs.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['7IUpQgVmcbkHV8zAGuLHIL']
metrics_alerts: []
drop_filter: []
---



:::note
For a much easier and more efficient way to collect and send metrics, consider using the [Logz.io telemetry collector](https://app.logz.io/#/dashboard/send-your-data/agent/new).
:::




Deploy this integration to send your Amazon EFS metrics to Logz.io.

This integration creates a Kinesis Data Firehose delivery stream that links to your Amazon EFS metrics stream and then sends the metrics to your Logz.io account. It also creates a Lambda function that adds AWS namespaces to the metric stream, and a Lambda function that collects and ships the resources' tags.

{@include: ../../_include/metric-shipping/custom-dashboard.html} Install the pre-built dashboard to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["7IUpQgVmcbkHV8zAGuLHIL"] -->

{@include: ../../_include/metric-shipping/generic-dashboard.html}


{@include: ../../_include/metric-shipping/aws-metrics.md}

{@include: ../../_include/metric-shipping/custom-dashboard.html} Install the pre-built dashboard to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["7IUpQgVmcbkHV8zAGuLHIL"] -->

{@include: ../../_include/metric-shipping/generic-dashboard.html}