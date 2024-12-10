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
metrics_dashboards: ['2YLu810AXPlVwzQen8vff1']
metrics_alerts: ['4iuPoRsdogZKww8d0NO7er']
drop_filter: []
---


## Metrics

Deploy this integration to send Amazon Lambda metrics to Logz.io. It creates a Kinesis Data Firehose delivery stream to send metrics to your Logz.io account and a Lambda function to add AWS namespaces and collect resource tags.

Install the pre-built dashboard to enhance the observability of your metrics.


{@include: ../../_include/metric-shipping/aws-metrics-new.md}


Install the pre-built dashboard to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["5tAA2oqe1KZmJqQAKUFYuq"] -->

{@include: ../../_include/metric-shipping/generic-dashboard.html}


## Traces

Deploy this integration for automatic instrumentation on AWS Lambda, forwarding traces to Logz.io. This involves adding an OpenTelemetry collector layer and configuring environment variables without modifying your application code.

These guides provide step-by-step instructions for sending traces with OpenTelemetry, tailored to your application's programming language:

* [Go](http://docs.logz.io/docs/shipping/Code/GO/#traces)
* [Node.js](http://docs.logz.io/docs/shipping/Code/Node-js/#traces)
* [.NET](http://docs.logz.io/docs/shipping/Code/dotnet/#traces)
* [Python](http://docs.logz.io/docs/shipping/Code/Python/#traces)