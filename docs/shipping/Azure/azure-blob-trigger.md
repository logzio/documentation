---
id: Azure-blob-trigger
title: Azure Blob Trigger
overview: Azure Blob Storage is Microsoft's object storage solution for the cloud. Deploy this integration to forward logs from your Azure Blob Storage account to Logz.io using an automated deployment process via the trigger function. Each new log in the container path inside the storage account (including sub directories), will trigger the Logz.io function that will ship the file content to Logz.io. 
product: ['logs']
os: ['windows', 'linux']
filters: ['Azure', 'Other']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/azure-blob.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---
 

Azure Blob Storage is Microsoft's object storage solution for the cloud. Deploy this integration to forward logs from your Azure Blob Storage account to Logz.io using an automated deployment process via the trigger function. Each new log in the container path inside the storage account (including sub directories), will trigger the Logz.io function that will ship the file content to Logz.io. 


The following resources are needed for this integration:

* Storage Account (general purpose v2) + Container
* App Service Plan - Consumption Plan
* Application Insights
* Logz.io Function App + Logz.io Blob Trigger Function
* Storage Account for Logz.io Function App logs

![Integration-architecture](https://dytvr9ot2sszz.cloudfront.net/logz-docs/azure_blob/blob-trigger-resources.png)

:::note
[Project's GitHub repo](https://github.com/logzio/logzio-azure-blob-trigger/)
:::

### Supported data types

This Logz.io function supports the following data types:

* JSON
* CSV
* Text (supports multiline text - MultilineRegex parameter)

:::note
The file name does not have to explicitly include these extensions.
:::
 

### Supported file formats

The Logz.io function supports the following file formats:

* Gzip
  
:::note
The file name does not have to explicitly include these extensions.
:::
 

  


## Create a new blob storage account

If you don't have a general purpose v2 storage account with a container for logs, or you want to create everything from scratch, this auto-deployment is for you.

* Storage Account (general purpose v2) + Container
* App Service Plan - Consumption Plan
* Application Insights
* Logz.io Function App and Logz.io Blob Trigger Function
* Storage Account for Logz.io Function App logs

 

### Launch an automated deployment

👇 Click this button:

[![Deploy to Azure](https://dytvr9ot2sszz.cloudfront.net/logz-docs/azure_blob/deploybutton-az.png)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Flogzio%2Flogzio-azure-blob-trigger%2Fmain%2Fazure%2Ffull-auto-deployment.json)
  
### Fill in the deployment parameters

In the **Custom deployment** screen, fill in all the parameters as per table below and click **Review + create**.

![Custom deployment](https://dytvr9ot2sszz.cloudfront.net/logz-docs/azure_blob/blob-trigger-1-new-acc.png)

| Parameter | Description | Is Required | Value If Empty |
| --- | --- | --- | --- |
| Storage Account Name | The storage account (general purpose v2) name | Required | - |
| Container Name | The name of the container inside the storage account | Required | - |
| Format | The format of the log files | Required | - |
| Logzio URL | The Logz.io listener URL fot your region. For more details, see the [Regions page](https://docs.logz.io/docs/user-guide/admin/hosting-regions/account-region/). | Required | - |
| Logzio Token | Your Logz.io Logs token (Available in the **Manage Tokens** page) | Required | - |
| Logs Path | The path from where blob files will trigger the Logz.io function (including subdirectories in that path). Leave empty if you want every blob file in the container to trigger the Logz.io function. | Not Required | `<<ContainerLogsPath>>/{name}` |
| Multiline Regex | The regex that matches the multiline logs in text blob files. Leave empty if you do not use multiline logs in your text blob files. | Not Required | NO_REGEX |
| Datetime Filter | Every log with a datetime greater than or equal to the specified datetime will be shipped to Logz.io (for example: 2021-11-05T10:10:10). For this to take effect, DatetimeFinder and DatetimeFormat must not be empty. Leave empty if you want all logs to be shipped to Logz.io. | Not Required | NO_DATETIME_FILTER |
| Datetime Finder | If file is CSV/JSON: Write the JSON path of the datetime field inside each log. The CSV JSON path will always be the name of the datetime field. The JSON's JSON path can be the name of the datetime field if it's in the root, or if the path contains fields separated by '.' (for example: metadata.datetime, metadata\[:1].datetime). If the file is text: write a regex to get the datetime from each log. If the log has many occurrences of datetime, make sure that the regex will retrieve the right one: For example: '(?:.\*?\[0-9]){2}.*?(\[0-9])' will return the third digit. If this value cannot be found inside a log, the log will be shipped to Logz.io. Leave empty if you are not using DatetimeFilter. | Required if using DatetimeFilter | NO_DATETIME_FINDER |
| Datetime Format | The datetime format of DatetimeFilter and datetime field in each log (for example: %Y/%m/%dT%H:%M:%S%z is for 2021/11/01T10:10:10+0000 datetime). If the format is wrong, the log will be shipped to Logz.io. Leave empty if you are not using DatetimeFilter. | Required if using DatetimeFilter | NO_DATETIME_FORMAT |

### Confirm the deployment parameters

In the **Custom deployment: review + create** screen, review the deployment and click **Create**.

![Custom deployment](https://dytvr9ot2sszz.cloudfront.net/logz-docs/azure_blob/blob-trigger-2.png)

If all the parameters have been configured correctly, the following conformation screen will appear:

![Custom deployment](https://dytvr9ot2sszz.cloudfront.net/logz-docs/azure_blob/blob-trigger-3.png)

Click **Go to resource group** to go to your resource group with all the created resources.


### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd). You can filter for logs of `type` `azure_blob_trigger` to see the incoming logs.

If you still don’t see your logs, see [log shipping troubleshooting](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/log-shipping-troubleshooting/).


 

## Connect to existing blob storage account

**Before you begin, you'll need**: a blob storage account of the type **StorageV2 (general purpose v2)**.


:::note
If your existing blob storage account is of any other kind, it will NOT work. Instead, follow the process to set up a new blob storage account.
:::
 


 

### Check your storage account for compatibility

Double-check your [_Storage accounts_](https://portal.azure.com/#blade/HubsExtension/BrowseResource/resourceType/Microsoft.Storage%2FStorageAccounts) to make sure that they are compatible with this integration. They should be of the type **StorageV2 (general purpose v2)**.


### Launch an automated deployment

👇 Click this button:

[![Deploy to Azure](https://dytvr9ot2sszz.cloudfront.net/logz-docs/azure_blob/deploybutton-az.png)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Flogzio%2Flogzio-azure-blob-trigger%2Fmain%2Fazure%2Ffunction-auto-deployment.json)
  

### Fill in the deployment parameters

In the **Custom deployment** screen, fill in all the parameters as per table below and click **Review + create**.

![Custom deployment](https://dytvr9ot2sszz.cloudfront.net/logz-docs/azure_blob/blob-trigger-1-existing-acc.png)

| Parameter | Description | Is Required | Value If Empty |
| --- | --- | --- | --- |
| Storage Account Name | The storage account (general purpose v2) name | Required | - |
| Storage Account Resource Name | The resource name that contains the storage account. Required only for the Logz.io Function Auto-Deployment. | Required | - |
| Container Name | The name of the container inside the storage account | Required | - |
| Format | The log files format | Required | - |
| Logzio URL | The Logz.io listener URL for your region. For more details, see the [Regions page.](https://docs.logz.io/docs/user-guide/admin/hosting-regions/account-region/) | Required | - |
| Logzio Token | Your Logz.io logs token. You can retrieve the token from the [**Manage tokens** page](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=logs). | Required | - |
| Logs Path | The path from where blob files will trigger the Logz.io function (including subdirectories in that path). Leave empty if you want every blob file in the container to trigger the Logz.io function. | Not Required | `<<ContainerLogsPath>>/{name}` |
| Multiline Regex | The regex that matches the multiline logs in text blob files. Leave empty if you do not use multiline logs in your text blob files. | Not Required | NO_REGEX |
| Datetime Filter | Every log with datetime greater than or equal to the specified datetime will be shipped to Logz.io (for example: 2021-11-05T10:10:10). For this to take effect, DatetimeFinder and DatetimeFormat must not be empty. Leave empty if you want all logs to be shipped to Logz.io. | Not Required | NO_DATETIME_FILTER |
| Datetime Finder | If file is CSV/JSON: write the JSON path of the datetime field inside each log. The CSV JSON path will always be the name of the datetime field.  The JSON's JSON path can be the name of the datetime field if it's in the root, or a path contains fields separated by '.' (for example: metadata.datetime, metadata\[:1].datetime). For a text file, write a regex that will get the datetime from each log. If the log has many occurrences of datetime, make sure the regex will return the right one (for example: '(?:.\*?\[0-9]){2}.*?(\[0-9])' will give the third digit). If this value cannot be found inside a log, the log will be shipped to Logz.io. Leave empty if you are not using DatetimeFilter. | Required if using DatetimeFilter | NO_DATETIME_FINDER |
| Datetime Format | The datetime format of DatetimeFilter and datetime field in each log (for example: %Y/%m/%dT%H:%M:%S%z is for 2021/11/01T10:10:10+0000 datetime). If the format is wrong, the log will be shipped to Logz.io. Leave empty if you are not using DatetimeFilter. | Required if using DatetimeFilter | NO_DATETIME_FORMAT |


:::note
Logs that were in the container before the deployment will be shipped to Logz.io. If these logs have already been shipped to Logz.io, we recommend that you empty the container before the deployment, or use the FilterDate and FilterDateJsonPath parameters.
:::
 

### Confirm the deployment parameters

In the **Custom deployment: review + create** screen, review the deployment and click **Create**.

![Custom deployment](https://dytvr9ot2sszz.cloudfront.net/logz-docs/azure_blob/blob-trigger-2-updated.png)

If all the parameters are configured correctly, the following confirmation screen will appear:

![Custom deployment](https://dytvr9ot2sszz.cloudfront.net/logz-docs/azure_blob/blob-trigger-3.png)

Click **Go to resource group** to go to your resource group with all the created resources.



### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd). You can filter for logs of `type` `azure_blob_trigger` to see the incoming logs.
  
If you still don’t see your logs, see [log shipping troubleshooting](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/log-shipping-troubleshooting/).

  



## Troubleshooting Azure blob

### Capture logs from Azure blob


To troubleshoot your Azure blob, you first need to view the logs in your Azure portal.

Navigate to your **[Azure Portal](https://portal.azure.com/)** > **Function App** and choose the relevant record from the list:

![Logz.io's Azure app](https://dytvr9ot2sszz.cloudfront.net/logz-docs/azure_blob/function-app-main.png)

Next, click on **Functions** and choose the Logz.io blob you'd like to monitor.

![Functions menu](https://dytvr9ot2sszz.cloudfront.net/logz-docs/azure_blob/logzio-blob-select.png)

Click on **Monitor** > **Logs** tab. Once the connection has been established, you'll see a **Connected!** message on the screen.

![Azure blob log screen](https://dytvr9ot2sszz.cloudfront.net/logz-docs/azure_blob/connected-screen.png)

Once you run your Azure blob, the Monitor screen will show the relevant logs based on your filtering criteria.

### Common use cases and solutions

#### Format error

If you encounter a `format error`, you need to check your configuration. First, verify that the storage account exists and is named properly.

After validating the account, check that the configuration file and format match.

In addition, check that you’re using the correct token and have configured the listeners to the relevant account.

If you've gone through these steps but still see a `format error`, contact the [Logz.io Support team](mailto:help@logz.io) for further assistance. 

#### StorageConnectionString error

The `StorageConnectionString` error indicates an issue with the connection to your storage account, and something is blocking the function from triggering.

If you're using a **Datetime** filter, check that it matches the Datetime format and Datetime finder.

In addition, verify that the **regex** matches your logs. For example, if there are 3 lines of logs, your regex should also contain 3 lines.

If the issue persists and you're still getting this error, contact the [Logz.io Support team](mailto:help@logz.io) for further assistance. 


  
