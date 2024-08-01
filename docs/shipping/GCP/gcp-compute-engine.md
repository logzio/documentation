---
id: GCP-Compute-Engine
title: GCP Compute Engine
overview: Send Google Cloud Compute Engine metrics to your Logz.io account.
product: ['logs', 'metrics']
os: ['windows', 'linux']
filters: ['GCP', 'Compute']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/computeengine.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['2UHWhKZvymlkGU7yy4jKIK']
metrics_alerts: []
drop_filter: []
---



Google Compute Engine is the Infrastructure as a Service component of Google Cloud Platform which is built on Google's global infrastructure. 

## Logs

{@include: ../../_include/general-shipping/gcp-logs.md}   

For this integration, the telemetry list needs to include `compute`.

### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

## Metrics

{@include: ../../_include/general-shipping/gcp-metrics.md}

For this integration, the telemetry list needs to include `compute.googleapis.com`.

### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).