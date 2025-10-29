---
id: real-user-monitoring
title: Real User Monitoring
overview: Send logs, metrics and traces of real user monitoring (RUM) from your JavaScript applications.
product: ["logs","metrics","tracing"]
os: ["windows", "linux"]
filters: ["JavaScript", "Real user monitoring", "RUM"]
recommendedFor: ["Software Engineer"]
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/js.jpg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---

## Setup

Install the dependency:

```shell
npm install @logzio/browser
```

## Configure LogzioRUM

Call `LogzioRUM.init()` to initialize the RUM client. **This should be done as early as possible in your application lifecycle.**

```javascript
LogzioRUM.init({
  region: <<LOGZIO_REGION_CODE>>,
  tokens: {
    traces: <<LOGZIO_TRACES_TOKEN>>,
    logs: <<LOGZIO_LOGS_TOKEN>>,       // Required unless enable.errorTracking, enable.consoleLogs and enable.viewEvents are set to false
    metrics: <<LOGZIO_METRICS_TOKEN>>, // Required unless enable.webVitals and enable.frustrationDetection are set to false
  },
  endpoint: {
    url: "<<LOGZIO_RUM_URL>>",
  }
  service: {
    name: <<SERVICE_NAME>>,        // Optional
    version: <<SERVICE_VERSION>>,  // Optional
  },
  customAttributes: {
    //// Optional, extra fields containing user metadata to be sent with each event
    //// example:
    // user.name: user.name,
    // user.id: user.id,
    // "user.role": user.role
  },
});
```

### Configuration Options

| Parameter Name                             | Description                                                                                                                                   | Required/Optional | Default                     |
|--------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|-------------------|-----------------------------|
| region                                     | The Logz.io account region code (e.g., `us`, `eu`, `au`, `uk`, `ca`)                                                                          | Required          | `us`                        |
| tokens.traces                              | The Logz.io traces shipping token                                                                                                             | Required          | -                           |
| tokens.logs                                | The Logz.io logs shipping token. **Required unless** `enable.errorTracking`, `enable.consoleLogs` and `enable.viewEvents` are set to `false`. | Required\*        | -                           |
| tokens.metrics                             | The Logz.io metrics shipping token. **Required unless** `enable.webVitals` and `enable.frustrationDetection` are set to `false`.              | Required\*        | -                           |
| endpoint.url                               | Endpoint URL to send the collected data to in OTLP. endpoint.                                                                                 | Required          | -                           |
| endpoint.addSuffix                         | Whether to append data type suffixes (`/traces`, `/metrics`, `/logs`) to the endpoint URL.                                                    | Optional          | `false`                     |
| service.name                               | The name of the service being monitored.                                                                                                      | Optional          | `""`                        |
| service.version                            | The version of the service being monitored.                                                                                                   | Optional          | `""`                        |
| session.maxDurationMs                      | The maximum duration of a session in ms.                                                                                                      | Optional          | `4 * 60 * 60 * 1000` (`4h`) |
| session.timeoutMs                          | If a user is inactive for this duration, the session will end.                                                                                | Optional          | `15 * 60 * 1000` (`15m`)    |
| enable.userActions                         | Enable user actions tracking.                                                                                                                 | Optional          | `true`                      |
| enable.navigation                          | Enables SPA route change detection and treats them as new views.                                                                              | Optional          | `true`                      |
| enable.documentLoad                        | Enables the initial page load span.                                                                                                           | Optional          | `true`                      |
| enable.resourceLoad                        | Enable resource loading tracking such as XHR, fetch, scripts, images.                                                                         | Optional          | `true`                      |
| enable.errorTracking                       | Enable exceptions tracking.                                                                                                                   | Optional          | `true`                      |
| enable.frustrationDetection                | Enable frustration detection such as rage clicks, dead clicks and heavy load times.                                                           | Optional          | `true`                      |
| enable.webVitals                           | Enable performance monitoring. If turned off, no metrics will be sent.                                                                        | Optional          | `true`                      |
| enable.viewEvents                          | Enable view end log event which contains the duration to indicate the current session state.                                                  | Optional          | `false`                     |
| enable.consoleLogs                         | Enable console logs tracking. If turned off, no console logs will be sent.                                                                    | Optional          | `false`                     |
| environmentData.collectOS                  | Enable collection of user operating system name, version and type information.                                                                | Optional          | `true`                      |
| environmentData.collectBrowser             | Enable collection of user browser name, version and engine                                                                                    | Optional          | `true`                      |
| environmentData.collectDevice              | Enable collection of user device type and screen dimensions                                                                                   | Optional          | `true`                      |
| environmentData.collectLanguage            | Enable collection of user language and timezone                                                                                               | Optional          | `true`                      |
| customAttributes                           | Extra fields containing data to be sent with each event. (such as user context)                                                               | Optional          | `{}`                        |
| propagateTraceHeaderCorsUrls               | A list of Backend URLs to propagate the trace header to.                                                                                      | Optional          | `[]`                        |
| samplingRate                               | The rate in which spans are sampled.                                                                                                          | Optional          | `100`(%)                    |
| frustrationThresholds.rageClickCount       | The number of clicks within `rageClickIntervalMs` to consider a click as a rage click.                                                        | Optional          | `3`                         |
| frustrationThresholds.rageClickIntervalMs  | The time interval in milliseconds to consider for rage clicks.                                                                                | Optional          | `1000` (`1s`)               |
| frustrationThresholds.heavyLoadThresholdMs | The time in milliseconds to consider a page load as heavy.                                                                                    | Optional          | `2000` (`2s`)               |
| logLevel                                   | The log level of the RUM library.                                                                                                             | Optional          | `info`                      |


## Dynamically inject attributes
You can dynamically inject attributes that will be added to all data generated by the library by using the `LogzioRUM.setAttributes()` method.
This allows you to add or update attributes at runtime, which can be useful for capturing user-specific data or application state.

```javascript
LogzioRUM.setAttributes({
  ...LogzioRUM.getAttributes(),
  theme: 'dark',
});
```

:::note
Please note that the `LogzioRUM.setAttributes()` method will override any existing attributes.
:::

## Correlate Browser Traces with Backend Traces
To correlate browser traces with backend traces, you need to follow the below steps, to ensure that the `traceparent` header is sent with requests to your backend services.

### Step 1
Configure the `propagateTraceHeaderCorsUrls` option with the URLs of your backend services.  This will ensure that the `traceparent` header is sent with requests to these services.
```javascript
LogzioRUM.init({
  // ... other options
  propagateTraceHeaderCorsUrls: [
    'https://api.example.com', 
    'https://backend.example.com'
  ]
});
```

### Step 2
The `traceparent` header is not CORS-safelisted, so you need to configure your backend to accept it and use it in your backend tracing implementation.
