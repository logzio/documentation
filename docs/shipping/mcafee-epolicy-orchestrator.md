---
id: McAfee-ePolicy-Orchestrator
title: McAfee ePolicy Orchestrator
overview: McAfee ePolicy Orchestrator (McAfee ePO) software centralizes and streamlines management of endpoint, network, data security, and compliance solutions. This integration allows you to send McAfee ePolicy Orchestrator logs to your Logz.io SIEM account.
product: ['metrics']
os: ['windows', 'linux']
filters: ['gcp', 'cloud']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/mcafee.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
---

McAfee ePolicy Orchestrator (McAfee ePO) software centralizes and streamlines management of endpoint, network, data security, and compliance solutions. This integration allows you to send McAfee ePolicy Orchestrator logs to your Logz.io SIEM account.

#### Configuration

**Before you begin, you'll need**:

* [Filebeat](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-installation.html)
* Root access

 

##### Configure McAfee ePO server to forward logs to Filebeat

You'll need to configure McAfee ePO server to forward logs to Filebeat over port 6514.

For more information, see
[Register syslog servers](https://docs.mcafee.com/bundle/epolicy-orchestrator-5.10.0-product-guide/page/GUID-5C5332B3-837A-4DDA-BE5C-1513A230D90A.html)
from McAfee.

##### Install the McAfee certificate on your Filebeat server

McAfee ePO sends encrypted data,
so you'll need to install the McAfee certificate on the Filebeat server.

```shell
sudo mkdir /etc/filebeat/certificates
sudo openssl req -newkey rsa:2048 -nodes \
-keyout /etc/filebeat/certificates/McAfeeEpo.key -x509 \
-days 365 \
-out /etc/filebeat/certificates/McafeeEpo.crt
```

{@include: ../_include/log-shipping/certificate.md}

##### Add TCP traffic as an input

In the Filebeat configuration file (/etc/filebeat/filebeat.yml), add TCP to the filebeat.inputs section.

{@include: ../_include/log-shipping/log-shipping-token.html}

{@include: ../_include/log-shipping/filebeat-input-extension.md}


```yaml
# ...
filebeat.inputs:
- type: tcp
  max_message_size: 10MiB
  host: "0.0.0.0:6514"
  ssl.enabled: true
  ssl.certificate: "/etc/filebeat/certificates/McAfeeEpo.crt"
  ssl.key: "/etc/filebeat/certificates/McAfeeEpo.key"
  ssl.verification_mode: none

  fields:
    logzio_codec: plain

    # Your Logz.io account token. You can find your token at
    #  https://app.logz.io/#/dashboard/settings/manage-accounts
    token: <<LOG-SHIPPING-TOKEN>>
    type: mcafee_epo
  fields_under_root: true
  encoding: utf-8
  ignore_older: 3h
```

If you're running Filebeat 7, paste this code block.
Otherwise, you can leave it out.

```yaml
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

If you're running Filebeat 6, paste this code block.

```yaml
# ... For Filebeat 6 only ...
registry_file: /var/lib/filebeat/registry
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

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [Filebeat troubleshooting](https://docs.logz.io/shipping/log-sources/filebeat.html#troubleshooting).

 
