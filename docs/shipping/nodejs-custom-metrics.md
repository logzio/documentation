---
id: Node-js-custom
title: Node.js
sidebar_position: 1
overview: Deploy this integration to send custom metrics from your Node.js application to Logz.io.
product: ['metrics']
os: ['windows', 'linux']
filters: ['gcp', 'cloud']
logo: https://docs.logz.io/images/logo/logz-symbol.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['']
metrics_alerts: []
---


Deploy this integration to send custom metrics from your Node.js application to Logz.io.

The provided example uses the [OpenTelemetry JS SDK](https://github.com/open-telemetry/opentelemetry-js) and is based on [OpenTelemetry exporter collector proto](https://github.com/open-telemetry/opentelemetry-js/tree/main/packages/opentelemetry-exporter-collector-proto).

**Before you begin, you'll need**:
Node 8 or higher

:::note
We advise to use this integration with [the Logz.io Metrics backend](https://app.logz.io/#/dashboard/metrics/). However, the integration is compatible with all backends that support metrics in `prometheuesrmotewrite` format.
:::
 

#### Configuring your Node.js applicatin to send custom metrics to Logz.io

 

##### Install the SDK package

```shell
npm install logzio-nodejs-metrics-sdk@0.2.1
```

##### Initialize the exporter and meter provider
  
Add the following code to your application:
  
```js
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
{@include: ../_include/general-shipping/replace-placeholders-prometheus.html}


##### Add required metrics to the code
  
This integration allows you to use the following metrics:

| Name | Behavior |
| ---- | ---------- |
| Counter           | Metric value can only go up or be reset to 0, calculated per `counter.Add(context,value,labels)` request. |
| UpDownCounter     | Metric value can arbitrarily increment or decrement, calculated per `updowncounter.Add(context,value,labels)` request. |
| Histogram         | Metric values captured by the `histogram.Record(context,value,labels)` function, calculated per request. |

  
For more information on each of these metrics, see the OpenTelemetry [documentation](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/metrics/api.md).

To add a required metric to your code, copy and paste the required metric code to your application, placing it after the initialization code:
  
###### Counter

```js
// Create your first counter metric
const requestCounter = meter.createCounter('Counter', {
    description: 'Example of a Counter', 
});
// Define some labels for your metrics
const labels = { environment: 'prod' };
// Record some value
requestCounter.bind(labels).add(1);
// In logzio Metrics you will see the following metric:
// Counter_total{environment: 'prod'} 1.0
```
  
###### UpDownCounter
  
```js
// Create UpDownCounter metric
const upDownCounter = meter.createUpDownCounter('UpDownCounter', {
    description: 'Example of a UpDownCounter',
});
// Define some labels for your metrics
const labels = { environment: 'prod' };
// Record some values
upDownCounter.bind(labels);
upDownCounter.add(5);
upDownCounter.add(-1);
// In logzio you will see the following metric:
// UpDownCounter{environment: 'prod'} 4.0
```

###### Histogram:
```js
// Create ValueRecorder metric
const histogram = meter.createHistogram('test_histogram', {
    description: 'Example of a histogram',
});
// Define some labels for your metrics
const labels = { environment: 'prod' };
// Record some values
histogram.bind(labels);
histogram.record(30);
histogram.record(20);
// In logzio you will see the following metrics:
// test_histogram_sum{environment: 'prod'} 50.0
// test_histogram_count{environment: 'prod'} 2.0
// test_histogram_avg{environment: 'prod'} 25.0
```

##### Run your application

Run your application to start sending metrics to Logz.io.


##### Check Logz.io for your metrics

Give your metrics some time to get from your system to ours, and then open [Metrics dashboard](https://app.logz.io/#/dashboard/metrics/discover?).
