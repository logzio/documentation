---
id: Microsoft-Graph-data
title: Microsoft Graph
overview: Microsoft Graph is a RESTful web API that enables you to access Microsoft Cloud service resources. This integration allows you to collect data from Microsoft Graph API and send it to your Logz.io account.
product: ['logs', 'siem']
os: ['windows']
filters: ['Other']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/graph-api-logo.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---



Microsoft Graph is a RESTful web API that enables you to access Microsoft Cloud service resources. This integration allows you to collect data from Microsoft Graph API and send it to your Logz.io account.

:::note
[Project's GitHub repo](https://github.com/logzio/logzio-api-fetcher/)
:::
 


### Pull the Docker image of the Logz.io API fetcher
```shell
docker pull logzio/logzio-api-fetcher
```

### Create a configuration file

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
| additional_fields | Additional custom fields to add to the logs before sending to logzio | Optional          | -                 |
| days_back_fetch       | The amount of days to fetch back in the first request                                               | Optional          | 1 (day)     |
| scrape_interval       | Time interval to wait between runs (unit: `minutes`)                                                | Optional          | 1 (minute)  |

### Run the Docker container
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

### Stop the Docker container

When you stop the container, the code will run until the iteration is completed. To make sure it will finish the iteration on time, please give it a grace period of 30 seconds when you run the `docker stop` command.

```shell
docker stop -t 30 logzio-api-fetcher
```

### Check Logz.io for your logs

Give your logs some time to get from your system to ours,
and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd). You can filter for data of your custom field type value or type `api_fetcher` to see the incoming Microsoft Graph logs.

If you still don't see your logs,
see [log shipping troubleshooting](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/log-shipping-troubleshooting/).
