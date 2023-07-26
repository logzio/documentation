---
id: ESET
title: ESET
overview: ESET provides anti-virus and firewall solutions. This integration allows you to send ESET logs to your Logz.io SIEM account.
product: ['metrics']
os: ['windows', 'linux']
filters: ['gcp', 'cloud']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/eset.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
---

ESET provides anti-virus and firewall solutions. This integration allows you to send ESET logs to your Logz.io SIEM account.

**Before you begin, you'll need**:

* [ESET Endpoint Protection Advanced](https://www.eset.com/us/business/endpoint-protection-advanced/download/) installed
* ESET Admin Console locally installed. (The cloud management console does not support sending logs to a Syslog server and therefore is not supported.)
* [Filebeat](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-installation.html)
* Root access


 

##### Install the ESET certificate on your Filebeat server

ESET sends encrypted data,
so you'll need to create a dedicated ESET certificate to decrypt the logs by the Filebeat server.

```shell
sudo mkdir /etc/filebeat/certificates
sudo openssl req -newkey rsa:2048 -nodes \
-keyout /etc/filebeat/certificates/ESET.key -x509 \
-days 365 \
-out /etc/filebeat/certificates/ESET.crt
```

{@include: ../_include/log-shipping/certificate.md}

##### Configure Filebeat

Open the Filebeat configuration file (/etc/filebeat/filebeat.yml) with your preferred text editor.
Copy and paste the code block below, overwriting the previous content. (You want to replace the file's content with this code block.)

This code block adds ESET as an input and sets Logz.io as the output.

{@include: ../_include/log-shipping/filebeat-input-extension.md}


```yaml
# ...
filebeat.inputs:
- type: tcp
  max_message_size: 10MiB
  host: "0.0.0.0:6514"
  ssl.enabled: true
  ssl.certificate: "/etc/filebeat/certificates/ESET.crt"
  ssl.key: "/etc/filebeat/certificates/ESET.key"
  ssl.verification_mode: none

  fields:
    logzio_codec: plain

    # Your Logz.io account token. You can find your token at
    #  https://app.logz.io/#/dashboard/settings/manage-accounts
    token: <<LOG-SHIPPING-TOKEN>>
    type: eset
  fields_under_root: true
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

##### Configure ESET to send logs to Logzio

Open the ESET Admin Console on the **Security Management Center**.

  1. In the left side menu, click the ellipsis **[⋯]** > **More** > **Server Settings**.
  2. Expand the **Advanced Settings** option.

![ESET Admin Console configuration](https://dytvr9ot2sszz.cloudfront.net/logz-docs/log-shipping/eset-admin-console.png)

Scroll down to **Server Settings** and configure the Syslog server:

In the **SYSLOG SERVER** section, enable the option to **Use Syslog server**. Fill in the details:

  * **Host** - Enter your host address.
  * **Port** - Enter your port number. (Port 6514 unless you've changed the default)
  * **Format** - Select **BSD** as the log format.
  * **Transport** - Select the **TLS** protocol.

In the **LOGGING** section, enable the option to **Export logs to Syslog**. Fill in the details:

  * **Exported logs format** - Select the **JSON** format.

![ESET Admin Console configuration](https://dytvr9ot2sszz.cloudfront.net/logz-docs/log-shipping/eset-admin-console-2.png)


##### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [Filebeat troubleshooting](https://docs.logz.io/shipping/log-sources/filebeat.html#troubleshooting).

 
