---
id: 1Password
title: 1Password
overview: 1Password is a password manager. This integration allows you to send event logs to your Logz.io account.
product: ['logs','siem']
os: ['windows', 'linux']
filters: ['Security']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/1password.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---

You can send available logs from the 1Password API with Logzio API fetcher.

## Pull Docker Image
Download the logzio-api-fetcher image:

```shell
docker pull logzio/logzio-api-fetcher
```

## Configuration
Create a local config file `config.yaml`.  

```yaml
apis:
  - name: 1Password Audit Events
    type: 1password
    onepassword_bearer_token: <<1PASSWORD_BEARER_TOKEN>>
    url: https://events.1password.com/api/v1/auditevents
    method: POST
    days_back_fetch: 7
    scrape_interval: 5    
    additional_fields:
      type: 1password
      eventType: auditevents

  - name: 1Password Item Usages
    type: 1password
    onepassword_bearer_token: <<1PASSWORD_BEARER_TOKEN>>
    url: https://events.1password.com/api/v1/itemusages
    method: POST
    days_back_fetch: 7
    scrape_interval: 5
    additional_fields:
      type: 1password
      eventType: itemusages

  - name: 1Password Sign In Attempts
    type: 1password
    onepassword_bearer_token: <<1PASSWORD_BEARER_TOKEN>>
    url: https://events.1password.com/api/v1/signinattempts
    method: POST
    days_back_fetch: 7
    scrape_interval: 5
    additional_fields:
      type: 1password
      eventType: signinattempts

logzio:
  url: https://<<LISTENER-HOST>>:8071
  token: <<LOG-SHIPPING-TOKEN>>
```

:::note
You can customize the endpoints to collect data from by adding extra API configurations under `apis`. 1Password API Docs can be found [here](https://developer.1password.com/docs/connect/connect-api-reference/).
:::

### 1Password configuration options
| Parameter Name           | Description                                                                                     | Required/Optional | Default           |
|--------------------------|-------------------------------------------------------------------------------------------------|-------------------|-------------------|
| name                     | Name of the API (custom name)                                                                   | Optional          | the defined `url` |
| onepassword_bearer_token | The 1Password Bearer token                                                                      | Required          | -                 |
| url                      | The request URL                                                                                 | Required          | -                 |
| method                   | The request method (`GET` or `POST`)                                                            | Optional          | `GET`             |
| additional_fields        | Additional custom fields to add to the logs before sending to logzio                            | Optional          | -                 |
| days_back_fetch          | The amount of days to fetch back in the first request. Applies a filter on 1password `start_time` parameter. | Optional          | -                 |
| scrape_interval          | Time interval to wait between runs (unit: `minutes`)                                            | Optional          | 1 (minute)        |
| onepassword_limit        | 1Password limit for number of events to return in a single request (allowed range: 100 to 1000) | Optional          | 100               |
| pagination_off           | True if builtin pagination should be off, False otherwise                                       | Optional          | `False`           |

### Logzio output configuration options
| Parameter Name | Description                 | Required/Optional | Default                         |
|----------------|-----------------------------|-------------------|---------------------------------|
| url            | The logzio Listener address (You can find the relevant `<<LISTENER-HOST>>` [here](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=logs).) | Optional          | `https://listener.logz.io:8071` |
| token          | The logzio shipping token   | Required          | -                               |


## Run The Docker Container
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

### Stopping the container
When you want to stop the container, to make sure it will finish the iteration on time, please give it a grace period of 30 seconds when you run the docker stop command:

```shell
docker stop -t 30 logzio-api-fetcher
```

## Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd). You can filter for data of your custom field type value or type `1password` to see the incoming logs.
