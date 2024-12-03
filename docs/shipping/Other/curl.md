---
id: cURL-data
title: cURL
overview: cURL is a command line utility for transferring data. cURL is a quick and easy way to test your configuration or troubleshoot your connectivity to Logz.io.
product: ['logs']
os: ['windows', 'linux']
filters: ['Other', 'Most Popular']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/curl.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---


 

cURL is a command line utility for transferring data, useful for testing configurations or troubleshooting connectivity to Logz.io. You can upload JSON or plain text files.

## Upload a JSON log file

**Limitations**

* Max body size: 10 MB (10,485,760 bytes).
* Max log line size: 500,000 bytes.
* Type field in the log overrides the `type` in the request header.

1. Download [cURL](https://curl.haxx.se/download.html).

2. Upload the file:


```shell 
cat /path/to/log/file | curl -X POST "https://<<LISTENER-HOST>>:8071?token=<<LOG-SHIPPING-TOKEN>>&type=<LOG-TYPE>" \
-H "user-agent:logzio-curl-logs" \
-v --data-binary @-
```

{@include: ../../_include/general-shipping/replace-placeholders.html}

* {@include: ../../_include/log-shipping/type.md} Otherwise, the default `type` is `http-bulk`.

3. View your logs

Allow some time for data ingestion, then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

Encounter an issue? See our [log shipping troubleshooting](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/log-shipping-troubleshooting/) guide.

 
## Upload a plain text log file



**Limitations**

* Max body size: 30 MB (31,457,280 bytes).
* Type field in the log overrides the `type` in the request header.


1. Download [cURL](https://curl.haxx.se/download.html).

2. Upload the file:


```shell
curl -T /path/to/log/file https://<<LISTENER-HOST>>:8022/file_upload/<<LOG-SHIPPING-TOKEN>>/<<LOG-TYPE>> \
-H "user-agent: logzio-curl-logs"
```

Replace the placeholders to match your specifics. (They are indicated by the double angle brackets `<< >>`):

* Replace `<<LOG-SHIPPING-TOKEN>>` with the token of the account you want to ship to.

* {@include: ../../_include/log-shipping/type.md} Otherwise, the default `type` is `http-bulk`.

3. View your logs

Allow some time for data ingestion, then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

Encounter an issue? See our [log shipping troubleshooting](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/log-shipping-troubleshooting/) guide.

 

  