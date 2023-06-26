---
sidebar_position: 3
title: Send Kubernetes Data with Telemetry Collector
---

:::note
Telemetry Collector is currently **available in all regions** except for Japan and Australia. If you're located in these regions, you can use **[Logz.io’s data shippers](https://app.logz.io/#/dashboard/send-your-data/collection?tag=all&collection=all)** to send your data.
:::

To start sending your Kubernetes data through the Telemetry Collector, you'll need the following:

* Admin privileges in your Logz.io account
* Outgoing traffic to destination ports `8053` and `8071` allowed

_If you're unsure whether traffic is allowed to these ports, continue the process, and Logz.io will notify you if access is restricted._


Navigate to [Send your data](https://app.logz.io/#/dashboard/send-your-data), and click on **Start collecting**.

:::caution Important
To configure the Telemetry Collector, you must be logged into your **main** Logz.io account.
:::


![Start collecting button](https://dytvr9ot2sszz.cloudfront.net/logz-docs/telemetry-agent/telemetry-start-here.png)

## Send Kubernetes data
### 1. Select your platform


Select the platform through which you’d like to ship your data. Then, if required, select the relevant sub-type.

![Select platform](https://dytvr9ot2sszz.cloudfront.net/logz-docs/telemetry-agent/telemetry-collector-main-aug22.png)

### 2. Select data sources

Next, select the data sources. Hover over each source to see the type of data it collects and processes.

*You'll have to manually [define auto-instrumentation](https://docs.logz.io/user-guide/distributed-tracing/tracing-instrumentation) to collect your **Distributed Tracing** through Logz.io’s Telemetry Collector.*

![Select data source](https://dytvr9ot2sszz.cloudfront.net/logz-docs/telemetry-agent/telemetry-step-2.png)

### 3. Define your collector

Choose a name and write a description to help identify the collector. 

Under **Accounts**, you can review the Logs, Metrics, and Tracing accounts to which the Telemetry Collector will send the data. If you don't have an existing account, you'll be able to review the account's name before continuing.

Click **Generate snippet** to continue.

![Define collector](https://dytvr9ot2sszz.cloudfront.net/logz-docs/telemetry-agent/telemetry-step-3.png)

Next, review your collector. The Summary, located on the left side of the screen, includes all of the data in the collector.

### 4. Choose a platform

Choose the platform on which you want to run the Telemetry Collector. You can choose between **Mac**, **Windows**, or **Linux**. 

* **Mac** users - Copy the snippet and run it in your terminal.
* **Windows** users - Copy the snippet and run it in your PowerShell x64 **as Administrator** (Note that PowerShell x86 and PowerShell ISE are currently not supported).
* **Linux** users - Copy the snippet and run it in your command line.

:::note
Some platforms might require additional details, such as admin privileges or passwords to complete the installation. These details are not sent to or stored by Logz.io.
:::

![Review collector](https://dytvr9ot2sszz.cloudfront.net/logz-docs/telemetry-agent/telemetry-snippet-last-step.png)

### 5. Run the Telemetry Collector

The Telemetry Collector will create all setters needed for the Helm install command to install Logz.io Helm chart and deploy the chart with the relevant parameters. Once running, the Telemetry Collector will continuously collect the relevant data from your end, and you'll be able to view and manage it in Logz.io.

You can review the complete list of parameters and commands that Logz.io runs in the background [on the **Logzio Monitoring GitHub repository**](https://github.com/logzio/logzio-helm/tree/master/charts/logzio-monitoring).

### 6. Collect data

That’s it! It might take a while for the Telemetry Collector to get up and running, after which you’ll be able to view your logs, metrics, or traces and get full observability into your system.


## Manage your Telemetry Collector


To manage a Kubernetes Telemetry Collector, you can use the following commands:

|Description|Command|
|-|-|
| **Show Helm Status:** | `helm status -n monitoring logzio-monitoring` |
| **Get Pods:** | `kubectl get pods -n monitoring` |
| **Show Pod's Logs:** | `kubectl logs <<POD_NAME>> -n monitoring` |
| **Show Pod's Info:** | `kubectl describe pod <<POD_NAME>> -n monitoring` |

_Replace `<<POD_NAME>>` with your pod's name._


If you're running your Kubernetes Telemetry Collector from a **Windows** machine, you can use the following commands to gain access to the Helm chart and Logz.io's logs:

|Description|Command|
|-|-|
| **Logz.io Helm:** | `C:\Users\<<USERNAME>>\AppData\Roaming\LogzioAgent\LogzioKubernetes\logzio_helm.txt` |
| **Logz.io Telemetry Collector Logs:** | `C:\Users\<<USERNAME>>\AppData\Roaming\LogzioAgent\logzio_agent.log` |
| **Install Logz.io Helm:** | `Invoke-Expression -Command (Get-Content -Path C:\Users\<<USERNAME>>\AppData\Roaming\LogzioAgent\LogzioKubernetes\logzio_helm.txt)` |
| **Uninstall Logz.io Helm:** | `helm uninstall -n monitoring logzio-monitoring` |

_Replace `<<USERNAME>>` with your Windows user name._


If you have additional questions about managing your Telemetry Collector, [contact Logz.io's Support team](mailto:help@logz.io).


## Remove your Telemetry Collector

You can uninstall your Telemetry Collector from **Kubernetes** by running the following snippet in the same platform you've used to install it:

`helm uninstall -n monitoring logzio-monitoring`

* **Mac** - Run the snippet in your terminal.
* **Windows** - Run the snippet in your PowerShell x64 **as Administrator**.
* **Linux** - Run the snippet in your command line.


This snippet removes the collector from Logz.io and stops sending your data. Of course, you can always create a new collector or use Logz.io's **[Send your data](https://app.logz.io/#/dashboard/send-your-data)** to ship your data.

If you have additional questions about managing your Telemetry Collector, [contact Logz.io's Support team](mailto:help@logz.io).


###### Additional resources

* [View Telemetry Collector on GitHub](https://github.com/logzio/logzio-agent-manifest)