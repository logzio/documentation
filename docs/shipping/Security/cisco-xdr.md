---
id: Cisco-XDR
title: Cisco XDR
overview: Cisco XDR connects the breadth of Cisco's integrated security portfolio and your infrastructure. This integration allows you to collect data from Cisco XDR API and send it to your Logz.io account.
product: ['logs']
os: ['windows', 'linux']
filters: ['Security']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/cisco-xdr.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---


> **Deprecation Notice:** Cisco SecureX is deprecated. Use Cisco XDR for new integrations. 

This guide describes how to collect Cisco XDR events using the Logz.io API Fetcher.

:::note
[Project's GitHub repo](https://github.com/logzio/logzio-api-fetcher)
:::


### Pull the Docker image of the Logz.io API fetcher

```shell
docker pull logzio/logzio-api-fetcher:latest
```

### Create a local directory for this integration

You will need a dedicated directory to mount into the Docker container of the Logz.io API fetcher.

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

apis:
  - name: cisco_xdr_events
    type: cisco_xdr
    cisco_client_id: ${CISCO_CLIENT_ID}
    client_password: ${CISCO_CLIENT_SECRET}
    scrape_interval: 5    
    data_request:
      url: https://visibility.amp.cisco.com/iroh/iroh-event/event/search
      method: POST
      body:
        query: <xdr_query>
        limit: 1000
      response_data_path: data
    additional_fields:
      product: cisco_xdr
      source_type: security_event
```

| Parameter Name | Description | Required/Optional | Default |
|----------------|-------------|-------------------|---------|
| name | Name of the API (custom name) | Optional | the defined `url` |
| cisco_client_id | Cisco Client ID | Required | - |
| client_password | Cisco Client password | Required | - |
| data_request.url | The request URL | Required | - |
| data_request.body | The request body | Optional | - |
| data_request.method | The request method (`GET` or `POST`) | Optional | `GET` |
| data_request.pagination | Pagination settings if needed | Optional | - |
| data_request.next_url | If needed to update the URL in next requests based on the last response | Optional | - |
| data_request.response_data_path | The path to the data inside the response | Optional | response root |
| additional_fields | Additional custom fields to add to the logs before sending to Logz.io | Optional | - |
| scrape_interval | Time interval to wait between runs (in minutes) | Optional | 1 (minute) |


### Authentication

This module uses OAuth 2.0 client credentials flow with Basic Authentication. The credentials are automatically encoded and sent in the Authorization header to the `/iroh/oauth2/token` endpoint.

### Create a Last Start Dates text file

Create an empty text file named last_start_dates.txt in the same directory as the config file:

```shell
touch last_start_dates.txt
```

After every successful iteration of an API, the last start date of the next iteration will be written to last_start_dates.txt. Each line begins with the API name and ends with the most recent start date.

If you stop the container, you can resume exactly where you left off by adding the date to the API filters in the configuration.

### Run the Docker container
In the path where you saved your `config.yaml`, run:

```shell
docker run --name logzio-api-fetcher \
-v "$(pwd)":/app/src/shared \
logzio/logzio-api-fetcher
```

### Stop the Docker container

When you stop the container, the code continues running until the current iteration is finished. To make sure it will finish the iteration on time, please give it a grace period of 30 seconds when you run the `docker stop` command.

```shell
docker stop -t 30 logzio-api-fetcher
```

### Check Logz.io for your logs

Give your logs a few moments to reach Logz.io. To view the incoming Cisco XDR logs, open [Explore](https://app.logz.io/#/dashboard/explore) and filter by your custom field’s product value or use the keyword `api_fetcher`.

If you still don't see your logs, refer to the [log shipping troubleshooting](https://docs.logz.io/docs/explore/troubleshooting/shipping-log-troubleshooting/).

 

