---
id: GCP-VM-Manager
title: GCP VM Manager
overview: Send Google Cloud VM Manager metrics to your Logz.io account.
product: ['logs', 'metrics']
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


Google VM Manager is a suite of tools that can be used to manage operating systems for large virtual machine (VM) fleets. 

## Logs

{@include: ../../_include/general-shipping/gcp-logs.md}

For this integration, the telemetry list needs to include `gce_instance`.

### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).


## Metrics

{@include: ../../_include/general-shipping/gcp-metrics.md}


### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).