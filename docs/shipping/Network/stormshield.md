---
id: Stormshield
title: Stormshield
overview: Stormshield provides cyber-security solutions. This integration allows you to send logs from your Stormshield applications to your Logz.io SIEM account.
product: ['logs']
os: ['windows', 'linux']
filters: ['Network', 'Security']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/stormshield.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['']
metrics_alerts: []
drop_filter: []
---

Stormshield provides cyber-security solutions. This integration allows you to send logs from your Stormshield applications to your Logz.io SIEM account.

**Before you begin, you'll need**:

* Stormshield syslog server configured to send logs in legacy format over port tcp/6514
* [Filebeat](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-installation.html)
* root access

 

{@include: ../_include/log-shipping/certificate.md}

##### Configure Filebeat

Open the Filebeat configuration file (/etc/filebeat/filebeat.yml) with your preferred text editor.

{@include: ../_include/log-shipping/filebeat-input-extension.md}


Copy and paste the code block below, overwriting the previous content, to replace the general configuration with the following settings:

```yaml
# ...
filebeat.inputs:
- type: tcp
  max_message_size: 10MiB
  host: "0.0.0.0:6514"

  fields:
    logzio_codec: plain

    # Your Logz.io account token. You can find your token at
    #  https://app.logz.io/#/dashboard/settings/manage-accounts
    token: <<LOG-SHIPPING-TOKEN>>
    type: stormshield
  fields_under_root: true
  encoding: utf-8
  ignore_older: 3h 
  # ... For Filebeat 7 only ...
filebeat.registry.path: /var/lib/filebeat
processors:
- rename:
    fields:
    - from: "agent"
      to: "filebeat_agent"
    ignore_missing: true
- rename:
    fields:
    - from: "log.file.path"
      to: "source"
    ignore_missing: true
```
{@include: ../_include/log-shipping/log-shipping-token.html}

##### Set Logz.io as the output

Still in the same configuration file, check if Logz.io is already an output. If not, add it now.

```
# ...
output.logstash:
  hosts: ["<<LISTENER-HOST>>:5015"]
  ssl:
    certificate_authorities: ['/etc/pki/tls/certs/COMODORSADomainValidationSecureServerCA.crt']
```

{@include: ../_include/log-shipping/listener-var.html} 

One last validation - make sure Logz.io is the only output and appears only once.
If the file has other outputs, remove them.

##### Start Filebeat

[Start or restart Filebeat](https://www.elastic.co/guide/en/beats/filebeat/master/filebeat-starting.html) for the changes to take effect.


##### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [Filebeat troubleshooting](https://docs.logz.io/shipping/log-sources/filebeat.html#troubleshooting).

 
