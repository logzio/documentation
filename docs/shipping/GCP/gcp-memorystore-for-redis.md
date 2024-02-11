---
id: GCP-Memorystore-for-Redis
title: GCP Memorystore for Redis
overview: Send Google Cloud Memorystore for Redis metrics to your Logz.io account.
product: ['logs', 'metrics']
os: ['windows', 'linux']
filters: ['GCP', 'Memory Caching']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/memorystore.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['771vgmjMzFBHHma1Jov3bG']
metrics_alerts: []
drop_filter: []
---



Google Memorystore for Redis a fully managed Redis service for the Google Cloud.  

## Logs

{@include: ../../_include/general-shipping/gcp-logs.md}  

For this integration, the telemetry list needs to include `redis_instance`.

### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).


## Metrics

{@include: ../../_include/general-shipping/gcp-metrics.md}

For this integration, the telemetry list needs to include `redis.googleapis.com`.

### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).