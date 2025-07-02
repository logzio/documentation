#### Pull the Docker image for the OpenTelemetry collector

```shell
docker pull otel/opentelemetry-collector-contrib:0.111.0
```

#### Create a configuration file

Create a file `config.yaml` with the following content:

```yaml
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: "0.0.0.0:4317"
      http:
        endpoint: "0.0.0.0:4318"
  

exporters:
  logzio/traces:
    account_token: "<<TRACING-SHIPPING-TOKEN>>"
    region: "<<LOGZIO_ACCOUNT_REGION_CODE>>"
    headers:
      user-agent: logzio-opentelemetry-traces

  debug:

processors:
  batch:
  tail_sampling:
    policies:
      [
        {
          name: policy-errors,
          type: status_code,
          status_code: {status_codes: [ERROR]}
        },
        {
          name: policy-slow,
          type: latency,
          latency: {threshold_ms: 1000}
        }, 
        {
          name: policy-random-ok,
          type: probabilistic,
          probabilistic: {sampling_percentage: 10}
        }        
      ]

extensions:
  pprof:
    endpoint: :1777
  zpages:
    endpoint: :55679
  health_check:

service:
  extensions: [health_check, pprof, zpages]
  pipelines:
    traces:
      receivers: [otlp]
      processors: [tail_sampling, batch]
      exporters: [logging, logzio/traces]
```
 
:::note
Ensure that your service pipeline includes the `debug` exporter in the `exporters` section.
See the OpenTelemetry [Debug Exporter documentation](https://github.com/open-telemetry/opentelemetry-collector/blob/v0.111.0/exporter/debugexporter/README.md) for more details.
:::

{@include: ../../_include/tracing-shipping/replace-tracing-token.html}

#### Tail Sampling  

{@include: ../../_include/tracing-shipping/tail-sampling.md}
 


If you already have an OpenTelemetry installation, add the following parameters to the configuration file of your existing OpenTelemetry collector:

* Under the `exporters` list

```yaml
  logzio/traces:
    account_token: <<TRACING-SHIPPING-TOKEN>>
    region: <<LOGZIO_ACCOUNT_REGION_CODE>>
    headers:
      user-agent: logzio-opentelemetry-traces
```

* Under the `service` list:

```yaml
  extensions: [health_check, pprof, zpages]
  pipelines:
    traces:
      receivers: [otlp]
      processors: [tail_sampling, batch]
      exporters: [logzio/traces]
```


{@include: ../../_include/tracing-shipping/replace-tracing-token.html}

Here is an example configuration file:

```yaml
receivers:  
  otlp:
    protocols:
      grpc:
      http:

exporters:
  logzio/traces:
    account_token: "<<TRACING-SHIPPING-TOKEN>>"
    region: "<<LOGZIO_ACCOUNT_REGION_CODE>>"
    headers:
      user-agent: logzio-opentelemetry-traces

processors:
  batch:
  tail_sampling:
    policies:
      [
        {
          name: policy-errors,
          type: status_code,
          status_code: {status_codes: [ERROR]}
        },
        {
          name: policy-slow,
          type: latency,
          latency: {threshold_ms: 1000}
        }, 
        {
          name: policy-random-ok,
          type: probabilistic,
          probabilistic: {sampling_percentage: 10}
        }        
      ]

extensions:
  pprof:
    endpoint: :1777
  zpages:
    endpoint: :55679
  health_check:

service:
  extensions: [health_check, pprof, zpages]
  pipelines:
    traces:
      receivers: [otlp]
      processors: [tail_sampling, batch]
      exporters: [logzio/traces]
```


{@include: ../../_include/tracing-shipping/replace-tracing-token.html}


#### Run the container

Mount the `config.yaml` as volume to the `docker run` command and run it as follows.

##### Linux

```
docker run  \
--network host \
-v <PATH-TO>/config.yaml:/etc/otelcol-contrib/config.yaml \
otel/opentelemetry-collector-contrib:0.111.0

```

Replace `<PATH-TO>` to the path to the `config.yaml` file on your system.

##### Windows

```
docker run  \
-v <PATH-TO>/config.yaml:/etc/otelcol-contrib/config.yaml \
-p 55678-55680:55678-55680 \
-p 1777:1777 \
-p 9411:9411 \
-p 9943:9943 \
-p 6831:6831 \
-p 6832:6832 \
-p 14250:14250 \
-p 14268:14268 \
-p 4317:4317 \
-p 55681:55681 \
otel/opentelemetry-collector-contrib:0.111.0
```