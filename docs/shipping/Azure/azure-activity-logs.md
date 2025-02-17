---
id: Azure-Activity-logs
title: Azure Activity Logs
overview: Ship your Azure activity logs using an automated deployment process.
product: ['logs', 'siem']
os: ['windows', 'linux']
filters: ['Azure', 'Security']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/azure-monitor.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---


Automate the deployment of your Azure activity logs. By the end of this process, you will have an event hub namespace, an event hub, and two storage blobs configured.

The deployed resources will collect data from a single Azure region.

:::note
[Project's GitHub repo](https://github.com/logzio/logzio-azure-serverless/)
:::

<!--
### Overview of the services you'll be setting up in your Azure account

The automated deployment sets up a new Event Hub namespace and all the components you'll need to collect logs in one Azure region.

Each automated deployment sets up these resources in your Azure environment:

* 1 namespace
* 1 Azure function
* 1 event hub
* 2 blobs (1 to store logs from the Azure functions, 1 for failover storage)

### Determining how many automated deployments to deploy

You'll need an event hub in the same region as your services.

How many automated deployments you will need, depends on the number of regions involved.

You'll need at least 1 automated deployment for each region where you want to collect logs.This is because Azure requires an event hub in the same region as your services. The good news is you can stream data from multiple services to the same event hub, just as long as they are in the same region.

-->

## Configuration

### 1. Deploy the Logz.io template 👇

[![Deploy to Azure](https://dytvr9ot2sszz.cloudfront.net/logz-docs/azure_blob/deploybutton-az.png)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Flogzio%2Flogzio-azure-serverless%2Fmaster%2Fdeployments%2Fazuredeploylogs.json)

This deployment will create the following services in Azure:

* Serverless Function App
* Event Hub Namespace
* Storage Account for Function Logs
* Backup Storage Account for Failed Shipments
* App Service Plan
* Application Insights

<!-- ![Customized template](https://dytvr9ot2sszz.cloudfront.net/logz-docs/azure-event-hubs/customized-template.png) -->

If you have already set up an automated deployment in this region, you can skip to the next step.

### 2. Configure the template

Use the following settings:

| Parameter | Description |
|---|---|
| Resource group* | Create a new resource group or select an existing one, then click **OK**.|
| Region* | Select the same region as the Azure services that will stream data to this event hub. |
| Debug* | Add debug logs to your function app. |
| Shipping token* | Add the [logs shipping token](https://app.logz.io/#/dashboard/settings/general) for the Logz.io account where you want to send data.  |
| Logs listener host* (Default: `listener.logz.io`)| Use the listener URL specific to your Logz.io account’s region. You can find it [here](https://docs.logz.io/user-guide/accounts/account-region.html). |
| buffersize (Default: 100) | Defines the maximum number of messages the logger accumulates before sending them in bulk.  |

*Required fields.

For all other parameters:

* To use existing services, enter the corresponding service name.
* Otherwise, the template will automatically create the necessary services.

At the bottom of the page, click **Review + Create**, then select **Create** to deploy.

Deployment may take a few minutes.

### 3. Stream Azure service data to your new event hubs

Once deployment is complete, configure Azure to stream service logs to the new event hub so that your function apps can forward them to Logz.io.

To send your data to this event hub choose your **service type** and create **diagnostic settings** for it. 

Under `Event hub policy name`, select `LogzioLSharedAccessKey` for logs.

Changes may take time to apply, and some services may require a restart.

For more details, see Microsoft's guide [Stream Azure monitoring data to an event hub for consumption by an external tool](https://docs.microsoft.com/en-us/azure/monitoring-and-diagnostics/monitor-stream-monitoring-data-event-hubs).

![Diagnostic-settings](https://dytvr9ot2sszz.cloudfront.net/logz-docs/azure-event-hubs/azure-diagnostic-settings.png)


### 4. Check Logz.io for your data

Give your data some time to be processed, and then open Logz.io.

If everything went according to plan, you should see logs with the type `eventHub` in Explore.

### Backing up your logs!

This deployment includes an automatic backup mechanism in case of connection issues or shipping failures. Logs that weren't shipped to Logz.io will be uploaded to the blob storage `logziologsbackupstorage` under the container `logziologsbackupcontainer`.

## Modifying configuration after deployment

To update parameter values post-deployment, go to your function app page in Azure, then on the left menu press the **Configuration** tab.

You'll have the option to edit the following values:

* Shipper's configurations such as `LogzioHost`, `LogzioToken`, `Buffersize`.
* FUNCTIONS_WORKER_PROCESS_COUNT - maximum of 10, see more details [here](https://docs.microsoft.com/en-us/azure/azure-functions/functions-app-settings#functions_worker_process_count).
* ParseEmptyFields - (Default: `false`) If Azure logs contain empty fields that prevent parsing in Kibana, set this to `true`. **Note that this option may impact the shipper's perfomance.**

![Function's configuration](https://dytvr9ot2sszz.cloudfront.net/logz-docs/azure-event-hubs/azure-configuration-settings.png)


## Migration to log analytics workspace-based model

If you are still using Classic Application Insights, migrating to the Log Analytics Workspace-based model is required.

To migrate:

1. Navigate to your Application Insights resource that hasn't been migrated yet.
2. Click the "Classic Application Insights is deprecated" notification.
3. In the "Migrate to Workspace-based" dialog, confirm your preferred Log Analytics Workspace and click **Apply**.

**Important**: Migration to the workspace-based model is **irreversible**.