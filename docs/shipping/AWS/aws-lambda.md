---
id: AWS-Lambda
title: AWS Lambda
overview: AWS Lambda serverless compute service runs code in response to events and automatically manages compute resources. Send these events to Logz.io to identify anomalies and issues and quickly solve them.
product: ['metrics']
os: ['windows', 'linux']
filters: ['AWS', 'Compute']
recommendedFor: ['DevOps Engineer']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/lambda-nodejs2.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['2YLu810AXPlVwzQen8vff1','5tAA2oqe1KZmJqQAKUFYuq']
metrics_alerts: ['4iuPoRsdogZKww8d0NO7er']
drop_filter: []
---


## Metrics


Deploy this integration to send your Amazon Lambda metrics to Logz.io.


This integration creates a Kinesis Data Firehose delivery stream that links to your Amazon Lambda metrics stream and then sends the metrics to your Logz.io account. It also creates a Lambda function that adds AWS namespaces to the metric stream, and a Lambda function that collects and ships the resources' tags.

{@include: ../../_include/metric-shipping/custom-dashboard.html} Install the pre-built dashboard to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["5tAA2oqe1KZmJqQAKUFYuq"] -->

{@include: ../../_include/metric-shipping/generic-dashboard.html}


{@include: ../../_include/metric-shipping/aws-metrics-new.md}


{@include: ../../_include/metric-shipping/custom-dashboard.html} Install the pre-built dashboard to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["5tAA2oqe1KZmJqQAKUFYuq"] -->

{@include: ../../_include/metric-shipping/generic-dashboard.html}


## Traces

Deploy this integration for automatic instrumentation of your Node.js or Go applications on AWS Lambda, enabling trace forwarding to your Logz.io account. It involves adding a specialized OpenTelemetry collector layer. Additionally, Node.js applications require an extra layer for auto-instrumentation. Environment variable configurations are necessary for both Node.js and Go integrations. This setup does not require modifications to your existing application code.




For detailed instructions on implementing this integration for your specific application, please refer to the following documentation:

- **Go Applications**: For deploying traces from Go applications on AWS Lambda using OpenTelemetry, visit [Traces from Go on AWS Lambda using OpenTelemetry](https://docs.logz.io/docs/shipping/AWS/Lambda-extension-go).

- **Node.js Applications**: For deploying traces from Node.js applications on AWS Lambda using OpenTelemetry, visit [Traces from Node.js on AWS Lambda using OpenTelemetry](https://docs.logz.io/docs/shipping/aws/lambda-extension-node/).

These guides offer step-by-step instructions tailored to your application's programming language, ensuring a seamless integration process.

