---
id: Filebeat-data
title: Filebeat
overview: Filebeat is often the easiest way to get logs from your system to Logz.io. Logz.io has a dedicated configuration wizard to make it simple to configure Filebeat. If you already have Filebeat and you want to add new sources, check out our other shipping instructions to copy&paste just the relevant changes from our code examples.
product: ['logs']
os: ['windows', 'linux']
filters: ['Other']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/beats.svg
logs_dashboards: ['5x2SJocfpcAfRIKZx72LwX']
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---


Filebeat is an easy way to send logs from your system to Logz.io. Use the dedicated configuration wizard for a simple setup.

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<Tabs>
<TabItem value="macos-or-linux" label="macOS or Linux" default>

## Configure Filebeat on MacOS or Linux

### Pre Requirements

Before you begin, you'll need:

{@include: ../../_include/log-shipping/filebeat-installed-port5015-begin.md} 

{@include: ../../_include/log-shipping/filebeat-installed-port5015-end.md}

{@include: ../../_include/log-shipping/certificate.md}

{@include: ../../_include/log-shipping/filebeat-ssl.md}

### Configure Filebeat with Logz.io configuration wizard

{@include: ../../_include/log-shipping/filebeat-input-extension.md}


{@include: ../../_include/log-shipping/filebeat-wizard.html}

<!-- logzio-inject:filebeat-wizard:os-linux -->


{@include: ../../_include/log-shipping/filebeat-wizard.md}


{@include: ../../_include/log-shipping/validate-yaml.md}


#### Move the configuration file to the Filebeat folder

Move your configuration file to `/etc/filebeat/filebeat.yml`.

### Start Filebeat and view logs

[Start or restart Filebeat](https://www.elastic.co/guide/en/beats/filebeat/master/filebeat-starting.html) for the changes to take effect.


Allow some time for data ingestion, then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you don't see your logs, see [Filebeat's troubleshooting guide](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/troubleshooting-filebeat/).

 </TabItem>
<TabItem value="windows" label="Windows" default>

## Configure Filebeat on Windows

### Pre Requirements

Before you begin, you'll need:

{@include: ../../_include/log-shipping/filebeat-installed-port5015-begin.md} installed as a Windows service

{@include: ../../_include/log-shipping/filebeat-installed-port5015-end.md}

### Download the Logz.io public certificate

For HTTPS shipping, download the Logz.io public certificate to your certificate authority folder.


Download the
[Logz.io public certificate]({@include: ../../_include/log-shipping/certificate-path.md})
to `C:\ProgramData\Filebeat\Logzio.crt`
on your machine.

{@include: ../../_include/log-shipping/filebeat-ssl.md}


### Configure Filebeat with Logz.io configuration wizard

{@include: ../../_include/log-shipping/filebeat-input-extension.md}

{@include: ../../_include/log-shipping/filebeat-wizard.html}


<!-- logzio-inject:filebeat-wizard:os-windows -->


{@include: ../../_include/log-shipping/filebeat-wizard.md}


{@include: ../../_include/log-shipping/validate-yaml.md}

#### Move the configuration file to the Filebeat folder

Move the configuration file to `C:\Program Files\Filebeat\filebeat.yml`.

### Restart Filebeat and view logs

Restart Filebeat for the changes to take effect.


```powershell
PS C:\Program Files\Filebeat> Restart-Service filebeat
```

Allow some time for data ingestion, then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).


If you don't see your logs, see [Filebeat's troubleshooting guide](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/troubleshooting-filebeat/).

  </TabItem>
</Tabs>

## Supported Modules

Beat shippers make use of modules to ship data from various sources. Refer to the list below to see which modules each shipper supports.

* [Apache ActiveMQ](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-module-activemq.html#filebeat-module-activemq)
* [AWS](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-module-aws.html)
* [Azure](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-module-azure.html)
* [Google Cloud](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-module-gcp.html)
* [MySQL](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-module-mysql.html)
* [And more](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-modules.html)
