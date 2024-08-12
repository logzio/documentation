---
sidebar_position: 11
title: Logz.io API Fetcher Configuration Guide
description: This guide outlines the steps for configuring the Logz.io API Fetcher to fetch and send data to Logz.io. 
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logz.io, opensearch dashboards, log analysis, observability]
---

The Logz.io API Fetcher supports both auth and OAuth APIs and includes specific implementations for Azure Graph, Cisco Secure X, and Office365 Message Trace reports.

This guide outlines the steps for configuring the Logz.io API Fetcher to fetch and send data to Logz.io. Our aim is to develop the API Fetcher as a generic tool capable of fetching data from any API endpoint. However, this presents significant challenges. If you encounter difficulties configuring the API Fetcher with a particular API endpoint, please reach out to our support team for assistance.

Below is a sample configuration template, as found in our documentation and on GitHub:

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

  - name: mail reports example
    type: azure_mail_reports
    azure_ad_tenant_id: <<AZURE_AD_TENANT_ID>>
    azure_ad_client_id: <<AZURE_AD_CLIENT_ID>>
    azure_ad_secret_value: <<AZURE_AD_SECRET_VALUE>>
    data_request:
      url: https://login.microsoftonline.com/<<AZURE_AD_TENANT_ID>>/oauth2/v2.0/token
      additional_fields:
        type: azure_mail_reports
    scrape_interval: 60  # for mail reports we suggest no less than 60 minutes
    days_back_fetch: 8  # for mail reports we suggest up to 8 days

  - name: cloudflare test
    type: cloudflare
    cloudflare_account_id: <<CLOUDFLARE_ACCOUNT_ID>>
    cloudflare_bearer_token: <<CLOUDFLARE_BEARER_TOKEN>>
    url: https://api.cloudflare.com/client/v4/accounts/{account_id}/alerting/v3/history
    next_url: https://api.cloudflare.com/client/v4/accounts/{account_id}/alerting/v3/history?since={res.result.[0].sent}
    days_back_fetch: 7
    scrape_interval: 5
    additional_fields:
      type: cloudflare

  - name: general example
    type: general
    url: https://first/request/url
    headers:
      CONTENT-TYPE: application/json
      another-header: XXX
    body: {
            "size": 1000
          }
    method: POST
    additional_fields:
      type: my_fetcher
      another_field: 123
    pagination:
      type: url
      url_format: ?page={res.info.page+1}
      update_first_url: True
      stop_indication:
        field: result
        condition: empty
    response_data_path: result
```

## Configuration

### Add Your Logz.io Listener and Token

Insert your Logz.io listener URL and token into the config to begin the setup process.

```yaml
logzio:
  url: https://<<LISTENER-HOST>>:8071 
  token: <<LOG-SHIPPING-TOKEN>>
