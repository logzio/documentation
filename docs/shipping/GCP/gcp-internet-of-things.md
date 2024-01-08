---
id: gcp-internet-of-things
title: GCP Cloud Internet of Things (IoT) Core
overview: Send Google Cloud Internet of Things (IoT) Core metrics to your Logz.io account.
product: ['metrics']
os: ['windows', 'linux']
filters: ['GCP', 'IoT']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/googleiot.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---


Google Cloud Internet of Things (IoT) Core is a fully managed service for securely connecting and managing IoT devices. 


{@include: ../../_include/general-shipping/gcp-metrics.md}  

For this integration, the telemetry list needs to include `cloudiot_device`, `cloudiot_device_registry`, `cloudiot_group`.

### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).
