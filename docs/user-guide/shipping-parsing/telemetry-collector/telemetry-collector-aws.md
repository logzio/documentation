---
sidebar_position: 2
title: Send AWS data with Telemetry Collector
---

:::note
Telemetry Collector is currently **available in all regions** except for Japan and Australia. If you're located in these regions, you can use **[Logz.io’s data shippers](https://app.logz.io/#/dashboard/send-your-data/collection?tag=all&collection=all)** to send your data.
:::

To start sending your AWS data through the Telemetry Collector, Log into your **main** Logz.io account, navigate to [Send your data](https://app.logz.io/#/dashboard/send-your-data), and click on **Start collecting**.

:::caution Important
To configure the Telemetry Collector, you must be logged into your **main** Logz.io account.
:::

:::caution Important
This integration is only compatible with Amazon Linux version 2 on EC2. The use of version 1 is deprecated.
:::

![Start collecting button](https://dytvr9ot2sszz.cloudfront.net/logz-docs/telemetry-agent/telemetry-start-here.png)

## Start sending AWS data

### 1. Select platform

Select the AWS platform and the relevant sub-type through which you want to send your data.

![Select platform](https://dytvr9ot2sszz.cloudfront.net/logz-docs/telemetry-agent/aws-agent.png)

### 2. Select data sources

Enter the full path location of your log files from your machine. You can add multiple files by clicking on the **Add a file** option.

Logz.io uses OpenTelemetry to monitor your EC2.

![Select data source](https://dytvr9ot2sszz.cloudfront.net/logz-docs/telemetry-agent/telemetry-aws-data-source.png)

### 3. Define your collector

Choose a name and write a description to help identify the collector. 

Under **Accounts**, you can review the Logs and Metrics accounts to which the Telemetry Collector will send the data. If you don't have an existing account, one will be generated for you, and you’ll be able to review its name before continuing.

Click **Generate snippet** to continue.

![Define collector](https://dytvr9ot2sszz.cloudfront.net/logz-docs/telemetry-agent/telemetry-aws-define.png)

### 4. Install the Telemetry Collector

Copy the code snippet and **run it in your EC2** to install the AWS Telemetry Collector.

:::note
Some platforms might require additional details, such as admin privileges or passwords, to complete the installation. These details are not sent to or stored by Logz.io.
:::

![Review collector](https://dytvr9ot2sszz.cloudfront.net/logz-docs/telemetry-agent/collector-localhost-finish.png)

### 5. Collect data

That’s it! It might take a while for the Telemetry Collector to get up and running, after which you’ll be able to view your logs, metrics, or traces and get full observability into your system.

## Manage your Telemetry Collector:

To manage an AWS Telemetry Collector on your **Linux** machine, you can use the following commands:

|Description|Command|
|--|--|
|**Collector Binary:** |`/opt/logzio-agent/logzio-otel-collector/otelcol-logzio-linux_amd64`|
|**Collector Config:**|`/opt/logzio-agent/logzio-otel-collector/otel_config.yaml`|
|**Logz.io Agent Logs:** |`/opt/logzio-agent/logzio_agent.log`|
|**Start Service:** |`sudo systemctl start logzioOTELCollector`|
|**Stop Service:** |`sudo systemctl stop logzioOTELCollector`|
|**Delete Service:** |`sudo /opt/logzio-agent/logzio-otel-collector/delete_service.bash`|
|**Show Service:** |`sudo systemctl` &#124; `grep logzioOTELCollector`|
|**Show Service Logs:** |`sudo systemctl status -l logzioOTELCollector`|


If you have additional questions about managing your Telemetry Collector, [contact Logz.io's Support team](mailto:help@logz.io).


###### Additional resources

* [View Telemetry Collector on GitHub](https://github.com/logzio/logzio-agent-manifest)