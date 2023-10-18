---
sidebar_position: 3
title: Send Kubernetes Data with Telemetry Collector
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Send your Kubernetes data with Logz.io's Telemetry Collector
keywords: [Kubernetes, ship kubernetes data, kubernetes logs, kubernetes metrics, kubernetes tracing]
---

:::note
Telemetry Collector is currently **available in all regions** except for Japan and Australia. If you're located in these regions, you can use **[Logz.io’s data shippers](https://app.logz.io/#/dashboard/send-your-data/collection?tag=all&collection=all)** to send your data.
:::

To start sending your Kubernetes data through the Telemetry Collector, you'll need the following:

* Admin privileges in your Logz.io account
* Outgoing traffic to destination ports `8053` and `8071` allowed

_If you're unsure whether traffic is allowed to these ports, continue the process, and Logz.io will notify you if access is restricted._


Navigate to [Send your data](https://app.logz.io/#/dashboard/send-your-data), and click on **Go to the Telemetry Collector**.

:::caution Important
To configure the Telemetry Collector, you must be logged into your **main** Logz.io account.
:::


![Start collecting button](https://dytvr9ot2sszz.cloudfront.net/logz-docs/telemetry-agent/start-collecting-sep.png)

## Send Kubernetes data

### Select your environment


Select the environment through which you’d like to ship your data. Then, if required, select the relevant sub-type.

![Select platform](https://dytvr9ot2sszz.cloudfront.net/logz-docs/telemetry-agent/telemetry-collector-main-sep.png)

### Activate your collector

Choose the platform on which you want to run the Telemetry Collector. You can choose between **Helm**, **Mac**, **Windows**, or **Linux**. 

* **Helm** users - Connect to the Kubernetes cluster from which you want to send telemetry, copy the Helm Install snippet, replace the placeholders with the relevant values, and run it in your terminal.
* **Mac** users - Copy the snippet and run it in your terminal.
* **Windows** users - Copy the snippet and run it in your PowerShell x64 **as Administrator** (Note that PowerShell x86 and PowerShell ISE are currently not supported).
* **Linux** users - Copy the snippet and run it in your command line.

:::note
Some platforms might require additional details, such as admin privileges or passwords to complete the installation. These details are not sent to or stored by Logz.io.
:::

![Review collector](https://dytvr9ot2sszz.cloudfront.net/logz-docs/telemetry-agent/activate-collector-sep.png)

### Run the Telemetry Collector

The Telemetry Collector will create all setters needed for the Helm install command to install Logz.io Helm chart and deploy the chart with the relevant parameters. Once running, the Telemetry Collector will continuously collect the relevant data from your end, and you can view and manage it in Logz.io.

You can review the complete list of parameters and commands that Logz.io runs in the background [on the **Logzio Monitoring GitHub repository**](https://github.com/logzio/logzio-helm/tree/master/charts/logzio-monitoring).

It might take a while for the Telemetry Collector to get up and running, after which you can view your logs, metrics, or traces and get full observability into your system.

### Optional - Select data sources

You can configure the data sources the Telemetry Collector will collect. To do so, click on **Advance settings** at the top of the page. Next, you can edit and change telemetries, which Logz.io will collect.


![Select data source](https://dytvr9ot2sszz.cloudfront.net/logz-docs/telemetry-agent/select-data-sources-sep.png)


<!-- *You'll have to manually [define auto-instrumentation](https://docs.logz.io/user-guide/distributed-tracing/tracing-instrumentation) to collect your **Distributed Tracing** through Logz.io’s Telemetry Collector.* -->



### Optional - Define your collector

You can edit your collector’s name and description and choose which Logs, Metrics, and Tracing accounts to use. If you don’t have active accounts, you’ll be able to review the newly generated account names before continuing.

Click **Save changes** to continue.

![Define collector](https://dytvr9ot2sszz.cloudfront.net/logz-docs/telemetry-agent/define-collector-sep.png)




## Manage your Telemetry Collector:


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


### Remove your Telemetry Collector:

You can uninstall your Telemetry Collector from **Kubernetes** by running the following snippet in the same platform you've used to install it:

`helm uninstall -n monitoring logzio-monitoring`

* **Mac** - Run the snippet in your terminal.
* **Windows** - Run the snippet in your PowerShell x64 **as Administrator**.
* **Linux** - Run the snippet in your command line.


This snippet removes the collector from Logz.io and stops sending your data. Of course, you can always create a new collector or use Logz.io's **[Send your data](https://app.logz.io/#/dashboard/send-your-data)** to ship your data.

If you have additional questions about managing your Telemetry Collector, [contact Logz.io's Support team](mailto:help@logz.io).


## Additional resources

* [View Telemetry Collector on GitHub](https://github.com/logzio/logzio-agent-manifest)