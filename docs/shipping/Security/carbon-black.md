---
id: Carbon-Black
title: Carbon Black
overview: Carbon Black enables multi-cloud workload and endpoint threat protection. Connect your Carbon Black to Logz.io to monitor and analyze endpoint security, threat detection, user behavior, software inventory, compliance, and incident response to enhance overall cybersecurity.
product: ['logs']
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

:::note
[Project's GitHub repo](https://github.com/logzio/s3-hook/)
:::

### Set Carbon Black Event Forwarder
  
Follow [Carbon Black instructions](https://developer.carbonblack.com/reference/enterprise-response/event-forwarder/event-forwarder-s3-bucket-configuration/) for forwarding events to S3 bucket

{@include: ../../_include/log-shipping/stack.md}


 