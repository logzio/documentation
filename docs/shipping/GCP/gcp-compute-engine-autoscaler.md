---
id: GCP-Compute-Engine-Autoscaler
title: GCP Compute Engine Autoscaler
overview: Send Google Cloud Compute Engine Autoscaler metrics to your Logz.io account.
product: ['metrics']
os: ['windows', 'linux']
filters: ['GCP', 'Compute']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/computeengine.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---


Google Compute Engine Autoscaler allows to automatically add or remove VM instances from a managed instance group based on increases or decreases in load. 


{@include: ../../_include/general-shipping/gcp-logs.md}  

For this integration, the telemetry list needs to include `gce_autoscaler`.

### Check Logz.io for your logs

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).
