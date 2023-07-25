---
id: MySQL
title: MySQL
overview: MySQL is an open-source relational database management system. Filebeat is often the easiest way to get logs from your system to Logz.io. Logz.io has a dedicated configuration wizard to make it simple to configure Filebeat. If you already have Filebeat and you want to add new sources, check out our other shipping instructions to copy&paste just the relevant changes from our code examples.
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

 
 
## MySQL + Filebeat setup

MySQL is an open-source relational database management system. Filebeat is often the easiest way to get logs from your system to Logz.io. Logz.io has a dedicated configuration wizard to make it simple to configure Filebeat. If you already have Filebeat and you want to add new sources, check out our other shipping instructions to copy&paste just the relevant changes from our code examples.

#### Configuration

**Before you begin, you'll need**:

* [Filebeat](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-installation.html) installed
* Port 5015 open

 

##### Configure MySQL to write general query logs

In the MySQL configuration file (/etc/mysql/my.cnf),
paste these lines:

```
general_log_file = /var/log/mysql/mysql.log
general_log= 1
log_slow_queries = /var/log/mysql/mysql-slow.log
long_query_time = 1
log-queries-not-using-indexes = 1
```

Restart MySQL:

```shell
sudo /etc/init.d/mysql restart
```


{@include: ../_include/log-shipping/certificate.md}

##### Add MySQL as an input in your Filebeat configuration

In the Filebeat configuration file (/etc/filebeat/filebeat.yml), add MySQL to the filebeat.inputs section.

{@include: ../_include/log-shipping/log-shipping-token.html}

{@include: ../_include/log-shipping/filebeat-input-extension.md}


```yaml
# ...
filebeat.inputs:
- type: filestream
  paths:
    - /var/log/mysql/mysql.log

  fields:
    logzio_codec: plain

    # You can manage your tokens at
    # https://app.logz.io/#/dashboard/settings/manage-tokens/log-shipping
    token: <<LOG-SHIPPING-TOKEN>>
    type: mysql
  fields_under_root: true
  encoding: utf-8
  ignore_older: 3h

- type: filestream
  paths:
    - /var/log/mysql/mysql-slow.log

  fields:
    logzio_codec: plain

    # You can manage your tokens at
    # https://app.logz.io/#/dashboard/settings/manage-tokens/log-shipping
    token: <<LOG-SHIPPING-TOKEN>>
    type: mysql_slow_query
  fields_under_root: true
  encoding: utf-8
  ignore_older: 3h
  multiline:
    pattern: '^# Time:'
    negate: true
    match: after

- type: filestream
  paths:
    - /var/log/mysql/error.log

  fields:
    logzio_codec: plain

    # You can manage your tokens at
    # https://app.logz.io/#/dashboard/settings/manage-tokens/log-shipping
    token: <<LOG-SHIPPING-TOKEN>>
    type: mysql_error
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
    - /var/log/mysql/mysql.log

  fields:
    logzio_codec: plain

    # You can manage your tokens at
    # https://app.logz.io/#/dashboard/settings/manage-tokens/log-shipping
    token: <<LOG-SHIPPING-TOKEN>>
    type: mysql
  fields_under_root: true
  encoding: utf-8
  ignore_older: 3h

- type: log
  paths:
    - /var/log/mysql/mysql-slow.log

  fields:
    logzio_codec: plain

    # You can manage your tokens at
    # https://app.logz.io/#/dashboard/settings/manage-tokens/log-shipping
    token: <<LOG-SHIPPING-TOKEN>>
    type: mysql_slow_query
  fields_under_root: true
  encoding: utf-8
  ignore_older: 3h
  multiline:
    pattern: '^# Time:'
    negate: true
    match: after

- type: log
  paths:
    - /var/log/mysql/error.log

  fields:
    logzio_codec: plain

    # You can manage your tokens at
    # https://app.logz.io/#/dashboard/settings/manage-tokens/log-shipping
    token: <<LOG-SHIPPING-TOKEN>>
    type: mysql_error
  fields_under_root: true
  encoding: utf-8
  ignore_older: 3h
```



