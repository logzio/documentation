---
id: Fluentd
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
| endpoint_url | A url composed of your Logz.io region's listener URL, account token, and log type. {@include: ../_include/log-shipping/listener-var.html} |
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
 


### Logzio-fluentd

[Helm](https://helm.sh/) is a tool for managing packages of pre-configured Kubernetes resources using Charts.
Logzio-fluentd allows you to ship logs from your Kubernetes cluster to Logz.io, using Fluentd.
Fluentd is flexible enough and has the proper plugins to distribute logs to different third parties such as Logz.io.

:::note
The chart defaults to configuration for Conatinerd CRI. If your cluster uses Docker as CRI, please refer to `daemonset.containerdRuntime` in the [configuration table](https://github.com/logzio/logzio-helm/tree/master/charts/fluentd#configuration).
:::
 

:::note
Fluentd will fetch all existing logs, as it is not able to ignore older logs.
:::
 

###### Sending logs from nodes with taints

If you want to ship logs from any of the nodes that have a taint, make sure that the taint key values are listed in your in your daemonset/deployment configuration as follows:
  
```yaml
tolerations:
- key: 
  operator: 
  value: 
  effect: 
```
  
To determine if a node uses taints as well as to display the taint keys, run:
  
```
kubectl get nodes -o json | jq ".items[]|{name:.metadata.name, taints:.spec.taints}"
```

#### Deploying the Chart

 


##### Create a monitoring namespace

Your DaemonSet will be deployed under the namespace `monitoring`.

```shell
kubectl create namespace monitoring
```

##### Add logzio-fluentd repo to your helm repo list

```shell
helm repo add logzio-helm https://logzio.github.io/logzio-helm
```

##### Deploy

The following command will install the Chart with the default values.
If you wish to change some of the values, add to this command `--set` flag(s) with the parameter(s) you'd like to change. For more information & example, see the [configuration table](https://github.com/logzio/logzio-helm/tree/master/charts/fluentd#configuration).
You can learn more about the ways you can customise the Chart's values [here](https://helm.sh/docs/helm/helm_install/#synopsis).

Replace `<<LOG-SHIPPING-TOKEN>>` with the [token](https://app.logz.io/#/dashboard/settings/general) of the account you want to ship to.

Replace `<<LISTENER-HOST>>` with your account's listener host. You can find your listener in your [manage tokens page](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping?product=logs).

```shell
helm install -n monitoring \
--set secrets.logzioShippingToken='<<LOG-SHIPPING-TOKEN>>' \
--set secrets.logzioListener='<<LISTENER-HOST>>' \
logzio-fluentd logzio-helm/logzio-fluentd
```

##### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Logz.io](https://app.logz.io/).
	
 

#### Configuration

This table contains all the parameters in `values.yaml`. If you wish to change the default values, specify each parameter using the `--set key=value` argument to `helm install` in step 2. For example:

```shell
helm install -n monitoring \
  --set terminationGracePeriodSeconds=40 \
  --set daemonset.logzioLogLevel=debug \
  --set-file configmap.extraConfig=/path/to/config.yaml \
  logzio-fluentd logzio-helm/logzio-fluentd
```

| Parameter | Description | Default |
|---|---|---|
| `image` | The logzio-fluentd docker image. | `logzio/logzio-fluentd` |
| `imageTag` | The logzio-fluentd docker image tag. | `1.0.1` |
| `nameOverride` | Overrides the Chart name for resources. | `""` |
| `fullnameOverride` | Overrides the full name of the resources. | `""` |
| `apiVersions.daemonset` | Daemonset API version. | `apps/v1` |
| `apiVersions.serviceAccount` | Service Account API version. | `v1` |
| `apiVersions.clusterRole` | Cluster Role API version. | `rbac.authorization.k8s.io/v1` |
| `apiVersions.clusterRoleBinding` | Cluster Role Binding API version. | `rbac.authorization.k8s.io/v1` |
| `apiVersions.configmap` | Configmap API version. | `v1` |
| `apiVersions.secret` | Secret API version. | `v1` |
| `namespace` | Chart's namespace. | `monitoring` |
| `isRBAC` | Specifies whether the Chart should be compatible to a RBAC cluster. If you're running on a non-RBAC cluster, set to `false`.  | `true` |
| `serviceAccount.name` | Name of the service account. | `""` |
| `daemonset.tolerations` | Set [tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) for all DaemonSet pods. | See [values.yaml](https://github.com/logzio/logzio-helm/blob/master/charts/fluentd/values.yaml). |
| `daemonset.nodeSelector` | Set [nodeSelector](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) for all DaemonSet pods. | `{}` |
| `daemonset.fluentdSystemdConf` | Controls whether Fluentd system messages will be enabled. | `disable` |
| `daemonset.fluentdPrometheusConf` | Controls the launch of a prometheus plugin that monitors Fluentd. | `disable` |
| `daemonset.includeNamespace` | Use if you wish to send logs from specific k8s namespaces, space delimited. Should be in the following format: `kubernetes.var.log.containers.**_<<NAMESPACE-TO-INCLUDE>>_** kubernetes.var.log.containers.**_<<ANOTHER-NAMESPACE>>_**`. | `""` |
| `daemonset.kubernetesVerifySsl` | Enables to validate SSL certificates. | `true` |
| `daemonset.auditLogFormat` | Match Fluentd's format for kube-apiserver audit logs. Set to `audit-json` if your audit logs are in json format. | `audit` |
| `daemonset.containerdRuntime` | **Deprecated from chart version 0.1.0.** Determines whether to use a configuration for a Containerd runtime. Set to `false` if your cluster doesn't use Containerd as CRI. | `true` |
| `daemonset.cri` | Container runtime interface of the cluster. Used to determine which configuration to use when concatenating partial logs. Valid options are: `docker`, `containerd`. | `containerd` |
| `daemonset.logzioBufferType` | Specifies which plugin to use as the backend. | `file` |
| `daemonset.logzioBufferPath` | Path of the buffer. | `/var/log/fluentd-buffers/stackdriver.buffer` |
| `daemonset.logzioOverflowAction` | Controls the behavior when the queue becomes full. | `block` |
| `daemonset.logzioChunkLimitSize` | Maximum size of a chunk allowed. | `2M` |
| `daemonset.logzioQueueLimitLength` | Maximum length of the output queue. | `6` |
| `daemonset.logzioFlushInterval` | Interval, in seconds, to wait before invoking the next buffer flush. | `5s` |
| `daemonset.logzioRetryMaxInterval` | Maximum interval, in seconds, to wait between retries. | `30` |
| `daemonset.logzioRetryForever` | If true, plugin will retry flushing forever | `true` |
| `daemonset.logzioFlushThreadCount` | Number of threads to flush the buffer. | `2` |
| `daemonset.logzioLogLevel` | The log level for this container. | `info` |
| `daemonset.extraEnv` | If needed, more env vars can be added with this field. | `[]` |
| `daemonset.resources` | Allows you to set the resources for Fluentd Daemonset. |  See [values.yaml](https://github.com/logzio/logzio-helm/blob/master/charts/fluentd/values.yaml). |
| `daemonset.extraVolumeMounts` | If needed, more volume mounts can be added with this field. | `[]` |
| `daemonset.terminationGracePeriodSeconds` | Termination period (in seconds) to wait before killing Fluentd pod process on pod shutdown. | `30` |
| `daemonset.extraVolumes` | If needed, more volumes can be added with this field. | `[]` |
| `daemonset.init.extraVolumeMounts` | If needed, more volume mounts to the init container can be added with this field. | `[]` |
| `clusterRole.rules` | Configurable [cluster role rules](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#role-and-clusterrole) that Fluentd uses to access Kubernetes resources. | See [values.yaml](https://github.com/logzio/logzio-helm/blob/master/charts/fluentd/values.yaml). |
| `secrets.logzioShippingToken` | Secret with your [logzio shipping token](https://app.logz.io/#/dashboard/settings/general). | `""` |
| `secrets.logzioListener` | Secret with your logzio listener host. `listener.logz.io`. | `" "` |
| `configMapIncludes` | Initial includes for `fluent.conf`. | See [values.yaml](https://github.com/logzio/logzio-helm/blob/master/charts/fluentd/values.yaml). |
| `configmap.extraConfig` | If needed, more Fluentd configuration can be added with this field. | `{}` |
| `configmap.fluent` | Configuration for `fluent.conf`. | See [values.yaml](https://github.com/logzio/logzio-helm/blob/master/charts/fluentd/values.yaml). |
| `configmap.kubernetes` | Configuration for `kubernetes.conf`. | See [values.yaml](https://github.com/logzio/logzio-helm/blob/master/charts/fluentd/values.yaml). |
| `configmap.system` | Configuration for `system.conf`. | See [values.yaml](https://github.com/logzio/logzio-helm/blob/master/charts/fluentd/values.yaml). |
| `configmap.systemd` | Configuration for `systemd.conf`. | See [values.yaml](https://github.com/logzio/logzio-helm/blob/master/charts/fluentd/values.yaml). |
| `configmap.kubernetesContainerd` | **Deprecated from chart version 0.1.0.** Configuration for `kubernetes-containerd.conf`. This is the configuration that's being used when `daemonset.containerdRuntime` is set to `true` | See [values.yaml](https://github.com/logzio/logzio-helm/blob/master/charts/fluentd/values.yaml). |
| `configmap.partialDocker` | Configuration for `partial-docker.conf`. Used to concatenate partial logs that split due to large size, for docker cri. | See [values.yaml](https://github.com/logzio/logzio-helm/blob/master/charts/fluentd/values.yaml). |
| `configmap.partialContainerd` | Configuration for `partial-containerd.conf`. Used to concatenate partial logs that split due to large size, for containerd cri. | See [values.yaml](https://github.com/logzio/logzio-helm/blob/master/charts/fluentd/values.yaml). |
| `configmap.audit` | Configuration for `audit.conf`. | See [values.yaml](https://github.com/logzio/logzio-helm/blob/master/charts/fluentd/values.yaml). |
| `configmap.auditJson` | Configuration for `audit-json.conf`. This is the configuration that's being used when `daemonset.auditLogFormat` is set to `audit-json` | See [values.yaml](https://github.com/logzio/logzio-helm/blob/master/charts/fluentd/values.yaml). |

**Note:** If you're adding your own configuration file via `configmap.extraConfig`:
- Add a `--set-file` flag to your `helm install` command, as seen in the [example above](https://github.com/logzio/logzio-helm/tree/master/charts/fluentd#configuration).
- Make sure that the `yaml` file with your configuration is in the following format:

```ini
my-custom-conf-name.conf: |-
	# .....
	# your config
	# .....
my-custom-conf-name2.conf: |-
	# .....
	# your config
	# .....
```

#### Adding a custom log_type field from attribute

To add a `log_type` field with a custom value to each log, you can use the annotation key `log_type` with a custom value. The annotation will be automatically parsed into a `log_type` field with the provided value. e.g:

```yaml
...
  metadata:
    annotations:
      log_type: "my_type"
```

Will result with the following log (json):

```json
{
...
,"log_type": "my_type"
...
}
```

#### Uninstalling the Chart

The command removes all the k8s components associated with the chart and deletes the release.  

To uninstall the `logzio-fluentd` deployment:

```shell
helm uninstall -n monitoring logzio-fluentd
```

  

{@include: ../_include//log-shipping/multiline-fluentd-plugin.md}



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
 
