---
id: GCP-Cloud-API
title: GCP API
overview: Send Google Cloud API metrics to your Logz.io account.
product: ['metrics']
os: ['windows', 'linux']
filters: ['GCP', 'Other']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/gcpapis.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---



Google Cloud APIs allow you to automate your workflows by using your favorite language. 


{@include: ../../_include/general-shipping/gcp-logs.md}  

For this integration, the telemetry list needs to include `k8s_cluster`, `bigquery_dts_config`, `client_auth_config_brand`, `client_auth_config_client`, `billing_account`, `organization`, `project`, `build`, `cloud_scheduler_job`, `service_account`, `gke_cluster`, `gke_nodepool`, `global`, `logging_exclusion`, `logging_log`, `logging_sink`, `metric`, `spanner_instance`, `security_scanner_scan_config`.

### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).
