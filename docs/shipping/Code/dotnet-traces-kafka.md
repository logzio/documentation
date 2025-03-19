---
id: dotnet-traces-with-kafka-using-opentelemetry
title: .NET Kafka Tracing with OpenTelemetry
overview: Deploy this integration to enable kafka instrumentation of your .NET application using OpenTelemetry.
product: ['tracing']
os: ['windows', 'linux']
filters: ['Code', 'Distributed Messaging']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/kafka.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---

## Manual configuration

This integration includes:

* Installing the `Confluent.Kafka.Extensions.OpenTelemetry` (package)[https://github.com/vhatsura/confluent-kafka-extensions-opentelemetry]. 
* Configuring OpenTelemetry for your .NET application.
* Setting up the OpenTelemetry collector to forward traces to Logz.io.


**Before you begin, you'll need**:

* A .NET application without instrumentation.
* An active Logz.io account.
* Port 4317 available on your host system.
* A name defined for your tracing service to identify traces in Logz.io.

### Install the necessary packages via NuGet

```bash
dotnet add package OpenTelemetry.Extensions.Hosting
dotnet add package OpenTelemetry.Instrumentation.AspNetCore
dotnet add package Confluent.Kafka.Extensions.OpenTelemetry
dotnet add package OpenTelemetry
dotnet add package OpenTelemetry.Exporter.OpenTelemetryProtocol
```
or
```shell
Install-Package OpenTelemetry.Extensions.Hosting
Install-Package OpenTelemetry.Instrumentation.AspNetCore
Install-Package Confluent.Kafka.Extensions.OpenTelemetry
Install-Package OpenTelemetry
Install-Package OpenTelemetry.Exporter.OpenTelemetryProtocol
```

### Kafka OpenTelemery .NET Application
You can download the (example)[https://logzio-aws-integrations-us-east-1.s3.amazonaws.com/dotnet-kafka.zip
] of a instrumented .NET application with a Kafka producer and consumer.

#### Configure OpenTelemetry in .NET
Add the following OpenTelemetry configuration to your .NET application's `Program.cs`:
```csharp
using OpenTelemetry.Trace;
using OpenTelemetry.Resources;
using OpenTelemetry.Exporter;
using Confluent.Kafka.Extensions.OpenTelemetry;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddOpenTelemetry()
    .WithTracing(traceBuilder =>
    {
        traceBuilder
            .SetResourceBuilder(ResourceBuilder.CreateDefault().AddService("kafka-api"))
            .AddAspNetCoreInstrumentation()
            .AddConfluentKafkaInstrumentation()
            .AddOtlpExporter();
    });

var app = builder.Build();
```

You can configure the otlp endpoint and protocol using envurinment variables:
  - OTEL_EXPORTER_OTLP_ENDPOINT (The destination of your otel collector 'http://localhost:4318`)
  - OTEL_EXPORTER_OTLP_PROTOCOL (`grpc` or `http/protubuf`)

#### Instrument Kafka Producer
Build your producer using `.BuildWithInstrumentation()` method, to add instrumentation to your Kafka producer:
```csharp
using Confluent.Kafka;
using Confluent.Kafka.Extensions.Diagnostics;

using var producer =
    new ProducerBuilder<Null, string>(new ProducerConfig(new ClientConfig { BootstrapServers = "localhost:9092" }))
        .SetKeySerializer(Serializers.Null)
        .SetValueSerializer(Serializers.Utf8)
        .BuildWithInstrumentation();

await producer.ProduceAsync("topic", new Message<Null, string> { Value = "Hello World!" });
```

#### Instrument Kafka Consumer
Use `ConsumeWithInstrumentation()` method to add instrumentation to your Kafka consumer:
```csharp
using Confluent.Kafka;
using Confluent.Kafka.Extensions.Diagnostics;

using var consumer = new ConsumerBuilder<Ignore, string>(
        new ConsumerConfig(new ClientConfig { BootstrapServers = "localhost:9092" })
        {
            GroupId = "group", AutoOffsetReset = AutoOffsetReset.Earliest
        })
    .SetValueDeserializer(Deserializers.Utf8)
    .Build();

consumer.Subscribe("topic");

consumer.ConsumeWithInstrumentation((result) =>
{
    Console.WriteLine(result.Message.Value);
});

```

{@include: ../../_include/tracing-shipping/docker.md}


{@include: ../../_include/tracing-shipping/replace-tracing-token.html}
 

* Replace `<path/to>` with the path to the directory where you downloaded the agent.
* Replace `<YOUR-SERVICE-NAME>` with the name of your tracing service defined earlier.

### Check Logz.io for your traces

Give your traces some time to get from your system to ours, and then open [Tracing](https://app.logz.io/#/dashboard/jaeger).


## Configuration via Helm

You can use a Helm chart to ship traces to Logz.io via the OpenTelemetry collector. The Helm tool is used to manage packages of preconfigured Kubernetes resources that use charts.

**logzio-monitoring** allows you to ship traces from your Kubernetes cluster to Logz.io with the OpenTelemetry collector.


### Deploy the Helm chart
 
Add `logzio-helm` repo as follows:
 
```shell
helm repo add logzio-helm https://logzio.github.io/logzio-helm
helm repo update
```

### Run the Helm deployment code

```sh
helm install -n monitoring \
--set logzio-apm-collector.enabled=true \
--set global.logzioTracesToken="{@include: ../../_include/tracing-shipping/replace-tracing-token.html}" \
--set global.logzioRegion="<<LOGZIO_ACCOUNT_REGION_CODE>>" \
--set global.env_id="<<CLUSTER-NAME>>" \
logzio-monitoring logzio-helm/logzio-monitoring
```

| Parameter | Description |
| --- | --- |
| `<<TRACES-SHIPPING-TOKEN>>` | Your [traces shipping token](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=tracing). |
| `<<CLUSTER-NAME>>` | The cluster's name, to easily identify the telemetry data for each environment. |
| `<<LOGZIO_ACCOUNT_REGION_CODE>>` | Name of your Logz.io traces region e.g `us`, `eu`... |



### Define the logzio-monitoring dns name

In most cases, the dns name will be `logzio-k8s-telemetry.<<namespace>>.svc.cluster.local`, where `<<namespace>>` is the namespace where you deployed the helm chart and `svc.cluster.name` is your cluster domain name.
  
If you are not sure what your cluster domain name is, you can run the following command to look it up: 
  
```shell
kubectl run -it --image=k8s.gcr.io/e2e-test-images/jessie-dnsutils:1.3 --restart=Never shell -- \
sh -c 'nslookup kubernetes.<<namespace>> | grep Name | sed "s/Name:\skubernetes.<<namespace>>//"'
```
  
It will deploy a small pod that extracts your cluster domain name from your Kubernetes environment. You can remove this pod after it has returned the cluster domain name.

### Configure your .NET Kafka application to send spans to `logzio-monitoring`

You can configure the otlp endpoint and protocol using envurinment variables:
  - OTEL_EXPORTER_OTLP_ENDPOINT (The destination of your otel collector `<<logzio-monitoring-service-dns>>`)
  - OTEL_EXPORTER_OTLP_PROTOCOL (`grpc` or `http/protubuf`)

* Replace `<<logzio-monitoring-service-dns>>` with the OpenTelemetry collector service DNS obtained previously (service IP is also allowed here).

### Check Logz.io for your traces

Give your traces some time to get from your system to ours, then open [Logz.io](https://app.logz.io/).


###  Customizing Helm chart parameters

#### Configure customization options

You can use the following options to update the Helm chart parameters: 

* Specify parameters using the `--set key=value[,key=value]` argument to `helm install`.

* Edit the `values.yaml`.

* Override default values with your own `my_values.yaml` and apply it in the `helm install` command. 

If required, you can add the following optional parameters as environment variables:
  
| Parameter | Description | 
|---|---|
| logzio-apm-collector.SamplingLatency | Threshold for the span latency - all traces slower than the threshold value will be filtered in. Default 500. | 
| logzio-apm-collector.SamplingProbability | Sampling percentage for the probabilistic policy. Default 10. | 


##### Example

You can run the logzio-monitoring chart with your custom configuration file that takes precedence over the `values.yaml` of the chart.

For example:

 
:::note
The collector will sample **ALL traces** where is some span with error with this example configuration. 
:::
  

```yaml
logzio-apm-collector:
  traceConfig:
    processors:
      tail_sampling:
        policies:
          [
            {
              name: error-in-policy,
              type: status_code,
              status_code: {status_codes: [ERROR]}
            },
            {
              name: slow-traces-policy,
              type: latency,
              latency: {threshold_ms: 400}
            },
            {
              name: health-traces,
              type: and,
              and: {
                and_sub_policy:
                [
                  {
                    name: ping-operation,
                    type: string_attribute,
                    string_attribute: { key: http.url, values: [ /health ] }
                  },
                  {
                    name: main-service,
                    type: string_attribute,
                    string_attribute: { key: service.name, values: [ main-service ] }
                  },
                  {
                    name: probability-policy-1,
                    type: probabilistic,
                    probabilistic: {sampling_percentage: 1}
                  }
                ]
              }
            },
            {
              name: probability-policy,
              type: probabilistic,
              probabilistic: {sampling_percentage: 20}
            }
          ] 
```

```
helm install -f <PATH-TO>/my_values.yaml -n monitoring \
--set logzio.region=<<LOGZIO_ACCOUNT_REGION_CODE>> \
--set logzio.tracing_token={@include: ../../_include/tracing-shipping/replace-tracing-token.html} \
--set traces.enabled=true \
logzio-monitoring logzio-helm/logzio-monitoring
```

Replace `<PATH-TO>` with the path to your custom `values.yaml` file.



### Uninstalling the Chart

The uninstall command is used to remove all the Kubernetes components associated with the chart and to delete the release.  

To uninstall the `logzio-monitoring` deployment, use the following command:

```shell
helm uninstall logzio-monitoring
```


{@include: ../../_include/tracing-shipping/otel-troubleshooting.md}

