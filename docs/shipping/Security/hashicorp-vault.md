---
id: HashiCorp-Vault
title: HashiCorp Vault
overview: HashiCorp Vault secures, stores, and tightly controls access to tokens, passwords, certificates, API keys, and other secrets in modern computing. This integration allows you to send HashiCorp Vault logs to your Logz.io SIEM account.
product: ['logs']
os: ['windows', 'linux']
filters: ['Security']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/hashicorp-vault.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---

HashiCorp Vault secures, stores, and tightly controls access to tokens, passwords, certificates, API keys, and other secrets in modern computing. This integration allows you to send HashiCorp Vault logs to your Logz.io SIEM account.


**Before you begin, you'll need**:

* [Filebeat](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-installation.html) installed
* Root access

 

### Configure Vault to output raw logs

Configure Vault to enable raw log output to the default location.
After making the change, start or restart Vault for the changes to take effect.

:::note
Disabling log hashing means that Vault will send logs in clear text. This is required at this time, because Vault supports decryption for only a limited number of fields that don’t match the fields required by Logz.io Cloud SIEM. When this limitation is resolved, the requirement to send raw logs will be lifted.
:::
 


For more information on logging and enabling audit devices,
see [File Audit Device](https://www.vaultproject.io/docs/audit/file.html) from HashiCorp.


{@include: ../../_include/log-shipping/certificate.md}

### Create your configuration file for Vault

The Filebeat configuration file is at `/etc/filebeat/filebeat.yml` by default.

:::note
To avoid conflicts with fields from other log sources, you'll need to run a dedicated Filebeat instance for Vault logs. This allows Filebeat to rename some fields
to keep Vault logs compatible with Logz.io.
:::
 

{@include: ../../_include/log-shipping/log-shipping-token.html}

{@include: ../../_include/log-shipping/listener-var.html} 

{@include: ../../_include/log-shipping/filebeat-input-extension.md}


```yaml
# ...
filebeat.inputs:
- type: filestream

  paths:
  - /var/log/vault_audit.log

    # Your Logz.io account token. You can find your token at
    #  https://app.logz.io/#/dashboard/settings/manage-accounts
    token: <<LOG-SHIPPING-TOKEN>>
    logzio_type: vault
  fields_under_root: true
  json.keys_under_root: true
  encoding: utf-8
  ignore_older: 3h

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
- rename:
  fields:
  - from: "type"
    to: "hashi_type"
  ignore_missing: true
- rename:
  fields:
  - from: "logzio_type"
    to: "type"
  ignore_missing: true

# ...
output.logstash:
  hosts: ["<<LISTENER-HOST>>:5015"]
  ssl:
    certificate_authorities: ['/etc/pki/tls/certs/COMODORSADomainValidationSecureServerCA.crt']
```

If you're running Filebeat 7 to 8.1, paste the code block below instead:

```yaml
# ...
filebeat.inputs:
- type: log

  paths:
  - /var/log/vault_audit.log

    # Your Logz.io account token. You can find your token at
    #  https://app.logz.io/#/dashboard/settings/manage-accounts
    token: <<LOG-SHIPPING-TOKEN>>
    logzio_type: vault
  fields_under_root: true
  json.keys_under_root: true
  encoding: utf-8
  ignore_older: 3h

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
- rename:
  fields:
  - from: "type"
    to: "hashi_type"
  ignore_missing: true
- rename:
  fields:
  - from: "logzio_type"
    to: "type"
  ignore_missing: true

# ...
output.logstash:
  hosts: ["<<LISTENER-HOST>>:5015"]
  ssl:
    certificate_authorities: ['/etc/pki/tls/certs/COMODORSADomainValidationSecureServerCA.crt']
```



### Start Filebeat

[Start or restart Filebeat](https://www.elastic.co/guide/en/beats/filebeat/master/filebeat-starting.html) for the changes to take effect.

### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [Filebeat troubleshooting](https://docs.logz.io/shipping/log-sources/filebeat.html#troubleshooting).

 
 
