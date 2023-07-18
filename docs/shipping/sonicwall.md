---
id: SonicWall
title: SonicWall
sidebar_position: 1
overview: SonicWall firewalls allow you to identify and control all of the applications in use on your network. This integration allows you to send logs from your SonicWall applications to your Logz.io SIEM account.
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

SonicWall firewalls allow you to identify and control all of the applications in use on your network. This integration allows you to send logs from your SonicWall applications to your Logz.io SIEM account.


#### Configuration

 

##### Before you begin

These are the prerequisites you'll need before you can begin:

* [SonicWall firewall](https://www.sonicwall.com/products/firewalls)
* [Filebeat](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-installation.html)
* root access

##### Configure SonicWall Server logging

Configure your SonicWall firewall to send logs to your Filebeat server.
Make sure you meet this configuration:

* Log format: syslog
* IP address: Filebeat server IP address
* Port 514

SonicWall firewall sends logs over UDP by default. See [SonicWall docs](https://www.sonicwall.com/support/technical-documentation/?language=English) for more information
on configuring your SonicWall firewall.

{@include: ../_include/log-shipping/certificate.md}

##### Configure Filebeat

Open the Filebeat configuration file (/etc/filebeat/filebeat.yml) with your preferred text editor. Copy and paste the code block below, overwriting the previous content.

{@include: ../_include/log-shipping/filebeat-input-extension.md}


This code block adds SonicWall as an input sent over UDP traffic.

```yaml
# ...
filebeat.inputs:
- type: udp
  max_message_size: 10MiB
  host: "0.0.0.0:514"

  fields:
    logzio_codec: plain

    # Your Logz.io account token. You can find your token at
    #  https://app.logz.io/#/dashboard/settings/manage-accounts
    token: <<LOG-SHIPPING-TOKEN>>
    type: sonicwall
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

Copy and paste the following code block directly below.
It sets Logz.io as the output.


```yaml
# ...
output.logstash:
  hosts: ["<<LISTENER-HOST>>:5015"]
  ssl:
    certificate_authorities: ['/etc/pki/tls/certs/COMODORSADomainValidationSecureServerCA.crt']
```


{@include: ../_include//general-shipping/replace-placeholders.html}


:::note
One last validation - make sure Logz.io is the only output and appears only once.
If the file has other outputs, remove them.
:::
 


##### Start Filebeat

[Start or restart Filebeat](https://www.elastic.co/guide/en/beats/filebeat/master/filebeat-starting.html) for the changes to take effect.
Start or restart Filebeat for the changes to take effect.

##### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [Filebeat troubleshooting](https://docs.logz.io/shipping/log-sources/filebeat.html#troubleshooting).

 
