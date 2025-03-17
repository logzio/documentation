---
id: java-traces-with-kafka-using-opentelemetry
title: Java Traces with Kafka using OpenTelemetry
overview: Deploy this integration to enable automatic instrumentation of your Java application with Kafka using OpenTelemetry.
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

* Downloading the OpenTelemetry Java agent to your application host
* Installing the OpenTelemetry collector with Logz.io exporter
* Establishing communication between the agent and collector

On deployment, the Java agent automatically captures spans from your application and forwards them to the collector, which exports the data to your Logz.io account.



### Setup auto-instrumentation for your Java application using Docker and send traces to Logz.io

This integration enables you to auto-instrument your Java application and run a containerized OpenTelemetry collector to send your traces to Logz.io. If your application also runs in a Docker container, make sure that both the application and collector containers are on the same network.

**Before you begin, you'll need**:

* A Java application without instrumentation
* An active Logz.io account
* Port `4317` available on your host system
* A name defined for your tracing service. You will need it to identify the traces in Logz.io.



### Download Java agent

Download the latest version of the [OpenTelemetry Java agent](https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases/latest/download/opentelemetry-javaagent.jar) to the host of your Java application.


{@include: ../../_include/tracing-shipping/docker.md}


{@include: ../../_include/tracing-shipping/replace-tracing-token.html}



### Attach the agent to the runtime and run it

{@include: ../../_include/tracing-shipping/collector-run-note.md}


Run the following command from the directory of your Java application:

:::note
If you produce and consume Kafka topics/messages from different applications, the Java agent command must be used with both applications in order to provide a full trace.
:::


```shell
java -javaagent:<path/to>/opentelemetry-javaagent.jar \
     -Dotel.metrics.exporter=none \
     -Dotel.resource.attributes=service.name=<YOUR-SERVICE-NAME> \
     -Dotel.instrumentation.messaging.experimental.receive-telemetry.enabled=true
     -jar target/*.jar
```

* Replace `<path/to>` with the path to the directory where you downloaded the agent.
* Replace `<YOUR-SERVICE-NAME>` with the name of your tracing service defined earlier.

### Kafka OpenTelemery Java Applications
There are some pre-written Java applications that insturment Kafka clients with OpenTelemetry.

