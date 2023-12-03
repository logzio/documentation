---
id: Salesforce-data
title: Salesforce
overview: Salesforce is a customer relationship management solution. The Account sObject is an abstraction of the account record and holds the account field information in memory as an object. This integration allows you to collect sObject data from Salesforce and send it to your Logz.io account.
product: ['metrics']
os: ['windows', 'linux']
filters: ['Other']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/salesforce-commerce-cloud-logo.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---




Salesforce is a customer relationship management solution. The Account sObject is an abstraction of the account record and holds the account field information in memory as an object. This integration allows you to collect sObject data from Salesforce and send it to your Logz.io account.


:::note
[Project's GitHub repo](https://github.com/logzio/salesforce-logs-receiver/)
:::


##### Pull the Docker image of the Logz.io API fetcher

```shell
docker pull logzio/logzio-salesforce-collector
```


##### Run the Docker container

```shell
 docker run --name logzio-salesforce-collector \
 --env SALESFORCE_URL="<<SALESFORCE_URL>>" \
 --env CLIENT_ID="<<CLIENT_ID>>" \
 --env API_VERSION="<<API_VERSION>>" \
 --env USERNAME="<<USERNAME>>" \
 --env PASSWORD="<<PASSWORD>>" \
 --env SECURITY_TOKEN="<<SECURITY_TOKEN>>" \
 --env SOBJECT_TYPES="<<SOBJECT_TYPES>>" \
 --env FROM_TIMESTAMP="<<FROM_TIMESTAMP>>" \
 --env INTERVAL="<<INTERVAL>>" \
 --env LOGZIO_LISTENER_URL="<<LISTENER-HOST>>" \
 --env LOGZIO_TOKEN="<<LOG-SHIPPING-TOKEN>>" \
logzio/logzio-salesforce-collector
```

Replace the parameter values as per the table below.


| Name | Description | Required? | Default |
| --- | --- | ---| ---|
| CLIENT_ID | Salesforce App Client ID. | Yes | - |
| API_VERSION	| Salesforce API version |	No	| 55.0 |
| USERNAME | Salesforce account username (your email) | Yes | - |
| PASSWORD | Salesforce account password | Yes | - |
| SECURITY_TOKEN | Salesforce account security token | Yes | - |
| SOBJECT_TYPES | List of sObject types to collect. Each type must be separated by comma, for example: "TYPE1,TYPE2,TYPE3". | Yes | - |
| FROM_TIMESTAMP | Timestamp from when to collect data. Must be in the following format: 2006-01-02T15:04:05.000Z .	| No	| Current time minus 1 hour |
| LOGZIO_TOKEN | Logz.io logs token. {@include: ../../_include/log-shipping/log-shipping-token.html}  | Yes | - |
| SALESFORCE_URL | Salesforce URL. | No | https://login.salesforce.com |
| INTERVAL | The time interval to collect Salesforce data (in seconds). | No | 5 (seconds) |
| LOGZIO_LISTENER_URL | Logz.io listener logs URL. {@include: ../../_include/log-shipping/listener-var.md} | No | https://listener.logz.io:8071


##### Check Logz.io for your logs

Give your logs some time to get from your system to ours,
and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd). You can filter for data of the `salesforce` field type value or type `salesforce` to see the Salesforce logs.

If you still don't see your logs,
see [log shipping troubleshooting](/docs/user-guide/log-management/troubleshooting/log-shipping-troubleshooting/).

 
