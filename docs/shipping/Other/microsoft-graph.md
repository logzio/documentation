---
id: Microsoft-Graph-data
title: Microsoft Graph
overview: Microsoft Graph is a RESTful web API that enables you to access Microsoft Cloud service resources. This integration allows you to collect data from Microsoft Graph API and send it to your Logz.io account.
product: ['logs']
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


### Create a local directory for this integration

You will need a dedicated directory to use it as mounted directory for the Docker container of the Logz.io API fetcher.

```shell
mkdir logzio-api-fetcher
cd logzio-api-fetcher
```

### Create a configuration file

In the directory created in the previous step, create a file `config.yaml` using the example configuration below:

```yaml
logzio:
  url: https://<<LISTENER-HOST>>:8071
  token: <<LOG-SHIPPING-TOKEN>>

oauth_apis:
  - type: api_fetcher
    name: azure_test
    credentials:
      id: <<AZURE_AD_SECRET_ID>>
      key: <<AZURE_AD_SECRET_VALUE>>
    token_http_request:
      url: https://login.microsoftonline.com/<<AZURE_AD_TENANT_ID>>/oauth2/v2.0/token
      body: client_id=<<AZURE_AD_CLIENT_ID>>
        &scope=https://graph.microsoft.com/.default
        &client_secret=<<AZURE_AD_SECRET_VALUE>>
        &grant_type=client_credentials
      headers:
      method: POST
    data_http_request:
      url: https://graph.microsoft.com/v1.0/auditLogs/signIns
      headers:
    json_paths:
      data_date: createdDateTime
    settings:
      time_interval: 1
      days_back_fetch: 30
  
```

| Parameter | Description | Required/Default |
|---|---|---|
| URL | {@include: ../../_include/log-shipping/listener-var.md} | Required |
| TOKEN | Your Logz.io account token. {@include: ../../_include/log-shipping/log-shipping-token.html}  | Required  |
| type | The type of the OAuth API. Currently we support the following types: azure_graph, general. | Required | 
| name | The name of the OAuth API. Please make names unique. | Required | 
| credentials.id | The OAuth API credentials id. | Required | 
| credentials.key | The OAuth API credentials key. | Required |
| http_request.method | The HTTP method. Can be GET or POST. | Required | 
| http_request.url | The OAuth API url. Make sure the url is without `?` at the end. | Required | 
| http_request.headers | Pairs of key and value the represents the headers of the HTTP request. | Optional | 
| http_request.body | The body of the HTTP request. Will be added to HTTP POST requests only. | Optional | 
| token_http_request.method | The HTTP method. Can be GET or POST. | Required |
| token_http_request.url | The OAuth API token request  url. Make sure the url is without `?` at the end. | Required | 
| token_http_request.headers | Pairs of key and value the represents the headers of the HTTP request. | Optional |
| token_http_request.body | The body of the HTTP request. Will be added to HTTP POST requests only. | Optional | 
| json_paths.data_date | The json path to the data's date value inside the response of the OAuth API. | Required | 
| settings.time_interval | The OAuth API time interval between runs. | Required | 
| settings.days_back_fetch | The max days back to fetch from the OAuth API. | Optional. Default value is 14 days.| 
| filters | Pairs of key and value of parameters that can be added to the OAuth API url. Make sure the keys and values are valid for the OAuth API. | Optional |
| custom_fields | Pairs of key and value that will be added to each data and be sent to Logz.io. | Optional | 

### Create a Last Start Dates text file

Create an empty text file named last_start_dates.txt in the same directory as the config file:

```shell
$ touch last_start_dates.txt
```

After every successful iteration of an API, the last start date of the next iteration will be written to last_start_dates.txt. Each line starts with the API name and ends with the last start date.

If you stopped the container, you can continue from the exact place you stopped, by adding the date to the API filters in the configuration.

### Run the Docker container

```shell
docker run --name logzio-api-fetcher \
-v "$(pwd)":/app/src/shared \
logzio/logzio-api-fetcher
```

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

 
