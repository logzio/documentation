---
sidebar_position: 2
title: Kubernetes 360 Prerequisites
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Everything you need to get started with Logz.io's Kubernetes 360
keywords: [kubernetes, k360, ship kubernetes data, kubernetes logs, metrics, labels]
slug: /user-guide/k8s-360/kubernetes-360-pre
---



Kubernetes 360 application provides an overview of your Kubernetes data, providing a quick overview of your current deployments, pods, and more useful information regarding your environment.

![Main dashboard](https://dytvr9ot2sszz.cloudfront.net/logz-docs/k360/k360-main.png)






## Manually shipping Kubernetes data


If you already have Kubernetes 360 data in your Logz.io account or prefer connecting Kubernetes [manually](https://app.logz.io/#/dashboard/integrations/collectors?tags=Tracing), you'll need an active **[Infrastructure Monitoring](https://app.logz.io/#/dashboard/metrics)** account, and ensure that your Kubernetes data is [connected to Logz.io](https://app.logz.io/#/dashboard/integrations/collectors?tags=Quick%20Setup).

In addition, you'll need to ship your cluster metrics from the following sources:

* Node exporter (should be installed on every node).
* CAdvisor.
* Kube-state-metrics version 2.1 or higher.

To ensure your Kubernetes 360 dashboard is up and running, you'll need to send the following metrics:

|**Metric name**|**Labels**|
| --- | --- |
|*|p8s_logzio_name `// Equivalent to a Cluster's name`|
|	kube_pod_status_phase	|	p8s_logzio_name, namespace, pod, phase, uid 	|
|	kube_pod_info	|	p8s_logzio_name, namespace, host_ip, node, pod	|  
|	container_cpu_usage_seconds_total	|	p8s_logzio_name, namespace, pod, region, topology_kubernetes_io_region, container |
|	kube_pod_container_resource_limits	|	p8s_logzio_name, namespace, pod, resource	|
|	container_memory_working_set_bytes	|	p8s_logzio_name, namespace, pod, container	| 
|	kube_pod_container_info	|	p8s_logzio_name, namespace, pod	| 
|	container_network_transmit_bytes_total	|	p8s_logzio_name, namespace, pod	|
|	container_network_receive_bytes_total	|	p8s_logzio_name, namespace, pod	| 
|	kube_pod_created	|	p8s_logzio_name, namespace, pod	| 
|	kube_pod_owner	|	p8s_logzio_name, namespace, pod, owner_kind, owner_name | 
|	kube_pod_container_status_restarts_total	|	p8s_logzio_name, namespace, pod | 
|	kube_pod_status_reason	|	p8s_logzio_name, namespace, pod, reason	|
|	kube_pod_container_status_waiting_reason	|	p8s_logzio_name, namespace, pod, reason	| 
|	node_cpu_seconds_total	|	p8s_logzio_name, instance, kubernetes_node	| 
|	kube_node_status_allocatable	|	p8s_logzio_name, node, resource	|
|	node_memory_MemAvailable_bytes	|	p8s_logzio_name, instance, kubernetes_node	| 
|	node_memory_MemTotal_bytes	|	p8s_logzio_name, instance, kubernetes_node	| 
|	kube_node_role	|	p8s_logzio_name, status, role, node	| 
|	kube_node_status_condition	|	p8s_logzio_name, status, role, node	|
|	kube_node_created	|	p8s_logzio_name, node	| 
|	node_filesystem_avail_bytes	|	p8s_logzio_name, instance, kubernetes_node	| 
|	node_filesystem_size_bytes	|	p8s_logzio_name, instance, kubernetes_node	|
|	kube_replicaset_owner	|	p8s_logzio_name, namespace, owner_kind, owner_name, replicaset	| 
|	kube_deployment_created	|	p8s_logzio_name, namespace, deployment	| 
|	kube_deployment_status_condition	|	p8s_logzio_name, namespace, deployment, status	| 


### Additional Kubernetes metrics

To enrich your services and infrastructure data **even further**, we recommend sending the following metrics as well:


<!--
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
-->

| **Metric name** | **Labels** |
|--|--|
|*|p8s_logzio_name `// Equivalent to a Cluster's name`|
|	kube_pod_container_resource_requests	|	p8s_logzio_name, namespace, pod, container, resource	| 
|	container_memory_usage_bytes	|	p8s_logzio_name, namespace, pod, container, instance, node	|
|	kube_pod_container_status_waiting	|	p8s_logzio_name, pod, container	| 
|	kube_pod_container_status_terminated	|	p8s_logzio_name, pod, container	| 
|	kube_pod_container_status_running	|	p8s_logzio_name, pod	|
|	kube_node_status_capacity	|	p8s_logzio_name, node, resource	| 
|	node_disk_reads_completed_total	|	p8s_logzio_name, kubernetes_node	| 
|	node_disk_read_bytes_total	|	p8s_logzio_name, kubernetes_node	| 
|	node_disk_read_time_seconds_total	|	p8s_logzio_name, kubernetes_node	| 
|	node_disk_writes_completed_total	|	p8s_logzio_name, kubernetes_node	|
|	node_disk_written_bytes_total	|	p8s_logzio_name, kubernetes_node	|
|	node_disk_write_time_seconds_total	|	p8s_logzio_name, kubernetes_node	|
|	node_network_transmit_bytes_total	|	p8s_logzio_name, kubernetes_node	|
|	node_receive_transmit_bytes_total	|	p8s_logzio_name, kubernetes_node	|
|	node_memory_MemFree_bytes	|	p8s_logzio_name, kubernetes_node	| 
|	kube_node_info	|	p8s_logzio_name, node	|
|	kube_deployment_status_replicas	|	p8s_logzio_name, namespace, deployment	|   
|	kube_deployment_status_replicas_updated	|	p8s_logzio_name, namespace, deployment	|
|	kube_deployment_spec_replicas	|	p8s_logzio_name, namespace, deployment	| 
|	kube_daemonset_status_number_available	|	p8s_logzio_name, daemonset	| 
|	kube_daemonset_status_number_unavailable	|	p8s_logzio_name, daemonset	|
|	kube_daemonset_status_current_number_scheduled	|	p8s_logzio_name, daemonset	|
|	kube_daemonset_status_number_misscheduled	|	p8s_logzio_name, daemonset	|
|	kube_daemonset_status_desired_number_scheduled	|	p8s_logzio_name, daemonset	|
|	kube_statefulset_status_replicas	|	p8s_logzio_name, namespace, app_kubernetes_io_instance, statefulset	| 
|	kube_statefulset_replicas	|	p8s_logzio_name, namespace, app_kubernetes_io_instance, statefulset	|
|	container_network_transmit_packets_total	|	p8s_logzio_name, namespace, pod	|
|	container_network_receive_packets_total	|	p8s_logzio_name, namespace, pod	|
|	container_network_transmit_packets_dropped_total	|	p8s_logzio_name, namespace, pod	|
|	container_network_receive_packets_dropped_total	|	p8s_logzio_name, namespace, pod, container	| 
|	node_memory_Cached_bytes	|	p8s_logzio_name, kubernetes_node	|
|	node_memory_Buffers_bytes	|	p8s_logzio_name, kubernetes_node	| 
|	kube_statefulset_status_replicas_updated	|	p8s_logzio_name, namespace, statefulset, app_kubernetes_io_instance	| 
|   kube_deployment_labels | p8s_logzio_name, namespace, deployment |
|   kube_daemonset_labels | all labels |
|   kube_statefulset_labels | all labels |
|   kube_job_labels | all labels |
|   kube_pod_labels | all labels |

## Manually configuring Security Risks

To add a Security risks view to your existing Kubernetes data, you need to:

* [Ship reports from Trivy operator](/docs/shipping/security/trivy/).
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