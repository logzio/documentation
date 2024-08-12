---
sidebar_position: 1
title: Kubernetes Content
description: Some content for Kubernetes
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [content, dashboard, alerts, observability]
---


**Monitoring Kubernetes Resources: Why it Matters**

Monitoring Kubernetes resources is crucial for maintaining the health, performance, and reliability of your applications and infrastructure. Our dashboards and alerts provide real-time visibility, enabling quick issue detection and resolution.

**The Importance of Observability**

Our dashboards, including Cluster Stats, Node Stats, and Pod Stats, offer a comprehensive view of your Kubernetes environment. By monitoring metrics and logs, you can optimize resources, improve performance, and enhance security.

**Dashboards and Alerts: Your Safety Net**

Prevent unplanned downtime, user dissatisfaction, and wasted costs with our dashboards and alerts. The Capacity Management dashboard optimizes resource use, while the OSD Dashboard Cluster Overview offers a full view of your logs.

Metrics alerts (Cluster CPU Overcommit, Node CPU Utilization, Pod Memory Usage) and logs alerts (k8s Internal Error, K8s Warning, K8s Connection Errors) notify you of potential issues early.

Use our dashboards and alerts to maintain Kubernetes health and performance, making data-driven decisions to optimize resources and applications.

## Dashboards

<h3 id="cluster-stats">Cluster Stats</h3>

Get a comprehensive view of the cluster's resource utilization, including total CPU, memory, and disk usage, along with detailed metrics for pods, nodes, deployments, and namespaces. Includes network traffic insights and integrated alerts for efficient Kubernetes management.

<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/content/dashmock.png" alt="cluster-stats" width="700"/>

<h3 id="node-stats">Node Stats</h3>

Get in-depth insights into each node's status, including uptime, running pods, and total CPU, memory, and disk resources. Monitor per-pod CPU and memory usage, overall resource utilization, and disk I/O metrics. Track network performance with real-time data on received and transmitted bytes and latency.

<h3 id="pod-stats">Pod Stats</h3>

The Pod Stats dashboard provides a focused view of each pod's health, showing ready state, container restarts, current phase, memory, CPU usage, and network activity.

<h3 id="deployment-stats">Deployment Stats</h3>

Monitor deployment health and performance with detailed views of desired vs. running replicas and replica trends over time. This dashboard offers insights into pod status, including total, terminated, and waiting pods, along with per-pod CPU, memory usage, container restarts, terminations, and network activity.

<h3 id="daemonset-stats">DaemonSet Stats</h3>

Get detailed DaemonSet performance metrics, including ready and unavailable replicas, scheduling trends, per-pod CPU and memory usage, container restarts, terminations, and network activity to ensure optimal operation.

<h3 id="replicaset-stats">ReplicaSet Stats</h3>

The ReplicaSet Stats dashboard offers an overview of performance, displaying desired, running, and ready replicas. It tracks pod status, including total, terminated, and waiting pods, as well as per-pod CPU, memory usage, container restarts, terminations, and network activity for reliable operations.

<h3 id="statefulset-stats">StatefulSet Stats</h3>

Get in-depth monitoring of StatefulSet performance, displaying desired and ready replicas and tracking trends over time. It offers detailed pod information, including phase, per-pod CPU and memory usage, container restarts, and comprehensive network monitoring to ensure optimal operations.

<h3 id="cronjobjob">CronJob&Job</h3>

Monitor Kubernetes CronJob and Job, including job status, success rate, and resource usage.

<h3 id="capacity-management">Capacity Management</h3>

This dashboard provides valuable insights into resource utilization across your clusters. It monitors CPU and memory usage, identifies under or over-utilized resources, and ensures efficient operation of your Kubernetes environment. This visibility enables proactive capacity planning, prevents bottlenecks, and optimizes costs by aligning resource allocations with actual needs, enhancing application performance and stability.

<h3 id="osd-overview">OSD Dashboard Cluster Overview</h3>

Get detailed insights into your cluster's logging activity. Filter logs by cluster, namespace, pod, and container for precise analysis. It displays counts of clusters, namespaces, nodes, pods, containers, and jobs, along with trends and activity by namespace. Visualize log levels, rates, sources, and top log volumes, errors, warnings, and debug messages to identify critical events and issues in your Kubernetes environment.



[Install and view dashboards](https://app.logz.io/#/dashboard)


## Metric Alerts

<h3 id="osd-overview">OSD Dashboard Cluster Overview</h3>

* Cluster CPU Overcommit - Cluster has overcommitted cpu resource requests
* Cluster CPU usage - Your cluster cpu usage is over 95% of the capacity
* Cluster Disk Usage - Your cluster disk space usage is over 95% of the capacity
* Cluster Memory Overcommit - Cluster has overcommitted memory resource requests
* Cluster Memory Usage - Your cluster memory usage is over 95% of the capacity
* DaemonSet Replicas Misscheduled - DaemonSet replicas are misscheduled
* DaemonSet Replicas Not Scheduled - DaemonSet replicas are not scheduled
* DaemonSet Rollout - Daemonset rollout is Stuck
* DaemonSet Running Replicas - The number of scheduled replicas are below the desired number
* Deployment Generation - Your deployment generation do not match
* Deployment Replicas - The number of running replicas dropped below the desired number 
* Job & CronJob Failed Jobs - There were jobs failures
* Job Completion Duration - The job duration exceeded the average duration
* Node CPU Utilization  - Your node CPU utilization is over 95%
* Node Disk Usage - Your node disk space usage is over 95% of the limit
* Node Kubelet Capacity - Your kubelet is running at capacity
* Node Memory Usage - Your Node memory usage is over 95% of the limit
* Node Not Ready - Your Node is not ready for more than 10 minutes
* Pod Container Restarts - The number of container restarts exceeds 1 within 5 minutes
* Pod Container Waiting - Pod container waiting longer than 1 hour
* Pod CPU Usage - Your pod cpu cores usage is over 95% of the limit
* Pod Memory Usage - Your pod memory usage is over 95% of the limit
* Pod Non-Ready State - Your pod has been in a non-ready state for more than 15 minutes
* ReplicaSet Replicas - The number of running replicas dropped below the desired number
* StatefulSet Generation - Your StatefulSet generation do not match
* StatefulSet Replicas  - The number of running replicas dropped below the desired number
* StatefulSet Update - StatefulSet update has not been rolled out

[Install and view metrics alerts](https://app.logz.io/#/dashboard)


## Log Alerts

* Internal Error - The "INTERNAL_ERROR" indicates an internal error within the system or service responsible for the UAS exporter. It suggests that something went wrong during the export process, which resulted in the stream being terminated.
* Warning - "WARNING" log level logs, please refer to message to inspect
* EOF Error - This error means that the end of a file or stream has been reached and there is no more data to read. It can occur when reading from or writing to a file or stream, or when a network connection is closed unexpectedly.
* Connection Errors - The error suggests that there was a problem establishing a network connection to the target IP address (10.120.0.1) on port 443. This could be due to various reasons, such as network connectivity issues or a timeout setting.
* Monitoring Error - An error occurred while trying to export metrics to Logz.io. The error is not retryable, and data has been dropped as a result. This may indicate a problem with the connection to Logz.io, or an issue with the Logz.io service itself.

[Install and view log alerts](https://app.logz.io/#/dashboard)




