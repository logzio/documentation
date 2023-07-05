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


Ship your Azure activity logs using an automated deployment process.
At the end of this process, your Azure function will forward logs from an Azure Event Hub to your Logz.io account.


![Overview of Azure Diagnostic Logz.io integration](https://dytvr9ot2sszz.cloudfront.net/logz-docs/log-shipping/azure-diagnostic-logs-overview.png)

###### Overview of the services you'll be setting up in your Azure account

The automated deployment sets up a new Event Hub namespace and all the components you'll need to collect logs in one Azure region.

The automated deployment will create the following services:

* Serveless Function App
* Event Hubs Namspace
* Storage Account for the Function's logs
* Storage Account for backing up failed shipping
* App Service Plan
* Application Insights


###### You'll need an event hub in the same region as your services

How many automated deployments you will need, depends on the number of regions involved.
You'll need at least 1 automated deployment for each region where you want to collect logs.


This is because Azure requires an event hub in the same region as your services. The good news is you can stream data from multiple services to the same event hub, just as long as they are in the same region.


###### Backing up your logs

This deployment will automatically back up your data in case of connection or shipping errors.

If this happens, the logs that weren't shipped to Logz.io will be uploaded to the blob storage `logziologsbackupstorage` under the container `logziologsbackupcontainer`.


#### Configuration

 

##### Configure an automated deployment

You can skip this step if you have already set up an automated deployment in this region before.

👇 Otherwise, click this button to start the automated deployment.

[![Deploy to Azure](https://dytvr9ot2sszz.cloudfront.net/logz-docs/azure_blob/deploybutton-az.png)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Flogzio%2Flogzio-azure-serverless%2Fmaster%2Fdeployments%2Fazuredeploylogs.json)
{:.override.btn-img}


You'll be taken to Azure, where you'll configure the resources to be deployed.

###### Recommended settings



| Parameter | Description |
|---|---|
| Resource group (**Required**) | Create a new resource group or select an existing one, and click **OK**. |
| Region (**Required**) | Select the same region as the Azure services that will stream data to this event hub. |
| Shipping token (**Required**) | Add the [Log shipping token](https://app.logz.io/#/dashboard/settings/general) for the Logz.io account you want to ship to.  |
| Logs listener host (Default: `listener.logz.io`)| Use the listener URL specific to the region of your Logz.io account. You can look it up [here](https://docs.logz.io/user-guide/accounts/account-region.html). |
| buffersize (Default: `100`) | The maximum number of messages the logger will accumulate before sending them in bulk.  |

For all other parameters: To use your existing services, change the parameter to the relevant service name. Otherwise, the template will build the necessary services automatically.

At the bottom of the form, select **Review + Create**. Next, click **Create** to deploy.
Deployment can take a few minutes.

##### Stream data to the new event hub

So far in this process, you've deployed an event hub and a function app.

Now you'll need to configure Azure to stream diagnostic logs to the event hub you just deployed.
When data comes into the event hub, the function app will forward that data to Logz.io.

Navigate to the **Diagnostics settings** page (You can search for it).
Choose a resource from the list of resources, and select **Turn on diagnostics settings** to open the _Diagnostics settings_ panel for that resource.

* Give your diagnostic settings a **Name**.
* Select **Stream to an event hub**. Next, select **Configure** to open the _Select event hub_ panel.


![Stream data to the new event hub](https://dytvr9ot2sszz.cloudfront.net/logz-docs/log-shipping/diagnostic-settings.png)


Select your event hub:

* **Event hub namespace**: Select the namespace that begins with **LogzioLNS** (For example, `LogzioLNS6nvkqdcci10p`)
* **Event hub name**: Select **logzioeventhub**
* **Event hub policy name**: Select **LogzioLSharedAccessKey**
* Click **OK** to return to the _Diagnostics settings_ panel.

* **Log**: In the _log_ section, select the data you want to stream, and then click **Save**.

The selected data will now begin streaming to the event hub.

##### Check Logz.io for your logs

Give your data some time to get from your system to ours, and then open your [Logz.io Open Search Dashboards account](https://app.logz.io/#/dashboard/osd/discover?).
If everything went according to plan, you should see logs of the `type:eventHub` in Open Search Dashboards.

If you still don’t see your logs, see [log shipping troubleshooting](https://docs.logz.io/user-guide/log-shipping/log-shipping-troubleshooting.html).


##### Updating your parameters after deployment

You may find that you want to make changes to the parameter values after you've deployed. Here's what you can do:

* Go to your function app page
* Select the **Configuration** tab in the left menu.

You'll have the option to edit the following values:

* The shipper's configurations, including: LogzioHost, LogzioToken, Buffersize.
* FUNCTIONS_WORKER_PROCESS_COUNT - maximum of 10. [Learn more in Azure Docs](https://docs.microsoft.com/en-us/azure/azure-functions/functions-app-settings#functions_worker_process_count).
* ParseEmptyFields (Default: `false`) - This option is a patch to handle a known bug. Consider changing this parameter to `true`, if you encounter invalid logs sent by Azure services that contain empty fields. Logs with empty fields will appear unparsed in Open Search Dashboards. **Please note that this option may slow the shipper's perfomance and should be enabled only as required.**


![Adjust your Azure Function's configuration settings](https://dytvr9ot2sszz.cloudfront.net/logz-docs/log-shipping/configuration-settings-azure-diagnostic-logs.png)


 

