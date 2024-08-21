---
id: azure-graph
title: Microsoft Azure Graph API
overview: You can ship logs available from the Microsoft Graph APIs with Logzio-api-fetcher.
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

Select **Microsoft Graph > Application permissions**.

Select the relevant permissions for your API, for AAD audit logs and AAD sign-ins enable these items:

* **AuditLog.Read.All**
* **Directory.Read.All**

Click **Add permissions**.

Click **Grant admin consent for Default Directory**, and then click **Yes** to confirm.

:::note
Only Azure administrators can grant consent for Default Directory. If the _Grant admin consent_ button is disabled, ask your Azure admin to update the setting for you.
:::
 

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
  - name: azure graph example
    type: azure_graph
    azure_ad_tenant_id: <<AZURE_AD_TENANT_ID>>
    azure_ad_client_id: <<AZURE_AD_CLIENT_ID>>
    azure_ad_secret_value: <<AZURE_AD_SECRET_VALUE>>
    data_request:
      url: https://graph.microsoft.com/v1.0/auditLogs/signIns
      additional_fields:
        type: azure_graph
        field_to_add_to_my_logs: 123
    scrape_interval: 1
    days_back_fetch: 30
```

| Parameter Name        | Description                                                                                         | Required/Optional | Default     |
|-----------------------|-----------------------------------------------------------------------------------------------------|-------------------|-------------|
| name                  | Name of the API (custom name)                                                                       | Optional          | `azure api` |
| azure_ad_tenant_id    | The Azure AD Tenant id                                                                              | Required          | -           |
| azure_ad_client_id    | The Azure AD Client id                                                                              | Required          | -           |
| azure_ad_secret_value | The Azure AD Secret value                                                                           | Required          | -           |
| date_filter_key                | The name of key to use for the date filter in the request URL params | Optional          | `createdDateTime` |
| data_request.url               | The request URL                                                      | Required          | -                 |
| data_request.additional_fields | Additional custom fields to add to the logs before sending to logzio | Optional          | -                 |
| days_back_fetch       | The amount of days to fetch back in the first request                                               | Optional          | 1 (day)     |
| scrape_interval       | Time interval to wait between runs (unit: `minutes`)                                                | Optional          | 1 (minute)  |


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
