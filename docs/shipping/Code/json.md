---
id: JSON
title: JSON
overview: Ship logs from your code directly to the Logz.io listener as a minified JavaScript Object Notation (JSON) file, a standard text-based format for representing structured data based on JavaScript object syntax.
product: ['logs']
os: ['windows', 'linux']
filters: ['Code', 'Most Popular']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/json.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<Tabs>
  <TabItem value="http" label="Bulk uploads over HTTP/HTTPS" default>

To ship logs directly to the Logz.io listener, send them as minified JSON files over an HTTP/HTTPS connection.


### Request path and header

For HTTPS _(recommended)_:

```
https://<<LISTENER-HOST>>:8071?token=<<LOG-SHIPPING-TOKEN>>&type=<<MY-TYPE>>
```

For HTTP: 

```
http://<<LISTENER-HOST>>:8070?token=<<LOG-SHIPPING-TOKEN>>&type=<<MY-TYPE>>
```

{@include: ../../_include/general-shipping/replace-placeholders.html}

* {@include: ../../_include/log-shipping/type.md} Otherwise, the default `type` is `http-bulk`.


### Request body

The request body is a list of logs in minified JSON format, with each log separated by a newline `(\n)`.



Example:

```json
{"message": "Hello there", "counter": 1}
{"message": "Hello again", "counter": 2}
```

### Limitations

* Max body size: 10 MB (10,485,760 bytes).
* Max log line size: 500,000 bytes.
* Type field in the log overrides the `type` in the request header.

For example:

```shell
echo $'{"message":"hello there", "counter": 1}\n{"message":"hello again", "counter": 2}' \
| curl -X POST "http://<<LISTENER-HOST>>:8070?token=<<LOG-SHIPPING-TOKEN>>&type=test_http_bulk" \
-H "user-agent:logzio-json-logs" \
-v --data-binary @-
```

### Possible responses

#### 200 OK

All logs received and validated. Allow some time for data ingestion, then open [Logz.io Log Management account](https://app.logz.io/#/dashboard/osd).

The response body is empty.

#### 400 BAD REQUEST

Invalid input. Response example:


```
{
  "malformedLines": 2, #The number of log lines that aren't valid JSON
  "successfulLines": 10, #The number of valid JSON log lines received
  "oversizedLines": 3, #The number of log lines that exceeded the line length limit
  "emptyLogLines": 4 #The number of empty log lines
}
```

#### 401 UNAUTHORIZED

Missing or invalid token query string parameter. Ensure you're using the correct account token.

Response: "Logging token is missing" or "Logging token is not valid".


#### 413 REQUEST ENTITY TOO LARGE

Request body size exceeds 10 MB.
 
</TabItem>
  <TabItem value="tcp" label="Bulk uploads over TCP">

To ship logs directly to the Logz.io listener, send them as minified JSON files over an HTTP/HTTPS connection.

### JSON log structure


Follow these practices when shipping JSON logs over TCP:


* Each log must be a single-line JSON object.
* Each log line must be 500,000 bytes or less.
* Each log line must be followed by a `\n` (even the last log).
* Include your account token as a top-level property: `{ ... "token": "<<LOG-SHIPPING-TOKEN>>" , ... }`.

### Send TLS/SSL streams over TCP


{@include: ../../_include/log-shipping/certificate.md}


### Send the logs

Using the downloaded certificate, send logs to TCP port 5052 on your region's listener host. For details on finding your account's region, refer to the [Account region](https://docs.logz.io/docs/user-guide/admin/hosting-regions/account-region/) section.


## Check Logz.io for your logs


Allow some time for data ingestion, then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

For troubleshooting, refer to our [log shipping troubleshooting](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/log-shipping-troubleshooting/) guide.

</TabItem>
</Tabs>
