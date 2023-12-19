---
sidebar_position: 2
title: Send AWS data with Telemetry Collector
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Send your AWS data with Logz.io's Telemetry Collector
keywords: [AWS, Amazon Web Service, ship AWS data, AWS logs, AWS metrics, AWS tracing]
---

:::note
Telemetry Collector is currently **available in all regions** except for Japan and Australia. If you're located in these regions, you can use **[Logz.io’s data shippers](https://app.logz.io/#/dashboard/send-your-data/collection?tag=all&collection=all)** to send your data.
:::

To start sending your AWS data through the Telemetry Collector, Log into your **main** Logz.io account, navigate to the [Integration hub](https://app.logz.io/#/dashboard/integrations/collectors) and choose one of the AWS integrations available under the **Quick Setup** option.


:::caution Important
To configure the Telemetry Collector, you must be logged into your **main** Logz.io account.
:::

:::caution Important
This integration is only compatible with Amazon Linux version 2 on EC2. The use of version 1 is deprecated.
:::

![Start collecting button](https://dytvr9ot2sszz.cloudfront.net/logz-docs/telemetry-agent/aws-shippers.png)

## Prerequisite

The IAM role assigned to the EC2 instance must include the `ec2:DescribeTags` permission in its policy.

## Configure AWS Logs / Metrics

### Select data sources

Each AWS environment requires different elements to collect your data.

* **AWS Logs** - Select your region, AWS services, and Custom Log Groups.
* **AWS Metrics** - Select your region and AWS namespace.
* **EC2 Monitoring** - Auto collects the data. Logz.io uses OpenTelemetry to monitor your EC2.

![Select data source](https://dytvr9ot2sszz.cloudfront.net/logz-docs/telemetry-agent/collector-data-sources-dec.png)


<!--
### Select your environment

Select the AWS platform and the relevant sub-type through which you want to send your data.

![Select platform](https://dytvr9ot2sszz.cloudfront.net/logz-docs/telemetry-agent/collector-main-aws-sep.png)
-->

### Define your collector

You can edit your collector’s name and description and choose which Logs, Metrics, and Tracing accounts to use. If you don’t have active accounts, you can review the newly generated account names before continuing.

Click **Generate collector** to continue.

![Define collector](https://dytvr9ot2sszz.cloudfront.net/logz-docs/telemetry-agent/finalize-telemetry-dec.png)


### _Optional_ - Define your EC2 collector

You can configure the data sources the Telemetry Collector will collect. To do so, after choosing the EC2 Monitoring option, click on **Advance settings** at the top of the page. Next, you can edit and change the location of your logs, and whether you want to monitor both logs and metrics. 


![configure ec2 data source](https://dytvr9ot2sszz.cloudfront.net/logz-docs/telemetry-agent/ec2-configure-dec.png)


### Install the Telemetry Collector


Login to your AWS account, launch the AWS stack to run stack configuration and click the **Run AWS stack** button to activate your collector. 

:::note
Some platforms require additional details, such as admin privileges or passwords, to complete the installation. These details are not sent to or stored by Logz.io.
:::

![Review collector](https://dytvr9ot2sszz.cloudfront.net/logz-docs/telemetry-agent/activate-aws-sep.png)

It might take a while for the Telemetry Collector to get up and running, after which you can view your logs, metrics, or traces and get full observability into your system.

## Manage your EC2 Telemetry Collector:

To manage an AWS EC2 Telemetry Collector on your **Linux** machine, you can use the following commands:

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


## Additional resources

* [View Telemetry Collector on GitHub](https://github.com/logzio/logzio-agent-manifest)