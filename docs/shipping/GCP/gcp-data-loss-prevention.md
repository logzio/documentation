---
id: GCP-Data-Loss-Prevention
title: GCP Data Loss Prevention
overview: Send Google Cloud Data Loss Prevention metrics to your Logz.io account.
product: ['logs', 'metrics']
os: ['windows', 'linux']
filters: ['GCP', 'Security']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/lossprevention.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---



Google Cloud Data Loss Prevention provides tools to classify, mask, tokenize, and transform sensitive elements to help better manage the data that is collected, stored, or used for business or analytics. 

## Logs

{@include: ../../_include/general-shipping/gcp-logs.md}   


### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

## Metrics

{@include: ../../_include/general-shipping/gcp-metrics.md}

For this integration, the telemetry list needs to include `dlp.googleapis.com`.


### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).