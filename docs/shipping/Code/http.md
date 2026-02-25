---
id: HTTP
title: HTTP
overview: Ship data from your code directly to the Logz.io listener as a minified JavaScript Object Notation (JSON) file, a standard text-based format for representing structured data based on JavaScript object syntax.
product: ['logs', 'tracing']
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
<TabItem value="http-otlp" label="Protobuf via OpenTelemetry" default>

This guide provides step-by-step instructions to Logz.io users on how to send logs in Protobuf format using the OTLP listener. Follow these steps to set up your environment and send logs via the OTLP protocol using the protocurl tool.

## Download `protocurl`

`protocurl` is a tool based on curl and Protobuf, designed for working with Protobuf-encoded requests over HTTP. Follow the instructions on the [`protocurl` GitHub page](https://github.com/qaware/protocurl) to download and install the tool on your machine.

Once installed, verify the installation with:

```bash
protocurl --version
```

## Download OpenTelemetry Protobuf Definitions

Download the OpenTelemetry Protobuf definitions from the [OpenTelemetry-proto GitHub repository](https://github.com/open-telemetry/opentelemetry-proto/tree/main).

You need the `.proto` files to compile Protobuf messages and send logs. Download the repository to a local folder, for example:

```bash
git clone <https://github.com/open-telemetry/opentelemetry-proto.git> ~/Downloads/proto/opentelemetry-proto
```

## Prepare the Command

Once `protocurl` is installed and the OpenTelemetry Protobuf files are downloaded, you can start sending logs. 

Here is the basic structure of the command:

```bash
protocurl -v \\
  -I ~/Downloads/proto/opentelemetry-proto \\
  -i opentelemetry.proto.collector.logs.v1.ExportLogsServiceRequest \\
  -o opentelemetry.proto.collector.logs.v1.ExportLogsServiceResponse \\
  -u '<https://otlp-listener.logz.io/v1/logs>' \\
  -H 'Authorization: Bearer <Logzio-Token-Logs>' \\
  -H 'user-agent: logzio-protobuf-logs' \\
  -d @export_logs_request.json
```

Breakdown:

* `I`: Points to the location of the OpenTelemetry Protobuf definitions.
* `i`: Specifies the Protobuf request type (`ExportLogsServiceRequest`).
* `o`: Specifies the Protobuf response type (`ExportLogsServiceResponse`).
* `u`: URL of the Logz.io OTLP listener endpoint. Adjust the URL for your region using Logz.io [region settings](https://docs.logz.io/docs/user-guide/admin/hosting-regions/account-region/#opentelemetry-protocol-otlp-regions).
* `H`: Include headers like the Authorization token and user-agent.
* `d`: Specifies the JSON file containing the log data.

## Prepare the JSON Data

You need to create the `export_logs_request.json` file, which contains the structure of the log data to be sent to the OTLP listener. The required fields in the log request are as follows:


```bash
{
  "resourceLogs": [
    {
      "resource": {
        "attributes": [
          {
            "key": "service.name",
            "value": { "stringValue": "example-service" }
          }
        ]
      },
      "scopeLogs": [
        {
          "scope": {
            "name": "example-scope"
          },
          "logRecords": [
            {
              "timeUnixNano": "<timestamp>", // e.g., 1727270794000000000
              "severityNumber": "SEVERITY_NUMBER_INFO",
              "severityText": "INFO",
              "body": { "stringValue": "Log message here" }
            }
          ]
        }
      ]
    }
  ]
}
```

Key fields:

* `timeUnixNano`: A required field that represents the timestamp in nanoseconds since epoch (e.g., `1727270794000000000` for a future time). This needs to be manually set, but you can automate it in future feature requests.
* `severityNumber`: Log severity level (e.g., `SEVERITY_NUMBER_INFO`).
* `body`: The log message content.


## Sample Output in Console

When you run the command, you should see an output like this in your console:

```bash
=========================== POST Request  JSON    =========================== >>>
{
  "resource_logs": [
    {
      "resource": {
        "attributes": [
          {
            "key": "service.name",
            "value": {"string_value": "example-service"}
          }
        ]
      },
      "scope_logs": [
        {
          "scope": {
            "name": "example-scope"
          },
          "log_records": [
            {
              "time_unix_nano": "1727065212000000000",
              "severity_number": "SEVERITY_NUMBER_INFO",
              "severity_text": "INFO",
              "body": {"string_value": "Log message here"}
            }
          ]
        }
      ]
    }
  ]
}
=========================== POST Request Binary =========================== >>>
00000000  0a 5c 0a 23 0a 21 0a 0c  73 65 72 76 69 63 65 2e  |.\\.#.!..service.|
00000010  6e 61 6d 65 12 11 0a 0f  65 78 61 6d 70 6c 65 2d  |name....example-|
...
=========================== POST Response Headers =========================== <<<
HTTP/1.1 200 OK
```

If everything is set correctly, you should see an HTTP status code `200 OK`, indicating the logs were successfully sent.

</TabItem>
</Tabs>
