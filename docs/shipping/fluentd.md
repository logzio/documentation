---
id: Fluentd
title: Fluentd
overview: Fluentd is a data collector, which unifies the data collection and consumption. This integration allows you to use Fluentd to send logs to your Logz.io account.
product: ['metrics']
os: ['windows', 'linux']
filters: ['GCP', 'Cloud']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/fluentd.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
---
 

Fluentd is a data collector, which unifies the data collection and consumption. This integration allows you to use Fluentd to send logs to your Logz.io account. 

:::note
Fluentd will fetch all existing logs, as it is not able to ignore older logs.
:::
 

  

#### Configure Fluentd

**Before you begin, you'll need**:
Ruby and ruby-dev 2.1 or higher

 

	
##### Install Fluentd and the Logz.io plugin

```shell
gem install fluentd fluent-plugin-logzio
```

##### Set up Fluentd

```shell
fluentd --setup ./fluent
```

##### Add an input plugin

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


##### Configure Fluentd with Logz.io output

Add this code block to your Fluent configuration file (`fluent.conf` by default).

See the configuration parameters below the code block.👇

```conf
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

###### Parameters

| Parameter | Description |
|---|---|
| endpoint_url | A url composed of your Logz.io region's listener URL, account token, and log type. {@include: ../_include/log-shipping/listener-var.html} {@include: ../_include/log-shipping/log-shipping-token.html} |
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

##### Run Fluentd

```shell
fluentd -c ./fluent/fluent.conf -vv
```

##### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [log shipping troubleshooting]({{site.baseurl}}/user-guide/log-shipping/log-shipping-troubleshooting.html).

 
 
Fluentd can receive and concatenate multiline logs. To do this, you need to add a parser and concatenation plugin to your Fluentd configuration.

 

##### Add multiline parser to your input plugin

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

 