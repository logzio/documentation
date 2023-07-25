---
id: Apache-Storm
title: Apache Storm
sidebar_position: 1
overview: test
product: ['logs', 'metrics']
os: ['windows', 'linux']
filters: ['apache', 'cloud']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/apache-storm.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
---

Apache Storm is a free and open source distributed realtime computation system. This integration allows you to send logs from your Apache Storm server instances to your Logz.io account.

#### Step by step

**Before you begin, you'll need**:

* [Filebeat](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-installation.html) installed
* Port 5015 open.
* Root access

 

{@include: ../_include/log-shipping/certificate.md}

##### Find Apache Storm log location

Run the following command to find your Apache Storm logs directory:

```shell
ps -o args= -C java | grep -Po -- '-Dstorm.log.dir=\K[^\s]+'
```



##### Add Apache Storm as an input

In the Filebeat configuration file (/etc/filebeat/filebeat.yml), add Apache to the filebeat.inputs section.


{@include: ../_include/log-shipping/log-shipping-token.html} Replace `<<LOGS_DIRECTORY>>` with the path to your Apache Storm logs directory mentioned in the step above. 

{@include: ../_include/log-shipping/filebeat-input-extension.md}

```yaml
# ...
filebeat.inputs:
- type: filestream

  paths:
    - <<LOGS_DIRECTORY>>/*.log
    - <<LOGS_DIRECTORY>>/workers-artifacts/*/*/*.log*


  fields:
    logzio_codec: plain

    # You can manage your tokens at
    #  https://app.logz.io/#/dashboard/settings/manage-tokens/log-shipping
    token: <<LOG-SHIPPING-TOKEN>>
    type: apache_storm
  fields_under_root: true
  encoding: utf-8
  ignore_older: 3h

```

If you're running Filebeat 7 to 8.1, paste the code block below instead:

```yaml
# ...
filebeat.inputs:
- type: log

  paths:
    - <<LOGS_DIRECTORY>>/*.log
    - <<LOGS_DIRECTORY>>/workers-artifacts/*/*/*.log*


  fields:
    logzio_codec: plain

    # You can manage your tokens at
    #  https://app.logz.io/#/dashboard/settings/manage-tokens/log-shipping
    token: <<LOG-SHIPPING-TOKEN>>
    type: apache_storm
  fields_under_root: true
  encoding: utf-8
  ignore_older: 3h

```



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

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd). You can search for `type:apache_storm` to filter for your Apache Storm logs. 

If you still don't see your logs, see [Filebeat troubleshooting](https://docs.logz.io/shipping/log-sources/filebeat.html#troubleshooting).

  
