---
sidebar_position: 2
title: OpenTelemetry Traces Troubleshooting
description: Common questions and use cases when setting up OpenTelemetry tracing account
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logz.io, traces, tracing, trace dashboard, dashboard, troubleshoot, opentelemetry, logs, observability, distributed tracing]
---


This section contains some guidelines for handling errors that you may encounter when trying to collect traces with OpenTelemetry.


## Problem: No traces are sent

The code has been instrumented, but the traces are not being sent.

### Possible cause - Collector not installed

The OpenTelemetry collector may not be installed on your system.

###### Suggested remedy

Check if you have an OpenTelemetry collector installed and configured to receive traces from your hosts.


### Possible cause - Collector path not configured

If the collector is installed, it may not have the correct endpoint configured for the receiver.

###### Suggested remedy

1. Check that the configuration file of the collector lists the following endpoints:

   ```yaml
   receivers:
     jaeger:
       protocols:
         thrift_compact:
           endpoint: "0.0.0.0:6831"
         thrift_binary:
           endpoint: "0.0.0.0:6832"
         grpc:
           endpoint: "0.0.0.0:14250"
         thrift_http:
           endpoint: "0.0.0.0:14268"
     opencensus:
       endpoint: "0.0.0.0:55678"
     otlp:
       protocols:
         grpc:
           endpoint: "0.0.0.0:4317"
         http:
           endpoint: "0.0.0.0:4318"
     zipkin:
       endpoint: "0.0.0.0:9411"
   ```

2. In the instrumentation code, make sure that the endpoint is specified correctly. Refer to Logz.io's [integrations hub](https://app.logz.io/#/dashboard/integrations/collectors?tags=Tracing) to learn more about how to send your data.


### Possible cause - Traces not genereated

If the collector is installed and the endpoints are properly configured, the instrumentation code may be incorrect.


###### Suggested remedy


1. Check if the instrumentation can output traces to a console exporter.
2. Use a web-hook to check if the traces are going to the output.
3. Use the metrics endpoint of the collector (`http://<<COLLECTOR-HOST>>:8888/metrics`) to see the number of spans received per receiver and the number of spans sent to the Logz.io exporter.

* Replace `<<COLLECTOR-HOST>>` with the address of your collector host, e.g. `localhost`, if the collector is hosted locally.

If the above steps do not work, refer to Logz.io's [integrations hub](hhttps://app.logz.io/#/dashboard/integrations/collectors?tags=Tracing) and re-instrument the application.


### Possible cause - Wrong exporter/protocol/endpoint

If traces are generated but not send, the collector may be using incorrect exporter, protocol and/or endpoint.

The correct endpoints are:

```yaml
   receivers:
     jaeger:
       protocols:
         thrift_compact:
           endpoint: "<<COLLECTOR-URL>>:6831"
         thrift_binary:
           endpoint: "<<COLLECTOR-URL>>:6832"
         grpc:
           endpoint: "<<COLLECTOR-URL>>:14250"
         thrift_http:
           endpoint: "<<COLLECTOR-URL>>:14268"
     opencensus:
       endpoint: "<<COLLECTOR-URL>>:55678"
     otlp:
       protocols:
         grpc:
           endpoint: "<<COLLECTOR-URL>>:4317"
         http:
           endpoint: "<<COLLECTOR-URL>>:4318/v1/traces"
     zipkin:
       endpoint: "<<COLLECTOR-URL>>:9411/api/v2/spans"
```

###### Suggested remedy


1. Activate `debug` logs in the configuration file of the collector as follows:

   ```yaml
   service:
     telemetry:
       logs:
         level: "debug"
   ```

Debug logs indicate the status code of the http/https post request.

If the post request is not successful, check if the collector is configured to use the correct exporter, protocol, and/or endpoint.

If the post request is successful, there will be an additional log with the status code 200. If the post request failed for some reason, there would be another log with the reason for the failure.


### Possible cause - Collector failure

If the `debug` logs are sent, but the traces are still not generated, the collector logs need to be investigated.

###### Suggested remedy


1. On Linux and MacOS, see the logs for the collector:

   ```shell
   journalctl | grep otelcol
   ```

   To only see errors:

   ```shell
   journalctl | grep otelcol | grep Error
   ```

2. Otherwise, navigate to the following URL - http://localhost:8888/metrics

This is the endpoint to access the collector metrics in order to see different events that might happen within the collector - receiving spans, sending spans as well as other errors.

### Possible cause - Exporter failure

Traces may not be generated if the exporter is not configured properly.

###### Suggested remedy


If you are unable to export traces to a destination, this may be caused by the following:

* There is a network configuration issue
* The exporter configuration is incorrect
* The destination is unavailable

To investigate this issue:

1. Make sure that the `exporters` and `service: pipelines` are configured correctly.
2. Check the collector logs as well as `zpages` for potential issues.
3. Check your network configuration, such as firewall, DNS, or proxy.

For example, those metrics can provide information about the exporter:

```shell
# HELP otelcol_exporter_enqueue_failed_metric_points Number of metric points failed to be added to the sending queue.

# TYPE otelcol_exporter_enqueue_failed_metric_points counter
otelcol_exporter_enqueue_failed_metric_points{exporter="logging",service_instance_id="0582dab5-efb8-4061-94a7-60abdc9867e1",service_version="latest"} 0
```


### Possible cause - Receiver failure

Traces may not be generated if the receiver is not configured properly.


###### Suggested remedy


If you are unable to receive data, this may be caused by the following:

* There is a network configuration issue
* The receiver configuration is incorrect
* The receiver is defined in the receivers section, but not enabled in any pipelines
* The client configuration is incorrect


Those metrics can provide about the receiver:

```shell
# HELP otelcol_receiver_accepted_spans Number of spans successfully pushed into the pipeline.

# TYPE otelcol_receiver_accepted_spans counter
otelcol_receiver_accepted_spans{receiver="otlp",service_instance_id="0582dab5-efb8-4061-94a7-60abdc9867e1",service_version="latest",transport="grpc"} 34


# HELP otelcol_receiver_refused_spans Number of spans that could not be pushed into the pipeline.

# TYPE otelcol_receiver_refused_spans counter
otelcol_receiver_refused_spans{receiver="otlp",service_instance_id="0582dab5-efb8-4061-94a7-60abdc9867e1",service_version="latest",transport="grpc"} 0
```
