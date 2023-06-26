---
sidebar_position: 4
title: Send Localhost Data with Telemetry Collector
---

:::note
Telemetry Collector is currently **available in all regions** except for Japan and Australia. If you're located in these regions, you can use **[Logz.io’s data shippers](https://app.logz.io/#/dashboard/send-your-data/collection?tag=all&collection=all)** to send your data.
:::

To start sending Localhost data through the Telemetry Collector, Log into your **main** Logz.io account, navigate to [Send your data](https://app.logz.io/#/dashboard/send-your-data), and click on **Start collecting**.

:::caution Important
To configure the Telemetry Collector, you must be logged into your **main** Logz.io account.
:::


![Start collecting button](https://dytvr9ot2sszz.cloudfront.net/logz-docs/telemetry-agent/telemetry-start-here.png)


## Send Localhost data

### 1. Select platform

Select the Localhost platform and the relevant sub-type through which you want to send your data.

![Localhost select platform](https://dytvr9ot2sszz.cloudfront.net/logz-docs/telemetry-agent/tc-select-localhost.png)

### 2. Select data sources


Enter the full path location of your log folders from your machine. You can add multiple log folders or files by clicking on the **Add a folder**/**Add a file** option.

The Telemetry Collector can also collect metrics data from your logs.

![Select folder collector](https://dytvr9ot2sszz.cloudfront.net/logz-docs/telemetry-agent/log-location.png)

If you're running on a **Windows** machine, you'll be able to choose whether you want to collect application, security, and system logs.

### 3. Define your collector

Choose a name and write a description to help identify the collector. 

Under **Accounts**, you can review the Logs and Metrics accounts to which the Telemetry Collector will send the data. If you don’t have an existing account, one will be created for you, and you’ll be able to review its name before continuing.

Click **Generate snippet** to continue.

![Define collector](https://dytvr9ot2sszz.cloudfront.net/logz-docs/telemetry-agent/define-collector-localhost.png)

### 4. Run the Telemetry Collector

Copy the code snippet and run it on your end:

* **Mac** and **Linux** users - Run the snippet in your terminal.
* **Windows** users - Run the snippet in your PowerShell x64 **as Administrator** (Note that PowerShell x86 and PowerShell ISE are currently not supported).

Some platforms might require additional details, such as admin privileges or passwords, to complete the installation. These details are not sent to or stored by Logz.io.

![Review collector](https://dytvr9ot2sszz.cloudfront.net/logz-docs/telemetry-agent/collector-localhost-finish.png)

### 5. Collect data

That’s it! It might take a while for the Telemetry Collector to get up and running, after which you’ll be able to view your logs or metrics and get full observability into your system.

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


###### Additional resources

* [View Telemetry Collector on GitHub](https://github.com/logzio/logzio-agent-manifest)