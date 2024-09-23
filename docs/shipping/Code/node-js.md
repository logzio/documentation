---
id: Node-js
title: Node.js
overview: Send Node.js logs, metrics, and traces to monitor and maintain your applications' stability, dependability, and performance. By sending your data to Logz.io, you can rapidly spot any issue that might harm your applications and quickly resolve them.
product: ['logs','metrics','tracing']
os: ['windows', 'linux']
filters: ['Code', 'Most Popular']
recommendedFor: ['Software Engineer']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/nodejs.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['2zAdXztEedvoRJzWTR2dY0']
metrics_alerts: ['14UC8nC6PZmuJ0lqOeHnhv']
drop_filter: []
---

## Logs

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<Tabs>
  <TabItem value="logzio-nodejs" label="logzio-nodejs" default>

:::note
[Project's GitHub repo](https://github.com/logzio/logzio-nodejs/)
:::

logzio-nodejs collects log messages in an array and sends them asynchronously when it reaches 100 messages or 10 seconds. It retries on connection reset or timeout every 2 seconds, doubling the interval up to 3 times. It operates asynchronously, ensuring it doesn't block other messages. By default, errors are logged to the console, but this can be customized with a callback function.


### Configure logzio-nodejs

Install the dependency:

```shell
npm install logzio-nodejs
```

Use the sample configuration and edit it according to your needs:

```javascript
// Replace these parameters with your configuration
var logger = require('logzio-nodejs').createLogger({
  token: '<<LOG-SHIPPING-TOKEN>>',
  protocol: 'https',
  host: '<<LISTENER-HOST>>',
  port: '8071',
  type: 'YourLogType'
});
```

### Parameters

| Parameter | Description | Required/Default |
|---|---|---|
| token | Your Logz.io log shipping token securely directs the data to your [Logz.io account](https://app.logz.io/#/dashboard/settings/manage-tokens/log-shipping). {@include: ../../_include/log-shipping/log-shipping-token.html} | Required |
| protocol | `http` or `https`. The value of this parameter affects the default of the `port` parameter. | `http` |
| host  |  {@include: ../../_include/log-shipping/listener-var.md} Replace `<<LISTENER-HOST>>` with the host [for your region](https://docs.logz.io/docs/user-guide/admin/hosting-regions/account-region/#available-regions). The required port depends whether HTTP or HTTPS is used: HTTP = 8070, HTTPS = 8071. | `listener.logz.io` |
| port | Destination port. The default port depends on the `protocol` parameter: `8070` (for HTTP) or `8071` (for HTTPS) | `8070` / `8071` |
| type | {@include: ../../_include/log-shipping/type.md} | `nodejs` |
| sendIntervalMs  | Time to wait between retry attempts, in milliseconds. | `2000` (2 seconds) |
| bufferSize  | Maximum number of messages the logger accumulates before sending them all as a bulk. | `100` |
| numberOfRetries | Maximum number of retry attempts. | `3` |
| debug | Set to `true` to print debug messages to the console.  | `false` |
| callback | A callback function to call when the logger encounters an unrecoverable error. The function API is `function(err)`, where `err` is the Error object. | -- |
| timeout | Read/write/connection timeout, in milliseconds. | -- |
| extraFields | JSON format. Adds your custom fields to each log. Format: `extraFields : { field_1: "val_1", field_2: "val_2" , ... }` | -- |
| setUserAgent | Set to false to send logs without the user-agent field in the request header.  | `true` |

**Code example:**

You can send log lines as a raw string or an object. For consistent and reliable parsing, we recommend sending them as objects:

  ```javascript
  var obj = {
      message: 'Some log message',
      param1: 'val1',
      param2: 'val2',
      tags : ['tag1']
  };
  logger.log(obj);
  ```

To send a raw string:

  ```javascript
  logger.log('This is a log message');
  ```

For serverless environments, such as AWS Lambda, Azure Functions, or Google Cloud Functions, include this line at the end of the run:

  ```javascript
  logger.sendAndClose();
  ```

</TabItem>
  <TabItem value="winston-logzio" label="winston-logzio">

:::note
[Project's GitHub repo](https://github.com/logzio/winston-logzio/)
:::

This winston plugin is a wrapper for the logzio-nodejs appender, allowing you to use the Logz.io shipper with the winston logger framework in your Node.js app.


### Configure winston-logzio

**Before you begin, you'll need**: Winston 3 (for Winston 2, see version v1.0.8). If you're using Typescript, follow the procedure to set up winston with Typescript.


Install the dependency:

```shell
npm install winston-logzio --save
```

Use the sample configuration and edit it according to your needs:

```javascript
const winston = require('winston');
const LogzioWinstonTransport = require('winston-logzio');

const logzioWinstonTransport = new LogzioWinstonTransport({
  level: 'info',
  name: 'winston_logzio',
  token: '<<LOG-SHIPPING-TOKEN>>',
  host: '<<LISTENER-HOST>>',
});


const logger = winston.createLogger({
    format: winston.format.simple(),
    transports: [logzioWinstonTransport],
});

logger.log('warn', 'Just a test message');
```

For serverless environments, such as AWS Lambda, Azure Functions, or Google Cloud Functions, add `await logger.info("API Called")` and include this line at the end of the run:

  ```javascript
  logger.close();
  ```


{@include: ../../_include/general-shipping/replace-placeholders.html}



### Parameters

For a complete list of your options, see the configuration parameters below.👇


| Parameter | Description | Required/Default |
|---|---|---|
| LogzioWinstonTransport | Determines the settings passed to the logzio-nodejs logger. Configure any parameters you want to send to winston when initializing the transport. | -- |
| token | Your Logz.io log shipping token securely directs data to your [Logz.io account](https://app.logz.io/#/dashboard/settings/manage-tokens/log-shipping). {@include: ../../_include/log-shipping/log-shipping-token.html} | Required |
| protocol | `http` or `https`, affecting the default `port` parameter. | `http` |
| host  |  {@include: ../../_include/log-shipping/listener-var.md} {@include: ../../_include/log-shipping/listener-var.html} | `listener.logz.io` |
| port | Destination port based on the `protocol` parameter: `8070` (for HTTP) or `8071` (for HTTPS) | `8070` / `8071` |
| type | {@include: ../../_include/log-shipping/type.md} | `nodejs` |
| sendIntervalMs  | Time to wait between retry attempts, in milliseconds. | `2000` (2 seconds) |
| bufferSize  | Maximum number of messages the logger will accumulate before sending them all as a bulk. | `100` |
| numberOfRetries | Maximum number of retry attempts. | `3` |
| debug | To print debug messages to the console, `true`. Otherwise, `false`. | `false` |
| callback | Callback function for unrecoverable errors. The function API is `function(err)`, where `err` is the Error object. | -- |
| timeout | Read/write/connection timeout, in milliseconds. | -- |
| extraFields | Adds custom fields to each log in JSON format: `extraFields : { field_1: "val_1", field_2: "val_2" , ... }` | -- |
| setUserAgent | Set to `false` to send logs without the user-agent field in the request header. Set to `false` if sending data from Firefox browser. | `true` |

### Additional configuration options

* By default, the winston logger sends all logs to the console. Disable this by adding the following line to your code:

  ```javascript
  winston.remove(winston.transports.Console);
  ```

* Log the last UncaughtException before Node exits:

  ```javascript
  var logzIOTransport = new (winstonLogzIO)(loggerOptions);
  var logger = new(winston.Logger)({
    transports: [
      logzIOTransport
    ],
    exceptionHandlers: [
      logzIOTransport
    ],
    exitOnError: true  // set this to true
  });

  process.on('uncaughtException', function (err) {
    logger.error("UncaughtException processing: %s", err);
    logzIOTransport.flush( function(callback) {
      process.exit(1);
    });
  });
  ```

* Configure HTTPS Shipping

  ```javascript
  var winston = require('winston');
  var logzioWinstonTransport = require('winston-logzio');

  // Replace these parameters with your configuration
  var loggerOptions = {
      token: '<<LOG-SHIPPING-TOKEN>>',
      protocol: 'https',
      host: '<<LISTENER-HOST>>',
      port: '8071',
      type: 'YourLogType'
  };

  winston.add(logzioWinstonTransport, loggerOptions);
  ```

* Add custom tags to winston-logzio

```javascript
var obj = {

    message: 'Your log message',

    tags : ['tag1']

};

logger.log(obj);
```


</TabItem>
  <TabItem value="Typescript" label="winston-logzio Typescript">


### Configure winston-logzio with Typescript


This winston plugin is a TypeScript-compatible wrapper for the logzio-nodejs appender, effectively integrating Logz.io shipper with your Node.js application. With winston-logzio, you can take advantage of the winston logger framework.



**Before you begin, you'll need**: Winston 3 (for Winston 2, see version v1.0.8).


Install the dependency:


```shell
npm install winston-logzio --save
```

Configure winston-logzio with Typescript. If you don't have a `tsconfig.json` file, start by adding one. Run the following command:

```javascript
tsc --init
```

On your `tsconfig.json` file, under `compilerOptions` ensure you have the `esModuleInterop` flag set to `true` or add it:

```javascript
"compilerOptions": {
  ...
  "esModuleInterop": true
}
```


Use the sample configuration and edit it according to your needs:


```javascript
import winston from 'winston';
import LogzioWinstonTransport from 'winston-logzio';
const logzioWinstonTransport = new LogzioWinstonTransport({
  level: 'info',
  name: 'winston_logzio',
  token: '<<LOG-SHIPPING-TOKEN>>',
  host: '<<LISTENER-HOST>>',
});
const logger = winston.createLogger({
    format: winston.format.simple(),
    transports: [logzioWinstonTransport],
});

var obj = {
    message: 'Your log message',
    tags : ['tag1']
};

logger.log(obj);
logger.log('warn', 'Just a test message');
```

### Parameters

For a complete list of your options, see the configuration parameters below.👇


| Parameter | Description | Required/Default |
|---|---|---|
| LogzioWinstonTransport | Determines the settings passed to the logzio-nodejs logger. Configure any parameters you want to send to winston when initializing the transport. | -- |
| token | Your Logz.io log shipping token securely directs data to your [Logz.io account](https://app.logz.io/#/dashboard/settings/manage-tokens/log-shipping). {@include: ../../_include/log-shipping/log-shipping-token.html} | Required |
| protocol | `http` or `https`, affecting the default `port` parameter. | `http` |
| host  |  {@include: ../../_include/log-shipping/listener-var.md} {@include: ../../_include/log-shipping/listener-var.html} | `listener.logz.io` |
| port | Destination port based on the `protocol` parameter: `8070` (for HTTP) or `8071` (for HTTPS) | `8070` / `8071` |
| type | {@include: ../../_include/log-shipping/type.md} | `nodejs` |
| sendIntervalMs  | Time to wait between retry attempts, in milliseconds. | `2000` (2 seconds) |
| bufferSize  | Maximum number of messages the logger will accumulate before sending them all as a bulk. | `100` |
| numberOfRetries | Maximum number of retry attempts. | `3` |
| debug | To print debug messages to the console, `true`. Otherwise, `false`. | `false` |
| callback | Callback function for unrecoverable errors. The function API is `function(err)`, where `err` is the Error object. | -- |
| timeout | Read/write/connection timeout, in milliseconds. | -- |
| extraFields | Adds custom fields to each log in JSON format: `extraFields : { field_1: "val_1", field_2: "val_2" , ... }` | -- |
| setUserAgent | Set to `false` to send logs without the user-agent field in the request header. Set to `false` if sending data from Firefox browser. | `true` |


If you are using winston-logzio in a serverless service (e.g., AWS Lambda, Azure Functions, Google Cloud Functions), add this line at the end of each run to ensure proper logging.

```javascript
await logger.info(“API Called”)

logger.close()
```

{@include: ../../_include/general-shipping/replace-placeholders.html}

### Troubleshooting

To resolve errors related to the `esModuleInterop` flag, ensure you run the appropriate `tsconfig` file. Use one of the following commands:

```
tsc <file-name>.ts --esModuleInterop
```

or

```
tsc --project tsconfig.json  
```

</TabItem>
<TabItem value="OpenTelemetry" label="OpenTelemetry">

This integration uses the OpenTelemetry logging exporter to send logs to Logz.io via the OpenTelemetry Protocol (OTLP) listener.

### Prerequisites
    
- Node
- A Node application
- An active account with Logz.io

:::note
If you need an example aplication to test this integration, please refer to our [NodeJS OpenTelemetry repository](https://github.com/logzio/opentelemetry-examples/tree/main/nodjs/logs).
:::

### Configure the instrumentation


1. Install the dependencies:

   ```shell
   npm install --save @opentelemetry/api-logs
   npm install --save @opentelemetry/sdk-logs
   npm install --save @opentelemetry/exporter-logs-otlp-proto
   ```

2. Configure the Opentelemetry Collector, You can use the sample configuration and edit it according to your needs:

   ```javascript
   const { LoggerProvider, SimpleLogRecordProcessor } = require('@opentelemetry/sdk-logs');
   const { OTLPLogExporter } = require('@opentelemetry/exporter-logs-otlp-proto');
   const { Resource } = require('@opentelemetry/resources');
   
   const resource = new Resource({'service.name': 'YOUR-SERVICE-NAME'});
   const loggerProvider = new LoggerProvider({ resource });
   
   const otlpExporter = new OTLPLogExporter({
     url: 'https://otlp-listener.logz.io/v1/logs',
     headers: {
       Authorization: 'Bearer <LOG-SHIPPING-TOKEN>',
       'user-agent': 'logzio-nodejs-logs-otlp'
     }
   });
   
   loggerProvider.addLogRecordProcessor(new SimpleLogRecordProcessor(otlpExporter));
   
   const logger = loggerProvider.getLogger('example_logger');
   module.exports.logger = logger;
   ```
   
   Replace `YOUR-SERVICE-NAME` with the required service name.
   
   
   {@include: ../../_include/log-shipping/log-shipping-token.md}


    Update the `listener.logz.io` part in `https://otlp-listener.logz.io/v1/logs` with the URL for [your hosting region](https://docs.logz.io/docs/user-guide/admin/hosting-regions/account-region).

   
   :::note
   If your Logz.io account region is not `us-east-1`, add your [region code](https://docs.logz.io/docs/user-guide/admin/hosting-regions/   account-region/#available-regions) to the `url` like so `https://otlp-listener-<<REGION-CODE>>.logz.io/v1/logs`.
   :::

3. Run the application.

### Check Logz.io for your logs


Allow some time for data ingestion, then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

Encounter an issue? See our [log shipping troubleshooting](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/log-shipping-troubleshooting/) guide.


</TabItem>
</Tabs>


## Metrics

These examples use the [OpenTelemetry JS SDK](https://github.com/open-telemetry/opentelemetry-js) and are based on the [OpenTelemetry exporter collector proto](https://github.com/open-telemetry/opentelemetry-js/tree/main/packages/opentelemetry-exporter-collector-proto).



:::note
[Project's GitHub repo](https://github.com/logzio/js-metrics/)
:::


**Before you begin, you'll need**:

Node 14 or higher.

:::note
We recommend using this integration with [the Logz.io Metrics backend](https://app.logz.io/#/dashboard/metrics/), though it is compatible with any backend that supports the `prometheusremotewrite` format.
:::


### Install the SDK package

```shell
npm install logzio-nodejs-metrics-sdk@0.5.0
```

### Initialize the exporter and meter provider

  
```javascript
const MeterProvider = require('@opentelemetry/sdk-metrics-base');
const sdk =  require('logzio-nodejs-metrics-sdk');

const collectorOptions = {
    url: 'https://<<LISTENER-HOST>>:8053',
    headers: {
        "Authorization":"Bearer <<PROMETHEUS-METRICS-SHIPPING-TOKEN>>"
    }
};
// Initialize the exporter
const metricExporter = new sdk.RemoteWriteExporter(collectorOptions);

// Initialize the meter provider
const meter = new MeterProvider({
    readers: [
        new PeriodicExportingMetricReader(
            {
                exporter: metricExporter, 
                exportIntervalMillis: 1000
            })
        ],
}).getMeter('example-exporter');
```
{@include: ../../_include/general-shipping/replace-placeholders-prometheus.html}


### Add required metrics to the code
  
You can use the following metrics:

| Name | Behavior |
| ---- | ---------- |
| Counter           | Metric value can only increase or reset to 0, calculated per `counter.Add(context,value,labels)` request. |
| UpDownCounter     | Metric value can arbitrarily increment or decrement, calculated per `updowncounter.Add(context,value,labels)` request. |
| Histogram         | Metric values are captured by the `histogram.Record(context,value,labels)` function and calculated per request. |

  
For details on these metrics, refer to the OpenTelemetry [documentation](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/metrics/api.md).

Insert the following code after initialization to add a metric:
  
#### Counter

```javascript
const requestCounter = meter.createCounter('Counter', {
    description: 'Example of a Counter', 
});
// Define some labels for your metrics
const labels = { environment: 'prod' };
// Record some value
requestCounter.add(1,labels);
// In logzio Metrics you will see the following metric:
// Counter_total{environment: 'prod'} 1.0
```
  
#### UpDownCounter
  
```javascript
const upDownCounter = meter.createUpDownCounter('UpDownCounter', {
    description: 'Example of an UpDownCounter',
});
// Define some labels for your metrics
const labels = { environment: 'prod' };
// Record some values
upDownCounter.add(5,labels);
upDownCounter.add(-1,labels);
// In logzio you will see the following metric:
// UpDownCounter{environment: 'prod'} 4.0
```

#### Histogram:

```javascript
const histogram = meter.createHistogram('test_histogram', {
    description: 'Example of a histogram',
});
// Define some labels for your metrics
const labels = { environment: 'prod' };
// Record some values
histogram.record(30,labels);
histogram.record(20,labels);
// In logzio you will see the following metrics:
// test_histogram_sum{environment: 'prod'} 50.0
// test_histogram_count{environment: 'prod'} 2.0
// test_histogram_avg{environment: 'prod'} 25.0
```

### View your metrics

Run your application to start sending metrics to Logz.io.

Allow some time for data ingestion, then check your [Metrics dashboard](https://app.logz.io/#/dashboard/metrics/discover?).

Install the pre-built dashboard for enhanced observability.

<!-- logzio-inject:install:grafana:dashboards ids=["2zAdXztEedvoRJzWTR2dY0"] -->

{@include: ../../_include/metric-shipping/generic-dashboard.html}


## Traces

### Auto-instrument Node.js and send Traces to Logz.io

<Tabs>
  <TabItem value="nodejs-traces" label="OpenTelemetry Collector" default>

**Before you begin, you'll need**:

* A Node.js application without instrumentation.
* An active Logz.io account.
* Port `4318` available on your host system.
* A name for your tracing service to identify traces in Logz.io.
 
:::note
This integration uses OpenTelemetry Collector Contrib, not the OpenTelemetry Collector Core.
:::
  

{@include: ../../_include/tracing-shipping/node-steps.md}
 


#### Download and configure the OpenTelemetry collector

Create a directory on your Node.js host, download the appropriate [OpenTelemetry collector](https://github.com/open-telemetry/opentelemetry-collector-contrib/releases) for your OS, and create a `config.yaml` file with the following parameters:


{@include: ../../_include/tracing-shipping/collector-config.md}


{@include: ../../_include/tracing-shipping/replace-tracing-token.html}


#### Start the collector


```shell
<path/to>/otelcontribcol_<VERSION-NAME> --config ./config.yaml
```
* Replace `<path/to>` with the path to the directory where you downloaded the collector.
* Replace `<VERSION-NAME>` with the version name of the collector applicable to your system, e.g. `otelcontribcol_darwin_amd64`.

#### Run the application

Run this command to generate traces:

```shell
node --require './tracer.js' <YOUR-APPLICATION-FILE-NAME>.js
```


#### View your traces

Give your traces some time to ingest, and then open your [Tracing account](https://app.logz.io/#/dashboard/jaeger).


</TabItem>
<TabItem value="nodejs-traces-docker" label="Docker" default>

This integration auto-instruments your Node.js app and runs a containerized OpenTelemetry collector to send traces to Logz.io. Ensure both application and collector containers are on the same network.

**Before you begin, you'll need**:

* A Node.js application without instrumentation.
* An active Logz.io account.
* Port `4317` available on your host system.
* A name for your tracing service to identify traces in Logz.io.


{@include: ../../_include/tracing-shipping/node-steps.md}


{@include: ../../_include/tracing-shipping/docker.md}


{@include: ../../_include/tracing-shipping/replace-tracing-token.html}


#### Run the application

{@include: ../../_include/tracing-shipping/collector-run-note.md}


Run the application to generate traces:

```shell
node --require './tracer.js' <YOUR-APPLICATION-FILE-NAME>.js
```


#### Check Logz.io for your traces

Give your traces some time to ingest, and then open your [Tracing account](https://app.logz.io/#/dashboard/jaeger).


</TabItem>
<TabItem value="nodejs-traces-helm" label="Helm" default>


### Configuration using Helm

You can use a Helm chart to ship traces to Logz.io via the OpenTelemetry collector. Helm is a tool for managing packages of preconfigured Kubernetes resources using charts.

**logzio-k8s-telemetry** allows you to ship traces from your Kubernetes cluster to Logz.io with the OpenTelemetry collector.

 
:::note
This chart is a fork of the [opentelemtry-collector](https://github.com/open-telemetry/opentelemetry-helm-charts/tree/main/charts/opentelemetry-collector) Helm chart. The main repository for Logz.io helm charts are [logzio-helm](https://github.com/logzio/logzio-helm).
:::
  

 
:::caution Important
This integration uses OpenTelemetry Collector Contrib, not the OpenTelemetry Collector Core.
:::
  


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

#### Define the logzio-k8s-telemetry dns name

In most cases, the service name will be `logzio-k8s-telemetry.default.svc.cluster.local`, where `default` is the namespace where you deployed the helm chart and `svc.cluster.name` is your cluster domain name.


  
To find your cluster domain name, run the following command:
  
```shell
kubectl run -it --image=k8s.gcr.io/e2e-test-images/jessie-dnsutils:1.3 --restart=Never shell -- \
sh -c 'nslookup kubernetes.default | grep Name | sed "s/Name:\skubernetes.default//"'
```
  
This command deploys a temporary pod to extract your cluster domain name. You can remove the pod after retrieving the domain name.
  

{@include: ../../_include/tracing-shipping/node-steps.md}

#### Check Logz.io for your traces

Give your traces some time to ingest, and then open your [Tracing account](https://app.logz.io/).





### Customizing Helm chart parameters


To customize the Helm chart parameters, you have the following options:

* Specify parameters using the `--set key=value[,key=value]` argument to `helm install`.

* Edit the `values.yaml`.

* Override default values with your own `my_values.yaml` and apply it in the `helm install` command. 

You can add the following optional parameters as environment variables if needed:
  
| Parameter | Description | 
|---|---|
| secrets.SamplingLatency | Threshold for the span latency - all traces slower than the threshold value will be filtered in. Default 500. | 
| secrets.SamplingProbability | Sampling percentage for the probabilistic policy. Default 10. | 

**Code example:**

You can run the logzio-k8s-telemetry chart with your custom configuration file, which will override the default `values.yaml` settings.

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

To remove all Kubernetes components associated with the chart and delete the release, use the uninstall command.

To uninstall the `logzio-k8s-telemetry` deployment, run:

```shell
helm uninstall logzio-k8s-telemetry
```


</TabItem>
</Tabs>


{@include: ../../_include/tracing-shipping/otel-troubleshooting.md}





 