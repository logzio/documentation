## Troubleshooting

If traces are not being sent despite instrumentation, follow these steps:


### Collector not installed

The OpenTelemetry collector may not be installed on your system.

**Suggested remedy**

Ensure the OpenTelemetry collector is installed and configured to receive traces from your hosts.


### Collector path not configured

The collector may not have the correct endpoint configured for the receiver.

**Suggested remedy**

1. Verify the configuration file lists the following endpoints:

   ```yaml
   receivers:
     otlp:
       protocols:
         grpc:
           endpoint: "0.0.0.0:4317"
         http:
           endpoint: "0.0.0.0:4318"
   ```

2. Ensure the endpoint is correctly specified in the instrumentation code. Use Logz.io's [integrations hub](https://app.logz.io/#/dashboard/integrations/collectors?tags=Tracing) to ship your data.




### Traces not generated

The instrumentation code may be incorrect even if the collector and endpoints are properly configured.


**Suggested remedy**


1. Check if the instrumentation can output traces to a console exporter.
2. Use a web-hook to check if the traces are going to the output.
3. Check the metrics endpoint `(http://<<COLLECTOR-HOST>>:8888/metrics)` to see spans received and sent. Replace `<<COLLECTOR-HOST>>` with your collector's address.

If issues persist, refer to Logz.io's [integrations hub](https://app.logz.io/#/dashboard/integrations/collectors?tags=Tracing) and re-instrument the application.


### Wrong exporter/protocol/endpoint

Incorrect exporter, protocol, or endpoint configuration.

The correct endpoints are:

```yaml
   receivers:
     otlp:
       protocols:
         grpc:
           endpoint: "<<COLLECTOR-URL>>:4317"
         http:
           endpoint: "<<COLLECTOR-URL>>:4318/v1/traces"
```

**Suggested remedy**

1. Activate `debug` logs in the collector's configuration


   ```yaml
   service:
     telemetry:
       logs:
         level: "debug"
   ```

Debug logs indicate the status code of the http/https post request.

If the post request is not successful, check if the collector is configured to use the correct exporter, protocol, and/or endpoint.

A successful post request will log status code 200; failure reasons will also be logged.


### Collector failure

The collector may fail to generate traces despite sending `debug` logs.

**Suggested remedy**


1. On Linux and MacOS, view collector logs:

   ```shell
   journalctl | grep otelcol
   ```

   To only see errors:

   ```shell
   journalctl | grep otelcol | grep Error
   ```

2. Otherwise, navigate to the following URL - http://localhost:8888/metrics

This is the endpoint to access the collector metrics in order to see different events that might happen within the collector - receiving spans, sending spans as well as other errors.

### Exporter failure

The exporter configuration may be incorrect, causing trace export issues.


**Suggested remedy**


If you are unable to export traces to a destination, this may be caused by the following:

* There is a network configuration issue.
* The exporter configuration is incorrect.
* The destination is unavailable.

To investigate this issue:

1. Make sure that the `exporters` and `service: pipelines` are configured correctly.
2. Check the collector logs and `zpages` for potential issues.
3. Check your network configuration, such as firewall, DNS, or proxy.

Metrics like the following can provide insights:


```shell
# HELP otelcol_exporter_enqueue_failed_metric_points Number of metric points failed to be added to the sending queue.

# TYPE otelcol_exporter_enqueue_failed_metric_points counter
otelcol_exporter_enqueue_failed_metric_points{exporter="logging",service_instance_id="0582dab5-efb8-4061-94a7-60abdc9867e1",service_version="latest"} 0
```


### Receiver failure

The receiver may not be configured correctly.


**Suggested remedy**

If you are unable to receive data, this may be caused by the following:

* There is a network configuration issue.
* The receiver configuration is incorrect.
* The receiver is defined in the receivers section, but not enabled in any pipelines.
* The client configuration is incorrect.


Metrics for receivers can help diagnose issues:


```shell
# HELP otelcol_receiver_accepted_spans Number of spans successfully pushed into the pipeline.

# TYPE otelcol_receiver_accepted_spans counter
otelcol_receiver_accepted_spans{receiver="otlp",service_instance_id="0582dab5-efb8-4061-94a7-60abdc9867e1",service_version="latest",transport="grpc"} 34


# HELP otelcol_receiver_refused_spans Number of spans that could not be pushed into the pipeline.

# TYPE otelcol_receiver_refused_spans counter
otelcol_receiver_refused_spans{receiver="otlp",service_instance_id="0582dab5-efb8-4061-94a7-60abdc9867e1",service_version="latest",transport="grpc"} 0
```
