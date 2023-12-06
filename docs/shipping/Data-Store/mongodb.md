---
id: MongoDB
title: MongoDB
overview: MongoDB is a source-available cross-platform document-oriented database program. This integration lets you send logs and metrics from your MongoDB instances to your Logz.io account.
product: ['logs','metrics']
os: ['windows', 'linux']
filters: ['Data Store']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/mongo-logo.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---

## Logs

Fluentd is an open source data collector and a great option because of its flexibility. This integration lets you send logs from your MongoDB instances to your Logz.io account using Fluentd.

**Before you begin, you'll need**:

* MongoDB installed on your host
* Ruby 2.4+ and Ruby-dev
 
### Configure MongoDB to write logs to a file

In the configuration file of your MongoDB instance, set the database to write logs to a file. You can skip this step if this has already been configured on your MongoDB host.

To do this, add the following to your MongoDB configuration file:


```yaml
systemLog:
   destination: file
   path: "<<MONGODB-FILE-PATH>>"
   logAppend: true
```

* Replace `<<MONGODB-FILE-PATH>>` with the path to the log file, for example, `/var/log/mongodb/mongod.log`.
  

Make sure Fluend can read from the MongoDB log file. You can set this as follows:

#### On macOS and Linux

```shell
sudo chmod 604 <<MONGODB-FILE-PATH>>
```

* Replace `<<MONGODB-FILE-PATH>>` with the path to the MongoDB log file.

#### On Windows

Enable the read access in the file properties.


### Install Fluentd 


```shell
gem install fluentd
```

```shell
fluentd --setup ./fluent
```
  
This command creates a directory called `fluent` where we will create the configuration file and Gemfile.

  
  
### Create a Gemfile for Fluentd

In your preffered directory, create a Gemfile with the following content:

```ruby
source "https://rubygems.org"
# You can use fixed version of Fluentd and its plugins
# Add plugins you want to use
gem "fluent-plugin-logzio", "0.0.21"
gem "fluent-plugin-record-modifier"
```
  
### Configure Fluentd with Logz.io output

Add this code block to your Fluent configuration file (`fluent.conf` by default).

See the configuration parameters below the code block.👇

```conf
# To ignore fluentd logs
<label @FLUENT_LOG>
  <match fluent.*>
    @type null
  </match>
</label>
# Tailing mongodb logs
<source>
  @type tail
  @id mongodb_logs
  path <<MONGODB-FILE-PATH>>
  # If you're running on windows, change the pos_file to a Windows path
  pos_file /var/log/fluentd-mongodb.log.pos
  tag logzio.mongodb.*
  read_from_head true
  <parse>
    @type json
  </parse>
</source>
# Parsing the logs
<filter logzio.mongodb.**>
  @type record_modifier
  <record>
    type  mongodb-fluentd
    message ${record["msg"]}
    mongodb_timestamp ${record["t"]["$date"]}
    log_id ${record["id"].to_s}
  </record>
  remove_keys msg,t,id
</filter>
# Sending logs to Logz.io
<match logzio.mongodb.**>
  @type logzio_buffered
  endpoint_url https://<<LISTENER-HOST>>:8071?token=<<LOGZIO-SHIPPING-TOKEN>>
  output_include_time true
  output_include_tags true
  http_idle_timeout 10
  <buffer>
      @type memory
      flush_thread_count 4
      flush_interval 3s
      chunk_limit_size 16m      # Logz.io bulk limit is decoupled from chunk_limit_size. Set whatever you want.
      queue_limit_length 4096
  </buffer>
</match>
```

#### Parameters

| Parameter | Description |
|---|---|
| `<<LOGZIO-SHIPPING-TOKEN>>` | {@include: ../../_include/log-shipping/log-shipping-token.md} |
| `<<LISTENER-HOST>>` | {@include: ../../_include/log-shipping/listener-var.html}  |
| `<<MONGODB-FILE-PATH>>` | Path to the log file of your MongoDB. |
| endpoint_url | A url composed of your Logz.io region's listener URL, account token, and log type. {@include: ../../_include/log-shipping/listener-var.html}  |
| output_include_time | To add a timestamp to your logs when they're processed, `true` (recommended). Otherwise, `false`. |
| output_include_tags | To add the `fluentd` tag to logs, `true`. Otherwise, `false`. If `true`, use in combination with `output_tags_fieldname`. |
| output_tags_fieldname | If `output_include_tags` is `true`, sets output tag's field name. The default is `fluentd_tag` |
| http_idle_timeout | Time, in seconds, that the HTTP connection will stay open without traffic before timing out. |






### Run Fluentd

```shell
fluentd -c ./fluent.conf --gemfile ./Gemfile
```



### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd). You can search for `type:mongodb-fluentd` to filter for your MongoDB logs. Your logs should be already parsed thanks to the Logz.io preconfigured parsing pipeline.

If you still don't see your logs, see [log shipping troubleshooting](/docs/user-guide/log-management/troubleshooting/log-shipping-troubleshooting/).

## Metrics

To send your Prometheus-format MongoDB metrics to Logz.io, you need to add the **inputs.mongodb** and **outputs.http** plug-ins to your Telegraf configuration file.


<!-- logzio-inject:install:grafana:dashboards ids=["13q1IECY8zfnnDXvUq7vvH"] -->

### Configure Telegraf to send your metrics data to Logz.io



#### Set up Telegraf v1.17 or higher

{@include: ../../_include/metric-shipping/telegraf-setup.md}

#### Add the inputs.mongodb plug-in

First you need to configure the input plug-in to enable Telegraf to scrape the MongoDB data from your hosts. To do this, add the following code to the configuration file:


``` ini
[[inputs.mongodb]]
  servers = ["mongodb://<<USER-NAME>>:<<PASSWORD>>@<<ADDRESS>>:<<PORT>>"]
  ## An array of URLs of the form:
  ##   "mongodb://" [user ":" pass "@"] host [ ":" port]
  ## For example:
  ##   mongodb://user:auth_key@10.10.3.30:27017,
  ##   mongodb://10.10.3.33:18832,
  ##   servers = ["mongodb://127.0.0.1:27017,10.10.3.33:18832,10.10.5.55:6565"]
​
  gather_cluster_status = true
  gather_perdb_stats = true
  gather_col_stats = true
```

* Replace `<<USER-NAME>>` with the user name for your MongoDB database.
* Replace `<<PASSWORD>>` with the password for your MongoDB database.
* Replace `<<ADDRESS>>` with the address of your MongoDB database host. This is `localhost` if installed locally.
* Replace `<<PORT>>` with the address of your host port allocated to MongoDB database.

:::note
The full list of data scraping and configuring options can be found [here](https://github.com/influxdata/telegraf/blob/release-1.18/plugins/inputs/mongodb/README.md).
:::


#### Add the outputs.http plug-in

{@include: ../../_include/metric-shipping/telegraf-outputs.md}
{@include: ../../_include/general-shipping/replace-placeholders-prometheus.html}

#### Start Telegraf

{@include: ../../_include/metric-shipping/telegraf-run.md}

#### Check Logz.io for your metrics

{@include: ../../_include/metric-shipping/custom-dashboard.html} Install the pre-built dashboard to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["13q1IECY8zfnnDXvUq7vvH"] -->

{@include: ../../_include/metric-shipping/generic-dashboard.html}



