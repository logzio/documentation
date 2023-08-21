---
id: Carbon-Black-security
title: Carbon Black
overview: This integration creates a Kinesis Data Firehose delivery stream that links to your Amazon S3 metrics stream and then sends the metrics to your Logz.io account. It also creates a Lambda function that adds AWS namespaces to the metric stream, and a Lambda function that collects and ships the resources' tags.
product: ['metrics']
os: ['windows', 'linux']
filters: ['Security']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/carbon-black.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---


 

With this integration, you can collect Logs from Carbon Black and forward them to Logz.io.

 

### Set Carbon Black Event Forwarder
  
Follow [Carbon Black instructions](https://developer.carbonblack.com/reference/enterprise-response/event-forwarder/event-forwarder-s3-bucket-configuration/) for forwarding events to S3 bucket

{@include: ../../_include/log-shipping/stack.md}


 