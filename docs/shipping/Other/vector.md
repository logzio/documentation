---
id: Vector-data
title: Vector
overview: Vector by Datadog is a lightweight, ultra-fast tool for building observability pipelines. Deploy this integration to send logs from your Vector tools to your Logz.io account.
product: ['logs']
os: ['windows', 'linux']
filters: ['Other']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/vector.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---


Vector by Datadog is a lightweight, ultra-fast tool for building observability pipelines. Deploy this integration to send logs from your Vector tools to your Logz.io account.

### Install Vector

If you haven't already, install Vector:

```shell
curl https://sh.vector.dev -sSf | sh
```

For alternate installation instructions,
see [Installation](https://vector.dev/docs/setup/) from Vector.

### Configure Vector with Logz.io sink

Add this code block to your Vector configuration file.
We recommend the configuaration shown in the code block.

:::note
Find the complete configuration docs at [http sink](https://vector.dev/docs/reference/configuration/sinks/http/) from Vector.
:::


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




#### Parameters

| Parameter | Description |
|---|---|
| uri (Required) | Your Logz.io region's listener URL account token, and log type. {@include: ../../_include/log-shipping/listener-var.html} Replace `<<LOG-SHIPPING-TOKEN>>` with the token of the account you want to ship to.|

### Run Vector

```shell
vector --config path/to/your/vector.toml
```

### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [log shipping troubleshooting]({{site.baseurl}}/user-guide/log-shipping/log-shipping-troubleshooting.html).


