---
id: GCP-Dataproc-Metastore 
title: GCP Dataproc Metastore 
overview: Send Google Cloud Dataproc Metastore metrics to your Logz.io account.
product: ['logs', 'metrics']
os: ['windows', 'linux']
filters: ['GCP', 'Data Store']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/gcpdataproc.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---

Google Dataproc Metastore is a critical component of data lakes built on open source processing frameworks like Apache Hadoop, Apache Spark, Apache Hive, Trino, Presto, and many others. 

## Logs

{@include: ../../_include/general-shipping/gcp-logs.md}   

For this integration, the telemetry list needs to include `cloud_dataproc_batch`, `cloud_dataproc_cluster`, `cloud_dataproc_job`, `cloud_dataproc_session`.

### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

## Metrics

{@include: ../../_include/general-shipping/gcp-metrics.md}

For this integration, the telemetry list needs to include `dataproc.googleapis.com`.

### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).
