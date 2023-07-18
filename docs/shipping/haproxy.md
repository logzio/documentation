---
id: HAProxy
title: HAProxy
sidebar_position: 1
overview: HAProxy is a network device, so it needs to transfer logs using the syslog protocol.
product: ['metrics']
os: ['windows', 'linux']
filters: ['gcp', 'cloud']
logo: https://docs.logz.io/images/logo/logz-symbol.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
---



HAProxy is a network device, so it needs to transfer logs using the syslog protocol.
To ship HAProxy logs to an ELK stack, you'll first need to configure HAProxy logging to transmit the logs to a local rsyslog server.
From there, you can ship the logs from rsyslog to Logz.io.

#### Guided configuration

**Before you begin, you'll need**:
root access,
rsyslog 5.8.0 or later

 

##### Configure HAProxy

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

##### Configure rsyslog

Copy this text to your rsyslog configuration (`/etc/rsyslog.conf` by default).

{@include: ../_include/log-shipping/log-shipping-token.html}

{@include: ../_include/log-shipping/listener-var.html} 

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

##### Restart rsyslog

```shell
sudo service rsyslog restart
```

##### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you don't see your logs, see [log shipping troubleshooting]({{site.baseurl}}/user-guide/log-shipping/log-shipping-troubleshooting.html).

 
