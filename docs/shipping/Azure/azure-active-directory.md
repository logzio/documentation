---
id: azure-active-Directory
title: Azure Active Directory
overview: You can ship logs available from the Microsoft Graph APIs with Logzio-MSGraph.
product: ['siem']
os: ['windows', 'linux']
filters: ['Azure', 'Access Management']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/azure.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---


You can ship logs available from the Microsoft Graph APIs with Logzio-MSGraph.
Logzio-MSGraph is a self-hosted application.

Logzio-MSGraph supports these APIs:

* Azure Active Directory audit logs
* Azure Active Directory sign-in logs

There are many other APIs available through Microsoft Graph.
If you don't see your API in the list,
please [open an issue](https://github.com/logzio/microsoft-graph/issues/new) at GitHub to request it.

 

### Register a new app in Azure Active Directory

In the Azure portal, go to [App registration](https://portal.azure.com/#blade/Microsoft_AAD_RegisteredApps/ApplicationsListBlade)
and select **New registration** from the top menu.

Name your app and click **Register**.

### Create a client secret

Choose **Certificates & secrets** from the side menu,
and click on **New client secret**.

Add a **Description**.
We recommend something specific, such as "secret for Logzio-MSGraph integration".

In the **Expires** list, choose **Never**.

Click **Add**.

Copy the value of the generated secret to your text editor.
You'll need this later.

:::note
You won't be able to retrieve the secret's value after you leave this page.
:::
 

### Set the app's permissions

Choose **API permissions** from the side menu,
and click **Add a permission**.

Select **Microsoft Graph > Application permissions**.

Select these items:

* **AuditLog.Read.All**
* **Directory.Read.All**

Click **Add permissions**.

Click **Grant admin consent for Default Directory**, and then click **Yes** to confirm.

:::note
Only Azure administrators can grant consent for Default Directory. If the _Grant admin consent_ button is disabled, ask your Azure admin to update the setting for you.
:::
 

### Create a configuration file

Create a configuration yaml file (`logzio-msgraph-config.yaml`) for Logzio-MSGraph.

For a complete list of options, see the configuration parameters below.👇

```yaml
senderParams:
  accountToken: "<<LOG-SHIPPING-TOKEN>>"
  listenerUrl: "<<LISTENER-HOST>>"

azureADClient:
  pullIntervalSeconds: 300
  tenantId: "<<AD_TENANT_ID>>"
  clientId: "<<APP_CLIENT_ID>>"
  clientSecret: "<<APP_CLIENT_SECRET_VALUE>>"

logLevel: INFO
```

#### Parameters

| Parameter | Description | Required/Default |
|---|---|---|
| senderParams.accountToken | Your Logz.io account token. {@include: ../../_include/log-shipping/log-shipping-token.html} | Required |
| senderParams.listenerUrl  | Listener URL.    {@include: ../../_include/log-shipping/listener-var.html}  | `listener.logz.io` |
| senderParams.fromDisk  | If `true`, logs are stored on disk until they're shipped. (See **If from-disk=true** below). If `false`, logs persist in memory until they're shipped. (See **If from-disk=false** below. | `true` |
| senderParams.senderDrainIntervals | How often the sender should drain the queue, in seconds. | `30` |
| azureADClient.tenantId  | Azure Active Directory tenant ID. You can find this in the _Overview_ section of the app you registered in step 1. | Required |
| azureADClient.clientId  | Application client ID.    You can find this in the _Overview_ section of the app you registered in step 1. | Required |
| azureADClient.clientSecret | Value of the Application Client Secret you created in step 2. | Required |
| azureADClient.pullIntervalSeconds | Time interval, in seconds, to pull the logs with the Graph API. | `300` |
| logLevel | Log level for Logizo-MSGraph to omit. Can be one of: `OFF`, `ERROR`, `WARN`, `INFO`, `DEBUG`, `TRACE`, `ALL`. | `INFO` |
| targetApi	 | Specifies types of api lists to run, each API provider has its own list. Must contain at least 1 list with 1 api in the list. Current supported providers: ADApis, ASCApis. | Required |

#### If fromDisk=true

| Parameter | Description | Required/Default |
|---|---|---|
senderParams.fileSystemFullPercentThreshold  | Threshold percentage of disk space at which to stop queueing. If this threshold is reached, all new logs are dropped until used space drops below the threshold. Set to `-1` to ignore threshold. | `98` |
| senderParams.gcPersistedQueueFilesIntervalSeconds | Time interval, in seconds, to clean sent logs from the disk. | `30` |
| senderParams.diskSpaceCheckInterval | Time interval, in milliseconds, to check for disk space.| `1000` |

#### If fromDisk=false 

| Parameter | Description | Required/Default |
|---|---|---|
| senderParams.inMemoryQueueCapacityInBytes  | The amount of memory, in bytes, Logzio-MSGraph can use for the memory queue. Set to `-1` for unlimited bytes. | `1024 * 1024 * 100` |
| senderParams.logsCountLimit | The number of logs in the memory queue before dropping new logs. Set to `-1` to configure the sender to not limit the queue by logs count. | `-1` |

### Download and run Logzio-MSGraph

You can launch Logzio-MSGraph in a Docker container or as a standalone Java app.

In a Docker container:

```shell
docker run -d -v $(pwd)/logzio-msgraph-config.yaml:/config.yaml logzio/logzio-msgraph
```

Or to run as a standalone Java app,
download the latest jar from the [release page](https://github.com/logzio/microsoft-graph/releases).
Then run:

```shell
java -jar logzio-msgraph.jar logzio-msgraph-config.yaml
```

Logs collected by this integration will have the type `Microsoft-Graph`

### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [log shipping troubleshooting]({{site.baseurl}}/user-guide/log-shipping/log-shipping-troubleshooting.html).

 
