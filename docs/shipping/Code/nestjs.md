---
id: Nestjs
title: NestJS OpenTelemetry
overview: Deploy this integration to enable automatic instrumentation of your NestJS application using OpenTelemetry. 
product: ['tracing']
os: ['windows', 'linux']
filters: ['Code']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/nest-logo.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---


Deploy this integration to enable automatic instrumentation of your NestJS application using OpenTelemetry. 

## Manual configuration

This integration includes:

* Installing the OpenTelemetry NestJS instrumentation packages on your application host
* Installing the OpenTelemetry collector with Logz.io exporter
* Running your NestJS application in conjunction with the OpenTelemetry instrumentation

On deployment, the NestJS instrumentation automatically captures spans from your application and forwards them to the collector, which exports the data to your Logz.io account.



### Setup auto-instrumentation for your locally hosted NestJS application and send traces to Logz.io

**Before you begin, you'll need**:

* A NestJS application without instrumentation
* An active account with Logz.io
* Port `4317` available on your host system
* A name defined for your tracing service. You will need it to identify the traces in Logz.io.

 
:::note
This integration uses OpenTelemetry Collector Contrib, not the OpenTelemetry Collector Core.
:::
  



#### Download instrumentation packages

Run the following command from the application directory:

```shell
npm install --save @opentelemetry/api
npm install --save @opentelemetry/instrumentation
npm install --save @opentelemetry/tracing
npm install --save @opentelemetry/exporter-collector
npm install --save @opentelemetry/resources
npm install --save @opentelemetry/semantic-conventions
npm install --save @opentelemetry/auto-instrumentations-node
npm install --save @opentelemetry/sdk-node
```

#### Create a tracer file

In the directory of your application file, create a file named `tracer.ts` with the following configuration:

```javascript
"use strict";

const {
    BasicTracerProvider,
    ConsoleSpanExporter,
    SimpleSpanProcessor,
} = require("@opentelemetry/tracing");
const { OTLPTraceExporter } = require("@opentelemetry/exporter-trace-otlp-http");
const { Resource } = require("@opentelemetry/resources");
const {
    SemanticResourceAttributes,
} = require("@opentelemetry/semantic-conventions");

const opentelemetry = require("@opentelemetry/sdk-node");
const {
    getNodeAutoInstrumentations,
} = require("@opentelemetry/auto-instrumentations-node");


const exporter = new OTLPTraceExporter({
    url: "http://localhost:4318/v1/traces"
});

const provider = new BasicTracerProvider({
    resource: new Resource({
        [SemanticResourceAttributes.SERVICE_NAME]:
            "YOUR-SERVICE-NAME", // add the name of your service
    }),
});
// export spans to console (useful for debugging)
provider.addSpanProcessor(new SimpleSpanProcessor(new ConsoleSpanExporter()));
// export spans to opentelemetry collector
provider.addSpanProcessor(new SimpleSpanProcessor(exporter));

provider.register();
const sdk = new opentelemetry.NodeSDK({
    traceExporter: exporter,
    instrumentations: [getNodeAutoInstrumentations()],
});

sdk
    .start()
console.log("Tracing initialized");

process.on("SIGTERM", () => {
    sdk
        .shutdown()
        .then(() => console.log("Tracing terminated"))
        .catch((error) => console.log("Error terminating tracing", error))
        .finally(() => process.exit(0));
});
	
```

#### Refer your application to the tracer file

Add the following to the function of your application code:

```javascript
require('<<PATH-TO-YOUR-FILE>>/tracer.ts');
```

Replace `<<PATH-TO-YOUR-FILE>>` with the path to your tracer file.


#### Download and configure OpenTelemetry collector

Create a dedicated directory on the host of your NestJS application and download the [OpenTelemetry collector](https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/tag/v0.70.0) that is relevant to the operating system of your host.


After downloading the collector, create a configuration file `config.yaml` with the following parameters:

{@include: ../../_include/tracing-shipping/collector-config.md}

{@include: ../../_include/tracing-shipping/replace-tracing-token.html}


#### Start the collector

Run the following command from the directory of your application file:

```shell
<path/to>/otelcontribcol_<VERSION-NAME> --config ./config.yaml
```
* Replace `<path/to>` with the path to the directory where you downloaded the collector.
* Replace `<VERSION-NAME>` with the version name of the collector applicable to your system, e.g. `otelcontribcol_darwin_amd64`.

#### Run the application

Run the following command from the application directory to generate traces:

```shell
npm run start
```


#### Check Logz.io for your traces

