---
id: azure-office365-message-trace-reports
title: Microsoft Azure Office365 Message Trace Reports (mail reports)
overview: You can ship mail report logs available from the Microsoft Office365 Message Trace API with Logzio-api-fetcher.
product: ['logs']
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


You can ship logs available from the Microsoft Graph APIs with Logzio-api-fetcher.
Microsoft Graph is a RESTful web API that enables you to access Microsoft Cloud service resources. This integration allows you to collect data from Microsoft Graph API and send it to your Logz.io account.

Logzio-api-fetcher supports many API endpoints, including but not limited to:

* Azure Active Directory audit logs
* Azure Active Directory sign-in logs

There are many other APIs available through Microsoft Graph.

:::note
[Project's GitHub repo](https://github.com/logzio/logzio-api-fetcher/)
:::
 

## Register a new app in Azure Active Directory

In the Azure portal, go to [App registration](https://portal.azure.com/#blade/Microsoft_AAD_RegisteredApps/ApplicationsListBlade)
and select **New registration** from the top menu.

Name your app and click **Register**.

## Create a client secret

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
 

## Set the app's permissions

Choose **API permissions** from the side menu,
and click **Add a permission**.

Select **Office 365 exchange online > Application permissions**.

Search for the following permssion: **ReportingWebService.Read.All**

Click **Add permissions**.

Click **Grant admin consent for Default Directory**, and then click **Yes** to confirm.

:::note
Only Azure administrators can grant consent for Default Directory. If the _Grant admin consent_ button is disabled, ask your Azure admin to update the setting for you.
:::

## Configure application to have one of the following IAM roles:
IAM roles are showen in least permissive order:
* Global Reader role
* Exchange Administrator
* Global Administrator


## Pull the Docker image of the Logz.io API fetcher

```shell
docker pull logzio/logzio-api-fetcher
```


## Create a configuration file

In the directory created in the previous step, create a file `config.yaml` using the example configuration below:

```yaml
logzio:
  url: https://<<LISTENER-HOST>>:8071
  token: <<LOG-SHIPPING-TOKEN>>

apis:
  - name: mail reports example
    type: azure_mail_reports
    azure_ad_tenant_id: <<AZURE_AD_TENANT_ID>>
    azure_ad_client_id: <<AZURE_AD_CLIENT_ID>>
    azure_ad_secret_value: <<AZURE_AD_SECRET_VALUE>>
    data_request:
      url: https://reports.office365.com/ecp/reportingwebservice/reporting.svc/MessageTrace
    additional_fields:
      type: azure_mail_reports
    scrape_interval: 60  # for mail reports we suggest no less than 60 minutes
    days_back_fetch: 8  # for mail reports we suggest up to 8 days

```

| Parameter Name        | Description                                                                                         | Required/Optional | Default     |
|-----------------------|-----------------------------------------------------------------------------------------------------|-------------------|-------------|
| name                  | Name of the API (custom name)                                                                       | Optional          | `azure api` |
| azure_ad_tenant_id    | The Azure AD Tenant id                                                                              | Required          | -           |
| azure_ad_client_id    | The Azure AD Client id                                                                              | Required          | -           |
| azure_ad_secret_value | The Azure AD Secret value                                                                           | Required          | -           |
| start_date_filter_key          | The name of key to use for the start date filter in the request URL params. | Optional          | `startDate` |
| end_date_filter_key            | The name of key to use for the end date filter in the request URL params.   | Optional          | `EndDate`   |
| data_request.url               | The request URL                                                      | Required          | -                 |
| data_request.additional_fields | Additional custom fields to add to the logs before sending to logzio | Optional          | -                 |
| days_back_fetch       | The amount of days to fetch back in the first request                                               | Optional          | 1 (day)     |
| scrape_interval       | Time interval to wait between runs (unit: `minutes`)                                                | Optional          | 1 (minute)  |

## Important notes and limitations

* We recommend setting the `days_back_fetch` parameter to no more than `8d` (~192 hours) as this might cause unexpected errors with the API.
* We recommend setting the `time_interval` parameter to no less than `60`, to avoid short time frames in which messages trace will be missed.
* Microsoft may delay trace events for up to 24 hours, and events are not guaranteed to be sequential during this delay. For more information, see the Data granularity, persistence, and availability section of the MessageTrace report topic in the Microsoft documentation: MessageTrace report API


## Run the Docker container
In the path where you saved your `config.yaml`, run:

```shell
docker run --name logzio-api-fetcher \
-v "$(pwd)":/app/src/shared \
logzio/logzio-api-fetcher
```

:::note
To run in Debug mode add `--level` flag to the command:
```shell
docker run --name logzio-api-fetcher \
-v "$(pwd)":/app/src/shared \
logzio/logzio-api-fetcher \
--level DEBUG
```
Available Options: `INFO`, `WARN`, `ERROR`, `DEBUG`
:::

## Stop the Docker container

When you stop the container, the code will run until the iteration is completed. To make sure it will finish the iteration on time, please give it a grace period of 30 seconds when you run the `docker stop` command.

```shell
docker stop -t 30 logzio-api-fetcher
```

## Check Logz.io for your logs

Give your logs some time to get from your system to ours,
and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd). You can filter for data of your custom field type value or type `api_fetcher` to see the incoming Microsoft Graph logs.

If you still don't see your logs,
see [log shipping troubleshooting](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/log-shipping-troubleshooting/).
 
You can see a full list of the possible configuration values in the [logzio-api-fetcher github repository](https://github.com/logzio/logzio-api-fetcher).
