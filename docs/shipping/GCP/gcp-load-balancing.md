---
id: gcp-load-balancing
title: GCP Load Balancing
overview: Send Google Cloud Load Balancing metrics to your Logz.io account.
product: ['metrics']
os: ['windows', 'linux']
filters: ['GCP', 'Load Balancer']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/gcplb.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['2qF8pBXlwH0Pw6noOMfzRk', '48vnzAEl0x6hh3DWKIWkpx', '7s5HblMf4IVimoRSwnCRJ6']
metrics_alerts: []
drop_filter: []
---

Google Cloud Load Balancing is a fully distributed, software-defined, managed service for all Google Cloud traffic. 


{@include: ../../_include/general-shipping/gcp-logs.md}  

For this integration, the telemetry list needs to include `aws_alb_load_balancer`.

### Check Logz.io for your logs

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).
