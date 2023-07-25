---
id: Cisco-SecureX
title: Cisco SecureX
overview: Cisco SecureX connects the breadth of Cisco's integrated security portfolio and your infrastructure. This integration allows you to collect data from Cisco SecureX API and send it to your Logz.io account.
product: ['metrics']
os: ['windows', 'linux']
filters: ['gcp', 'cloud']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/aiven-logo.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
---



Cisco SecureX connects the breadth of Cisco's integrated security portfolio and your infrastructure. This integration allows you to collect data from Cisco SecureX API and send it to your Logz.io account. 
  

 



##### Pull the Docker image of the Logz.io API fetcher

```shell
docker pull logzio/logzio-api-fetcher
```


##### Create a local directory for this integration

You will need a dedicated directory to use it as mounted directory for the Docker container of the Logz.io API fetcher.

```shell
mkdir logzio-api-fetcher
cd logzio-api-fetcher
```

##### Create a configuration file

In the directory created in the previous step, create a file `config.yaml` using the example configuration below:

```yaml
logzio:
  url: https://<<LISTENER-HOST>>:8071
  token: <<LOG-SHIPPING-TOKEN>>

auth_apis:
  - type: api_fetcher
    name: cisco
    credentials:
      id: <<API_CREDENTIALS_ID>>
      key: <<API_CREDENTIALS_KEY>>
    settings:
      time_interval: 5
      days_back_fetch: 7
    filters:
      event_type%5B%5D: '1090519054'
      start_date: 2021-10-05T10%3A10%3A10%2B00%3A00
    custom_fields:
      type: cisco
      level: high
```

| Parameter | Description | Required/Default |
|---|---|---|
| URL | {@include: ../_include/log-shipping/listener-var.md} | Required |
| TOKEN | Your Logz.io account token. {@include: ../_include/log-shipping/log-shipping-token.html}  | Required  |
| type | The type of the Auth API. Currently we support the following types: cisco_secure_x, general. | Required |
| name | The name of the Auth API. Please make names unique. | Required | 
| credentials.id | The Auth API credentials id. | Required |
| credentials.key | The Auth API credentials key. | Required | 
| settings.time_interval | The Auth API time interval between runs. | Required |
| settings.days_back_fetch | The max days back to fetch from the Auth API. | Optional. Default value is 14 days. | 
| filters | Pairs of key and value of parameters that can be added to the Auth API url. Make sure the keys and values are valid for the Auth API. | Optional | 
| custom_fields | Pairs of key and value that will be added to each data and be sent to Logz.io. | Optional | 


##### Create a Last Start Dates text file

Create an empty text file named last_start_dates.txt in the same directory as the config file:

```shell
$ touch last_start_dates.txt
```

After every successful iteration of an API, the last start date of the next iteration will be written to last_start_dates.txt. Each line starts with the API name and ends with the last start date.

If you stopped the container, you can continue from the exact place you stopped, by adding the date to the API filters in the configuration.

##### Run the Docker container

```shell
docker run --name logzio-api-fetcher \
-v "$(pwd)":/app/src/shared \
logzio/logzio-api-fetcher
```

##### Stop the Docker container

When you stop the container, the code will run until the iteration is completed. To make sure it will finish the iteration on time, please give it a grace period of 30 seconds when you run the `docker stop` command.

```shell
docker stop -t 30 logzio-api-fetcher
```

##### Check Logz.io for your logs

Give your logs some time to get from your system to ours,
and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd). You can filter for data of your custom field type value or type `api_fetcher` to see the incoming Cisco SecureX logs.

If you still don't see your logs,
see [log shipping troubleshooting]({{site.baseurl}}/user-guide/log-shipping/log-shipping-troubleshooting.html).

 

