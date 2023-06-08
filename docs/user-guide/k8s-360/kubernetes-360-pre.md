---
sidebar_position: 2
title: Kubernetes 360 Prerequisite
---


<!-- #### Meet your dashboard

Your Kubernetes 360 dashboard includes an overview of your clusters and deployments' current status.

![K360 Overview](https://dytvr9ot2sszz.cloudfront.net/logz-docs/k360/k360-overview.png) -->

Kubernetes 360 application provides an overview of your Kubernetes data, providing a quick overview of your current deployments, pods, and more useful information regarding your environment.

![Main dashboard](https://dytvr9ot2sszz.cloudfront.net/logz-docs/k360/k360-main.png)






### Manually shipping Kubernetes data


If you already have Kubernetes 360 data in your Logz.io account or prefer connecting Kubernetes [manually](https://app.logz.io/#/dashboard/send-your-data/collection?tag=all&collection=prometheus-sources), you'll need an active **[Infrastructure Monitoring](https://app.logz.io/#/dashboard/metrics)** account, and ensure that your Kubernetes data is [connected to Logz.io](https://app.logz.io/#/dashboard/send-your-data/agent/new).

In addition, you'll need to ship your cluster metrics from the following sources:

* Node exporter (should be installed on every node).
* CAdvisor.
* Kube-state-metrics version 2.1 or higher.

And send the following metrics:

|**Metric name**|**Labels**|
| --- | --- |
|*|p8s_logzio_name `// Equivalent to a Cluster's name`|
|kube_pod_status_phase|pod, uid, node, host_ip, phase, namespace|
|kube_pod_info|pod,namespace,p8s_logzio_name,region|
|container_cpu_usage_seconds_total|pod, region, topology_kubernetes_io_region, container|
|container_memory_working_set_bytes|pod, container, resource|
|kube_pod_container_resource_limits|pod|
|kube_pod_container_info|pod|
|container_network_transmit_bytes_total|pod|
|container_network_receive_bytes_total|pod|
|kube_pod_created|pod|
|kube_pod_owner|pod, owner_kind, owner_name|
|kube_pod_container_status_restarts_total|pod|
|kube_pod_status_reason|pod, reason|
|kube_pod_container_status_waiting_reason|pod, reason|
|||
|node_cpu_seconds_total|instance, mode|
|node_memory_MemAvailable_bytes|instance|
|node_memory_MemTotal_bytes|instance|
|kube_node_role|node,role|
|kube_node_status_condition|node, status, condition|
|kube_node_created|node|
|node_filesystem_avail_bytes|instance|
|node_filesystem_size_bytes|instance|
|kube_node_status_allocatable|resource, resource|
|kube_node_labels|logzio_p8s_name|
|||
|kube_replicaset_owner|owner_kind, owner_name,replicaset|
|kube_deployment_created|deployment|
|kube_deployment_status_condition|deployment,status|
|||
|kube_daemonset_labels|all labels|
|kube_daemonset_status_number_ready|all labels|
|kube_daemonset_status_number_available|all labels|
|kube_daemonset_status_number_unavailable|all labels|
|kube_daemonset_status_current_number_scheduled|all labels|
|kube_daemonset_status_number_misscheduled|all labels|
|kube_daemonset_status_desired_number_scheduled|all labels|
|kube_job_labels|all labels|
|kube_job_complete|all labels|
|kube_job_status_failed|all labels|
|kube_job_status_succeeded|all labels|
|kube_job_complete|all labels|
|kube_job_status_failed|all labels|
|kube_job_status_completion_time|all labels|
|kube_replicaset_labels|all labels|
|kube_replicaset_spec_replicas|all labels|
|kube_replicaset_status_replicas|all labels|
|kube_replicaset_status_ready_replicas|all labels|
|kube_statefulset_replicas|all labels|
|kube_statefulset_status_replicas|all labels|
|kube_statefulset_status_replicas_updated|all labels|
|kube_statefulset_status_replicas_available|all labels|
|kube_job_owner|all labels|


### Manually configuring Security Risks

To add Security risks view to your existing Kubernetes data, you need to:

* [Ship reports from Trivy operator](/shipping/log-sources/trivy.html).
* Configure and send security logs.

After setting up the Trivy operator, ensure your account receives `type:trivy` logs. 

<!-- 
After deploying the updated Helm chart, ensure you're sending the following logs:

|**Source**|**Log**|
|kubernetes|host_ip|
|kubernetes|container_name|
|kubernetes|pod_uid|
|kubernetes|deployment_name|
|kubernetes|pod_ip|
|kubernetes|node_name|
|kubernetes|resource_kind|
|kubernetes|resource_name|
|kubernetes|namespace_name|
|kubernetes|pod_name|
||severity|
||resource|
||title|
||env_id|
||vulnerabilityID|
||primaryLink|
-->

If you encounter an issue while setting up your metrics or logs, [contact Logz.io's support team](mailto:help@logz.io) for additional help.