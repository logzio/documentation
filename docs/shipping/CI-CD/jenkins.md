---
id: Jenkins
title: Jenkins
overview: Jenkins is an automation server for building, testing, and deploying software. This integration allows you to send logs and metrics from your Jenkins servers to your Logz.io account.
product: [ 'metrics', 'logs']
os: ['windows', 'linux']
filters: ['CI/CD']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/jenkins.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['7bmikAb2xNPTy7PESlBqXY']
metrics_alerts: []
drop_filter: []
---

## Logs

### Shipping Jenkins logs with Filebeat

**Before you begin, you'll need**:

* [Filebeat](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-installation.html) installed
* Root access
* Port 5015 open



{@include: ../../_include/log-shipping/certificate.md}

#### Add Jenkins as an input

In the Filebeat configuration file (/etc/filebeat/filebeat.yml), add Jenkins to the filebeat.inputs section.

{@include: ../../_include/log-shipping/log-shipping-token.html}

Replace "JENKINS-HOME" with home location of your Jenkins installation

{@include: ../../_include/log-shipping/filebeat-input-extension.md}


```yaml
# ...
filebeat.inputs:
- type: filestream
  paths:
  - /var/log/jenkins/jenkins.log
  - /var/<<JENKINS-HOME>>/jobs/*/builds/lastFailedBuild/log
  fields:
    logzio_codec: plain

    # You can manage your tokens at
    # https://app.logz.io/#/dashboard/settings/manage-tokens/log-shipping
    token: <<LOG-SHIPPING-TOKEN>>
    type: jenkins
  fields_under_root: true
  encoding: utf-8
  ignore_older: 3h
  multiline:
    pattern: '^[A-Z]{1}[a-z]{2} {1,2}[0-9]{1,2}, [0-9]{4} {1,2}[0-9]{1,2}:[0-9]{2}:[0-9]{2}'
    negate: true
    match: after
```

If you're running Filebeat 7 to 8.1, paste the code block below instead:

```yaml
# ...
filebeat.inputs:
- type: log
  paths:
  - /var/log/jenkins/jenkins.log
  - /var/<<JENKINS-HOME>>/jobs/*/builds/lastFailedBuild/log
  fields:
    logzio_codec: plain

    # You can manage your tokens at
    # https://app.logz.io/#/dashboard/settings/manage-tokens/log-shipping
    token: <<LOG-SHIPPING-TOKEN>>
    type: jenkins
  fields_under_root: true
  encoding: utf-8
  ignore_older: 3h
  multiline:
    pattern: '^[A-Z]{1}[a-z]{2} {1,2}[0-9]{1,2}, [0-9]{4} {1,2}[0-9]{1,2}:[0-9]{2}:[0-9]{2}'
    negate: true
    match: after
```



The above configuration assumes the following defaults:

* Log location - `/var/log/jenkins/jenkins.log`
* Log type - `jenkins`

#### Set Logz.io as the output

If Logz.io is not an output, add it now.
Remove all other outputs.

{@include: ../../_include/log-shipping/listener-url.html} 

```yaml
# ...
output.logstash:
  hosts: ["<<LISTENER-HOST>>:5015"]
  ssl:
    certificate_authorities: ['/etc/pki/tls/certs/COMODORSADomainValidationSecureServerCA.crt']
```

#### Start Filebeat

