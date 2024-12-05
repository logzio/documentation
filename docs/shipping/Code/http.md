---
id: HTTP
title: HTTP
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

Encounter an issue? See our [log shipping troubleshooting](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/log-shipping-troubleshooting/) guide.

</TabItem>
<TabItem value="otlp" label="Bulk uploads over OpenTelemetry" default>

Follow this guide to send logs in Protobuf format using the Logz.io OTLP listener with the protocurl tool.

### Download protocurl

Download and install `protocurl`, a tool that simplifies interacting with Protobuf files via HTTP. Follow the instructions on the [protocurl GitHub repository](https://github.com/fullstorydev/protocurl).

Verify the installation with:

```bash
protocurl --version
```

### Get OpenTelemetry protobuf definitions

Download the [OpenTelemetry Protobuf definitions](https://github.com/open-telemetry/opentelemetry-proto). The `.proto` files are required to compile Protobuf messages and send logs. Clone the repository to a local folder. For example:

```bash
git clone https://github.com/open-telemetry/opentelemetry-proto.git ~/Downloads/proto/opentelemetry-proto
```

### Construct the command

Use the following command to send logs via `protocurl`:

```bash
protocurl -v \
  -I ~/Downloads/proto/opentelemetry-proto \
  -i opentelemetry.proto.collector.logs.v1.ExportLogsServiceRequest \
  -o opentelemetry.proto.collector.logs.v1.ExportLogsServiceResponse \
  -u '<https://otlp-listener.logz.io/v1/logs>' \
  -H 'Authorization: Bearer <Your-Logzio-Token>' \
  -H 'user-agent: logzio-protobuf-logs' \
  -d @export_logs_request.json
```

Breakdown:

* `-I`: Points to the Protobuf definitions.
* `-i`: Specifies the Protobuf request type.
* `-o`: Specifies the Protobuf response type.
* `-u`: URL of the OTLP listener (update based on your region).
* `-H`: Includes headers like authorization and user-agent.
* `-d`: Path to the JSON file with log data.

### Prepare the JSON data

Create a JSON file (`export_logs_request.json`) 


with the log data structure:








===




Step 4: Prepare the JSON Data
You need to create the export_logs_request.json file, which contains the structure of the log data to be sent to the OTLP listener. The required fields in the log request are as follows:



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
Important Fields:

timeUnixNano: A required field that represents the timestamp in nanoseconds since epoch (e.g., 1727270794000000000 for a future time).

This needs to be manually set, but you can automate it in future feature requests.

severityNumber: Represents the severity level of the log (SEVERITY_NUMBER_INFO, for example).

body: Contains the actual log message.

Step 5: Adjust the Region URL
You must adjust the OTLP listener URL based on your Logz.io account region. Find the correct endpoint for your region here.
For example, if you're in the US region, your endpoint might be:



-u '<https://otlp-listener.logz.io/v1/logs>'
For EU region:



-u '<https://otlp-eu.logz.io/v1/logs>'
Step 6: Full Command Example



protocurl -v \\
  -I ~/Downloads/proto/opentelemetry-proto \\
  -i opentelemetry.proto.collector.logs.v1.ExportLogsServiceRequest \\
  -o opentelemetry.proto.collector.logs.v1.ExportLogsServiceResponse \\
  -u '<https://otlp-listener.logz.io/v1/logs>' \\
  -H 'Authorization: Bearer <Your-Logzio-Token>' \\
  -H 'user-agent: logzio-protobuf-logs' \\
  -d @export_logs_request.json
Step 7: Sample Output in Console
When you run the command, you should see output like this in your console:



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
If everything is set correctly, you should see an HTTP status code 200 OK, indicating that the logs were successfully sent.
===

</TabItem>
</Tabs>
