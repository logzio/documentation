---
id: GCP-Cloud-SQL
title: GCP SQL
overview: Send Google Cloud SQL metrics to your Logz.io account.
product: ['logs', 'metrics']
os: ['windows', 'linux']
filters: ['GCP', 'Database']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/gcpsql.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['4KUp9D8EhuMuCuLLhIZBEP', '5DIgZxsYxBjeNlEAexf2A3']
metrics_alerts: []
drop_filter: []
---


Google Cloud SQL is a fully-managed database service that is used to set up, maintain, manage, and administer MySQL and PostgreSQL databases in the cloud. 

## Logs

{@include: ../../_include/general-shipping/gcp-logs.md}   

For this integration, the telemetry list needs to include `cloudsql_database`.

### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

## Metrics

{@include: ../../_include/general-shipping/gcp-metrics.md}

For this integration, the telemetry list needs to include `cloudsql.googleapis.com`.

### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).
