---
id: JSON
title: JSON
overview: If you want to ship logs from your code but don't have a library in place, you can send them directly to the Logz.io listener as a minified JSON file.
product: ['logs']
os: ['windows', 'linux']
filters: ['Code']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/json.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---


## Bulk uploads over HTTP/HTTPS

If you want to ship logs from your code but don't have a library in place, you can send them directly to the Logz.io listener as a minified JSON file.

The listeners accept bulk uploads over an HTTP/HTTPS connection or TLS/SSL streams over TCP.

### The request path and header

For HTTPS shipping _(recommended)_, use this URL configuration:

```
https://<<LISTENER-HOST>>:8071?token=<<LOG-SHIPPING-TOKEN>>&type=<<MY-TYPE>>
```

Otherwise, for HTTP shipping, use this configuration:

```
http://<<LISTENER-HOST>>:8070?token=<<LOG-SHIPPING-TOKEN>>&type=<<MY-TYPE>>
```

{@include: ../../_include//general-shipping/replace-placeholders.html}

* {@include: ../../_include/log-shipping/type.md} Otherwise, the default `type` is `http-bulk`.


### The request body

Your request's body is a list of logs in minified JSON format. Also, each log must be separated by a new line. You can escape newlines in a JSON string with `\n`.

For example:

```json
{"message": "Hello there", "counter": 1}
{"message": "Hello again", "counter": 2}
```

### Limitations

* Max body size is 10 MB (10,485,760 bytes)
* Each log line must be 500,000 bytes or less
* If you include a `type` field in the log, it overrides `type` in the request header


### Code sample

```shell
echo $'{"message":"hello there", "counter": 1}\n{"message":"hello again", "counter": 2}' \
  | curl -X POST "http://<<LISTENER-HOST>>:8070?token=<<LOG-SHIPPING-TOKEN>>&type=test_http_bulk" -v --data-binary @-
```

### Possible responses

#### 200 OK

All logs were received and validated. Give your logs some time to get from your system to ours, and then check your [Logz.io Log Management account](https://app.logz.io/#/dashboard/osd) for your logs.

The response body is empty.

#### 400 BAD REQUEST

The input wasn't valid. The response message will look like this:


```
{
  "malformedLines": 2, #The number of log lines that aren't valid JSON
  "successfulLines": 10, #The number of valid JSON log lines received
  "oversizedLines": 3, #The number of log lines that exceeded the line length limit
  "emptyLogLines": 4 #The number of empty log lines
}
```

#### 401 UNAUTHORIZED

The token query string parameter is missing or not valid.
Make sure you're using the right account token.

In the response body, you'll see either "Logging token is missing" or "Logging token is not valid" as the reason for the response.

#### 413 REQUEST ENTITY TOO LARGE

The request body size is larger than 10 MB.
 

## Bulk uploads over TCP



If you want to ship logs from your code but don't have a library in place, you can send them directly to the Logz.io listener as a minified JSON file.

The listeners accept bulk uploads over an HTTP/HTTPS connection or TLS/SSL streams over TCP.


### JSON log structure


Keep to these practices when shipping JSON logs over TCP:

* Each log must be a single-line JSON object
* Each log line must be 500,000 bytes or less
* Each log line must be followed by a `\n` (even the last log)
* Include your account token as a top-level property: `{ ... "token": "<<LOG-SHIPPING-TOKEN>>" , ... }`

### Send TLS/SSL streams over TCP


{@include: ../../_include/log-shipping/certificate.md}


### Send the logs

Using the certificate you just downloaded, send the logs to TCP port 5052 on your region’s listener host. For more information on finding your account’s region, see [Account region](https://docs.logz.io/user-guide/accounts/account-region.html).


## Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [log shipping troubleshooting](https://docs.logz.io/user-guide/log-shipping/log-shipping-troubleshooting.html).
