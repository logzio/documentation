---
id: GCP-VPN
title: GCP VPN
overview: Send Google Cloud VPN metrics to your Logz.io account.
product: ['metrics']
os: ['windows', 'linux']
filters: ['GCP', 'Network']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/aws-vpn.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['4gdYz2iIWFeIL3WDDcYRm']
metrics_alerts: []
drop_filter: []
---


Google Cloud VPN provides networking functionality to Compute Engine virtual machine (VM) instances, Google Kubernetes Engine (GKE) clusters, and the App Engine flexible environment. 

## Logs

{@include: ../../_include/general-shipping/gcp-logs.md}

For this integration, the telemetry list needs to include `vpn_gateway`, `vpn_tunnel`.

### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).


## Metrics

{@include: ../../_include/general-shipping/gcp-metrics.md}


### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).