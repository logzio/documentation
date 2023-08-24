---
id: Fluentd-data
title: Fluentd
overview: Fluentd is a data collector, which unifies the data collection and consumption. This integration allows you to use Fluentd to send logs to your Logz.io account.
product: ['logs']
os: ['windows', 'linux']
filters: ['Other','Most Popular']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/fluentd.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---
 

Fluentd is a data collector, which unifies the data collection and consumption. This integration allows you to use Fluentd to send logs to your Logz.io account. 

:::note
Fluentd will fetch all existing logs, as it is not able to ignore older logs.
:::

## Configure Fluentd with Ruby Gems

**Before you begin, you'll need**:
Ruby and ruby-dev 2.1 or higher

	
### Install Fluentd and the Logz.io plugin

```shell
gem install fluentd fluent-plugin-logzio
```

### Set up Fluentd

```shell
fluentd --setup ./fluent
```

### Add an input plugin

Add a required input plugin to the configuration file. You can find the list of available input plugins [here](https://docs.fluentd.org/input).
	
An example input plugin looks as follows:
	
```xml
<source>
  @type tail
  path /var/log/httpd-access.log
  pos_file /var/log/td-agent/httpd-access.log.pos
  tag apache.access
  <parse>
    @type apache2
  </parse>
</source>
```


### Configure Fluentd with Logz.io output

Add this code block to your Fluent configuration file (`fluent.conf` by default).

See the configuration parameters below the code block.👇

```java
<match **>
  @type logzio_buffered
  endpoint_url https://<<LISTENER-HOST>>:8071?token=<<LOG-SHIPPING-TOKEN>>&type=my_type
  output_include_time true
  output_include_tags true
  http_idle_timeout 10
  <buffer>
      @type memory
      flush_thread_count 4
      flush_interval 3s
      chunk_limit_size 16m
      queue_limit_length 4096
  </buffer>
</match>
```

### Parameters

| Parameter | Description |
|---|---|
| endpoint_url | A url composed of your Logz.io region's listener URL, account token, and log type. {@include: ../../_include/log-shipping/listener-var.html} |
| output_include_time | To add a timestamp to your logs when they're processed, `true` (recommended). Otherwise, `false`. |
| output_include_tags | To add the `fluentd` tag to logs, `true`. Otherwise, `false`. If `true`, use in combination with `output_tags_fieldname`. |
| output_tags_fieldname | If `output_include_tags` is `true`, sets output tag's field name. The default is `fluentd_tag` |
| http_idle_timeout | Time, in seconds, that the HTTP connection will stay open without traffic before timing out. |
| retry_count | Counter of the times to resend failed bulks. The default is `4`. |
| retry_sleep | Interval in seconds to sleep initially between retries, exponential step-off. The default is `2s`. |
| bulk_limit | Limit to the size of the Logz.io upload bulk. Defaults to 1000000 bytes, leaving about 24kB for overhead. |
| bulk_limit_warning_limit | Limit to the size of the Logz.io warning message when a record exceeds bulk_limit to prevent a recursion when Fluent warnings are sent to the Logz.io output. The default is `nil` (no truncation). |
| proxy_uri | Your proxy uri. The default is `nil`. For example: "my.ip:12345". |
| proxy_cert | Your proxy cert. The default is `nil`. |
| gzip | Defines if the plugin needs to ship the logs in gzip compression. The default is `false`. |

### Run Fluentd

```shell
fluentd -c ./fluent/fluent.conf -vv
```

### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [log shipping troubleshooting]({{site.baseurl}}/user-guide/log-shipping/log-shipping-troubleshooting.html).

 
 
Fluentd can receive and concatenate multiline logs. To do this, you need to add a parser and concatenation plugin to your Fluentd configuration.

 

### Add multiline parser to your input plugin

:::note
Multiline parsing only works with `in_tail` plugins. Refer to the [Fluentd documentation](https://docs.fluentd.org/parser/multiline) for more on this.
:::
 

Add the following code block to your `in_tail` plugin:

```xml
<parse>
  @type multiline
  format_firstline /^<<YOUR-REGEX-PATTERN>>/
</parse>
```

* Replace `<<YOUR-REGEX-PATTERN>>` with the definition of your Regex pattern. You can use [regex101](https://regex101.com/) to define it.

The indentation of the parse plugin must be one level under the tail function as in the example below:

```xml
<source>
  @type tail
  path /var/log/httpd-access.log
  pos_file /var/log/td-agent/httpd-access.log.pos
  tag apache.access
	<parse>
	  @type multiline
	  format_firstline /\d{4}-\d{1,2}-\d{1,2}/
	  format1 /^(?<time>\d{4}-\d{1,2}-\d{1,2} \d{1,2}:\d{1,2}:\d{1,2}) \[(?<thread>.*)\] (?<level>[^\s]+)(?<message>.*)/
	</parse>
</source>
```


 
Fluentd is a data collector, which unifies the data collection and consumption. This integration allows you to use Fluentd to send logs from your Windows system to your Logz.io account. 

:::note
Fluentd will fetch all existing logs, as it is not able to ignore older logs.
:::
  

## Configure Fluentd with td-agent for Windows

**Before you begin, you'll need**:
Ruby and ruby-dev 2.1 or higher

	
### Install Fluentd td-agent

Navigate to the [downloads](https://docs.fluentd.org/installation/install-by-msi) page of td-agent and download the latest version of the installer. After that, run the installer and follow the wizard instructions.

### Install the Logz.io plugin

```shell
gem install fluentd fluent-plugin-logzio
```

### Set up td-agent.conf

Open C:/opt/td-agent/etc/td-agent/td-agent.conf and replace its content with the following configuration:

```xml
<source>
  @type windows_eventlog2
  @id windows_eventlog2
  channels application,system,security
  read_existing_events false
  tag winevt.raw
  rate_limit 200
  <storage>
    @type local
    persistent true
    path C:\opt\td-agent\winlog.json
  </storage>
</source>

<match **>
  @type logzio_buffered
  endpoint_url https://<<LISTENER-HOST>>:8071?token=<<LOG-SHIPPING-TOKEN>>&type=<<LOG-TYPE>>
  output_include_time true
  output_include_tags true
  http_idle_timeout 10
  <buffer>
      @type memory
      flush_thread_count 4
      flush_interval 3s
      chunk_limit_size 16m
      queue_limit_length 4096
  </buffer>
</match>
```

### Parameters

| Parameter | Description |
|---|---|
| endpoint_url | A url composed of your Logz.io region's listener URL, account token, and log type. {@include: ../../_include/log-shipping/listener-var.html} {@include: ../../_include/log-shipping/log-shipping-token.html} |
| type | Log type. If required, replace `<<LOG_TYPE>>` with the desired name for the log type, the default value is `fluentbit` |
| output_include_time | To add a timestamp to your logs when they're processed, `true` (recommended). Otherwise, `false`. |
| output_include_tags | To add the `fluentd` tag to logs, `true`. Otherwise, `false`. If `true`, use in combination with `output_tags_fieldname`. |
| output_tags_fieldname | If `output_include_tags` is `true`, sets output tag's field name. The default is `fluentd_tag` |
| http_idle_timeout | Time, in seconds, that the HTTP connection will stay open without traffic before timing out. |




### Run Fluentd td-agent

Open `Td-agent Command Prompt` from the Windows Start menu and run the following command:

```shell
C:\opt\td-agent> td-agent
```

### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [log shipping troubleshooting]({{site.baseurl}}/user-guide/log-shipping/log-shipping-troubleshooting.html).

Fluentd can receive and concatenate multiline logs. To do this, you need to add a parser and concatenation plugin to your Fluentd configuration.

 

### Add multiline parser to your input plugin

:::note
Multiline parsing only works with `in_tail` plugins. Refer to the [Fluentd documentation](https://docs.fluentd.org/parser/multiline) for more on this.
:::
 

Add the following code block to your `in_tail` plugin:

```xml
<parse>
  @type multiline
  format_firstline /^<<YOUR-REGEX-PATTERN>>/
</parse>
```

* Replace `<<YOUR-REGEX-PATTERN>>` with the definition of your Regex pattern. You can use [regex101](https://regex101.com/) to define it.

The indentation of the parse plugin must be one level under the tail function as in the example below:

```xml
<source>
  @type tail
  path /var/log/httpd-access.log
  pos_file /var/log/td-agent/httpd-access.log.pos
  tag apache.access
	<parse>
	  @type multiline
	  format_firstline /\d{4}-\d{1,2}-\d{1,2}/
	  format1 /^(?<time>\d{4}-\d{1,2}-\d{1,2} \d{1,2}:\d{1,2}:\d{1,2}) \[(?<thread>.*)\] (?<level>[^\s]+)(?<message>.*)/
	</parse>
</source>
```
 
## Docker logs with Fluentd

### Architecture overview

This integration includes:


* Pulling a Docker image of containerized Fluentd
* Configuring and running containerized Fluentd

![Integration architecture Fluentd on Docker](https://dytvr9ot2sszz.cloudfront.net/logz-docs/log-shipping/docker-fluentd-hla-v2.png)

Upon deployment, each container on your host system, including the Fluentd container, writes logs to a dedicated log file. Fluentd fetches the log data from this file and ships the data over HTTP or HTTPS to your Logz.io account, either via an optional proxy sever or directly.


**Before you begin, you'll need**:
Docker installed on your host system

 

### Pull the Docker image for containerized Fluentd

```shell
docker pull logzio/fluentd-docker-logs
```

### Start the container

Run the following command:

   ```java
   docker run -it --rm \
   --name fluentd-docker-logs \
   -v $(pwd)/log:/fluentd/log \
   -v /var/lib/docker/containers:/var/lib/docker/containers \
   -v /var/run/docker.sock:/var/run/docker.sock:ro \
   -p 5001:5001 \
   -e LOGZIO_LOG_LISTENER="https://<<LISTENER-HOST>>:8071" \
   -e LOGZIO_LOG_SHIPPING_TOKEN=<<LOG-SHIPPING-TOKEN>> \
   -e LOGZIO_TYPE=docker-fluentd \
   logzio/fluentd-docker-logs
   ```

{@include: ../../_include/log-shipping/listener-var.html}
{@include: ../../_include/log-shipping/log-shipping-token.html}

If you need to send the logs via a proxy server:

   * Add `-e LOGZIO_PROXY_URI=<<YOUR-PROXY-URI>>` to the above command and replace `<<YOUR-PROXY-URI>>` with your proxy URI.
   * Add `-e LOGZIO_PROXY_CERT=<<YOUR-PROXY-CERTIFICATE>>` to the above commad and replace `<<YOUR-PROXY-CERTIFICATE>>` with your proxy certificate value.

### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd). You can filter for data of type `docker-fluentd` to see the incoming container logs.
  
If you still don’t see your data, see [log shipping troubleshooting](https://docs.logz.io/user-guide/log-shipping/log-shipping-troubleshooting.html).
  
 

### Advanced settings

If you need to customize the default settings of the configuration parameters, add any of the following lines to the command:

| Parameter | Description | Default |
|---|---|---|
| `-e LOGZIO_INCLUDE_REGEX=<<LOGZIO_INCLUDE_REGEX>> \` | If a container name does not match the Regex, logs from this container will not be shipped. | `.+` |
| `-e LOGZIO_SLOW_FLUSH_LOG_THRESHOLD=<<LOGZIO_SLOW_FLUSH_LOG_THRESHOLD>> \` | Specifies the threshold for chunk flush performance check. |  `20.0` |
| `-e LOGZIO_BUFFER_TYPE=<<LOGZIO_BUFFER_TYPE>> \` | Specifies which plugin to use as the backend. |  `file` |
| `-e LOGZIO_BUFFER_PATH=<<LOGZIO_BUFFER_PATH>> \`  | Specifies the path to the backend plugin. | `/var/log/Fluentd-buffers/stackdriver.buffer` |
| `-e LOGZIO_OVERFLOW_ACTION=<<LOGZIO_OVERFLOW_ACTION>> \` | Specifies the parameter that controls the behavior when the queue becomes full. Refer to [documentation on Fluentd](https://docs.fluentd.org/output#overflow_action) for more on this. | `block` |
| `-e LOGZIO_CHUNK_LIMIT_SIZE=<<LOGZIO_CHUNK_LIMIT_SIZE>> \` | Specifies the maximum size of a chunk allowed.  | `2M` |
| `-e LOGZIO_QUEUE_LIMIT_LENGTH=<<LOGZIO_QUEUE_LIMIT_LENGTH>> \` | Specifies the maximum length of the output queue.  | `6` |
| `-e LOGZIO_FLUSH_INTERVAL=<<LOGZIO_FLUSH_INTERVAL>> \` | Specifies the interval, in seconds, to wait before invoking the next buffer flush.  | `5s` |
| `-e LOGZIO_RETRY_MAX_INTERVAL=<<LOGZIO_RETRY_MAX_INTERVAL>> \` | Specifies the maximum interval, in seconds, to wait between retries.  | `30s` |
| `-e LOGZIO_FLUSH_THREAD_COUNT=<<LOGZIO_FLUSH_THREAD_COUNT>> \` | Specifies the number of threads to flush the buffer.  | `2` |
| `-e LOGZIO_LOG_LEVEL=<<LOGZIO_LOG_LEVEL>> \` | Specifies the log level for this container.  | `info` |
| `ADDITIONAL_FIELDS` | Include additional fields with every message sent, formatted as `fieldName1=fieldValue1,fieldName2=fieldValue2` | `nil` |


 ## Ship Kubernetes logs with Fluentd

 See the full documentation for shipping your Kubernetes logs with Fluentd [here](/shipping/Containers/kubernetes.md).