```

{@include: ../../_include/log-shipping/log-shipping-token.md}
{@include: ../../_include/log-shipping/listener-var.html}

### Configure your APIs

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<Tabs>
 <TabItem value="General-Settings" label="General API" default>

  #### General API Settings

## Configuration
| Parameter Name     | Description                                                                                                                       | Required/Optional | Default                     |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------|-------------------|-----------------------------|
| name               | Name of the API (custom name)                                                                                                     | Optional          | the defined `url`           |
| url                | The request URL                                                                                                                   | Required          | -                           |
| headers            | The request Headers                                                                                                               | Optional          | `{}`                        |
| body               | The request body                                                                                                                  | Optional          | -                           |
| method             | The request method (`GET` or `POST`)                                                                                              | Optional          | `GET`                       |
| pagination         | Pagination settings if needed (see [options below](#pagination-configuration-options))                                            | Optional          | -                           |
| next_url           | If needed to update the URL in next requests based on the last response. Supports using variables ([see below](#using-variables)) | Optional          | -                           |
| response_data_path | The path to the data inside the response                                                                                          | Optional          | response root               |
| additional_fields  | Additional custom fields to add to the logs before sending to logzio                                                              | Optional          | Add `type` as `api-fetcher` |
| scrape_interval    | Time interval to wait between runs (unit: `minutes`)                                                                              | Optional          | 1 (minute)                  |

## Pagination Configuration Options
If needed, you can configure pagination.

| Parameter Name   | Description                                                                                                                                      | Required/Optional                                  | Default |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|---------|
| type             | The pagination type (`url`, `body` or `headers`)                                                                                                 | Required                                           | -       |
| url_format       | If pagination type is `url`, configure the URL format used for the pagination. Supports using variables ([see below](#using-variables)).         | Required if pagination type is `url`               | -       |
| update_first_url | `True` or `False`; If pagination type is `url`, and it's required to append new params to the first request URL and not reset it completely.     | Optional if pagination type is `url`               | False   |
| headers_format   | If pagination type is `headers`, configure the headers format used for the pagination. Supports using variables ([see below](#using-variables)). | Required if pagination type is `headers`           | -       |
| body_format      | If pagination type is `body`, configure the body format used for the pagination. Supports using variables ([see below](#using-variables)).       | Required if pagination type is `body`              | -       |
| stop_indication  | When should the pagination end based on the response. (see [options below](#pagination-stop-indication-configuration)).                          | Optional (if not defined will stop on `max_calls`) | -       |
| max_calls        | Max calls that the pagination can make. (Supports up to 1000)                                                                                    | Optional                                           | 1000    |

## Pagination Stop Indication Configuration

| Parameter Name | Description                                                                             | Required/Optional                               | Default |
|----------------|-----------------------------------------------------------------------------------------|-------------------------------------------------|---------|
| field          | The name of the field in the response body, to search the stop indication at            | Required                                        | -       |
| condition      | The stop condition (`empty`, `equals` or `contains`)                                    | Required                                        | -       |
| value          | If condition is `equals` or `contains`, the value of the `field` that we should stop at | Required if condition is `equals` or `contains` | -       |

## Using Variables
Using variables allows taking values from the response of the first request, to structure the request after it.  
Mathematical operations `+` and `-` are supported, to add or reduce a number from the variable value.  

Use case examples for variable usage:
1. Update a date filter at every call
2. Update a page number in pagination

To use variables:
- Wrap the variable name in curly brackets
- Provide the full path to that variable in the response
- Add `res.` prefix to the path.

Example: Say this is my response:
```json
{
  "field": "value",
  "another_field": {
    "nested": 123
  },
  "num_arr": [1, 2, 3],
  "obj_arr": [
    {
      "field2": 345
    },
    {
      "field2": 567
    }
  ]
}
```
Paths to fields values are structured like so:
- `{res.field}` = `"value"`
- `{res.another_field.nested}` = `123`
- `{res.num_arr.[2]}` = `3`
- `{res.obj_arr.[0].field2}` = `345`

Using the fields values in the `next_url` for example like the below:
```Yaml
next_url: https://logz.io/{res.field}/{res.obj_arr[0].field2}
```
Would update the URL at every call to have the value of the given fields from the response.  In our example the url for the next call would be:
```
https://logz.io/value/345
```
And in the call after it, it would update again according to the response and the `next_url` structure, and so on.


  </TabItem>
  <TabItem value="OAuth-General-Settings" label="OAuth API" default>

#### General OAuth API Settings

| Parameter Name    | Description                                                                                                                   | Required/Optional | Default                     |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------|-------------------|-----------------------------|
| name              | Name of the API (custom name)                                                                                                 | Optional          | the defined `url`           |
| token_request     | Nest here any detail relevant to the request to get the bearer access token. | Required          | -                           |
| data_request      | Nest here any detail relevant to the data request.                           | Required          | -                           |
| scrape_interval   | Time interval to wait between runs (unit: `minutes`)                                                                          | Optional          | 1 (minute)                  |
| additional_fields | Additional custom fields to add to the logs before sending to logzio                                                          | Optional          | Add `type` as `api-fetcher` |

</TabItem>
<TabItem value="Azure" label="Azure API" default>

#### Azure API Settings
Below fields are relevant for **all Azure API types**

| Parameter Name        | Description                                                                                         | Required/Optional | Default     |
|-----------------------|-----------------------------------------------------------------------------------------------------|-------------------|-------------|
| name                  | Name of the API (custom name)                                                                       | Optional          | `azure api` |
| azure_ad_tenant_id    | The Azure AD Tenant id                                                                              | Required          | -           |
| azure_ad_client_id    | The Azure AD Client id                                                                              | Required          | -           |
| azure_ad_secret_value | The Azure AD Secret value                                                                           | Required          | -           |
| data_request          | Nest here any detail relevant to the data request. | Required          | -           |
| days_back_fetch       | The amount of days to fetch back in the first request                                               | Optional          | 1 (day)     |
| scrape_interval       | Time interval to wait between runs (unit: `minutes`)                                                | Optional          | 1 (minute)  |

#### Azure Graph
By default `azure_graph` API type has built in pagination settings and sets the `response_data_path` to `value` field.  
The below fields are relevant **in addition** to the required ones listed under Azure General.

| Parameter Name                 | Description                                                          | Required/Optional | Default           |
|--------------------------------|----------------------------------------------------------------------|-------------------|-------------------|
| date_filter_key                | The name of key to use for the date filter in the request URL params | Optional          | `createdDateTime` |
| data_request.url               | The request URL                                                      | Required          | -                 |
| data_request.additional_fields | Additional custom fields to add to the logs before sending to logzio | Optional          | -                 |

#### Azure Mail Reports
By default `azure_mail_reports` API type has built in pagination settings and sets the `response_data_path` to `d.results` field.  
The below fields are relevant **in addition** to the required ones listed under Azure General.

| Parameter Name                 | Description                                                                 | Required/Optional | Default     |
|--------------------------------|-----------------------------------------------------------------------------|-------------------|-------------|
| start_date_filter_key          | The name of key to use for the start date filter in the request URL params. | Optional          | `startDate` |
| end_date_filter_key            | The name of key to use for the end date filter in the request URL params.   | Optional          | `EndDate`   |
| data_request.url               | The request URL                                                             | Required          | -           |
| data_request.additional_fields | Additional custom fields to add to the logs before sending to logzio        | Optional          | -           |

</TabItem>
<TabItem value="Cloudflare" label="Cloudflare" default>

#### Cloudflare API Settings
By default `cloudflare` API type has built in pagination settings and sets the `response_data_path` to `result` field.  

| Parameter Name          | Description                                                                                                                                 | Required/Optional | Default           |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|-------------------|-------------------|
| name                    | Name of the API (custom name)                                                                                                               | Optional          | the defined `url` |
| cloudflare_account_id   | The CloudFlare Account ID                                                                                                                   | Required          | -                 |
| cloudflare_bearer_token | The Cloudflare Bearer token                                                                                                                 | Required          | -                 |
| url                     | The request URL                                                                                                                             | Required          | -                 |
| next_url                | If needed to update the URL in next requests based on the last response. Supports using variables. | Optional          | -                 |
| additional_fields       | Additional custom fields to add to the logs before sending to logzio                                                                        | Optional          | -                 |
| days_back_fetch         | The amount of days to fetch back in the first request. Applies a filter on `since` parameter.                                               | Optional          | -                 |
| scrape_interval         | Time interval to wait between runs (unit: `minutes`)                                                                                        | Optional          | 1 (minute)        |
| pagination_off          | True if builtin pagination should be off, False otherwise                                                                                   | Optional          | `False`           |

  </TabItem>

</Tabs>


## Launch the Docker Container

Use Docker to run the Logz.io API Fetcher with the provided command in the path where you saved your `config.yaml`:

```shell
docker run --name logzio-api-fetcher \
-v "$(pwd)":/app/src/shared \
logzio/logzio-api-fetcher
```

:::info
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
