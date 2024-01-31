---
id: gcp-managed-service-for-microsoft-active-directory
title: GCP Managed Service for Microsoft Active Directory
overview: Send Google Cloud Managed Service for Microsoft Active Directory metrics to your Logz.io account.
product: ['logs', 'metrics']
os: ['windows', 'linux']
filters: ['GCP', 'Access Management']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/gcpiam.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---


Google Managed Service for Microsoft Active Directory is a fully managed, real-time log management with storage, search, analysis and alerting at exabyte scale. 

## Logs

{@include: ../../_include/general-shipping/gcp-logs.md}  

For this integration, the telemetry list needs to include `microsoft_ad_domain`.

### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).


## Metrics

{@include: ../../_include/general-shipping/gcp-metrics.md}

For this integration, the telemetry list needs to include `managedidentities.googleapis.com`.

### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).