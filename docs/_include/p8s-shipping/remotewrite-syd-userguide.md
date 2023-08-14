
To send your Prometheus application metrics to a Logz.io Infrastructure Monitoring account, use remote write to connect to Logz.io as the endpoint. Your data is formatted as JSON documents by the Logz.io listener.


:::note
**Multiple server environments:**  If you have multiple Prometheus server instances, you'll have to add Logz.io as an endpoint for each instance.
:::


#### Configuring Remote Write to Logz.io


##### Get your Logz.io Infrastructure Monitoring account information

Within Logz.io, look up the Listener host for your region (URL) and the Logz.io Metrics Account token.

+ You'll find the correct Region and Listener URL for your region in the [*Regions and Listener Hosts*](https://docs.logz.io/user-guide/accounts/account-region.html#available-regions) table. 

+ Look up your Prometheus Metrics account token in the [Settings > Manage tokens > Data shipping tokens > Metrics](https://app.logz.io/#/dashboard/settings/manage-tokens/data-shipping) tab of your Operations workspace. For more information, see [Metrics shipping token. ](https://docs.logz.io/user-guide/accounts/finding-your-metrics-account-token/) 



##### Add a remote_write url


Configure your Prometheus yaml file or use a Helm chart:

###### To configure a Prometheus yaml file with `bearer_token`

Add the following parameters to your Prometheus yaml file:

| Environment variable | Description |Required/Default|
|---|---|---|



| external_labels | Parameters to tag the metrics from this specific Prometheus server. | |
| p8s_logzio_name |Use the value of the parameter `p8s_logzio_name` to identify from which Prometheus environment the metrics are arriving to Logz.io. Replace the `<labelvalue>` placeholder with a label that will be added to all the metrics that are sent from this specific Prometheus server. |  |
| remote_write | The remote write section configuration sets Logz.io as the endpoint for your Prometheus metrics data. Place this section at the same indentation level as the `global` section. ||
|url|  The Logz.io Listener URL for for your region, configured to use port **8052** for http traffic, or port **8053** for https traffic. For more details, see the [Prometheus configuration file remote write reference. ](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#remote_write) | Required|
|bearer_token|The Logz.io Prometheus Metrics account token.  | Required|


```yaml
global:
  external_labels:
    p8s_logzio_name: <labelvalue>
remote_write:
  - url: https://<<LISTENER-HOST>>:8053
    bearer_token: <<PROMETHEUS-METRICS-SHIPPING-TOKEN>>
    remote_timeout: 30s
    queue_config:
      batch_send_deadline: 5s  #default = 5s
      max_shards: 10  #default = 1000
      min_shards: 1
      max_samples_per_send: 500 #default = 100
      capacity: 10000  #default = 500

```

###### To configure a Prometheus yaml file with `bearer_token_file`

If you want to use a `bearer_token_file` to configure your Prometheus account, create a .txt file that contains the Logz.io token and use its path when configuring your yaml file:

| Environment variable | Description |Required/Default|
|---|---|---|
| external_labels | Parameters to tag the metrics from this specific Prometheus server. |
| p8s_logzio_name |Use the value of the parameter `p8s_logzio_name` to identify from which Prometheus environment the metrics are arriving to Logz.io. Replace the `<labelvalue>` placeholder with a label that will be added to all the metrics that are sent from this specific Prometheus server. |
| remote_write | The remote write section configuration sets Logz.io as the endpoint for your Prometheus metrics data. Place this section at the same indentation level as the `global` section. ||
|url|  The Logz.io Listener URL for for your region, configured to use port **8052** for http traffic, or port **8053** for https traffic. For more details, see the [Prometheus configuration file remote write reference. ](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#remote_write) | Required|
|bearer_token_file|The file path that holds Logz.io Prometheus Metrics account token.  | Required|

```yaml
global:
  external_labels:
    p8s_logzio_name: <labelvalue>
remote_write:
  - url: https://listener.logz.io:8053
    bearer_token_file: path/to/token.txt
    remote_timeout: 30s
    queue_config:
      batch_send_deadline: 5s  #default = 5s
      max_shards: 10  #default = 1000
      min_shards: 1
      max_samples_per_send: 500 #default = 100
      capacity: 10000  #default = 500

```


###### To configure a Helm chart

For [kube-prometheus-stack](https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack) Helm chart users:

Edit your chart `values.yaml` file in the following sections:

+ remote write:

```yaml
remoteWrite:
    - url: https://<<LISTENER-HOST>>:8053  # The Logz.io Listener URL for your region, configured to use port **8052** for http traffic, or port **8053** for https traffic.
      bearerToken: <<PROMETHEUS-METRICS-SHIPPING-TOKEN>> # The Logz.io Prometheus metrics account token
      remoteTimeout: 30s
      queueConfig:
        batchSendDeadline: 5s  #default = 5s
        maxShards: 10  #default = 1000
        maxSamplesPerSend: 500 #default = 100
        capacity: 10000  #default = 500
```

+ externalLabels:

```yaml
externalLabels:
  p8s_logzio_name: <labelvalue>
```


##### Verify the remote_write configuration

+ **Run a query**: If you are scraping Prometheus metrics, you can check that the remote_write configuration is working properly by doing one of the following and verifying that the result is greater than zero (n > 0) for the url:

  * Run a query on your local Prometheus interface for the metric `prometheus_remote_storage_samples_in_total`.

  * Check for the metric in the `/metrics` endpoint on your Prometheus server.

+ **Check via Metrics Explore**: To verify that metrics are arriving to Logz,io:
  1. Open Metrics **Explore** via the compass icon in the left menu bar.

  2. Examine the **Metrics** dropdown list below the **Explore** heading in the upper left of the pane. <br />
    An empty list or the text _no metrics_ indicates that the remote write configuration is not working properly.
    ![Verify Prometheus metrics](https://dytvr9ot2sszz.cloudfront.net/logz-docs/grafana/select-metric-query.png)

##### Open Metrics Explore

Once you've verified that your data is available in Logz.io, [explore your Prometheus metrics.](https://docs.logz.io/user-guide/infrastructure-monitoring/metrics-explore-prometheus/)


After your metrics are flowing, [import your existing Prometheus and Grafana dashboards](https://docs.logz.io/user-guide/infrastructure-monitoring/prometheus-importing-dashbds.html) to Logz.io Infrastructure Monitoring as JSON files.



### Performance tips


* **Reduce tagging**: By default, all the metrics from your Prometheus server(s) are sent to Logz.io. To drop or send specific metrics, add Prometheus labeling _before_ enabling the remote write, or as part of the remote write configuration.  Learn more about Prometheus [relabeling tricks here.](https://medium.com/quiq-blog/prometheus-relabeling-tricks-6ae62c56cbda)


* **Metrics metadata dashboards**: If you have both Prometheus & Grafana, you can activate a dashboard as part of the remote write configuration that will show you the queue size and how many metrics you're sending. If your queue size increases, it might be necessary to open an additional channel. _(currently in development)_

* **Tune the remote write process**: Learn more about Prometheus [remote write tuning here.](https://prometheus.io/docs/practices/remote_write/)
