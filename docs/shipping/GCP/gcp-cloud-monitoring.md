---
id: GCP-Cloud-Monitoring
title: GCP Monitoring
overview: Send Google Cloud Monitoring metrics to your Logz.io account.
product: ['logs', 'metrics']
os: ['windows', 'linux']
filters: ['GCP', 'Monitoring']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/cloudmonitoring.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---


Google Cloud Monitoring provides visibility into the performance, uptime, and overall health of cloud-powered applications. 

## Logs 

{@include: ../../_include/general-shipping/gcp-logs.md}   

For this integration, the telemetry list needs to include `metric`.

### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

## Metrics

{@include: ../../_include/general-shipping/gcp-metrics.md}

For this integration, the telemetry list needs to include `monitoring.googleapis.com`.

### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).
