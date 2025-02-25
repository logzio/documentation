---
id: Docker
title: Docker
overview: Docker lets you work in standardized environments using local containers, promoting continuous integration and continuous delivery (CI/CD) workflows. With Logz.io you can collect logs and metrics from your Docker environment to gain observability and know if and when issues occur.
product: ['logs','metrics']
recommendedFor: ['DevOps Engineer']
os: ['windows', 'linux']
filters: ['Containers', 'Most Popular']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/docker.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['5Wbud46hwzhpFeokC69j0Z']
metrics_alerts: []
drop_filter: []
---

## Logs

### Docker collector

Docker is a set of platform-as-a-service products that deliver software in containers. This integration is a Docker container that can use either Filebeat or Fluent Bit to collect logs from other Docker containers and forward them to your Logz.io account.

To use docker-collector-logs, you'll set environment variables when you run the container. The Docker logs directory and docker.sock are mounted to the container, enabling Filebeat or Fluent Bit to collect logs and metadata.


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<Tabs>
<TabItem value="fluentbit-docker" label="Fluent Bit" default>

:::note
[Project's GitHub repo](https://github.com/logzio/docker-logs-collector)
:::


#### Pull the Docker image

Download the logzio/docker-collector-logs image.

```shell
docker pull logzio/docker-logs-collector:latest
```

#### Run the Docker image
  

For a complete list of options, see the parameters below the code block.👇
  
##### Docker

```shell
docker run --name docker-logs-collector \
--env LOGZIO_LOGS_TOKEN="<LOGS-SHIPPING-TOKEN>" \
-v /var/run/docker.sock:/var/run/docker.sock:ro \
-v /var/lib/docker/containers:/var/lib/docker/containers \
-e HEADERS="user-agent:logzio-docker-logs" \
logzio/docker-logs-collector:latest
```  
#### Parameters

| Parameter | Description | Field Type |
|---|---|---|
| LOGZIO_LOGS_TOKEN| Your Logz.io logs account token. Replace `<LOGS-SHIPPING-TOKEN>` with the [token](https://app.logz.io/#/dashboard/settings/general) associated with the account you want to use for shipping logs. | Required |
| LOGZIO_URL | The full URL to send logs to, including your region if needed. For example, for the EU region, use `https://listener-eu.logz.io:8071`. | _Default_: `https://listener.logz.io:8071` |
| LOGZIO_TYPE | Sets the log type.| _Default_: `logzio-docker-logs` |
| LOGS_PATH   | The path to docker container logs, supports globs.| _Default_: `/var/lib/docker/containers/*/*.log` |                                                                                                                                                                     
| MATCH_CONTAINER_NAME | Specify a container to collect logs from. If the container's name matches, its logs are shipped; otherwise, its logs are ignored. **Note**: This option cannot be used with SKIP_CONTAINER_NAMES. Use regular expressions to keep records that match a specific field.| _optional_ (Example: `^my-app-container.*`) |
| SKIP_CONTAINER_NAMES | Comma-separated list of containers to ignore. If a container's name matches a name on this list, its logs are ignored; otherwise, its logs are shipped. **Note**: This option cannot be used with MATCH_CONTAINER_NAME. Use regular expressions to exclude records matching a specific field. | _optional_ (Example: `test-container,debug-container`)|
| MATCH_IMAGE_NAME | Specify an image to collect logs from. If the image's name matches, its logs are shipped; otherwise, its logs are ignored. **Note**: This option cannot be used with SKIP_IMAGE_NAMES. Use regular expressions to keep records that match a specific field. | _optional_ (Example: `my-app-image:v1.2.3`) |
| SKIP_IMAGE_NAMES | Comma-separated list of images to ignore. If an image's name matches a name on this list, its logs are ignored; otherwise, its logs are shipped. **Note**: This option cannot be used with MATCH_IMAGE_NAME. Use regular expressions to exclude records that match a specific field. | _optional_ (Example: `test-image,debug-image`)|
| INCLUDE_LINE | Regular expression to match which lines Fluent Bit should include. | _optional_ (Example: `^ERROR.*`) |
| EXCLUDE_LINES | Regular expression to match which lines Fluent Bit should exclude. | _optional_ (Example: `.*DEBUG.*`) |
| ADDITIONAL_FIELDS | Include additional fields with every message sent, formatted as `"fieldName1:fieldValue1,fieldName2:fieldValue2"`.| _optional_ |
| SET_FIELDS | Set fields with every message sent, formatted as `"fieldName1:fieldValue1,fieldName2:fieldValue2"`. | _optional_ |
| LOG_LEVEL | Set log level for Fluent Bit. Allowed values: `debug`, `info`, `warning`, `error`.| _Default_: `info` |
| MULTILINE_START_STATE_RULE** | Regular expression for the start state rule of multiline parsing. See [Fluent Bit's official documentation](https://docs.fluentbit.io/manual/administration/configuring-fluent-bit/multiline-parsing#rules-definition) for further info.| _optional_ (Example: `^Exception`) |
| MULTILINE_CUSTOM_RULES | Custom rules for multiline parsing, separated by semicolons `;`.| _optional_ (Example: `^\\sat\\s;^Caused by:`) |
| READ_FROM_HEAD | Specify if Fluent Bit should read logs from the beginning.|_Default_: `true`|
| OUTPUT_ID | Specify the output ID for Fluent Bit logs.|_Default_: `output_id`|
| HEADERS | Custom headers for Fluent Bit logs.| _optional_ (Example: `x-custom-header:myCustomValue,x-other-header:someOtherValue`) |


</TabItem>
<TabItem value="filebeat-docker" label="Filebeat" default>

:::note
[Project's GitHub repo](https://github.com/logzio/docker-collector-logs/)
:::


##### Upgrading to a newer version

* When upgrading to a newer version of docker-collector-logs while it is already running, logs within the `ignoreOlder` timeframe may be resent. To minimize log duplicates, configure the `ignoreOlder` parameter of the new container to a lower value (e.g., `20m`).

* Version 0.1.0 of docker-collector-logs includes breaking changes. Refer to the [change log](https://github.com/logzio/docker-collector-logs#change-log) for further details.


#### Pull the Docker image

Download the logzio/docker-collector-logs image.

```shell
docker pull logzio/docker-collector-logs
```

#### Run the Docker image
  

For a complete list of options, see the parameters below the code block.👇
  
##### Docker

```shell
docker run --name docker-collector-logs \
--env LOGZIO_TOKEN="<<LOG-SHIPPING-TOKEN>>" \
-v /var/run/docker.sock:/var/run/docker.sock:ro \
-v /var/lib/docker/containers:/var/lib/docker/containers \
logzio/docker-collector-logs
```
  
##### Docker Swarm

```shell
docker service create --name docker-collector-logs \
--env LOGZIO_TOKEN="<<LOG-SHIPPING-TOKEN>>" \
--mount type=bind,source=/var/run/docker.sock,target=/var/run/docker.sock \
--mount type=bind,source=/var/lib/docker/containers,target=/var/lib/docker/containers \
--mode global logzio/docker-collector-logs
```  

#### Parameters

| Parameter | Description | Field Type |
|---|---|---|
| LOGZIO_TOKEN | Your Logz.io account token. {@include: ../../_include/log-shipping/log-shipping-token.html}   | Required |
| LOGZIO_REGION | Logz.io region code to ship the logs to. This region code changes depending on the region your account is hosted in. For example, accounts in the EU region have region code `eu`. If you don't specify this parameter, the default value will be used. For more information, see [Account region](https://docs.logz.io/docs/user-guide/admin/hosting-regions/account-region/) on the Logz.io Docs. | _Default_: (US region) |
| LOGZIO_TYPE | The log type you'll use with this Docker. {@include: ../../_include/log-shipping/type.md} | _Default_: Docker image name |
| LOGZIO_CODEC | Set to `json` if shipping JSON logs. Otherwise, set to `plain` for plain text format. | _Default_: `plain` |
| ignoreOlder |  Set a time limit on back shipping logs. Upgrading to a newer version of docker-collector-logs while it is already running will cause it to resend logs that are within the `ignoreOlder` timeframe. You can minimize log duplicates by setting the `ignoreOlder` parameter of the new docker to a lower value (for example, `20m`). | _Default_: `3h` |
| LOGZIO_URL  |  URL for your account listener host. The URL changes depending on the region your account is hosted in. You can skip this parameter if you specify `LOGZIO_REGION`. If neither `LOGZIO_URL` nor `LOGZIO_REGION` is specified, the default value will be used. For more information, see [Account region](https://docs.logz.io/docs/user-guide/admin/hosting-regions/account-region/) on the Logz.io Docs. | _Default_: `listener.logz.io:5015` |
| additionalFields | Include additional fields with every message sent, formatted as `"fieldName1=fieldValue1;fieldName2=fieldValue2"`. To use an environment variable, format as `"fieldName1=fieldValue1;fieldName2=$ENV_VAR_NAME"`. In that case, the environment variable should be the only value in the field. If the environment variable can't be resolved, the field is omitted. | _optional_ |
| matchContainerName | Comma-separated list of containers you want to collect the logs from. If a container's name partially matches a name on the list, that container's logs are shipped. Otherwise, its logs are ignored. **Note: Can't be used with skipContainerName** | _optional_ |
| skipContainerName | Comma-separated list of containers you want to ignore. If a container's name partially matches a name on the list, that container's logs are ignored. Otherwise, its logs are shipped. **Note: Can't be used with matchContainerName** | _optional_ |
| includeLines | Comma-separated list of regular expressions to match the lines that you want to include. **Note**: Regular expressions in this list should not contain commas. | _optional_ |
| excludeLines | Comma-separated list of regular expressions to match the lines that you want to exclude. **Note**: Regular expressions in this list should not contain commas. | _optional_ |
| renameFields | Rename fields with every message sent, formatted as `"oldName,newName;oldName2,newName2"`. To use an environment variable, format as `"oldName,newName;oldName2,$ENV_VAR_NAME"`. When using an environment variable, it should be the only value in the field. If the environment variable can't be resolved, the field will be omitted. | _optional_ |
| HOSTNAME | Include your host name to display it for the field `agent.name`. If no value is entered, `agent.name`displays the container id.| _Default_: `''` |
| multilinePattern | Include your regex pattern. See [Filebeat's official documentation](https://www.elastic.co/guide/en/beats/filebeat/7.12/multiline-examples.html#multiline) for more information. | _Default_: `''` |
| multilineNegate |Include `'true'` to negate the pattern. **Note**: Cannot be used without multilinePattern. See [Filebeat's official documentation](https://www.elastic.co/guide/en/beats/filebeat/7.12/multiline-examples.html#multiline) for more information.| `'false'`  |
| multilineMatch | Specifies how Filebeat combines matching lines into an event. The settings are `after` or `before`. The behavior of these settings depends on what you specify for negate. **Note**: Cannot be used without multilinePattern. See [Filebeat's official documentation](https://www.elastic.co/guide/en/beats/filebeat/7.12/multiline-examples.html#multiline) for more information.| _Default_: `'after'` |
| LOG_LEVEL | Set log level for the collector. Allowed values are: `debug`, `info`, `warning`, `error` | _Default_: `info` |
| INPUT_ENCODING | Here is a full list of [valid encodings](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-input-container.html#_encoding) you can use. | _Default_: `utf-8` |


:::note
By default, logs from docker-collector-logs and docker-collector-metrics containers are ignored.
:::
  

</TabItem>
</Tabs>





 

#### Check Logz.io for your logs

Spin up your Docker containers if you haven't done so already.
Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [log shipping troubleshooting](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/log-shipping-troubleshooting/).

 
### The logzio-logging plugin
  
Docker is a set of platform as a service products that deliver software in containers. Deploy this integration to send your Docker logs to your Logz.io account using a dedicated Logz.io plugin. 

**Before you begin, you'll need**:
Docker Engine 17.05 or later,
Docker Community Edition (Docker CE) 18.03 or later

 

#### Install the plugin from the Docker store

```shell
docker plugin install logzio/logzio-logging-plugin:1.0.2 \
--alias logzio/logzio-logging-plugin
```

Check to see if logzio-logging-plugin is enabled.

```shell
docker plugin ls --filter enabled=true
```

If logzio-logging-plugin isn't on the list, enable it now.

```shell
docker plugin enable logzio/logzio-logging-plugin
```

#### Configure global settings with daemon.json

You can configure all containers with the same options using daemon.json.

For a complete list of options, see the configuration parameters below the code sample.👇

##### Code sample

```json
{
  "log-driver": "logzio/logzio-logging-plugin",
  "log-opts": {
    "logzio-url": "<<LISTENER-HOST>>",
    "logzio-token": "<<LOG-SHIPPING-TOKEN>>",
    "logzio-dir-path": "<dir_path_to_logs_disk_queue>"
  }
}
```

##### Parameters

| Parameter | Description | Required/Default |
|---|---|---|
| logzio-token | Your Logz.io account token. {@include: ../../_include/log-shipping/log-shipping-token.html}   | Required |
| logzio-url | Listener URL and port. {@include: ../../_include/log-shipping/listener-var.html}  | Required |
| logzio-dir-path | Unsent logs are saved to this location on the disk. | Required |
| logzio-source | Event source. | _optional_ |
| logzio-format | Log message format, either `json` or `text`. | `text` |
| logzio-tag | Log tag for the Container ID. For more information, see [Log tags for logging driver](https://docs.docker.com/v17.09/engine/admin/logging/log_tags/) from Docker. |  `\{\{.ID\}\}` |
| labels | Comma-separated list of labels to include in the log message. | _optional_ |
| env | Comma-separated list of environment variables to include in the log message. | _optional_ |
| env-regex | A regular expression to match logging-related environment variables. Used for advanced log tag options. If there is collision between the `label` and `env` keys, `env` wins. Both options add additional fields to the attributes of a logging message. | _optional_ |
| logzio-attributes | JSON-formatted metadata to include in the log message. | _optional_ | 


#### _(Optional)_ Set environment variables

Some logzio-logging-plugin options are controlled using environment variables.
Each of these variables has a default value, so you can skip this step if you're comfortable with the defaults.

##### Environment variables

| Parameter | Description | Required/Default |
|---|---|---|
| LOGZIO_DRIVER_LOGS_DRAIN_TIMEOUT | Time to wait between sending attempts. | `5s` |
| LOGZIO_DRIVER_DISK_THRESHOLD | Threshold, as % of disk usage, over which plugin will start dropping logs. | `70` |
| LOGZIO_DRIVER_CHANNEL_SIZE | The number of pending messages that can be in the channel before adding them to the disk queue. | `10000` |
| LOGZIO_MAX_MSG_BUFFER_SIZE | Appends logs that are segmented by Docker with 16kb limit. Specifies the biggest message, in bytes, that the system can reassemble. `1048576` (1 MB) maximum. | `1048576` (1 MB) |
| LOGZIO_MAX_PARTIAL_BUFFER_DURATION | How long the buffer keeps the partial logs before flushing them. | `500ms` |


#### _(Optional)_ Override global settings for an individual container

You can configure the plugin separately for each container when using the `docker run` command.

##### Code sample


```shell
docker run --log-driver=logzio/logzio-logging-plugin \
--log-opt logzio-token=<<LOG-SHIPPING-TOKEN>> \
--log-opt logzio-url=https://<<LISTENER-HOST>>:8071 \
--log-opt logzio-dir-path=./docker_logs \
--log-opt logzio-tag="{{Name}}/{{FullID}}" \
--log-opt labels=region \
--log-opt env=DEV \
--env "DEV=true" \
--label region=us-east-1 \
<<DOCKER-IMAGE-NAME>>
```


{@include: ../../_include/log-shipping/log-shipping-token.html}

{@include: ../../_include/log-shipping/listener-var.html} 

For a complete list of options, see the configuration parameters above. 👆

#### Check Logz.io for your logs

Spin up your Docker containers if you haven't done so already. Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [log shipping troubleshooting](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/log-shipping-troubleshooting/).

 
## Metrics

Deploy this integration to ship metrics from your Docker network using containerized Telegraf agent.


<!-- logzio-inject:install:grafana:dashboards ids=["5Wbud46hwzhpFeokC69j0Z"] -->


  

#### Pull the Docker image

```shell
docker pull logzio/docker-metrics-collector:latest
```
#### Run the Docker image
  

For a complete list of options, see the parameters below the code block.👇

##### Docker

```shell
docker run --name telegraf-docker-collector-metrics \
 --env METRICS_TOKEN="<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>" \
 --env LOGZIO_LISTENER="https://<<LISTENER-HOST>>:8053" \
 -v /var/run/docker.sock:/var/run/docker.sock \
 logzio/docker-metrics-collector:latest
```
##### Docker Swarm

```shell
docker service create --name telegraf-docker-collector-metrics \
 --env METRICS_TOKEN="<<PROMETHEUS-METRICS-SHIPPING-TOKEN>" \
 --env LOGZIO_LISTENER="https://<<LISTENER-HOST>>:8053" \
 --mount type=bind,source=/var/run/docker.sock,target=/var/run/docker.sock \
 --mode global logzio/docker-metrics-collector:latest 
 ```

{@include: ../../_include/general-shipping/replace-placeholders-prometheus.html}


If you prefer to keep these environment variables in an `.env` file, run the following command:

`docker run -d --env-file=docker.env -v /var/run/docker.sock:/var/run/docker.sock logzio/docker-metrics-collector:latest`

#### Parameters

Below is a list of all environment variables available with this integration. If required, add a variable to the `docker run` command using the `--env` flag.

|Name|Description|Required/Default|
|---|---|---|
|METRICS_TOKEN|Your Logz.io metrics account token.|Required|
|LOGZIO_LISTENER|Your Logz.io listener address followed by port `8053`.|Required/Default: `https://listener.logz.io:8053`.|
|DOCKER_ENDPOINT|Address to reach the required Docker Daemon.|Default: `unix:///var/run/docker.sock`.|
|TIMEOUT|The request timeout for any Docker Daemon query.|Default: `5s`.|
|EXCLUDED_IMAGES|A list of strings, regexes, or globs, the container image names of which, will not be among the queried containers. !-prefixed negations are possible for all item types to signify that only unmatched container image names should be monitored. For example: `imageNameToExclude1,imageNameToExclude2)`|Default: `nil`.|
|GLOBAL_TAGS| A comma separated list of key-value pairs that will be added to every metric. For example - `key1=value1,key2=value2`| Default: `nil`. |

#### Check Logz.io metrics

Install the pre-built dashboards to enhance the observability of your metrics.

<!-- logzio-inject:install:grafana:dashboards ids=["5Wbud46hwzhpFeokC69j0Z"] -->

{@include: ../../_include/metric-shipping/generic-dashboard.html} 

 

 

