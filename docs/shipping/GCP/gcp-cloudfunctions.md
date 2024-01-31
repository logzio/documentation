---
id: GCP-Cloud-Functions
title: GCP Cloud Functions
overview: Send Google Cloud Functions metrics to your Logz.io account.
product: ['metrics']
os: ['windows', 'linux']
filters: ['GCP', 'Compute']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/cloudfunctions.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['78mU6GZUeRLhMtExlMvshT']
metrics_alerts: []
drop_filter: []
---



Google Cloud Functions is a serverless execution environment for building and connecting cloud services. 

## Logs

{@include: ../../_include/general-shipping/gcp-logs.md}  

For this integration, the telemetry list needs to include `cloud_function`.

### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

## Metrics

{@include: ../../_include/general-shipping/gcp-metrics.md}


### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).