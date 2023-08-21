---
id: OSSEC
title: OSSEC
overview: OSSEC is a multiplatform, open source and free Host Intrusion Detection System (HIDS). This integration allows you to send OSSEC logs to your Logz.io SIEM account.
product: ['siem', 'logs']
os: ['windows', 'linux']
filters: ['Security']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/ossec.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---

OSSEC is a multiplatform, open source and free Host Intrusion Detection System (HIDS). This integration allows you to send OSSEC logs to your Logz.io SIEM account.

#### Filebeat configuration

**Before you begin, you'll need**:

* [Filebeat](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-installation.html)
* Root access
* Port 5015 open


 

##### Configure OSSEC to output JSON alerts

In the OSSEC configuration file (/var/ossec/etc/ossec.conf), find the `<global>` tag.
Add the `<jsonout_output>` property and set to `yes`.

```xml
<global>
  <jsonout_output>yes</jsonout_output>
</global>
```

Restart OSSEC.

```shell
sudo /var/ossec/bin/ossec-control restart
```

{@include: ../../_include/log-shipping/certificate.md}

##### Add OSSEC as an input

In the Filebeat configuration file (/etc/filebeat/filebeat.yml), add OSSEC to the filebeat.inputs section.

{@include: ../../_include/log-shipping/log-shipping-token.html}

{@include: ../../_include/log-shipping/filebeat-input-extension.md}


```yaml
# ...
filebeat.inputs:
- type: filestream

  paths:
  - /var/ossec/logs/alerts/alerts.json

  fields:
    logzio_codec: json

    # Your Logz.io account token. You can find your token at
    #  https://app.logz.io/#/dashboard/settings/manage-accounts
    token: <<LOG-SHIPPING-TOKEN>>
    type: ossec
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
  - /var/ossec/logs/alerts/alerts.json

  fields:
    logzio_codec: json

    # Your Logz.io account token. You can find your token at
    #  https://app.logz.io/#/dashboard/settings/manage-accounts
    token: <<LOG-SHIPPING-TOKEN>>
    type: ossec
  fields_under_root: true
  encoding: utf-8
  ignore_older: 3h
```


The above assumes the following defaults:

* Log locations (JSON format) - `/var/ossec/logs/alerts/alerts.json`
* Log locations (plain text format) - `/var/ossec/logs/alerts/alerts.log`

##### Set Logz.io as the output

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

##### Start Filebeat

[Start or restart Filebeat](https://www.elastic.co/guide/en/beats/filebeat/master/filebeat-starting.html) for the changes to take effect.

##### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).


You can search for `type:ossec` to filter for your logs. Your logs should be already parsed thanks to the Logz.io preconfigured parsing pipeline.


If you still don't see your logs, see [Filebeat troubleshooting](https://docs.logz.io/shipping/log-sources/filebeat.html#troubleshooting).

  