###### Preconfigured log types

| Parameter | Log Type | Default log location |
|---|---|---|
| General query log | `mysql` | `/var/log/mysql/mysql.log` |
| Slow query log | `mysql_slow_query` | `/var/log/mysql/mysql-slow.log` |
| Error log | `mysql_error` | `/var/log/mysql/error.log` |

The log type is used to apply the appropriate Logz.io preconfigured parsing pipeline so that your logs will be automatically parsed.

##### Set Logz.io as the output

If Logz.io is not an output, add it now.
Remove all other outputs.

{@include: ../_include/log-shipping/listener-var.html} 

```yaml
# ...
output.logstash:
  hosts: ["<<LISTENER-HOST>>:5015"]
  ssl:
    certificate_authorities: ['/etc/pki/tls/certs/COMODORSADomainValidationSecureServerCA.crt']
```

##### Start Filebeat

[Start or restart Filebeat](https://www.elastic.co/guide/en/beats/filebeat/master/filebeat-starting.html) for the changes to take effect.

##### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [Filebeat troubleshooting](https://docs.logz.io/shipping/log-sources/filebeat.html#troubleshooting).

 
 

## Set up a Docker sidecar for MySQL

MySQL is an open-source relational database management system. Docker sidecar is a container that runs on the same Pod as the application container. This integration allows you to send your MySQL logs to your Logz.io account using a Docker sidecar. 


 

##### Pull the Docker image

Download the logzio/mysql-logs image:

```shell
docker pull logzio/mysql-logs
```

##### Run the Docker image

For a complete list of options, see the parameters below the code block.👇

<!--
```shell
docker run -d 
  --name logzio-mysql-logs 
  -e LOGZIO_TOKEN=<<LOG-SHIPPING-TOKEN>> [-e LOGZIO_LISTENER=<<LISTENER-HOST>>] \
  [-e MYSQL_ERROR_LOG_FILE=<<PATH-TO-ERROR-LOG-FILE>>] [-e MYSQL_SLOW_LOG_FILE=<<PATH-TO-SLOW-LOG-FILE>>] [-e MYSQL_LOG_FILE=<<PATH-TO-LOG-FILE>>] \
  -v path_to_directory:/var/log/logzio -v path_to_directory:/var/log/mysql \
  logzio/mysql-logs:latest
```
--
-->

```shell
docker run -d --name logzio-mysql-logs \
-e LOGZIO_TOKEN="<<LOG-SHIPPING-TOKEN>>" \
-e LOGZIO_LISTENER_HOST="<<LISTENER-HOST>>" \
-v /var/log/logzio:/var/log/logzio \
-v /var/log/mysql:/var/log/mysql \
logzio/mysql-logs:latest
```

###### Parameters

| Parameter | Description | Required/Default |
|---|---|---|
| LOGZIO_TOKEN |{@include: ../_include/log-shipping/log-shipping-token.md}  {@include: ../_include/log-shipping/log-shipping-token.html} | Required |
| LOGZIO_LISTENER | Listener URL.    {@include: ../_include/log-shipping/listener-var.html}  | `listener.logz.io` |
| MYSQL_ERROR_LOG_FILE | The path to MySQL error log. | Optional. `/var/log/mysql/error.log` |
| MYSQL_SLOW_LOG_FILE | The path to MySQL slow query log. | Optional. `/var/log/mysql/mysql-slow.log` |
| MYSQL_LOG_FILE | The path to MySQL general log. | Optional. `/var/log/mysql/mysql.log` |


Below is an example configuration for running the Docker container:

```bash
docker run -d \
  --name logzio-mysql-logs \
  -e LOGZIO_TOKEN="<<LOG-SHIPPING-TOKEN>>" \
  -v /path/to/directory/logzio:/var/log/logzio \
  -v /path/to/directory/mysql:/var/log/mysql \
  --restart=always \
  logzio/mysql-logs:latest
```


##### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [Filebeat troubleshooting](https://docs.logz.io/shipping/log-sources/filebeat.html#troubleshooting).

  