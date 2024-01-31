---
id: GCP-Identity-and-Access-Management
title: GCP Identity and Access Management 
overview: Send Google Cloud Identity and Access Management metrics to your Logz.io account.
product: ['metrics']
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


Google Identity and Access Management lets administrators authorize who can take action on specific resources, giving them full control and visibility to manage Google Cloud resources centrally. 


{@include: ../../_include/general-shipping/gcp-logs.md}  

For this integration, the telemetry list needs to include `identitytoolkit_project`, `identitytoolkit_tenant`.

### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).
