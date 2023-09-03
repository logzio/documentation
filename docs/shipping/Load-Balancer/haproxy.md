---
id: HAProxy-load
title: HAProxy
overview: HAProxy is a network device, so it needs to transfer logs using the syslog protocol.
product: ['logs', 'metrics']
os: ['windows', 'linux']
filters: ['Load Balancer']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/haproxy-logo.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---


## Logs

HAProxy is a network device, so it needs to transfer logs using the syslog protocol.
To ship HAProxy logs to an ELK stack, you'll first need to configure HAProxy logging to transmit the logs to a local rsyslog server.
From there, you can ship the logs from rsyslog to Logz.io.



**Before you begin, you'll need**:
root access,
rsyslog 5.8.0 or later

 

### Configure HAProxy

Copy this text to your HAProxy configuration (`/etc/haproxy/haproxy.cfg` by default).

```conf
global
  log 127.0.0.1:514 len 4096 local1 # Send logs to localhost port 514 over UDP, facility set to ‘local1’

defaults HTTP # HTTP Defaults
  log global # refer to the global log definition
  option dontlog-normal # disable logging of normal, successful connections
  mode http
  option httplog # Enable logging of HTTP request, session state and timers

listen INPUT_NAME_HTTP
  bind :PORT

  server SERVER_NAME SERVER_ADDRESS:PORT

defaults TCP # TCP Defaults
  log global # refer to the global log definition
  option dontlog-normal # disable logging of normal, successful connections
  mode tcp
  option tcplog # Enable advanced logging of TCP connections, session state and timers

listen INPUT_NAME_TCP
  bind :PORT

  server SERVER_NAME SERVER_ADDRESS:PORT
```

### Configure rsyslog

Copy this text to your rsyslog configuration (`/etc/rsyslog.conf` by default).

{@include: ../../_include/log-shipping/log-shipping-token.html}

{@include: ../../_include/log-shipping/listener-var.html} 

```conf
$ModLoad imuxsock # provides support for local system logging
$ModLoad imklog # provides kernel logging support
$ModLoad imudp
$UDPServerAddress 0.0.0.0 # listen on the localhost , protocol UDP
$UDPServerRun 514 # listen on port 514, protocol UDP
$KLogPermitNonKernelFacility on
$ActionFileDefaultTemplate RSYSLOG_TraditionalFileFormat
$RepeatedMsgReduction on
$FileOwner syslog
$FileGroup adm
$FileCreateMode 0640
$DirCreateMode 0755
$Umask 0022
$PrivDropToUser syslog
$PrivDropToGroup syslog
$WorkDirectory /var/spool/rsyslog

# the logz.io syslog template,
$template HAProxyLogzioFormat,"[<<LOG-SHIPPING-TOKEN>>] <%pri%>%protocol-version% %timestamp:::date-rfc3339% %HOSTNAME% %app-name% %procid% %msgid% [type=haproxy] %msg%\n"

# Send messages to Logz over TCP using the template.
*.* @@<<LISTENER-HOST>>:5000;HAProxyLogzioFormat
```

### Restart rsyslog

```shell
sudo service rsyslog restart
```

### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you don't see your logs, see [log shipping troubleshooting]({{site.baseurl}}/user-guide/log-shipping/log-shipping-troubleshooting.html).

 ## Metrics

 To send your Prometheus-format HAProxy metrics to Logz.io, you need configure the OpenTelemetry collector to send your collected Prometheus-format HAproxy metrics to Logz.io.

#### Configuring OpenTelemetry to send your metrics data to Logz.io

##### Download OpenTelemetry collector
  
:::note
If you already have OpenTelemetry, proceed to the next step.
:::

Create a dedicated directory on your host and download the [OpenTelemetry collector](https://github.com/open-telemetry/opentelemetry-collector/releases/tag/v0.60.0) that is relevant to the operating system of your host.

After downloading the collector, create a configuration file `config.yaml`.

##### Configure the receivers
  
Open the configuration file and make sure that it states the receivers required for your source.

```yaml
receivers:
  prometheus:
    config:
      scrape_configs:
        - job_name: 'haproxy'
          static_configs:
            - targets: ['localhost:1936']
              labels:
                instance: 'haproxy_instance'
          metrics_path: '/haproxy?stats;csv'
          basic_auth:
            username: 'your_username'
            password: 'your_password'
```

Adjust the `targets`, `username`, and `password` as per your HAProxy setup.

##### Configure the exporters

In the same configuration file, add the following to the `exporters` section:
  
```yaml  
exporters:
  prometheusremotewrite:
    endpoint: https://<<LISTENER-HOST>>:8053
    headers:
      Authorization: Bearer <<PROMETHEUS-METRICS-SHIPPING-TOKEN>>
```
  
{@include: ../../_include/general-shipping/replace-placeholders-prometheus.html}

##### Configure the service pipeline
  
In the `service` section of the configuration file, add the following configuration
  
```yaml
service:
  pipelines:
    metrics:
      receivers: [<<YOUR-RECEIVER>>]
      exporters: [prometheusremotewrite]
```
* Replace `<<YOUR_RECEIVER>>` with the name of your receiver.



##### Start the collector

Run the following command:

```shell
<path/to>/otelcol-contrib --config ./config.yaml
```

* Replace `<path/to>` with the path to the directory where you downloaded the collector. If the name of your configuration file is different to `config`, adjust name in the command accordingly.

##### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).


 

