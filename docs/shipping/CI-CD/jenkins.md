---
id: Jenkins
title: Jenkins
overview: Jenkins is an automation server for building, testing, and deploying software. This integration allows you to send logs and metrics from your Jenkins servers to your Logz.io account.
product: ['logs']
os: ['windows', 'linux']
filters: ['CI/CD']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/jenkins.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
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

{@include: ../../_include/log-shipping/listener-var.html}

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

#### Check Logz.io for your metrics

{@include: ../../_include/metric-shipping/custom-dashboard.html} Install the pre-built dashboards to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["7bmikAb2xNPTy7PESlBqXY"] -->

{@include: ../../_include/metric-shipping/generic-dashboard.html} 

