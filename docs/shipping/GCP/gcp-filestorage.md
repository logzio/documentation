---
id: GCP-Filestore
title: GCP Filestore
overview: Send Google Cloud Filestore metrics to your Logz.io account.
product: ['logs', 'metrics']
os: ['windows', 'linux']
filters: ['GCP', 'Data Store']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/gcpfilestore.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['4LAZ8Zep644MzbT1x089GG']
metrics_alerts: []
drop_filter: []
---



Google Filestore is a fully managed Google Cloud service that provides network file storage. 

## Logs

{@include: ../../_include/general-shipping/gcp-logs.md}  


### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

## Metrics

{@include: ../../_include/general-shipping/gcp-metrics.md}

For this integration, the telemetry list needs to include `file.googleapis.com`.

### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).