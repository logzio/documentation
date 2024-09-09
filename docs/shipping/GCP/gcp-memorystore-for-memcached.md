---
id: gcp-memorystore-for-memcached
title: GCP Memorystore for Memcached
overview: Send Google Cloud Memorystore for Memcached metrics to your Logz.io account.
product: ['logs', 'metrics']
os: ['windows', 'linux']
filters: ['GCP', 'Memory Caching']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/memorystore.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['6V6DBzsX8cRZXCSvuSkHiA']
metrics_alerts: []
drop_filter: []
---



Google Memorystore for Memcached is a fully managed Memcached service for Google Cloud. 

## Logs

{@include: ../../_include/general-shipping/gcp-logs.md}   


### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

## Metrics

{@include: ../../_include/general-shipping/gcp-metrics.md}

For this integration, the telemetry list needs to include `memcache.googleapis.com`.

### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).
