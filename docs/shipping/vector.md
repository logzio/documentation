---
id: Amazon-S3
title: Amazon S3
sidebar_position: 1
overview: This integration creates a Kinesis Data Firehose delivery stream that links to your Amazon S3 metrics stream and then sends the metrics to your Logz.io account. It also creates a Lambda function that adds AWS namespaces to the metric stream, and a Lambda function that collects and ships the resources' tags.
product: ['metrics']
os: ['windows', 'linux']
filters: ['gcp', 'cloud']
logo: https://docs.logz.io/images/logo/logz-symbol.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['1Pm3OYbu1MRGoELc2qhxQ1']
metrics_alerts: []
---


Vector by Datadog is a lightweight, ultra-fast tool for building observability pipelines. Deploy this integration to send logs from your Vector tools to your Logz.io account.

#### Configure Vector

 

##### Install Vector

If you haven't already, install Vector:

```shell
curl https://sh.vector.dev -sSf | sh
```

For alternate installation instructions,
see [Installation](https://vector.dev/docs/setup/) from Vector. 

##### Configure Vector with Logz.io sink

Add this code block to your Vector configuration file.
We recommend the configuaration shown in the code block.

:::note
Find the complete configuration docs at [http sink](https://vector.dev/docs/reference/configuration/sinks/http/) from Vector.
{:.info-box.read}
 

```toml
[sinks.logzio]
  # REQUIRED - General
  type = "http" # Don't change this setting
  inputs = ["YOUR_SOURCE_ID"]
  encoding.codec = "json" # enum: "json" or "text"

  # More information on uri below this code block
  uri = "https://<<LISTENER-HOST>>:8071/?token=<<LOG-SHIPPING-TOKEN>>&type=vector"

  # OPTIONAL - General
  compression = "gzip" # no default, must be: "gzip" (if supplied)

  # OPTIONAL - Batching
  batch.max_bytes = 9000000 # bytes - Logz.io max batch is 10MB
  batch.timeout_secs = 3

  # OPTIONAL - Buffer
  [sinks.logzio.buffer]
    type = "disk" # default, enum: "memory" or "disk"
    when_full = "block" # default, enum: "block" or "drop_newest"
    max_size = 268435488 # no default, bytes(104.9mb), relevant when type = "disk"
```

:::note
If you get a 400 error when using `json` encoding, try use port 8081 instead of 8071. 
:::
 

:::note
If your logs are sent in batches, change the `encoding.codec` setting from `json` to `text`. 
:::
 



###### Parameters

| Parameter | Description |
|---|---|
| uri (Required) | Your Logz.io region's listener URL account token, and log type. <br> {@include: ../_include/log-shipping/listener-var.html}  <br> {@include: ../_include/log-shipping/log-shipping-token.html} |
{:.paramlist}

##### Run Vector

```shell
vector --config path/to/your/vector.toml
```

##### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [log shipping troubleshooting]({{site.baseurl}}/user-guide/log-shipping/log-shipping-troubleshooting.html).

 
