---
id: OpenVAS
title: OpenVAS
sidebar_position: 1
overview: These instructions show you how to configure Filebeat to send OpenVAS reports to Logz.io.
product: ['metrics']
os: ['windows', 'linux']
filters: ['gcp', 'cloud']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/aiven-logo.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['']
metrics_alerts: []
---


[OpenVAS](https://www.openvas.org/about.html) (Open Vulnerability Assessment System) is an open source vulnerability scanner. The following instructions show you how to configure Filebeat to send OpenVAS reports to Logz.io.

Once you start sending OpenVAS reports to your Cloud SIEM, you'll be able to review events triggered by pre-configured [OpenVAS security rules](https://app.logz.io/#/dashboard/security/rules/rule-definitions?from=0&sortBy=updatedAt&sortOrder=DESC&search=openvas) and [dashboards](https://app.logz.io/#/dashboard/security/research/dashboards?).

#### Step by step


**Before you begin, you'll need**:

* [Filebeat](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-installation.html)
* Root access
* [OpenVAS](https://www.openvas.org/about.html)

 

{@include: ../_include/log-shipping/certificate.md}

##### Configure Filebeat

Open the Filebeat configuration file (/etc/filebeat/filebeat.yml) with your preferred text editor.
Copy and paste the code block below, overwriting the previous content. (You want to replace the file's content with this code block.)

This code block adds OpenVAS as an input and sets Logz.io as the output.

{@include: ../_include/log-shipping/filebeat-input-extension.md}


```yaml
# ...
filebeat.inputs:

- type: filestream
  paths:
    - <<FILEPATH-TO-OPENVAS-REPORTS>>/*.csv
  fields:
    logzio_codec: plain
    token: <<LOG-SHIPPING-TOKEN>>
    type: openvas
  fields_under_root: true
  encoding: utf-8
  ignore_older: 3h
  multiline:
    pattern: '^(?:[0-9]{1,3}\.){3}[0-9]{1,3}'
    negate: true
    match: after

#...
output:
  logstash:
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
    - <<FILEPATH-TO-OPENVAS-REPORTS>>/*.csv
  fields:
    logzio_codec: plain
    token: <<LOG-SHIPPING-TOKEN>>
    type: openvas
  fields_under_root: true
  encoding: utf-8
  ignore_older: 3h
  multiline:
    pattern: '^(?:[0-9]{1,3}\.){3}[0-9]{1,3}'
    negate: true
    match: after

#For version 6.x and lower
#filebeat.registry_file: /var/lib/filebeat/registry

#For version 7 and higher
filebeat.registry.path: /var/lib/filebeat

#The following processors are to ensure compatibility with version 7
processors:
- rename:
    fields:
     - from: "agent"
       to: "beat_agent"
    ignore_missing: true
- rename:
    fields:
     - from: "log.file.path"
       to: "source"
    ignore_missing: true

#...
output:
  logstash:
    hosts: ["<<LISTENER-HOST>>:5015"]
    ssl:
      certificate_authorities: ['/etc/pki/tls/certs/COMODORSADomainValidationSecureServerCA.crt']
```



{@include: ../_include//general-shipping/replace-placeholders.html}

* Replace the filepath placeholder `<<FILEPATH-TO-OPENVAS-REPORTS>>` with the file path to the folder where you’ll be keeping your OpenVAS reports. For example, `/home/kali/Downloads/Filebeat_read/*.csv` will look for any file with a csv extension under that path.



:::note
One last validation - make sure Logz.io is the only output and appears only once.
If the file has other outputs, remove them.
:::
 


##### Start Filebeat

[Start or restart Filebeat](https://www.elastic.co/guide/en/beats/filebeat/master/filebeat-starting.html) for the changes to take effect.
  
Filebeat is now configured to send OpenVAS CSV reports directly to Logz.io.

##### Generate a CSV report in OpenVAS

OpenVAS reports are typically generated manually, as needed.

After completing a scan in OpenVAS, perform the following steps to generate a CSV report.

1. Click the **Scans tab**, then select **Reports**.
2. Select a report from the list of results.
3. The report summary will open. Select **CSV Results** from the drop-down menu (top left corner) and click the download option (It's the green arrow ⬇️.

    ![OpenVAS image](https://dytvr9ot2sszz.cloudfront.net/logz-docs/security-analytics/openvas.png)

4. The CSV file will be downloaded to the default Downloads path set for your Web browser.    If your Filebeat is configued to read reports from another folder, you can manually copy OpenVAS reports to another folder or change the browser's default Downloads path.

##### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [Filebeat troubleshooting](https://docs.logz.io/shipping/log-sources/filebeat.html#troubleshooting).

  
