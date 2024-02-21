---
id: Apache-HTTP-Server
title: Apache HTTP Server
overview: The Apache HTTP Server, colloquially called Apache, is a free and open-source cross-platform web server. This integration sends Apache HTTP server logs and metrics to Logz.io.
product: ['metrics']
os: ['windows', 'linux']
filters: ['Compute']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/apache-http-logo.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---


## Logs

 
The Apache HTTP Server, colloquially called Apache, is a free and open-source cross-platform web server. This integration allows you to send logs from your Apache server instances to your Logz.io account.

**Before you begin, you'll need**:

* [Filebeat](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-installation.html) installed
* Port 5015 open.
* Root access

 

{@include: ../../_include/log-shipping/certificate.md}

### Add Apache as an input

In the Filebeat configuration file (/etc/filebeat/filebeat.yml), add Apache to the filebeat.inputs section.


The default log locations for:

* Ubuntu and Debian - `/var/log/apache2/access.log`
* RHEL, CentOS, Fedora - `/var/log/httpd/access_log`


{@include: ../../_include/log-shipping/log-shipping-token.html}

{@include: ../../_include/log-shipping/filebeat-input-extension.md}


```yaml
# ...
filebeat.inputs:
- type: filestream

  paths:
  # Ubuntu, Debian: `/var/log/apache2/access.log`
  #  RHEL, CentOS, Fedora: `/var/log/httpd/access_log`
  - /var/log/apache2/access.log

  fields:
    logzio_codec: plain

    # You can manage your tokens at
    #  https://app.logz.io/#/dashboard/settings/manage-tokens/log-shipping
    token: <<LOG-SHIPPING-TOKEN>>
    type: apache_access
  fields_under_root: true
  encoding: utf-8
  ignore_older: 3h

- type: filestream

  paths:
  # Ubuntu, Debian: `/var/log/apache2/error.log`
  #  RHEL, CentOS, Fedora: `/var/log/httpd/error_log`
  - /var/log/apache2/error.log

  fields:
    logzio_codec: plain

    # You can manage your tokens at
    #  https://app.logz.io/#/dashboard/settings/manage-tokens/log-shipping
    token: <<LOG-SHIPPING-TOKEN>>
    type: apache_error
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
  # Ubuntu, Debian: `/var/log/apache2/access.log`
  #  RHEL, CentOS, Fedora: `/var/log/httpd/access_log`
  - /var/log/apache2/access.log

  fields:
    logzio_codec: plain

    # You can manage your tokens at
    #  https://app.logz.io/#/dashboard/settings/manage-tokens/log-shipping
    token: <<LOG-SHIPPING-TOKEN>>
    type: apache_access
  fields_under_root: true
  encoding: utf-8
  ignore_older: 3h

- type: log

  paths:
  # Ubuntu, Debian: `/var/log/apache2/error.log`
  #  RHEL, CentOS, Fedora: `/var/log/httpd/error_log`
  - /var/log/apache2/error.log

  fields:
    logzio_codec: plain

    # You can manage your tokens at
    #  https://app.logz.io/#/dashboard/settings/manage-tokens/log-shipping
    token: <<LOG-SHIPPING-TOKEN>>
    type: apache_error
  fields_under_root: true
  encoding: utf-8
  ignore_older: 3h
```



### Set Logz.io as the output

If Logz.io is not an output, add it now.
Remove all other outputs.

{@include: ../../_include/log-shipping/listener-url.html} 

```yaml
# ...
output.logstash:
  hosts: ["<<LISTENER-HOST>>:5015"]
  ssl:
    certificate_authorities: ['/etc/pki/tls/certs/COMODORSADomainValidationSecureServerCA.crt']
```

### Start Filebeat

[Start or restart Filebeat](https://www.elastic.co/guide/en/beats/filebeat/master/filebeat-starting.html) for the changes to take effect.

### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd). You can search for `type:apache OR apache_access OR apache-access` to filter for your Apache logs. Your logs should be already parsed thanks to the Logz.io preconfigured parsing pipeline.

If you still don't see your logs, see [Filebeat troubleshooting](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/troubleshooting-filebeat/).

  


## Metrics

The Apache HTTP Server, colloquially called Apache, is a free and open-source cross-platform web server. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.

To send your Prometheus-format Apache HTTP Server metrics to Logz.io, you need to add the **inputs.apache** and **outputs.http** plug-ins to your Telegraf configuration file.

### Configure Telegraf to send your metrics data to Logz.io

 

#### Set up Telegraf v1.17 or higher

{@include: ../../_include/metric-shipping/telegraf-setup.md}

#### Add the inputs.apache plug-in

First you need to configure the input plug-in to enable Telegraf to scrape the Apache HTTP Server data from your hosts. To do this, add the following code to the configuration file:

``` ini
[[inputs.apache]]
  ## An array of URLs to gather from, must be directed at the machine
  ## readable version of the mod_status page including the auto query string.
  ## Default is "http://localhost/server-status?auto".
  urls = ["http://localhost/server-status?auto"]

  ## Credentials for basic HTTP authentication.
  # username = "myuser"
  # password = "mypassword"

  ## Maximum time to receive response.
  # response_timeout = "5s"

  ## Optional TLS Config
  # tls_ca = "/etc/telegraf/ca.pem"
  # tls_cert = "/etc/telegraf/cert.pem"
  # tls_key = "/etc/telegraf/key.pem"
  ## Use TLS but skip chain & host verification
  # insecure_skip_verify = false
```

:::note
The full list of data scraping and configuring options can be found [here](https://github.com/influxdata/telegraf/blob/release-1.18/plugins/inputs/apache/README.md)
:::
 
  

#### Enable the ExtendedStatus option on your server
  
The `ExtendedStatus` option must be enabled on your server in order to collect all available fields. To do this, add the following code to your `httpd.conf` configuration file:
  
```html
<Location "/server-status">
    SetHandler server-status
    Require host example.com
</Location>
```


#### Add the outputs.http plug-in
  
{@include: ../../_include/metric-shipping/telegraf-outputs.md}
{@include: ../../_include/general-shipping/replace-placeholders-prometheus.html}
  
#### Start Telegraf

{@include: ../../_include/metric-shipping/telegraf-run.md}

#### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).

