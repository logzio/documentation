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

logzio-nodejs collects log messages in an array, which is sent asynchronously when it reaches its size limit or time limit (100 messages or 10 seconds), whichever comes first.
It contains a simple retry mechanism which upon connection reset or client timeout, tries to send a waiting bulk (2 seconds default).

It's asynchronous, so it doesn't block other messages from being collected and sent.
The interval increases by a factor of 2 between each retry until it reaches the maximum allowed attempts (3).

By default, any error is logged to the console.
You can change this by using a callback function.

#### Configure logzio-nodejs

##### Add the dependency to your project

Navigate to your project's folder in the command line, and run this command to install the dependency.

```shell
npm install logzio-nodejs
```

##### Configure logzio-nodejs

Use the samples in the code block below as a starting point, and replace the sample with a configuration that matches your needs.

For a complete list of options, see the configuration parameters below the code block.👇

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

###### Parameters

| Parameter | Description | Required/Default |
|---|---|---|
| token | Your Logz.io log shipping token securely directs the data to your [Logz.io account](https://app.logz.io/#/dashboard/settings/manage-tokens/log-shipping). {@include: ../../_include/log-shipping/log-shipping-token.html} | Required |
| protocol | `http` or `https`. The value of this parameter affects the default of the `port` parameter. | `http` |
| host  |  {@include: ../../_include/log-shipping/listener-var.md} Replace `<<LISTENER-HOST>>` with the host [for your region](https://docs.logz.io/docs/user-guide/admin/hosting-regions/account-region/#available-regions). For example, `listener.logz.io` if your account is hosted on AWS US East, or `listener-nl.logz.io` if hosted on Azure West Europe. The required port depends whether HTTP or HTTPS is used: HTTP = 8070, HTTPS = 8071. | `listener.logz.io` |
| port | Destination port. The default port depends on the `protocol` parameter: `8070` (for HTTP) or `8071` (for HTTPS) | `8070` / `8071` |
| type | {@include: ../../_include/log-shipping/type.md} | `nodejs` |
| sendIntervalMs  | Time to wait between retry attempts, in milliseconds. | `2000` (2 seconds) |
| bufferSize  | Maximum number of messages the logger accumulates before sending them all as a bulk. | `100` |
| numberOfRetries | Maximum number of retry attempts. | `3` |
| debug | Set to `true` to print debug messsages to the console.  | `false` |
| callback | A callback function to call when the logger encounters an unrecoverable error. The function API is `function(err)`, where `err` is the Error object. | -- |
| timeout | Read/write/connection timeout, in milliseconds. | -- |
| extraFields | JSON format. Adds your custom fields to each log. Format: `extraFields : { field_1: "val_1", field_2: "val_2" , ... }` | -- |
| setUserAgent | Set to false to send logs without the user-agent field in the request header.  | `true` |

###### Code sample

You can send log lines as a raw string or as an object.
For more consistent and reliable parsing, we recommend sending logs as objects.

To send an object (recommended):

  ```javascript
  var obj = {
      message: 'Some log message',
      param1: 'val1',
      param2: 'val2'
  };
  logger.log(obj);
  ```

To send raw text:

  ```javascript
  logger.log('This is a log message');
  ```

Include this line at the end of the run if you're using logzio-nodejs in a severless environment, such as AWS Lambda, Azure Functions, or Google Cloud Functions:

  ```javascript
  logger.sendAndClose();
  ```

###### Custom tags

You can add custom tags to your logs using the following format: `{ tags : ['tag1']}`, for example:

```javascript
var obj = {

    message: 'Your log message',

    tags : ['tag1']

};

logger.log(obj);
```
</TabItem>
  <TabItem value="winston-logzio" label="winston-logzio">

:::note
[Project's GitHub repo](https://github.com/logzio/winston-logzio/)
:::

This winston plugin is a wrapper for the logzio-nodejs appender, which basically means it just wraps our nodejs logzio shipper.
With winston-logzio, you can take advantage of the winston logger framework with your Node.js app.


#### Configure winston-logzio

**Before you begin, you'll need**: Winston 3 (If you're looking for Winston 2, checkout v1.0.8). If you need to run with Typescript, follow the procedure to set up winston with Typescript.

 

##### Add the dependency to your project

Navigate to your project's folder in the command line, and run this command to install the dependency.

```shell
npm install winston-logzio --save
```

##### Configure winston-logzio

Here's a sample configuration that you can use as a starting point.
Use the samples in the code block below or replace the sample with a configuration that matches your needs.

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

If winston-logzio is used as part of a serverless service (AWS Lambda, Azure Functions, Google Cloud Functions, etc.), add `await logger.info(“API Called”)` and `logger.close()` at the end of the run, every time you are using the logger.

{@include: ../../_include/general-shipping/replace-placeholders.html}



##### Parameters

For a complete list of your options, see the configuration parameters below.👇



| Parameter | Description | Required/Default |
|---|---|---|
| LogzioWinstonTransport | This variable determines what will be passed to the logzio nodejs logger itself. If you want to configure the nodejs logger, add any parameters you want to send to winston when initializing the transport. | -- |
| token | Your Logz.io log shipping token securely directs the data to your [Logz.io account](https://app.logz.io/#/dashboard/settings/manage-tokens/log-shipping). {@include: ../../_include/log-shipping/log-shipping-token.html} | Required |
| protocol | `http` or `https`. The value here affects the default of the `port` parameter. | `http` |
| host  |  {@include: ../../_include/log-shipping/listener-var.md} {@include: ../../_include/log-shipping/listener-var.html} | `listener.logz.io` |
| port | Destination port. The default port depends on the `protocol` parameter: `8070` (for HTTP) or `8071` (for HTTPS) | `8070` / `8071` |
| type | {@include: ../../_include/log-shipping/type.md} | `nodejs` |
| sendIntervalMs  | Time to wait between retry attempts, in milliseconds. | `2000` (2 seconds) |
| bufferSize  | Maximum number of messages the logger will accumulate before sending them all as a bulk. | `100` |
| numberOfRetries | Maximum number of retry attempts. | `3` |
| debug | To print debug messsages to the console, `true`. Otherwise, `false`. | `false` |
| callback | A callback function to call when the logger encounters an unrecoverable error. The function API is `function(err)`, where `err` is the Error object. | -- |
| timeout | Read/write/connection timeout, in milliseconds. | -- |
| extraFields | JSON format. Adds your custom fields to each log. Format: `extraFields : { field_1: "val_1", field_2: "val_2" , ... }` | -- |
| setUserAgent | Set to false to send logs without the user-agent field in the request header. If you want to send data from Firefox browser, set that option to false. | `true` |

##### Additional configuration options

* If winston-logzio is used as part of a serverless service (AWS Lambda, Azure Functions, Google Cloud Functions, etc.), add this line at the end of the configuration code block.

  ```javascript
  logger.close()
  ```

* The winston logger by default sends all logs to the console. You can easily disable this by adding this line to your code:

  ```javascript
  winston.remove(winston.transports.Console);
  ```
* To send a log line:

  ```javascript
  winston.log('info', 'winston logger configured with logzio transport');
  ```

* To log the last UncaughtException before Node exits:

  ```javascript
  var logzIOTransport = new (winstonLogzIO)(loggerOptions);
  var logger = new(winston.Logger)({
    transports: [
      logzIOTransport
    ],
    exceptionHandlers: [
      logzIOTransport
    ],
    exitOnError: true    // set this to true
  });

  process.on('uncaughtException', function (err) {
    logger.error("UncaughtException processing: %s", err);
    logzIOTransport.flush( function(callback) {
      process.exit(1);
    });
  });
  ```

* Another configuration option

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

###### Custom tags

You can add custom tags to your logs using the following format: `{ tags : ['tag1']}`, for example:

```javascript
var obj = {

    message: 'Your log message',

    tags : ['tag1']

};

logger.log(obj);
```



  

### winston-logzio setup with Typescript

This winston plugin is a wrapper for the logzio-nodejs appender that runs with Typescript, which basically means it just wraps our nodejs logzio shipper.
With winston-logzio, you can take advantage of the winston logger framework with your Node.js app.


#### Configure winston-logzio

**Before you begin, you'll need**: Winston 3 (If you're looking for Winston 2, checkout v1.0.8)

 

##### Add the dependency to your project

Navigate to your project's folder in the command line, and run this command to install the dependency.

```shell
npm install winston-logzio --save
```

##### Configure winston-logzio with Typescript

If you don't have a `tsconfig.json` file, you'll need to add it first. Start by running:

```javascript
tsc --init
```

On your `tsconfig.json` file, under the parameter `compilerOptions` make sure you have the `esModuleInterop` flag set to `true` or add it:

```javascript
"compilerOptions": {
  ...
  "esModuleInterop": true
}
```

Here's a sample configuration that you can use as a starting point.
Use the samples in the code block below or replace the sample with a configuration that matches your needs.

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
logger.log('warn', 'Just a test message');
```

If winston-logzio is used as part of a serverless service (AWS Lambda, Azure Functions, Google Cloud Functions, etc.), add this line at the end of the configuration code block, every time you are using the logger.

```javascript
await logger.info(“API Called”)

logger.close()
```

{@include: ../../_include/general-shipping/replace-placeholders.html}

### Troubleshooting

To fix errors related to `esModuleInterop` flag make sure you run the relevant `tsconfig` file.
These might help:

```
tsc <file-name>.ts --esModuleInterop
```

or

```
tsc --project tsconfig.json  
```


###### Custom tags

You can add custom tags to your logs using the following format: `{ tags : ['tag1']}`, for example:

```javascript
var obj = {

    message: 'Your log message',

    tags : ['tag1']

};

logger.log(obj);
```
</TabItem>
</Tabs>

## Metrics


Deploy this integration to send custom metrics from your Node.js application to Logz.io.

The provided example uses the [OpenTelemetry JS SDK](https://github.com/open-telemetry/opentelemetry-js) and is based on [OpenTelemetry exporter collector proto](https://github.com/open-telemetry/opentelemetry-js/tree/main/packages/opentelemetry-exporter-collector-proto).

:::note
[Project's GitHub repo](https://github.com/logzio/js-metrics/)
:::


**Before you begin, you'll need**:

Node 8 or higher

:::note
We advise to use this integration with [the Logz.io Metrics backend](https://app.logz.io/#/dashboard/metrics/). However, the integration is compatible with all backends that support metrics in `prometheuesrmotewrite` format.
:::
 

### Configuring your Node.js application to send custom metrics to Logz.io

 

#### Install the SDK package

```shell
npm install logzio-nodejs-metrics-sdk@0.4.0
```

#### Initialize the exporter and meter provider
  
Add the following code to your application:
  
```javascript
const MeterProvider = require('@opentelemetry/sdk-metrics-base');
const sdk =  require('logzio-nodejs-metrics-sdk');

const collectorOptions = {
    url: '<<LISTENER-HOST>>',
    headers: {
        "Authorization":"Bearer <<PROMETHEUS-METRICS-SHIPPING-TOKEN>>"
    }
};
// Initialize the exporter
const metricExporter = new sdk.RemoteWriteExporter(collectorOptions);

// Initialize the meter provider
const meter = new MeterProvider.MeterProvider({
    exporter: metricExporter,
    interval: 15000, // Push interval in milliseconds
}).getMeter('example-exporter');


```
{@include: ../../_include/general-shipping/replace-placeholders-prometheus.html}


#### Add required metrics to the code
  
This integration allows you to use the following metrics:

| Name | Behavior |
| ---- | ---------- |
| Counter           | Metric value can only go up or be reset to 0, calculated per `counter.Add(context,value,labels)` request. |
| UpDownCounter     | Metric value can arbitrarily increment or decrement, calculated per `updowncounter.Add(context,value,labels)` request. |
| Histogram         | Metric values captured by the `histogram.Record(context,value,labels)` function, calculated per request. |

  
For more information on each of these metrics, see the OpenTelemetry [documentation](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/metrics/api.md).

To add a required metric to your code, copy and paste the required metric code to your application, placing it after the initialization code:
  
#### Counter

```javascript
// Create your first counter metric
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
// Create UpDownCounter metric
const upDownCounter = meter.createUpDownCounter('UpDownCounter', {
    description: 'Example of a UpDownCounter',
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
// Create ValueRecorder metric
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

#### Run your application

Run your application to start sending metrics to Logz.io.


#### Check Logz.io for your metrics

Give your metrics some time to get from your system to ours, and then open [Metrics dashboard](https://app.logz.io/#/dashboard/metrics/discover?).

{@include: ../../_include/metric-shipping/custom-dashboard.html} Install the pre-built dashboard to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["2zAdXztEedvoRJzWTR2dY0"] -->

{@include: ../../_include/metric-shipping/generic-dashboard.html}










## Traces




Deploy this integration to enable automatic instrumentation of your Node.js application using OpenTelemetry. 

### Manual configuration

This integration includes:

* Installing the OpenTelemetry Node.js instrumentation packages on your application host
* Installing the OpenTelemetry collector with Logz.io exporter
* Running your Node.js application in conjunction with the OpenTelemetry instrumentation

On deployment, the Node.js instrumentation automatically captures spans from your application and forwards them to the collector, which exports the data to your Logz.io account.



#### Setup auto-instrumentation for your locally hosted Node.js application and send traces to Logz.io

**Before you begin, you'll need**:

* A Node.js application without instrumentation
* An active account with Logz.io
* Port `4318` available on your host system
* A name defined for your tracing service. You will need it to identify the traces in Logz.io.

 
:::note
This integration uses OpenTelemetry Collector Contrib, not the OpenTelemetry Collector Core.
:::
  


{@include: ../../_include/tracing-shipping/node-steps.md}


##### Download and configure OpenTelemetry collector

Create a dedicated directory on the host of your Node.js application and download the [OpenTelemetry collector](https://github.com/open-telemetry/opentelemetry-collector-contrib/releases/tag/v0.82.0) that is relevant to the operating system of your host.


After downloading the collector, create a configuration file `config.yaml` with the following parameters:

{@include: ../../_include/tracing-shipping/collector-config.md}

-

{@include: ../../_include/tracing-shipping/replace-tracing-token.html}


##### Start the collector

Run the following command from the directory of your application file:

```shell
<path/to>/otelcontribcol_<VERSION-NAME> --config ./config.yaml
```
* Replace `<path/to>` with the path to the directory where you downloaded the collector.
* Replace `<VERSION-NAME>` with the version name of the collector applicable to your system, e.g. `otelcontribcol_darwin_amd64`.

##### Run the application

Run the application to generate traces:

```shell
node --require './tracer.js' <YOUR-APPLICATION-FILE-NAME>.js
```


##### Check Logz.io for your traces

Give your traces some time to get from your system to ours, and then open [Tracing](https://app.logz.io/#/dashboard/jaeger).




### Setup auto-instrumentation for your Node.js application using Docker and send traces to Logz.io

This integration enables you to auto-instrument your Node.js application and run a containerized OpenTelemetry collector to send your traces to Logz.io. If your application also runs in a Docker container, make sure that both the application and collector containers are on the same network.

**Before you begin, you'll need**:

* A Node.js application without instrumentation
* An active account with Logz.io
* Port `4317` available on your host system
* A name defined for your tracing service. You will need it to identify the traces in Logz.io.


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

Give your traces some time to get from your system to ours, and then open [Tracing](https://app.logz.io/#/dashboard/jaeger).

### Configuratiion using Helm

You can use a Helm chart to ship Traces to Logz.io via the OpenTelemetry collector. The Helm tool is used to manage packages of preconfigured Kubernetes resources that use charts.

**logzio-k8s-telemetry** allows you to ship traces from your Kubernetes cluster to Logz.io with the OpenTelemetry collector.

 
:::note
This chart is a fork of the [opentelemtry-collector](https://github.com/open-telemetry/opentelemetry-helm-charts/tree/main/charts/opentelemetry-collector) Helm chart. The main repository for Logz.io helm charts are [logzio-helm](https://github.com/logzio/logzio-helm).
:::
  

 
:::caution Important
This integration uses OpenTelemetry Collector Contrib, not the OpenTelemetry Collector Core.
:::
  

#### Standard configuration



##### 1. Deploy the Helm chart
 
Add `logzio-helm` repo as follows:
 
```shell
helm repo add logzio-helm https://logzio.github.io/logzio-helm
helm repo update
```

##### 2. Run the Helm deployment code

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

##### 3. Define the logzio-k8s-telemetry dns name

In most cases, the service name will be `logzio-k8s-telemetry.default.svc.cluster.local`, where `default` is the namespace where you deployed the helm chart and `svc.cluster.name` is your cluster domain name.
  
If you are not sure what your cluster domain name is, you can run the following command to look it up: 
  
```shell
kubectl run -it --image=k8s.gcr.io/e2e-test-images/jessie-dnsutils:1.3 --restart=Never shell -- \
sh -c 'nslookup kubernetes.default | grep Name | sed "s/Name:\skubernetes.default//"'
```
  
It will deploy a small pod that extracts your cluster domain name from your Kubernetes environment. You can remove this pod after it has returned the cluster domain name.
  

{@include: ../../_include/tracing-shipping/node-steps.md}

##### 4. Check Logz.io for your traces

Give your traces some time to get from your system to ours, then open [Logz.io](https://app.logz.io/).



#### Customizing Helm chart parameters

##### Configure customization options

You can use the following options to update the Helm chart parameters: 

* Specify parameters using the `--set key=value[,key=value]` argument to `helm install`.

* Edit the `values.yaml`.

* Overide default values with your own `my_values.yaml` and apply it in the `helm install` command. 

If required, you can add the following optional parameters as environment variables:
  
| Parameter | Description | 
|---|---|
| secrets.SamplingLatency | Threshold for the spand latency - all traces slower than the threshold value will be filtered in. Default 500. | 
| secrets.SamplingProbability | Sampling percentage for the probabilistic policy. Default 10. | 

##### Example

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






#### Uninstalling the Chart

The uninstall command is used to remove all the Kubernetes components associated with the chart and to delete the release.  

To uninstall the `logzio-k8s-telemetry` deployment, use the following command:

```shell
helm uninstall logzio-k8s-telemetry
```


{@include: ../../_include/tracing-shipping/otel-troubleshooting.md}





