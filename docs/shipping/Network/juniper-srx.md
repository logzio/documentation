---
id: Juniper-SRX 
title: Juniper SRX 
overview: Juniper SRX is a networking firewall solution and services gateway. If you ship your Juniper firewall logs to your Logz.io Cloud SIEM, you can centralize your security ops and receive alerts about security events logged by Juniper SRX.
product: ['logs']
os: ['windows', 'linux']
filters: ['Network']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/juniper.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---


Juniper SRX is a networking firewall solution and services gateway. If you ship your Juniper firewall logs to your Logz.io Cloud SIEM, you can centralize your security ops and receive alerts about security events logged by Juniper SRX.

Here are just a few examples for security rules written specifically for Juniper SRX and provided out-of-the-box by Logz.io's security team: port scanning activity detected, failed login attempt from a malicious address, and more.

You can review the Juniper SRX resources in your Logz.io Cloud SIEM account, under the pre-configured [Juniper SRX security rules](https://app.logz.io/#/dashboard/security/rules/rule-definitions?from=0&sortBy=updatedAt&sortOrder=DESC&search=juniper) and search for the provided Juniper SRX [dashboards](https://app.logz.io/#/dashboard/security/research/dashboards?) to get you started.


**Before you begin, you'll need**:

* Juniper SRX
* [Filebeat](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-installation.html)
* Root access

 

### Configure Juniper SRX Server logging

Configure your Juniper firewall to send logs to your Filebeat server. Make sure you meet this configuration:

* Log format: syslog
* Send over: UDP
* IP address: Filebeat server IP address
* Port 514

See [Juniper SRX docs](https://kb.juniper.net/InfoCenter/index?page=content&id=KB16502&actp=METADATA) for more information on configuring your Juniper SRX firewall.

{@include: ../../_include/log-shipping/certificate.md}

### Configure Filebeat

Open the Filebeat configuration file (/etc/filebeat/filebeat.yml) with your preferred text editor.
Copy and paste the code block below, overwriting the previous content. (You want to replace the file's content with this code block.)

This code block adds Juniper SRX as an input sent over UDP traffic.

{@include: ../../_include/log-shipping/filebeat-input-extension.md}


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
    type: juniper
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

Copy and paste the following code block directly below. It sets Logz.io as the output.

```yaml
# ...
output.logstash:
  hosts: ["<<LISTENER-HOST>>:5015"]
  ssl:
    certificate_authorities: ['/etc/pki/tls/certs/COMODORSADomainValidationSecureServerCA.crt']
```



{@include: ../../_include//general-shipping/replace-placeholders.html}


:::note
One last validation - make sure Logz.io is the only output and appears only once.
If the file has other outputs, remove them.
:::
 


### Start Filebeat

[Start or restart Filebeat](https://www.elastic.co/guide/en/beats/filebeat/master/filebeat-starting.html) for the changes to take effect.

### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [Filebeat troubleshooting](https://docs.logz.io/shipping/log-sources/filebeat.html#troubleshooting).

 