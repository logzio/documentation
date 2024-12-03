---
id: GCP-API-Gateway
title: GCP API Gateway
overview: Send Google Cloud API Gateway metrics to your Logz.io account.
product: ['logs', 'metrics']
os: ['windows', 'linux']
filters: ['GCP', 'Access Management']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/apigateway.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---


Google API Gateway allows you to create, secure, and monitor APIs for Google Cloud serverless back ends, including Cloud Functions, Cloud Run, and App Engine. 

## Logs

{@include: ../../_include/general-shipping/gcp-logs.md}    

For this integration, the telemetry list needs to include `apigateway`.

### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

## Metrics

{@include: ../../_include/general-shipping/gcp-metrics.md}

For this integration, the telemetry list needs to include `apigateway.googleapis.com`.

### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).