Give your traces some time to get from your system to ours, and then open [Tracing](https://app.logz.io/#/dashboard/jaeger).




## Setup auto-instrumentation for your NestJS application using Docker and send traces to Logz.io

This integration enables you to auto-instrument your NestJS application and run a containerized OpenTelemetry collector to send your traces to Logz.io. If your application also runs in a Docker container, make sure that both the application and collector containers are on the same network.

**Before you begin, you'll need**:

* A NestJS application without instrumentation
* An active account with Logz.io
* Port `4317` available on your host system
* A name defined for your tracing service. You will need it to identify the traces in Logz.io.



### Download instrumentation packages

Run the following command from the application directory:

```shell
npm install --save @opentelemetry/api
npm install --save @opentelemetry/instrumentation
npm install --save @opentelemetry/tracing
npm install --save @opentelemetry/exporter-collector
npm install --save @opentelemetry/resources
npm install --save @opentelemetry/semantic-conventions
npm install --save @opentelemetry/auto-instrumentations-node
npm install --save @opentelemetry/sdk-node
```

### Create a tracer file

In the directory of your application file, create a file named `tracer.ts` with the following configuration:

```javascript
"use strict";

const {
	BasicTracerProvider,
	ConsoleSpanExporter,
	SimpleSpanProcessor,
} = require("@opentelemetry/tracing");
const { CollectorTraceExporter } = require("@opentelemetry/exporter-collector");
const { Resource } = require("@opentelemetry/resources");
const {
	SemanticResourceAttributes,
} = require("@opentelemetry/semantic-conventions");

const opentelemetry = require("@opentelemetry/sdk-node");
const {
	getNodeAutoInstrumentations,
} = require("@opentelemetry/auto-instrumentations-node");
const exporter = new CollectorTraceExporter({});

const provider = new BasicTracerProvider({
	resource: new Resource({
		[SemanticResourceAttributes.SERVICE_NAME]:
			"YOUR-SERVICE-NAME", // add the name of your service
	}),
});
provider.addSpanProcessor(new SimpleSpanProcessor(exporter));
provider.addSpanProcessor(new SimpleSpanProcessor(new ConsoleSpanExporter()));
provider.register();
const sdk = new opentelemetry.NodeSDK({
	traceExporter: new opentelemetry.tracing.ConsoleSpanExporter(),
	instrumentations: [getNodeAutoInstrumentations()],
});

sdk
	.start()
console.log("Tracing initialized");

process.on("SIGTERM", () => {
	sdk
		.shutdown()
		.then(() => console.log("Tracing terminated"))
		.catch((error) => console.log("Error terminating tracing", error))
		.finally(() => process.exit(0));
});

```

### Refer your application to the tracer file

Add the following to the function of your application code:

```javascript
require('<<PATH-TO-YOUR-FILE>>/tracer.ts');
```

Replace `<<PATH-TO-YOUR-FILE>>` with the path to your tracer file.


{@include: ../../_include/tracing-shipping/docker.md}
{@include: ../../_include/tracing-shipping/replace-tracing-token.html}


### Run the application

{@include: ../../_include/tracing-shipping/collector-run-note.md}


Run the following command from the application directory to generate traces:

```shell
npm run start
```



### Check Logz.io for your traces

Give your traces some time to get from your system to ours, and then open [Tracing](https://app.logz.io/#/dashboard/jaeger).


## Configuration using Helm

You can use a Helm chart to ship Traces to Logz.io via the OpenTelemetry collector. The Helm tool is used to manage packages of preconfigured Kubernetes resources that use charts.

**logzio-k8s-telemetry** allows you to ship traces from your Kubernetes cluster to Logz.io with the OpenTelemetry collector.

 
:::note
This chart is a fork of the [opentelemtry-collector](https://github.com/open-telemetry/opentelemetry-helm-charts/tree/main/charts/opentelemetry-collector) Helm chart. The main repository for Logz.io helm charts are [logzio-helm](https://github.com/logzio/logzio-helm).
:::
  

 
:::caution Important
This integration uses OpenTelemetry Collector Contrib, not the OpenTelemetry Collector Core.
:::
  

### Standard configuration



#### Deploy the Helm chart
 
Add `logzio-helm` repo as follows:
 
```shell
helm repo add logzio-helm https://logzio.github.io/logzio-helm
helm repo update
```
	
#### Run the Helm deployment code

```
helm install  \
--set secrets.LogzioRegion=<<LOGZIO_ACCOUNT_REGION_CODE>> \
--set secrets.TracesToken=<<TRACING-SHIPPING-TOKEN>> \
--set traces.enabled=true \
--set secrets.env_id=<<ENV_ID>> \
logzio-k8s-telemetry logzio-helm/logzio-k8s-telemetry
```

{@include: ../../_include/tracing-shipping/replace-tracing-token.html}
`<<LOGZIO_ACCOUNT_REGION_CODE>>` - Your Logz.io account region code. [Available regions](https://docs.logz.io/docs/user-guide/admin/hosting-regions/account-region/#available-regions).

#### Define the logzio-k8s-telemetry service dns

In most cases, the service dns will be `logzio-k8s-telemetry.default.svc.cluster.local`, where `default` is the namespace where you deployed the helm chart and `svc.cluster.name` is your cluster domain name.
  
If you are not sure what your cluster domain name is, you can run the following command to look it up: 
  
```shell
kubectl run -it --image=k8s.gcr.io/e2e-test-images/jessie-dnsutils:1.3 --restart=Never shell -- \
sh -c 'nslookup kubernetes.default | grep Name | sed "s/Name:\skubernetes.default//"'
```
  
It will deploy a small pod that extracts your cluster domain name from your Kubernetes environment. You can remove this pod after it has returned the cluster domain name.
  

#### Download instrumentation packages

Run the following command from the application directory:

```shell
npm install --save @opentelemetry/api
npm install --save @opentelemetry/instrumentation
npm install --save @opentelemetry/tracing
npm install --save @opentelemetry/exporter-collector
npm install --save @opentelemetry/resources
npm install --save @opentelemetry/semantic-conventions
npm install --save @opentelemetry/auto-instrumentations-node
npm install --save @opentelemetry/sdk-node
```

#### Create a tracer file

In the directory of your application file, create a file named `tracer.ts` with the following configuration:

```javascript
"use strict";

const {
	BasicTracerProvider,
	ConsoleSpanExporter,
	SimpleSpanProcessor,
} = require("@opentelemetry/tracing");
const { CollectorTraceExporter } = require("@opentelemetry/exporter-collector");
const { Resource } = require("@opentelemetry/resources");
const {
	SemanticResourceAttributes,
} = require("@opentelemetry/semantic-conventions");

const opentelemetry = require("@opentelemetry/sdk-node");
const {
	getNodeAutoInstrumentations,
} = require("@opentelemetry/auto-instrumentations-node");
const exporter = new CollectorTraceExporter({});

const provider = new BasicTracerProvider({
	resource: new Resource({
		[SemanticResourceAttributes.SERVICE_NAME]:
			"YOUR-SERVICE-NAME", // add the name of your service
	}),
});
provider.addSpanProcessor(new SimpleSpanProcessor(exporter));
provider.addSpanProcessor(new SimpleSpanProcessor(new ConsoleSpanExporter()));
provider.register();
const sdk = new opentelemetry.NodeSDK({
	traceExporter: new opentelemetry.tracing.ConsoleSpanExporter(),
	instrumentations: [getNodeAutoInstrumentations()],
});

sdk
	.start()
console.log("Tracing initialized");

process.on("SIGTERM", () => {
	sdk
		.shutdown()
		.then(() => console.log("Tracing terminated"))
		.catch((error) => console.log("Error terminating tracing", error))
		.finally(() => process.exit(0));
});

```

#### Refer your application to the tracer file

Add the following to the function of your application code:

```javascript
require('<<PATH-TO-YOUR-FILE>>/tracer.ts');
```

Replace `<<PATH-TO-YOUR-FILE>>` with the path to your tracer file.



#### Check Logz.io for your traces

Give your traces some time to get from your system to ours, then open [Logz.io](https://app.logz.io/).


###  Customizing Helm chart parameters

#### Configure customization options

You can use the following options to update the Helm chart parameters: 

* Specify parameters using the `--set key=value[,key=value]` argument to `helm install`.

* Edit the `values.yaml`.

* Overide default values with your own `my_values.yaml` and apply it in the `helm install` command. 

If required, you can add the following optional parameters as environment variables:
  
| Parameter | Description | 
|---|---|
| secrets.SamplingLatency | Threshold for the spand latency - all traces slower than the threshold value will be filtered in. Default 500. | 
| secrets.SamplingProbability | Sampling percentage for the probabilistic policy. Default 10. | 

#### Example

You can run the logzio-k8s-telemetry chart with your custom configuration file that takes precedence over the `values.yaml` of the chart.

For example:

 
:::note
The collector will sample **ALL traces** where is some span with error with this example configuration. 
:::
  

```yaml
baseCollectorConfig:
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
helm install -f <PATH-TO>/my_values.yaml \
--set secrets.LogzioRegion=<<LOGZIO_ACCOUNT_REGION_CODE>> \
--set secrets.TracesToken=<<TRACING-SHIPPING-TOKEN>> \
--set traces.enabled=true \
--set secrets.env_id=<<ENV_ID>> \
logzio-k8s-telemetry logzio-helm/logzio-k8s-telemetry
```

Replace `<PATH-TO>` with the path to your custom `values.yaml` file.

{@include: ../../_include/tracing-shipping/replace-tracing-token.html}





### Uninstalling the Chart

The uninstall command is used to remove all the Kubernetes components associated with the chart and to delete the release.  

To uninstall the `logzio-k8s-telemetry` deployment, use the following command:

```shell
helm uninstall logzio-k8s-telemetry
```


{@include: ../../_include/tracing-shipping/otel-troubleshooting.md}

