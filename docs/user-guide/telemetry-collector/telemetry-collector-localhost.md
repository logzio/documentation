---
sidebar_position: 4
title: Send Localhost Data with Telemetry Collector
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Send your Localhost data with Logz.io's Telemetry Collector
keywords: [log-shipping, telemetry collector, localhost data, local host, agent, collector, mac, linux, windows]
---

:::note
Telemetry Collector is currently **available in all regions** except for Japan and Australia. If you're located in these regions, you can use **[Logz.io’s data shippers](https://app.logz.io/#/dashboard/send-your-data/collection?tag=all&collection=all)** to send your data.
:::

To start sending Localhost data through the Telemetry Collector, Log into your **main** Logz.io account, navigate to the [Integration hub](https://app.logz.io/#/dashboard/integrations/collectors) and choose one of the integrations under **Quick Setup**.

:::caution Important
To configure the Telemetry Collector, you must be logged into your **main** Logz.io account.
:::


![Start collecting button](https://dytvr9ot2sszz.cloudfront.net/logz-docs/telemetry-agent/quick-setup-localhost-dec.png)


## Send Localhost data

<!-- 
### Select your environment

Select your preferred Localhost platform through which you want to send your data.

![Localhost select platform](https://dytvr9ot2sszz.cloudfront.net/logz-docs/telemetry-agent/collector-localhost-sep.png)
-->

### Activate your collector

Select your preferred Localhost platform through which you want to send your data.

Copy the code snippet and run it on your end:

* **Windows** users - Run the snippet in your PowerShell x64 **as Administrator** (Note that PowerShell x86 and PowerShell ISE are currently not supported).
* **Linux** and **Mac** users - Run the snippet in your terminal. Note that your Bash version should be **4.0** or higher.

Some platforms might require additional details, such as admin privileges or passwords, to complete the installation. These details are not sent to or stored by Logz.io.

![Review collector](https://dytvr9ot2sszz.cloudfront.net/logz-docs/telemetry-agent/activate-localhost-dec.png)

It might take a while for the Telemetry Collector to get up and running, after which you can view your logs or metrics and get full observability into your system.

### _Optional_ - Configure data sources

You can configure the data sources the Telemetry Collector will collect. To do so, click on **Advance settings** at the top of the page. 

You can review and edit the telemetries collected by Logz.io, or change the location of your data.

![Select folder collector](https://dytvr9ot2sszz.cloudfront.net/logz-docs/telemetry-agent/configure-localhost-data-sources-dec.png)

<!-- If you're running on a **Windows** machine, you can choose whether you want to collect application, security, and system logs.-->

### _Optional_ - Define your collector

You can edit your collector’s name and description and choose which Logs, Metrics, and Tracing accounts to use. To do so, click on **Advance settings** at the top of the **Activate your collector** page, and click **Next** to reach the **Finalize Telemetry Collector** page.

If you don't have Logs, Metrics, or Traces accounts, you can review the newly generated accounts.

Click **Save changes** to continue.

![Define collector](https://dytvr9ot2sszz.cloudfront.net/logz-docs/telemetry-agent/localhost-finalize-dec.png)


If you encounter issues in installing or running your Telemetry Collector, [contact Logz.io's Support team](mailto:help@logz.io).


## Manage and remove a Telemetry Collector:

To manage a Localhost Telemetry Collector on your **Linux** machine, you can use the following commands:

|Description|Command|
|-|-|
|**Collector Binary:** |`/opt/logzio-agent/logzio-otel-collector/otelcol-logzio-linux_amd64`|
|**Collector Config:**|`/opt/logzio-agent/logzio-otel-collector/otel_config.yaml`|
|**Logz.io Agent Logs:** |`/opt/logzio-agent/logzio_agent.log`|
|**Start Service:** |`sudo systemctl start logzioOTELCollector`|
|**Stop Service:** |`sudo systemctl stop logzioOTELCollector`|
|**Delete Service:** |`sudo /opt/logzio-agent/logzio-otel-collector/delete_service.bash`|
|**Show Service:** |`sudo systemctl` &#124; `grep logzioOTELCollector`|
|**Show Service Logs:** |`sudo systemctl status -l logzioOTELCollector`|

To manage a Localhost Telemetry Collector on your **Mac** machine, you can use the following commands:

|Description|Command|
|-|-|
|**Collector Binary:**| `/opt/logzio-agent/logzio-otel-collector/otelcol-logzio-darwin_amd64`|
|**Collector Config:**| `/opt/logzio-agent/logzio-otel-collector/otel_config.yaml`|
|**Logz.io Agent Logs:**| `/opt/logzio-agent/logzio_agent.log`|
|**Start Service:**| `sudo launchctl load /Library/LaunchDaemons/com.logzio.OTELCollector.plist`|
|**Stop Service:**| `sudo launchctl stop com.logzio.OTELCollector`|
|**Delete Service:**| `sudo /opt/logzio-agent/logzio-otel-collector/delete_service.bash`|
|**Show Service:**| `sudo launchctl list` &#124; `grep com.logzio.OTELCollector`|
|**Show Service Logs:**| `sudo tail -F /opt/logzio-agent/logzio-otel-collector/logzio_otel_collector.log`|

To manage a Localhost Telemetry Collector on your **Windows** machine, you can use the following commands:

|Description|Command|
|-|-|
| **Collector Binary:** | `C:\Users\<<USERNAME>>\AppData\Roaming\LogzioAgent\LogzioOTELCollector\otelcol-logzio-windows_amd64.exe` |
| **Collector Config:** | `C:\Users\<<USERNAME>>\AppData\Roaming\LogzioAgent\LogzioOTELCollector\otel_config.yaml` |
| **Logz.io Agent Logs:** | `C:\Users\<<USERNAME>>\AppData\Roaming\LogzioAgent\logzio_agent.log` |
| **Start Service Command:** | `Start-Service -Name LogzioOTELCollector` |
| **Stop Service Command:** | `Stop-Service -Name LogzioOTELCollector` |
| **Delete Service Command** | `sc.exe DELETE LogzioOTELCollector` (stop the service before deleting it) |
| **Show Service Command:** | `Get-Service -Name LogzioOTELCollector` |
| **Show Logs Command:** | `eventvwr.msc ('Windows Logs'->'Application' all logs with source 'LogzioOTELCollector')` |


Replace `<<USERNAME>>` with your Windows user name. If you have additional questions about managing your Telemetry Collector, [contact Logz.io's Support team](mailto:help@logz.io).


## Additional resources

* [View Telemetry Collector on GitHub](https://github.com/logzio/logzio-agent-manifest)