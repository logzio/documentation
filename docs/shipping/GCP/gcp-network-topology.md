---
id: gcp-network-topology
title: GCP Network Topology
overview: Send Google Cloud Network Topology metrics to your Logz.io account.
product: ['logs', 'metrics']
os: ['windows', 'linux']
filters: ['GCP', 'Network']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/gcpnetwork.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---



Google Network Topology is a visualization tool that shows the topology of your Virtual Private Cloud (VPC) networks, hybrid connectivity to and from your on-premises networks, connectivity to Google-managed services, and the associated metrics. 

## Logs

{@include: ../../_include/general-shipping/gcp-logs.md}   

For this integration, the telemetry list needs to include `gce_network`, `gce_network_endpoint_group`, `gce_network_region`.

### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).


## Metrics

{@include: ../../_include/general-shipping/gcp-metrics.md}

For this integration, the telemetry list needs to include `networking.googleapis.com`

### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).