---
id: Carbon-Black
title: Carbon Black
sidebar_position: 1
overview: This integration creates a Kinesis Data Firehose delivery stream that links to your Amazon S3 metrics stream and then sends the metrics to your Logz.io account. It also creates a Lambda function that adds AWS namespaces to the metric stream, and a Lambda function that collects and ships the resources' tags.
product: ['metrics']
os: ['windows', 'linux']
filters: ['gcp', 'cloud']
logo: https://docs.logz.io/images/logo/logz-symbol.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
---


 

With this integration, you can collect Logs from Carbon Black and forward them to Logz.io.

 

##### Set Carbon Black Event Forwarder
  
Follow [Carbon Black instructions](https://developer.carbonblack.com/reference/enterprise-response/event-forwarder/event-forwarder-s3-bucket-configuration/) for forwarding events to S3 bucket

{@include: ../_include/log-shipping/stack.md}


 