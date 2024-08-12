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

Get a comprehensive view of the cluster's resource utilization, including total CPU, memory, and disk usage, along with detailed metrics for pods, nodes, deployments, and namespaces. Visualize key utilization patterns and network traffic

his dashboard displays a comprehensive view of the cluster's resource utilization, including total CPU, memory, and disk usage, along with detailed metrics for pods, nodes, deployments, and namespaces. It visualizes key utilization patterns and network traffic, ensuring efficient monitoring and management. Alerts and notifications integrate seamlessly, helping maintain a healthy and performant Kubernetes environment

Monitor CPU, memory, disk usage, and key metrics for pods, nodes, deployments, and namespaces. Includes network traffic insights and integrated alerts for efficient Kubernetes management.

* Cluster stats —-   monitoring Kubernetes cluster resources
* Node stats —-   monitoring individual Kubernetes node
* Pod Stats —--  monitoring Kubernetes pod, including container resource usage
* Deployment stats — monitoring Kubernetes deployment 
* DaemonSet stats — monitoring Kubernetes DaemonSet 
* ReplicaSet stats — monitoring Kubernetes ReplicaSet 
* StatefulSet stats —- monitoring Kubernetes StatefulSet 
* CronJob&Job — monitoring Kubernetes CronJob and Job, including job status, success rate, and resource usage.
* Capacity Management -  dashboard for k8s metrics to achieve effective observability, optimize resource utilization, and reduce costs by identifying wasted resources and misconfigurations.
* OSD Dashboard Cluster Overview - Monitor your logs you and give you the ability to see your logs activity errors end container restart and e

[Install and view dashboards](https://app.logz.io/#/dashboard)


## Metric alerts

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


## Log alerts

* Internal Error - The "INTERNAL_ERROR" indicates an internal error within the system or service responsible for the UAS exporter. It suggests that something went wrong during the export process, which resulted in the stream being terminated.
* Warning - "WARNING" log level logs, please refer to message to inspect
* EOF Error - This error means that the end of a file or stream has been reached and there is no more data to read. It can occur when reading from or writing to a file or stream, or when a network connection is closed unexpectedly.
* Connection Errors - The error suggests that there was a problem establishing a network connection to the target IP address (10.120.0.1) on port 443. This could be due to various reasons, such as network connectivity issues or a timeout setting.
* Monitoring Error - An error occurred while trying to export metrics to Logz.io. The error is not retryable, and data has been dropped as a result. This may indicate a problem with the connection to Logz.io, or an issue with the Logz.io service itself.

[Install and view log alerts](https://app.logz.io/#/dashboard)




