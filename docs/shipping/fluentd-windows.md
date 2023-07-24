---
id: Fluentd-Windows
title: Fluentd
sidebar_position: 1
overview: Fluentd is a data collector, which unifies the data collection and consumption. This integration allows you to use Fluentd to send logs from your Windows system to your Logz.io account.
product: ['metrics']
os: ['windows', 'linux']
filters: ['gcp', 'cloud']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/aiven-logo.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
---

 
Fluentd is a data collector, which unifies the data collection and consumption. This integration allows you to use Fluentd to send logs from your Windows system to your Logz.io account. 

:::note
Fluentd will fetch all existing logs, as it is not able to ignore older logs.
:::
  

#### Configure Fluentd

**Before you begin, you'll need**:
Ruby and ruby-dev 2.1 or higher

 

	
##### Install Fluentd td-agent

Navigate to the [downloads](https://docs.fluentd.org/installation/install-by-msi) page of td-agent and download the latest version of the installer. After that, run the installer and follow the wizard instructions.

##### Install the Logz.io plugin

```shell
gem install fluentd fluent-plugin-logzio
```

##### Set up td-agent.conf

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

###### Parameters

| Parameter | Description |
|---|---|
| endpoint_url | A url composed of your Logz.io region's listener URL, account token, and log type. {@include: ../_include/log-shipping/listener-var.html} {@include: ../_include/log-shipping/log-shipping-token.html} |
| type | Log type. If required, replace `<<LOG_TYPE>>` with the desired name for the log type, the default value is `fluentbit` |
| output_include_time | To add a timestamp to your logs when they're processed, `true` (recommended). Otherwise, `false`. |
| output_include_tags | To add the `fluentd` tag to logs, `true`. Otherwise, `false`. If `true`, use in combination with `output_tags_fieldname`. |
| output_tags_fieldname | If `output_include_tags` is `true`, sets output tag's field name. The default is `fluentd_tag` |
| http_idle_timeout | Time, in seconds, that the HTTP connection will stay open without traffic before timing out. |




##### Run Fluentd td-agent

Open `Td-agent Command Prompt` from the Windows Start menu and run the following command:

```shell
C:\opt\td-agent> td-agent
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
 