---
id: Fluentd
title: Fluentd
overview: Fluentd is a data collector, which unifies the data collection and consumption. Deploy this integration to ship logs from Docker containers on your host system to Logz.io using Fluentd running in a separate container. The host system refers to a physical or virtual machine that hosts your Docker containers. 
product: ['metrics']
os: ['windows', 'linux']
filters: ['GCP', 'Cloud']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/FluentD_Docker.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
---
 

Fluentd is a data collector, which unifies the data collection and consumption. Deploy this integration to ship logs from Docker containers on your host system to Logz.io using Fluentd running in a separate container. The host system refers to a physical or virtual machine that hosts your Docker containers. 

:::note
Fluentd will fetch all existing logs, as it is not able to ignore older logs.
:::
 

### Architecture overview

This integration includes:


* Pulling a Docker image of containerized Fluentd
* Configuring and running containerized Fluentd

![Integration architecture Fluentd on Docker](https://dytvr9ot2sszz.cloudfront.net/logz-docs/log-shipping/docker-fluentd-hla-v2.png)

Upon deployment, each container on your host system, including the Fluentd container, writes logs to a dedicated log file. Fluentd fetches the log data from this file and ships the data over HTTP or HTTPS to your Logz.io account, either via an optional proxy sever or directly.

  

#### Deploy containerized Fluentd to ship container logs to your Logz.io account

**Before you begin, you'll need**:
Docker installed on your host system

 

##### Pull the Docker image for containerized Fluentd

```shell
docker pull logzio/fluentd-docker-logs
```

##### Start the container

Run the following command:

   ```conf
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

{@include: ../_include/log-shipping/listener-var.html}
{@include: ../_include/log-shipping/log-shipping-token.html}

If you need to send the logs via a proxy server:

   * Add `-e LOGZIO_PROXY_URI=<<YOUR-PROXY-URI>>` to the above command and replace `<<YOUR-PROXY-URI>>` with your proxy URI.
   * Add `-e LOGZIO_PROXY_CERT=<<YOUR-PROXY-CERTIFICATE>>` to the above commad and replace `<<YOUR-PROXY-CERTIFICATE>>` with your proxy certificate value.

##### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd). You can filter for data of type `docker-fluentd` to see the incoming container logs.
  
If you still don’t see your data, see [log shipping troubleshooting](https://docs.logz.io/user-guide/log-shipping/log-shipping-troubleshooting.html).
  
 

#### Advanced settings

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
 