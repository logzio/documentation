---
id: Amazon-S3
title: Amazon S3
sidebar_position: 1
overview: This integration creates a Kinesis Data Firehose delivery stream that links to your Amazon S3 metrics stream and then sends the metrics to your Logz.io account. It also creates a Lambda function that adds AWS namespaces to the metric stream, and a Lambda function that collects and ships the resources' tags.
product: ['metrics']
os: ['windows', 'linux']
filters: ['gcp', 'cloud']
logo: https://docs.logz.io/images/logo/logz-symbol.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['1Pm3OYbu1MRGoELc2qhxQ1']
metrics_alerts: []
---


## Overview

MySQL is an open-source relational database management system. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.

To send your Prometheus-format MySQL metrics to Logz.io, you need to add the **inputs.mysql** and **outputs.http** plug-ins to your Telegraf configuration file.

<!-- logzio-inject:install:grafana:dashboards ids=["2zMVEOdWnIMgOPATDLByX7"] --> 

#### Configuring Telegraf to send your metrics data to Logz.io

 

##### Set up Telegraf v1.17 or higher

{@include: ../_include/metric-shipping/telegraf-setup.md}

##### Add the inputs.mysql plug-in

First you need to configure the input plug-in to enable Telegraf to scrape the MySQL data from your hosts. To do this, add the following code to the configuration file:

``` ini
[[inputs.mysql]]
  servers = ["<<USER-NAME>>:<<PASSWORD>>@<<PROTOCOL>>(<<ADDRESS>>)/?tls=false"]
  ##  e.g.
  ##    servers = ["user:passwd@tcp(127.0.0.1:3306)/?tls=false"]
  ##    servers = ["user@tcp(127.0.0.1:3306)/?tls=false"]
  metric_version = 2
  # gather metrics from INFORMATION_SCHEMA.TABLES for databases provided above list
   gather_table_schema = true

  # gather thread state counts from INFORMATION_SCHEMA.PROCESSLIST
   gather_process_list = true

  # gather user statistics from INFORMATION_SCHEMA.USER_STATISTICS
   gather_user_statistics = true

  # gather auto_increment columns and max values from information schema
   gather_info_schema_auto_inc = true

  # gather metrics from INFORMATION_SCHEMA.INNODB_METRICS
   gather_innodb_metrics = true

  # gather metrics from SHOW SLAVE STATUS command output
   gather_slave_status = true

  # gather metrics from SHOW BINARY LOGS command output
   gather_binary_logs = true

  # gather metrics from SHOW GLOBAL VARIABLES command output
   gather_global_variables = true

  # gather metrics from PERFORMANCE_SCHEMA.TABLE_IO_WAITS_SUMMARY_BY_TABLE
   gather_table_io_waits = true

  # gather metrics from PERFORMANCE_SCHEMA.TABLE_LOCK_WAITS
   gather_table_lock_waits = true

  # gather metrics from PERFORMANCE_SCHEMA.TABLE_IO_WAITS_SUMMARY_BY_INDEX_USAGE
   gather_index_io_waits = true

  # gather metrics from PERFORMANCE_SCHEMA.EVENT_WAITS
   gather_event_waits = true

  # gather metrics from PERFORMANCE_SCHEMA.FILE_SUMMARY_BY_EVENT_NAME
   gather_file_events_stats = true

  # gather metrics from PERFORMANCE_SCHEMA.EVENTS_STATEMENTS_SUMMARY_BY_DIGEST
   gather_perf_events_statements = true
  
  # gather metrics from PERFORMANCE_SCHEMA.EVENTS_STATEMENTS_SUMMARY_BY_ACCOUNT_BY_EVENT_NAME
   gather_perf_sum_per_acc_per_event = true
```

* Replace `<<USER-NAME>>` with the user name for your MySQL database.
* Replace `<<PASSWORD>>` with the password for your MySQL database.
* Replace `<<PROTOCOL>>` with the name of your shipping protocol (tcp protocol recommended).
* Replace `<<ADDRESS>>` with the address of your MySQL database host. This is `localhost` if installed locally.

:::note
The full list of data scraping and configuring options can be found [here](https://github.com/influxdata/telegraf/blob/release-1.18/plugins/inputs/mysql/README.md)
:::
 

##### Add the outputs.http plug-in
  
{@include: ../_include/metric-shipping/telegraf-outputs.md}
{@include: ../_include/general-shipping/replace-placeholders-prometheus.html}

##### Start Telegraf

{@include: ../_include/metric-shipping/telegraf-run.md}

##### Check Logz.io for your metrics

{@include: ../_include/metric-shipping/custom-dashboard.html} Install the pre-built dashboard to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["2zMVEOdWnIMgOPATDLByX7"] --> 

{@include: ../_include/metric-shipping/generic-dashboard.html} 


 
