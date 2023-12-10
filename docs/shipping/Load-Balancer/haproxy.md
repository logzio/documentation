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

If you don't see your logs, see [log shipping troubleshooting](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/log-shipping-troubleshooting/).

 ## Metrics

 To send your Prometheus-format HAProxy metrics to Logz.io, you need to add the **inputs.haproxy** and **outputs.http** plug-ins to your Telegraf configuration file.

### Configure Telegraf to send your metrics data to Logz.io

 

#### Set up Telegraf v1.17 or higher

{@include: ../../_include/metric-shipping/telegraf-setup.md}
 
#### Add the inputs.haproxy plug-in

First you need to configure the input plug-in to enable Telegraf to scrape the HAProxy data from your hosts. To do this, add the following code to the configuration file:


``` ini
[[inputs.haproxy]]
  ## An array of address to gather stats about. Specify an ip on hostname
  ## with optional port. ie localhost, 10.10.3.33:1936, etc.
  ## Make sure you specify the complete path to the stats endpoint
  ## including the protocol, ie http://10.10.3.33:1936/haproxy?stats

  ## Credentials for basic HTTP authentication
  # username = "admin"
  # password = "admin"

  ## If no servers are specified, then default to 127.0.0.1:1936/haproxy?stats
  servers = ["http://myhaproxy.com:1936/haproxy?stats"]

  ## You can also use local socket with standard wildcard globbing.
  ## Server address not starting with 'http' will be treated as a possible
  ## socket, so both examples below are valid.
  # servers = ["socket:/run/haproxy/admin.sock", "/run/haproxy/*.sock"]

  ## By default, some of the fields are renamed from what haproxy calls them.
  ## Setting this option to true results in the plugin keeping the original
  ## field names.
  # keep_field_names = false

  ## Optional TLS Config
  # tls_ca = "/etc/telegraf/ca.pem"
  # tls_cert = "/etc/telegraf/cert.pem"
  # tls_key = "/etc/telegraf/key.pem"
  ## Use TLS but skip chain & host verification
  # insecure_skip_verify = false
```

:::note
The database name is only required for instantiating a connection with the server and does not restrict the databases that we collect metrics from. The full list of data scraping and configuring options can be found [here](https://github.com/influxdata/telegraf/blob/release-1.18/plugins/inputs/haproxy/README.md).
:::
 

#### Add the outputs.http plug-in

{@include: ../../_include/metric-shipping/telegraf-outputs.md}
{@include: ../../_include/general-shipping/replace-placeholders-prometheus.html}

### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).


 