[Start or restart Filebeat](https://www.elastic.co/guide/en/beats/filebeat/master/filebeat-starting.html) for the changes to take effect.

#### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd). You can search for `type:jenkins` to filter for your Jenkins logs. Your logs should be already parsed thanks to the Logz.io preconfigured parsing pipeline.

If you still don't see your logs, see [Filebeat troubleshooting](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/troubleshooting-filebeat/).


## Metrics

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<Tabs>
  <TabItem value="telegraf" label="Telegraf" default>
To send your Prometheus-format Jenkins metrics to Logz.io, you need to add the **inputs.prometheus** and **outputs.http** plug-ins to your Telegraf configuration file.

<!-- logzio-inject:install:grafana:dashboards ids=["7bmikAb2xNPTy7PESlBqXY"] -->

#### Configure Telegraf to send your metrics data to Logz.io

 

##### Set up Telegraf v1.17 or higher

{@include: ../../_include/metric-shipping/telegraf-setup.md}
 
##### Enable the metrics plugin from the Jenkins Web UI

First you need to add the metrics plug-in to your Jenkins configuration. To do this:

1. Login to the Jenkins Web UI and navigate to **Manage Jenkins > Manage Plugins > Available**.
2. Select **Prometheus metrics** and click **Install without restart**.


##### Add the inputs.prometheus plug-in

Now you need to configure the input plug-in to enable Telegraf to scrape the Jenkins data from your hosts. To do this, add the following code to the configuration file:


``` ini
[[inputs.prometheus]]
  # An array of urls to scrape metrics from.
  urls = ["http://localhost:8080/prometheus/"]
  metric_version = 2
```

##### Add the outputs.http plug-in

{@include: ../../_include/metric-shipping/telegraf-outputs.md}
{@include: ../../_include/general-shipping/replace-placeholders-prometheus.html}
  
  </TabItem>
  
  <TabItem value="opentelemetry-collector" label="OpenTelemetry Collector" default>

## Sending Jenkins Metrics to Logz.io with OpenTelemetry

This guide provides step-by-step instructions for configuring a Jenkins server to send metrics to your Logz.io account using the official Jenkins OpenTelemetry plugin and an OpenTelemetry Collector.

We cover two common setup methods: using **Docker** for a containerized environment and a **Local/Native** installation for running directly on a host machine.

### Prerequisites

Before you begin, make sure you have:

* A **Logz.io account** with access to the Metrics tab.
* Your **Logz.io Metrics Shipping Token**.
* Your account's **Logz.io Listener Host**. You can find the correct host for your region in the [Logz.io 
documentation](https://docs.logz.io/docs/user-guide/admin/hosting-regions/account-region/
#supported-regions-for-prometheus-metrics).
* **Docker** installed and running (for the Docker setup).
* **Java 11 or 17** installed on your system (for the Local/Native setup).

### Step 1: Configure the OpenTelemetry Collector

Create a file named `config.yaml` with the following content (applies to both setup methods):

```yaml
receivers:
  otlp:
    protocols:
      grpc:
        # The collector listens on gRPC port 4317 on all available network interfaces.
        endpoint: '0.0.0.0:4317'

exporters:
  prometheusremotewrite:
    endpoint: 'https://<<YOUR-LOGZIO-LISTENER-HOST>>:8053'
    headers:
      Authorization: 'Bearer <<YOUR-LOGZIO-METRICS-TOKEN>>'

processors:
  batch:

service:
  pipelines:
    metrics:
      receivers: [otlp]
      processors: [batch]
      exporters: [prometheusremotewrite]
```

Replace the placeholders:

* `<<YOUR-LOGZIO-LISTENER-HOST>>` – your account's listener host (for example `listener.logz.io` or `listener-eu.logz.io`).
* `<<YOUR-LOGZIO-METRICS-TOKEN>>` – your Logz.io Metrics Shipping Token.

### Step 2: Install and Run Jenkins & the Collector

Choose the installation method that matches your environment.

#### Method A: Docker Setup

1. **Create a Docker network**

   ```bash
   docker network create jenkins-net
   ```

2. **Run the OpenTelemetry Collector container**

   ```bash
   docker run --name otel-collector -d --network jenkins-net -p 4317:4317 -v $(pwd)/config.yaml:/etc/otelcol-contrib/config.yaml otel/opentelemetry-collector-contrib:latest
   ```

3. **Run the Jenkins container**

   ```bash
   docker run --name jenkins-server -d --network jenkins-net -p 8080:8080 jenkins/jenkins:lts-jdk11
   ```

#### Method B: Local/Native Setup

> **Note:** If you haven't already set up Jenkins, follow the [official Jenkins installation guide](https://www.jenkins.io/doc/book/installing/) for your operating system before proceeding with the steps below.

1. **Download and run the Collector**

   ```bash
   # Make the binary executable (macOS/Linux)
   chmod +x ./otelcol-contrib

   # Run the collector
   ./otelcol-contrib --config ./config.yaml
   ```

2. **Download and run Jenkins**

   ```bash
   java -jar jenkins.war
   ```

### Step 3: Configure the Jenkins OpenTelemetry Plugin

1. Open `http://localhost:8080` in your browser and finish the Jenkins setup wizard.
2. Go to **Manage Jenkins › Plugins › Available** and install the **OpenTelemetry** plugin (restart if prompted).
3. Go to **Manage Jenkins › Configure System › OpenTelemetry** and set:
   * **OTLP Endpoint**
     * Docker setup: `http://otel-collector:4317`
     * Local setup: `http://localhost:4317`
   * **Authentication**: *No Authentication*
4. Click **Save**.

### Step 4: Verify the Integration

1. Run a Pipeline job a few times to generate metrics.
2. In Logz.io, open **Metrics › Metrics Explorer**.
3. Search for metrics starting with `jenkins_` (for example `jenkins_job_duration_milliseconds_sum`, `jenkins_job_success_count`). Seeing these metrics confirms the integration is working.

### Troubleshooting

| Symptom | Possible Cause & Fix |
|---------|----------------------|
| `UnknownHostException` (Docker) | Jenkins and Collector containers are not on the same Docker network. Ensure both `docker run` commands include `--network jenkins-net`. |
| `permission denied` or “malware” warning (Local) | Make the Collector executable (`chmod +x`) and, on macOS, remove the quarantine attribute (`xattr -d com.apple.quarantine <file>`). |
| `Connection refused` | Ensure the Collector is running and that the OTLP endpoint value matches your setup (`otel-collector` for Docker, `localhost` for Local). |
| No metrics in Logz.io | Check the listener host and token in `config.yaml` and review Collector logs (`docker logs otel-collector` or terminal output) for exporter errors. |

</Tabs>

#### Check Logz.io for your metrics

Install the pre-built dashboards to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["7bmikAb2xNPTy7PESlBqXY"] -->

{@include: ../../_include/metric-shipping/generic-dashboard.html} 

