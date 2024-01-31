---
id: GCP-Cloud-IDS
title: GCP IDS
overview: Send Google Cloud IDS metrics to your Logz.io account.
product: ['logs', 'metrics']
os: ['windows', 'linux']
filters: ['GCP', 'Security']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/ids.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---


Google Cloud IDS delivers cloud-native, managed, network-based threat detection, built with Palo Alto Networks’ industry-leading threat detection technologies to provide high levels of security efficacy. 

## Logs

{@include: ../../_include/general-shipping/gcp-logs.md}  

For this integration, the telemetry list needs to include `ids`.

### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

## Metrics

{@include: ../../_include/general-shipping/gcp-metrics.md}

For this integration, the telemetry list needs to include `ids.googleapis.com`.

### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).