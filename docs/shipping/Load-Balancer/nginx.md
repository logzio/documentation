---
id: Nginx
title: Nginx
overview: Nginx is a web server that can also be used as a reverse proxy, load balancer, mail proxy and HTTP cache. Deploy this integration to ship Nginx logs to your Logz.io SIEM account and metrics, including Plus API, Plus, Stream STS, VTS.
product: ['logs','metrics']
os: ['windows', 'linux']
filters: ['Load Balancer']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/nginx.svg
logs_dashboards: []
logs_alerts: ['5tov4MgrnR6vXZhh1MyuHO','63MnOu9ZzkCXdX0KOhXghi','4V8BXcfr7noTdtU6EjXp7w','2EXnb71ucdTnVolN1PqbM6']
logs2metrics: []
metrics_dashboards: ['3HKho6pQhCmEYmwMc4xCeY']
metrics_alerts: ['1Bz57jmzsN7uIiyZLdnNpx']
drop_filter: []
---

## Logs

### Filebeat configuration

**Before you begin, you'll need**:

* [Filebeat](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-installation.html)
* Root access
* Port 5015 open

 

{@include: ../../_include/log-shipping/certificate.md}

#### Add nginx as an input

In the Filebeat configuration file (/etc/filebeat/filebeat.yml), add nginx to the filebeat.inputs section.

{@include: ../../_include/log-shipping/log-shipping-token.html}

{@include: ../../_include/log-shipping/filebeat-input-extension.md}


```yaml
# ...
filebeat.inputs:
- type: filestream
  paths:
  - /var/log/nginx/access.log

  fields:
    logzio_codec: plain

    # Your Logz.io account token. You can find your token at
    #  https://app.logz.io/#/dashboard/settings/manage-accounts
    token: <<LOG-SHIPPING-TOKEN>>
    type: nginx_access
  fields_under_root: true
  encoding: utf-8
  ignore_older: 3h

- type: filestream
  paths:
  - /var/log/nginx/error.log

  fields:
    logzio_codec: plain

    # Your Logz.io account token. You can find your token at
    #  https://app.logz.io/#/dashboard/settings/manage-accounts
    token: <<LOG-SHIPPING-TOKEN>>
    type: nginx_error
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
  - /var/log/nginx/access.log

  fields:
    logzio_codec: plain

    # Your Logz.io account token. You can find your token at
    #  https://app.logz.io/#/dashboard/settings/manage-accounts
    token: <<LOG-SHIPPING-TOKEN>>
    type: nginx_access
  fields_under_root: true
  encoding: utf-8
  ignore_older: 3h

- type: log
  paths:
  - /var/log/nginx/error.log

  fields:
    logzio_codec: plain

    # Your Logz.io account token. You can find your token at
    #  https://app.logz.io/#/dashboard/settings/manage-accounts
    token: <<LOG-SHIPPING-TOKEN>>
    type: nginx_error
  fields_under_root: true
  encoding: utf-8
  ignore_older: 3h
```

The above assumes the following defaults for Access logs:

* Log location - `/var/log/nginx/access.log`
* Log type - `nginx`, `nginx_access`, or `nginx-access`

Defaults for Error logs:

* Log location - `/var/log/nginx/error.log`
* Log type - `nginx-error`

#### Set Logz.io as the output

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

#### Start Filebeat

[Start or restart Filebeat](https://www.elastic.co/guide/en/beats/filebeat/master/filebeat-starting.html) for the changes to take effect.

#### Check Logz.io for your logs

Confirm you're shipping logs by opening an nginx-hosted webpage in your browser. Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

You can search for `type:nginx OR nginx_access OR nginx-access OR nginx-error` to filter for your logs. Your logs should be already parsed thanks to the Logz.io preconfigured parsing pipeline.



If you still don't see your logs, see [Filebeat troubleshooting](https://docs.logz.io/shipping/log-sources/filebeat.html#troubleshooting).

## Metrics

To send your Prometheus-format Nginx metrics to Logz.io, you need to add the **inputs.nginx** and **outputs.http** plug-ins to your Telegraf configuration file.

<!-- logzio-inject:install:grafana:dashboards ids=["3HKho6pQhCmEYmwMc4xCeY"] -->

### Configure Telegraf to send your metrics data to Logz.io

 

#### Configure Nginx server

1. Enable `stub_status` module in the NGINX configuration file - nginx.conf:

   ```
   server {
   
           listen       80;
   
           server_name  localhost;

     
           location / {
   
           stub_status;
   
           allow `<<YOUR-LOCALHOST-ADDRESS>>`;
   
           deny all;
   
           }

   }
   ```

2. Replace `<<YOUR-LOCALHOST-ADDRESS>>` with your localhost address.
3. Restart Nginx. 

#### Set up Telegraf v1.17 or higher

{@include: ../../_include/metric-shipping/telegraf-setup.md}
 
#### Add the inputs.nginx plug-in

First you need to configure the input plug-in to enable Telegraf to scrape the Nginx data from your hosts. To do this, add the following code to the configuration file:


``` ini
[[inputs.nginx]]
  ## An array of Nginx stub_status URI to gather stats.
  urls = ["http://localhost/server_status"]

  ## Optional TLS Config
  # tls_ca = "/etc/telegraf/ca.pem"
  # tls_cert = "/etc/telegraf/cert.pem"
  # tls_key = "/etc/telegraf/key.pem"
  ## Use TLS but skip chain & host verification
  # insecure_skip_verify = false

  ## HTTP response timeout (default: 5s)
  response_timeout = "5s"
  
[[inputs.disk]]
[[inputs.net]]
[[inputs.mem]]
[[inputs.system]]
[[inputs.cpu]]
   ## Whether to report per-cpu stats or not
   percpu = false
   ## Whether to report total system cpu stats or not
   totalcpu = true
   ## If true, collect raw CPU time metrics.
   collect_cpu_time = true
   ## If true, compute and report the sum of all non-idle CPU states.
   report_active = true
  
```



#### Add the outputs.http plug-in

{@include: ../../_include/metric-shipping/telegraf-outputs.md}
{@include: ../../_include/general-shipping/replace-placeholders-prometheus.html}

#### Check Logz.io for your metrics
  
{@include: ../../_include/metric-shipping/custom-dashboard.html} Install the pre-built dashboards to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["3HKho6pQhCmEYmwMc4xCeY"] -->

{@include: ../../_include/metric-shipping/generic-dashboard.html} 

 

