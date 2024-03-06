---
id: Rsyslog-data
title: Rsyslog
overview: Rsyslog is an open-source software utility used on most UNIX and Unix-like computer systems. It offers a great lightweight service to consolidate logs. With Logz.io, you can monitor these logs, identify if and when issues arise, and solve them before they impact your customers. 
product: ['logs']
os: ['windows', 'linux']
filters: ['Other', 'Most Popular']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/linux.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---
 
## Rsyslog over TLS

Most Unix systems these days come with pre-installed rsyslog, which is a great lightweight service to consolidate logs.

You can configure rsyslog to monitor a single log file or directory and ship them over to Logz.io over TLS. For directories, all the first level files are monitored.

#### Configuration

**Before you begin, you'll need**:

* Sudo access
* Rsyslog version 5.8.0 and above
* Outgoing TCP traffic to destination port 5001 allowed
* A common linux distribution

 

##### Install the rsyslog-gnutls add-on

On your Debian or Ubuntu Linux machine, run:

```
sudo apt-get install rsyslog-gnutls
```

For distributions based on Red Hat, use `rpm` or `yum` in place of `apt-get`.

{@include: ../../_include/log-shipping/certificate.md}

##### Configure rsyslog file spooling

To ship a log to Logz.io, SSH to your Linux server, and run the command below. The code verifies the working directory exists. For an Ubuntu server, it will set the proper permissions.

```
sudo mkdir -v /var/spool/rsyslog 
if [ "$(lsb_release -ds | grep Ubuntu)" != "" ]; then
    sudo chown -R syslog:adm /var/spool/rsyslog
fi
```

##### Create a new configuration file for Logz.io

```
sudo vim /etc/rsyslog.d/21-logzio-sample.conf
```

Add the additional configuration:

```shell
#   -------------------------------------------------------
#        File Logging Directives for Logz.io
#   -------------------------------------------------------

$ModLoad imfile
$InputFilePollInterval 10
$PrivDropToGroup adm
$WorkDirectory /var/spool/rsyslog

# File access file:
$InputFileName <<PATH_TO_FILE>>
$InputFileTag TYPE:
$InputFileStateFile stat-TYPE
$InputFileSeverity info
$InputFilePersistStateInterval 20000
$InputRunFileMonitor

$DefaultNetstreamDriverCAFile /etc/pki/tls/certs/COMODORSADomainValidationSecureServerCA.crt
$ActionSendStreamDriver gtls
$ActionSendStreamDriverMode 1
$ActionSendStreamDriverAuthMode x509/name
$ActionSendStreamDriverPermittedPeer *.logz.io

$template logzFormatFileTagName,"[<<LOG-SHIPPING-TOKEN>>] <%pri%>%protocol-version% %timestamp:::date-rfc3339% %HOSTNAME% %app-name% %procid% %msgid% [type=<<TYPE>>] %msg%\n"
if $programname == 'TYPE' then @@<<LISTENER-HOST>>:5001;logzFormatFileTagName
if $programname == 'TYPE' then ~
```

{@include: ../../_include/general-shipping/replace-placeholders-rsyslog.html}
* `<<PATH_TO_FILE>>`: Path to your file or directory.
* `<<TYPE>>`: {@include: ../../_include/log-shipping/type.md}


##### Restart rsyslog

```
sudo service rsyslog restart
```

##### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then [open Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see our [Rsyslog troubleshooting guide](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/troubleshooting-rsyslog-selinux/).

  


## Rsyslog with SELinux



Security-Enhanced Linux (SELinux) is a security architecture for Linux based systems that allows administrators to have more control over who can access the system.

In systems where SELinux is enabled, rsyslog is one of the system processes that SELinux protects. One of the ways SELinux protects the service is by allowing it to only send logs using the standard port, which is 514 UDP. To be able to ship logs to Logz.io, you’ll need to modify the current SELinux policy to allow shipping logs using the non-standard port 5000 TCP.


#### Modify the SELinux policy to allow shipping logs to Logz.io

**Before you begin, you'll need**:

* Sudo access
* Rsyslog version 5.8.0 and above
* Outgoing TCP traffic to destination port 5000 allowed
* A common linux distribution

:::note
The commands presented here are for Red Hat/Fedora-based distributions. Depending on which distribution you’re using, you may need to modify the commands slightly.
:::
 


 

##### Ensure that logs are not being sent to Logz.io from your system



Execute the command below to check if your system sends logs to Logz.io. 

The following defaults are assumed: 
  
* Log location - `/var/log/`
* Log type - `syslog`


```shell
curl -sLO https://github.com/logzio/logzio-shipper/raw/master/dist/logzio-rsyslog.tar.gz \
  && tar xzf logzio-rsyslog.tar.gz \
  && sudo rsyslog/install.sh -t linux -a "<<LOG-SHIPPING-TOKEN>>" -l "<<LISTENER-HOST>>"
```

{@include: ../../_include/log-shipping/log-shipping-token.html}

{@include: ../../_include/log-shipping/listener-var.html} 

