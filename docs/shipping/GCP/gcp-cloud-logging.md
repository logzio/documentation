---
id: GCP-Cloud-Logging
title: GCP Cloud Logging
overview: Send Google Cloud Logging metrics to your Logz.io account.
product: ['logs', 'metrics']
os: ['windows', 'linux']
filters: ['GCP', 'Other']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/cloudlogging.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---



Google Cloud Logging is fully managed, real-time log management with storage, search, analysis and alerting at exabyte scale. 

## Logs 

{@include: ../../_include/general-shipping/gcp-logs.md}   

For this integration, the telemetry list needs to include `logging_bucket`, `logging_exclusion`, `logging_log`, `logging_sink`  .

### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

## Metrics

{@include: ../../_include/general-shipping/gcp-metrics.md}

For this integration, the telemetry list needs to include `logging.googleapis.com`.

### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).
