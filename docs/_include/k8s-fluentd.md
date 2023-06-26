###### Environment variables

The following environment variables can be edited directly from the DaemonSet without editing the Configmap.


| Parameter | Description | Default |
|---|---|---|
| output_include_time | To append a timestamp to your logs when they're processed, `true`. Otherwise, `false`. | `true` |
| buffer_type | Specifies which plugin to use as the backend | `file` |
| buffer_path | Path of the buffer | `/var/log/Fluentd-buffers/stackdriver.buffer` |
| buffer_queue_full_action  | Controls the behavior when the queue becomes full | `block` |
| buffer_chunk_limit | Maximum size of a chunk allowed. | `2M` |
| buffer_queue_limit | Maximum length of the output queue. | `6` |
| flush_interval | Interval, in seconds, to wait before invoking the next buffer flush. | `5s` |
| max_retry_wait | Maximum interval, in seconds, to wait between retries. | `30s` |
| num_threads | Number of threads to flush the buffer. | `2` |
| INCLUDE_NAMESPACE | Sends logs from all namespaces by default. To send logs from specific k8s namespaces, specify them in the following format, space delimited: `kubernetes.var.log.containers.**_<<NAMESPACE-TO-INCLUDE>>_** kubernetes.var.log.containers.**_<<ANOTHER-NAMESPACE>>_**`. | `""` |
| KUBERNETES_VERIFY_SSL | Enable to validate SSL certificates. | `true` |
| FLUENT_FILTER_KUBERNETES_URL | URL to the API server. This parameter isn't part of the default Daemonset. You can set it to retrieve additional Kubernetes metadata for logs from the  Kubernetes API server.  | `null` |
| AUDIT_LOG_FORMAT |  The format of your audit logs. If your audit logs are in json format, set to `audit-json`.  | `audit` |
| CRI | The CRI of the cluster. In `logzio-daemonset` & `logzio-daemonset-rbac` is set to `docker`, and in `logzio-daemonset-containerd` is set to `containerd`. The configmap uses this var to determin which includes it needs to make for the fluent.conf file, when configuration needs to be adjusted by the CRI. |