If you do not see logs on [your Open Search Dashboards](https://app.logz.io/#/dashboard/osd), proceed to the next step.

##### Check the audit logs for incoming logs

Navigate to the directory or to your audit logs (by default, this is `/var/log/audit/audit.log`) and check for AVC records containing `dest=5000`. If you see them, this means that SELinux is blocking the logs export over port TCP 5000.


##### Ensure that logs are sent to Logz.io when SELinux is disabled

Temporarily disable SELinux by running this command:

```shell
$ sudo setenforce 0
```

Wait a few minutes and check [your Open Search Dashboards](https://app.logz.io/#/dashboard/osd). If you see the logs, it means that the problem is caused by SELinux and using port 5000 TCP to send logs.


##### Enable SELinux 

At this point, switch SELinux back on to ensure that the system remains protected.

To do this, run:

```shell
$ sudo setenforce 1
```

##### Install the SELinux policy core utilities package

To enable modifications to the SELinux policy, add the package `policycoreutils`, which includes the SELinux command `semanage`.

If you already have this package installed, proceed to the next step. Otherwise, run:

```shell
$ sudo dnf install policycoreutils
```

##### Add port 5000 TCP to the SELinux policy

Execute the following command to add port 5000 TCP to the SELinux policy:

```shell
$ sudo semanage port -m -t syslogd_port_t -p tcp 5000
```

##### Check your dashboard for logs

Give your logs some time to get from your system to ours, and then [open Open Search Dashboards](https://app.logz.io/#/dashboard/osd)

If you still don't see your logs, see our [Rsyslog troubleshooting guide](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/troubleshooting-rsyslog-selinux/).

 
## Automatic configuration

###### Shipping with Rsyslog

Most Unix systems these days come with pre-installed rsyslog, which is a great lightweight service to consolidate logs.

You can configure rsyslog to monitor a single log file or directory, and ship them over to Logz.io.
For directories, all the first level files are monitored.

#### Automatic configuration

**Before you begin, you'll need**:

* Sudo access
* Rsyslog version 5.8.0 and above
* Outgoing TCP traffic to destination port 5000 allowed
* A common linux distribution


 

##### Configure your rsyslog daemon

###### If your are monitoring plain-text logs

Run the following to configure your rsyslog daemon to monitor a log file or directory.

```
curl -sLO https://github.com/logzio/logzio-shipper/raw/master/dist/logzio-rsyslog.tar.gz && tar xzf logzio-rsyslog.tar.gz && sudo rsyslog/install.sh -t file -a "<<LOG-SHIPPING-TOKEN>>" -l "<<LISTENER-HOST>>" --filepath "<<PATH_TO_FILE>>" -tag "<<TYPE>>" 
```


###### If you are monitoring JSON logs

Run the following command to configure your rsyslog daemon to monitor JSON log files.  Each log should be formatted as a single JSON line that ends with a newline character.


```
curl -sLO https://github.com/logzio/logzio-shipper/raw/master/dist/logzio-rsyslog.tar.gz && tar xzf logzio-rsyslog.tar.gz && sudo rsyslog/install.sh -t file -a "<<LOG-SHIPPING-TOKEN>>" -l "<<LISTENER-HOST>>" --filepath "<<PATH_TO_FILE>>" -tag "<<TYPE>>" -c json
```

{@include: ../../_include/general-shipping/replace-placeholders.html}
* `<<PATH_TO_FILE>>`: Path to your file or directory.
* `<<TYPE>>`: {@include: ../../_include/log-shipping/type.md}


## Manual configuration

###### Shipping with Rsyslog

Most Unix systems these days come with pre-installed rsyslog, which is a great lightweight service to consolidate logs.

You can configure rsyslog to monitor a single log file or directory, and ship them over to Logz.io.
For directories, all the first level files are monitored.

#### Manual configuration

**Before you begin, you'll need**:

* Sudo access
* Rsyslog version 5.8.0 and above
* Outgoing TCP traffic to destination port 5000 allowed
* A common linux distribution


 

##### Configure rsyslog file spooling

To ship a log to Logz.io, SSH to your Linux server, copy the code snippet below to your terminal window and execute it. The code verifies that the working directory exists. For an Ubuntu server, it sets the proper permissions.

```
sudo mkdir -v /var/spool/rsyslog
if [ "$(lsb_release -ds | grep Ubuntu)" != "" ]; then
    sudo chown -R syslog:adm /var/spool/rsyslog
fi
```

##### Create a new configuration file for Logz.io

```
sudo vim /etc/rsyslog.d/21-logzio-sample.conf
```

Add the additional configuration

```shell
#   -------------------------------------------------------
#        File Logging Directives for Logz.io
#   -------------------------------------------------------

$ModLoad imfile
$InputFilePollInterval 10
$PrivDropToGroup adm
$WorkDirectory /var/spool/rsyslog

# File access file:
$InputFileName <<PATH_TO_FILE>>
$InputFileTag TYPE:
$InputFileStateFile stat-TYPE
$InputFileSeverity info
$InputFilePersistStateInterval 20000
$InputRunFileMonitor

$template logzFormatFileTagName,"[<<LOG-SHIPPING-TOKEN>>] <%pri%>%protocol-version% %timestamp:::date-rfc3339% %HOSTNAME% %app-name% %procid% %msgid% [type=TYPE] %msg%\n"
if $programname == 'TYPE' then @@<<LISTENER-HOST>>:5000;logzFormatFileTagName
if $programname == 'TYPE' then ~
```


{@include: ../../_include/general-shipping/replace-placeholders.html}
* `<<PATH_TO_FILE>>`: Path to your file or directory.
* `<<TYPE>>`: {@include: ../../_include/log-shipping/type.md}


##### Restart rsyslog

After editing and saving the file, execute the following command:

```
sudo service rsyslog restart
```


##### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then [open Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see our [Rsyslog troubleshooting guide](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/troubleshooting-rsyslog-selinux/).

 
  