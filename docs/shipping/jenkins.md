---
id: Jenkins
title: Jenkins
sidebar_position: 1
overview: Jenkins is an automation server for building, testing, and deploying software. This integration allows you to send logs from your Jenkins servers to your Logz.io account.
product: ['metrics']
os: ['windows', 'linux']
filters: ['gcp', 'cloud']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/aiven-logo.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
---


Jenkins is an automation server for building, testing, and deploying software. This integration allows you to send logs from your Jenkins servers to your Logz.io account.

#### Shipping Jenkins logs with Filebeat

**Before you begin, you'll need**:

* [Filebeat](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-installation.html) installed
* Root access
* Port 5015 open



{@include: ../_include/log-shipping/certificate.md}

##### Add Jenkins as an input

In the Filebeat configuration file (/etc/filebeat/filebeat.yml), add Jenkins to the filebeat.inputs section.

{@include: ../_include/log-shipping/log-shipping-token.html}

Replace "JENKINS-HOME" with home location of your Jenkins installation

{@include: ../_include/log-shipping/filebeat-input-extension.md}


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

##### Set Logz.io as the output

If Logz.io is not an output, add it now.
Remove all other outputs.

{@include: ../_include/log-shipping/listener-var.html}

```yaml
# ...
output.logstash:
  hosts: ["<<LISTENER-HOST>>:5015"]
  ssl:
    certificate_authorities: ['/etc/pki/tls/certs/COMODORSADomainValidationSecureServerCA.crt']
```

##### Start Filebeat

[Start or restart Filebeat](https://www.elastic.co/guide/en/beats/filebeat/master/filebeat-starting.html) for the changes to take effect.

##### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd). You can search for `type:jenkins` to filter for your Jenkins logs. Your logs should be already parsed thanks to the Logz.io preconfigured parsing pipeline.

If you still don't see your logs, see [Filebeat troubleshooting](https://docs.logz.io/shipping/log-sources/filebeat.html#troubleshooting).