You can download the relevant applications from the [kafka-opentelemetry GitHub repository](https://github.com/ppatierno/kafka-opentelemetry/tree/main) and compile the JAR file using the `mvn install` command. 

#### Kafka Consumer Example 
Run the OpenTelemetry Java Agent insturmated with the [Kafka consumer application](https://github.com/ppatierno/kafka-opentelemetry/tree/main/kafka-consumer-agent) in the following way:
```shell
java -javaagent:<path/to>/opentelemetry-javaagent.jar \
     -Dotel.metrics.exporter=none \
     -Dotel.resource.attributes=service.name=<YOUR-CONSUMER-NAME> \
     -Dotel.instrumentation.messaging.experimental.receive-telemetry.enabled=true \
     -jar kafka-consumer-agent/target/kafka-consumer-agent-1.0-SNAPSHOT-jar-with-dependencies.jar
```

#### Kafka Producer Example
Run the OpenTelemetry Java Agent insturmated with the [Kafka producer application](https://github.com/ppatierno/kafka-opentelemetry/tree/main/kafka-producer-agent) in the following way:
```shell
java -javaagent:<path/to>/opentelemetry-javaagent.jar \
     -Dotel.metrics.exporter=none \
     -Dotel.resource.attributes=service.name=<YOUR-PRODUCER-NAME> \
     -Dotel.instrumentation.messaging.experimental.receive-telemetry.enabled=true \
     -jar kafka-producer-agent/target/kafka-producer-agent-1.0-SNAPSHOT-jar-with-dependencies.jar
```

### Check Logz.io for your traces

Give your traces some time to get from your system to ours, and then open [Tracing](https://app.logz.io/#/dashboard/jaeger).


### Controlling the number of spans

To limit the number of outgoing spans, you can use the sampling option in the Java agent.

The sampler configures whether spans will be recorded for any call to `SpanBuilder.startSpan`.

| System property                 | Environment variable            | Description                                                  |
|---------------------------------|---------------------------------|--------------------------------------------------------------|
| otel.traces.sampler              | OTEL_TRACES_SAMPLER              | The sampler to use for tracing. Defaults to `parentbased_always_on` |
| otel.traces.sampler.arg          | OTEL_TRACES_SAMPLER_ARG          | An argument to the configured tracer if supported, for example a ratio. |

Supported values for `otel.traces.sampler` are

- "always_on": AlwaysOnSampler
- "always_off": AlwaysOffSampler
- "traceidratio": TraceIdRatioBased. `otel.traces.sampler.arg` sets the ratio.
- "parentbased_always_on": ParentBased(root=AlwaysOnSampler)
- "parentbased_always_off": ParentBased(root=AlwaysOffSampler)
- "parentbased_traceidratio": ParentBased(root=TraceIdRatioBased). `otel.traces.sampler.arg` sets the ratio.



## Configuration via Helm

You can use a Helm chart to ship Traces to Logz.io via the OpenTelemetry collector. The Helm tool is used to manage packages of preconfigured Kubernetes resources that use charts.

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
| `<<LISTENER-HOST>>` | Your account's [listener host](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=logs). |
| `<<LOGZIO-REGION>>` | Name of your Logz.io traces region e.g `us`, `eu`... |



### Define the logzio-monitoring dns name

In most cases, the dns name will be `logzio-apm-collector.<<namespace>>.svc.cluster.local`, where `<<namespace>>` is the namespace where you deployed the helm chart and `svc.cluster.name` is your cluster domain name.
  
If you are not sure what your cluster domain name is, you can run the following command to look it up: 
  
```shell
kubectl run -it --image=k8s.gcr.io/e2e-test-images/jessie-dnsutils:1.3 --restart=Never shell -- \
sh -c 'nslookup kubernetes.<<namespace>> | grep Name | sed "s/Name:\skubernetes.<<namespace>>//"'
```
  
It will deploy a small pod that extracts your cluster domain name from your Kubernetes environment. You can remove this pod after it has returned the cluster domain name.

### Download Java agent

Download the latest version of the [OpenTelemetry Java agent](https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases/latest/download/opentelemetry-javaagent.jar) to the host of your Java application.

### Attach the agent to your java application 

 
:::note
If you produce and consume Kafka topics/messages from different applications, the Java agent command must be used with both applications in order to provide a full trace.
:::
  

Add the following command to your Java application Dockerfile or equivalent:

```shell
java -javaagent:<path/to>/opentelemetry-javaagent-all.jar \
     -Dotel.metrics.exporter=none \
     -Dotel.resource.attributes=service.name=<<YOUR-SERVICE-NAME>> \
     -Dotel.instrumentation.messaging.experimental.receive-telemetry.enabled=true
     -jar target/*.jar
```

* Replace `<<path/to>>` with the path to the directory where you downloaded the agent.
* Replace `<<YOUR-SERVICE-NAME>>` with a name for your service under which it will appear in Logz.io Jaeger UI.
* Replace `<<logzio-monitoring-service-dns>>` with the OpenTelemetry collector service dns obtained previously (service IP is also allowed here).

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
| SamplingLatency | Threshold for the span latency - all traces slower than the threshold value will be filtered in. Default 500. | 
| SamplingProbability | Sampling percentage for the probabilistic policy. Default 10. | 


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

```shell
helm install -f <PATH-TO>/my_values.yaml -n monitoring \
--set global.logzioRegion="<<LOGZIO_ACCOUNT_REGION_CODE>>" \
--set global.env_id="<<ENV-ID>>" \
--set global.logzioTracesToken={@include: ../../_include/tracing-shipping/replace-tracing-token.html} \
--set logzio-apm-collector.enabled=true \
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

