---
sidebar_position: 1
title: Getting Started with Kubernetes 360
tags: ['logs', 'metrics', 'traces', 'siem', 'os']

---

<Tags tags={frontMatter.tags} />

Kubernetes 360 is part of Logz.io's Open 360, a unified platform combining a true log analytics solution, the best Prometheus metrics monitoring, and the value of distributed tracing powered by Jaeger.

Kubernetes 360 lets R&D and engineering teams monitor and troubleshoot applications deployed in Kubernetes environments.

The platform utilizes Kubernetes' numerous advantages for R&D and dev teams, allowing you to monitor application SLOs in a simple, efficient, and actionable manner. Kubernetes 360 offers flexibility and visibility while providing service discovery, balancing load, and allowing developer autonomy and business agility.

![Main dashboard](https://dytvr9ot2sszz.cloudfront.net/logz-docs/k360/k360-jul-overview-.png)


To activate your Kubernetes 360 dashboard, connect your Kubernetes data quickly and easily through Logz.io's **[Telemetry Collector](https://app.logz.io/#/dashboard/integrations/collectors?tags=Quick%20Setup)**.

If you already have Kubernetes 360 data in your Logz.io account or prefer connecting Kubernetes manually, follow our **[Kubernetes 360 Prerequisite](/docs/user-guide/k8s-360/kubernetes-360-pre)** guide.

Once everything is up and running, you can use your Kubernetes 360 application.

<!-- ![Main dashboard](https://dytvr9ot2sszz.cloudfront.net/logz-docs/k360/k360-jul-overview-numbers.png)-->

## Kubernetes 360 overview



<!-- The **node view** includes a summary of each node's physical CPU, memory, and disk. It also has a rundown of the inner pods’ status similar to the deployments view, including how many pods are failing, whether they’re using a high CPU or memory, the number of restarts, and the log error rate.

![deployments card](https://dytvr9ot2sszz.cloudfront.net/logz-docs/k360/focus-on-nodes.png) -->

You can dive deeper into each card by clicking on it and opening the **[Quick view](#quick-view)** menu.

## Customize your application

You can change and adjust Kubernetes 360 application to match your monitoring and troubleshooting needs. To help you get started, we'll break down the different options, how you can access them, and how they can help you and your team.

![Dashboard breakdown](https://dytvr9ot2sszz.cloudfront.net/logz-docs/k360/k360-jul-overview-numbers-.png)



<h4 id="#filters">Filters</h4>


First, choose the environment you'd like to view. Environments with many users, teams, or projects use a namespace to bundle relevant clusters and nodes. This filter allows you to focus on all elements inside a specific namespace.

Next, choose whether to view the environment's clusters, nodes, or both. Each dropdown menu includes all clusters and nodes in the chosen Kubernetes account, and you can use the search bar to find and add nodes to your view easily.

<h4 id="#view">View</h4>

You can switch your view to filter by the following resources: **Node**, **Pod**, **Deployment**, **Daemonset**, **Statefulset**, or **Job**.

![switch view](https://dytvr9ot2sszz.cloudfront.net/logz-docs/k360/filter-view-jul-.png)

In addition, you can also switch between the **Map** and **List** views, according to your monitoring needs. Note that the Pod view can only be seen as a list.

When switching between views, the main cards change to represent the different resources. Each card includes several essential measurements, such as average CPU and memory usage, and a rundown of the resource’s status. The cards help you quickly identify which resources require your attention by marking failings or issues in red.

![deployments card](https://dytvr9ot2sszz.cloudfront.net/logz-docs/k360/node-view-jul-.png)

You can dive deeper into each card by clicking on it and opening the **[Quick view](#quick-view)** menu.

<h4 id="#search">Search</h4>

You can search your environment for specific elements you’d like to view. Note that the search focuses on the elements' names, not their status, cluster, namespace, etc.

<h4 id="#auto-refresh">Auto refresh</h4>

You can set your Kubernetes 360 application to auto refresh every 60 seconds, to ensure you view the most recent data. To do so, hover over the refresh button and click the auto refresh toggle. You can also click on the button to manually refresh the data. 

![autorefresh button](https://dytvr9ot2sszz.cloudfront.net/logz-docs/k360/toggle-auto-refresh.png)


<h4 id="#change-view">Change your metrics view</h4>

By default, Kubernetes 360 provides an overview of your current environment. Use the bottom menu to focus on different metrics according to your monitoring needs:

* **Status** - Understand which pods are running, failing, pending, or which pods succeeded.
* **CPU** - View CPU consumtions by percentage: 0-50%, 50%-80%, 80%-100%, or over 100%.
* **Memory** - Know how much memory each pod uses: 0-50%, 50%-80%, 80%-100%, or over 100%.
* **Restarts** - Get a numeric overview of how many restarts occurred in each pod: 0, 1-10, 11-20, or over 20 restarts.
* **Log Error Rate** - Analyze the percentage of log errors that occurred and how many pods were affected. [_How do we calculate the log error rate?_](/docs/user-guide/k8s-360/overview#calculating-log-error-rate)
* **Security risks** - Presents how many potential security risks are in each of your pods. 


## Quick view

Clicking on one of the cards or rows opens the quick view menu. This menu provides additional information about each element, allowing you to investigate and understand what’s happening inside your Kubernetes environment.

For each available view -  Deployment, Pod, Node, Dameonset, Statefulset, and Job - you can access the quick view to gain more information, such as: 

* **Cluster** - The cluster associated with the chosen view.
* **Namespace** - The unique namespace.
* **Status** - Indicates whether that condition is applicable, with possible values **True**, **False**, or **Unknown**.
* **CPU** - Amount of CPU used. If the CPU is not capped, you'll see an indicator stating **no limit**.
* **Memory** - An average calculation of how much memory is in use.
* **Uptime** - The duration of how long the chosen view has been running.
* **Security risks** - The number of potential security risks. 

And more. 

![Pod upper menu Overview](https://dytvr9ot2sszz.cloudfront.net/logz-docs/k360/pod-upper-overview-sep.png)

Each view lets you dive deeper into the data by using the links at the top of the quick view. Click on **See Metrics**, **See Traces**, or **See Logs** to navigate directly to the relevant view.

### Quick view tabs

:::note
To enrich your existing and newly sent data, use the [Telemetry Collector](https://app.logz.io/#/dashboard/integrations/collectors?tags=Quick%20Setup) to configure and send data quickly, followed by the [Easy Connect](https://docs.logz.io/user-guide/log-shipping/ezkonnect.html) platform to effectively instrument Kubernetes applications with OpenTelemetry auto-instrumentation.
:::

Each quick view includes several tabs that provide additional information you can act on. For each tab, you can change the time frame chosen by clicking on the date bar at the top.

<h3 id="#pods-tab">Pods tab</h3>

The Pods tab provides a list of all pods related to this node. The table includes each pod's status, the number of containers they’re in, and how much CPU and memory they use. Clicking on one of the pods will lead you to that pod's quick view menu.

![Node menu Overview](https://dytvr9ot2sszz.cloudfront.net/logz-docs/k360/node-quick-view-sep.png)

<h3 id="#logs-tab">Logs tab</h3>

In the Logs tab you can view the time, log level, and message for each log line. You can search for specific logs using the search bar, which supports free text and Lucene queries. 

![Pod menu Overview](https://dytvr9ot2sszz.cloudfront.net/logz-docs/k360/pod-quick-view-sep.png)

<h3 id="#metrics-tab">Metrics tab</h3>

The **Metrics** tab presents useful data in graph form. These graphs provides a view of Replicas Over Time, CPU Usage (cores) per pod, Memory Usage Per Pod, CPU Usage, Requests and Limits (Cores), Memory Usage, Requests and Limits, and Received & Transmitted Bytes.

![Stateful menu Overview](https://dytvr9ot2sszz.cloudfront.net/logz-docs/k360/metrics-quick-view.png)

<h3 id="#traces-tab">Traces tab</h3>

The **Traces** tab includes all of the spans in this deployment, including the following:

* Time
* Trace ID
* The Service related to the span
* Which Operation ran
* The Duration of the run, represented in milliseconds
* Status code indicating whether a specific HTTP request has been successfully completed

![Quick menu Overview](https://dytvr9ot2sszz.cloudfront.net/logz-docs/k360/deployment-quick-view-sep.png)


<!-- 
At the bottom of the quick view menu's **Pods** tab, you'll find a list of all pods related to this node. The table includes each pod's status, the number of containers they’re in, and how much CPU and memory they use. Clicking on one of the pods will lead you to that pod's quick view menu. 

In addition, you can browse through the following tabs:

### Deployment Logs View


**Logs** include the time, log level, and message for each log in this deployment. You can search for specific logs using the search bar, which supports free text and Lucene queries. 

### Deployment Metrics View


The **Metrics** tab presents useful data in graph form, including:

* Replicas Over Time
* CPU Usage (cores) per pod
* Memory Usage Per Pod
* CPU Usage
* Requests and Limits (Cores)
* Memory Usage
* Requests and Limits
* Received & Transmitted Bytes

### Deployment Traces View


The **Traces** tab includes all of the spans in this deployment, including the following:

* Time
* Trace ID
* The Service related to the span
* Which Operation ran
* The Duration of the run, represented in milliseconds
* Status code indicating whether a specific HTTP request has been successfully completed

For each tab, you can change the time frame chosen by clicking on the date bar at the top.
-->


<!-- 
### Deployment quick view


A **deployment** quick view includes the following fields:

* **Cluster** - The cluster that this deployment is a part of.
* **Region**- Your deployment's region.
* **Namespace** - The deployment's unique namespace.
* **Status** - An indicator of the deployment's status. It can be **True**, **False**, or **Unknown**. 
* **CPU** - Amount of CPU used by this deployment. If the CPU is not capped, you'll see an indicator stating **no limit**.
* **Memory** - An average calculation of how much memory this deployment uses.
* **Uptime** - The duration of how long this deployment has been running.
* **Security risks** - The number of potential security risks in this deployment. 

-->

<!-- * **Disk** - The amount of disk space taken up by this node. -->


<!--
### Deployment Pods View


At the bottom of the quick view menu's **Pods** tab, you'll find a list of all pods related to this node. The table includes each pod's status, the number of containers they’re in, and how much CPU and memory they use. Clicking on one of the pods will lead you to that pod's quick view menu. 

In addition, you can browse through the following tabs:

### Deployment Logs View


**Logs** include the time, log level, and message for each log in this deployment. You can search for specific logs using the search bar, which supports free text and Lucene queries. 

### Deployment Metrics View


The **Metrics** tab presents useful data in graph form, including:

* Replicas Over Time
* CPU Usage (cores) per pod
* Memory Usage Per Pod
* CPU Usage
* Requests and Limits (Cores)
* Memory Usage
* Requests and Limits
* Received & Transmitted Bytes

### Deployment Traces View


The **Traces** tab includes all of the spans in this deployment, including the following:

* Time
* Trace ID
* The Service related to the span
* Which Operation ran
* The Duration of the run, represented in milliseconds
* Status code indicating whether a specific HTTP request has been successfully completed

For each tab, you can change the time frame chosen by clicking on the date bar at the top.


### Node quick view


A node quick view menu includes the following fields: 

* **Role** - Master or worker.
* **Status** - Indicates whether that condition is applicable, with possible values **True**, **False**, or **Unknown**.
* **Cluster** - The cluster to which this node belongs.
* **Region** - The node's region.
* **Uptime** - The number of hours this node has been running.
* **CPU** - A percentile average of how much CPU has been used.
* **Memory** - An average percentage of how much memory was consumed.
* **Disk** - The amount of disk space this node takes, and how much is left.
* **Security risks** - Number of potential security risks in this node.

![Node menu Overview](https://dytvr9ot2sszz.cloudfront.net/logz-docs/k360/node-quick-view-sep.png)

At the top of the quick view menu, there are links that can take you directly to the relevant logs (**See Logs**), open Logz.io's Livetail for quick troubleshooting (**Open Livetail**), or see the relevant metrics (**See Metrics**).

### Node Pods View


At the bottom of the quick view menu's **Pods** tab, you'll find a list of all pods related to this node. The table includes each pod's status, the number of containers they’re in, and how much CPU and memory they use. Clicking on one of the pods will lead you to that pod's quick view menu. 

In addition, you can browse through the following tabs:

### Node Logs View


**Logs** include the time, log level, and message for each log in this node. You can search for specific logs using the search bar, which supports free text and Lucene queries. 

### Node Metrics View


The third tab, **Metrics**, presents useful data in graph form, including:

* CPU Utilization Over Time (%)
* Node Memory (%)
* Node CPU Absolute
* Node memory
* Node disk reads
* Node disk writes
* Network Bytes
* CPU usage per pod
* Memory usage per pod

### Node Traces View


The **Traces** tab includes all of the spans in this deployment, including the following:

* Time
* Trace ID
* The Service related to the span
* Which Operation ran
* The Duration of the run, represented in milliseconds
* Status code indicating whether a specific HTTP request has been successfully completed

For each tab, you can change the time frame chosen by clicking on the date bar at the top.


### Pod quick view


Click on a pod to access its quick view menu and gain access to this additional information:

* **Status** - Indicates whether that condition is applicable, with possible values **True**, **False**, or **Unknown**.
* **Node** - The node that this pod is a part of.
* **Workload type** - The configuration of this pod.
* **Workload name** - The name of the pod.
* **Cluster** - The cluster in which this pod resided. 
* **Containers number** - Number of containers inside the pod.
* **Namespace** - The pod's unique namespace.
* **Uptime** - The duration of how long this pod has been up and running.
* **Restarts** - The number of restarts in this pod.
* **CPU** - A percentile average of how much CPU has been used.
* **Memory** - An average percentage of how much memory was consumed.
* **Security event count** - The number of security events in this pod.
-->

<!-- * **Deployment** - The deployment related to this pod. -->
<!-- 
![Pod menu Overview](https://dytvr9ot2sszz.cloudfront.net/logz-docs/k360/pod-quick-view-sep.png)

At the top of the quick view menu, there are links that can take you directly to the relevant logs (**See Logs**), open Logz.io's Livetail for quick troubleshooting (**Open Livetail**), or see the relevant metrics (**See Metrics**).

### Pod Logs View


At the bottom of the quick view menu's **Logs** tab you can review all relevant logs with their timestamp, log level, and message for each one. You can search for specific logs using the search bar, which supports free text and Lucene queries. 

### Pod Metrics View


The **Metrics** tab presents useful data in graph form, including:

* Pod CPU
* Pod Memory
* Container status
* Container restarts
* Pod traffic bytes
* Pod traffic packets
* Pod dropped packets

### Pod Traces View


And the **Traces** tab includes all of the spans in this deployment, including the following:

* Time
* Trace ID
* The Service related to the span
* Which Operation ran
* The Duration of the run, represented in milliseconds
* Status code indicating whether a specific HTTP request has been successfully completed

For each tab, you can change the time frame chosen by clicking on the date bar at the top.

### Dameonset, Statefulset, and Job quick view

All 3 views include the following information as part of their quick view menu:

* **Cluster** - The cluster in which this element resided. 
* **Region** - This element's region.
* **Namespace** - The element's unique namespace.
* **CPU** - A percentile average of how much CPU has been used.
* **Memory** - An average percentage of how much memory was consumed.
* **Security risks** - The number of security events in this element.

![Stateful menu Overview](https://dytvr9ot2sszz.cloudfront.net/logz-docs/k360/daemon-quick-view-sep.png)

At the top of the quick view menu, there are links that can take you directly to the relevant metrics (**See Metrics**).

### Dameonset, Statefulset, and Job Pods View


At the bottom of the quick view menu's **Pods** tab, you'll find a list of all pods related to this node. The table includes each pod's status, the number of containers they’re in, and how much CPU and memory they use. Clicking on one of the pods will lead you to that pod's quick view menu. 

In addition, you can browse through the following tabs:

### Dameonset, Statefulset, and Job Logs View


**Logs** include the time, log level, and message for each log in this node. You can search for specific logs using the search bar, which supports free text and Lucene queries. 

### Dameonset, Statefulset, and Job Metrics View


The **Metrics** tab presents useful data in graph form, including:

* Nodes Available & Unavailable Over Time
* Nodes Schedule Over Time
* CPU Usage (cores) per pod
* Memory Usage per pod
* CPU Usage, Requests and Limits (Cores)
* Memory Usage, Requests and Limits
* Received & Transmitted Bytes

### Dameonset, Statefulset, and Job Traces View


The **Traces** tab includes all of the spans in this deployment, including the following:

* Time
* Trace ID
* The Service related to the span
* Which Operation ran
* The Duration of the run, represented in milliseconds
* Status code indicating whether a specific HTTP request has been successfully completed


For each tab, you can change the time frame chosen by clicking on the date bar at the top.
-->



<!-- ###### Cluster quick view

To access a cluster quick view, click the cluster's name in a deployment, node, or pod quick view menu. A cluster quick view menu includes the following:

* **Name** - The name of the cluster you're focusing on. 
* **Region** - This cluster's region.
* **Cores** - The number of cores used inside the cluster.
* **Pods** - The number of pods that are part of this cluster.
* **Nodes** - The number of nods that are part of this cluster.
* **CPU** - A percentile average of how much CPU has been used.
* **Memory** - An average percentage of how much memory was consumed.


![Cluster menu Overview](https://dytvr9ot2sszz.cloudfront.net/logz-docs/k360/deployment-to-cluster.gif)
-->

### Investigate through quick view 

<h4 id="#see-metrics">See Metrics</h4>

You can easily investigate the different issues you might encounter. 

Each quick view menu contains the **View Metrics** button, allowing you to view the relevant information in a Grafana application. This can provide a focused overview of the chosen element, allowing you to pinpoint what happened and when it started quickly.

<h4 id="#see-logs">See Logs</h4>


Node and pod views include the **See Logs** button, which opens an OpenSearch Dashboards screen with the relevant query to display the log information.

If you’ve manually set up your Kubernetes account, you might get an empty query with no results. In this case, you can view all related logs using a custom filter.

Click on **Add filter** at the top of the screen. The fields vary according to your chosen view; add `kubernetes.host` to the field to view Node related logs. To view Pod related logs, add `kubernetes.pod_name` to the field.

Next, choose the operator. For example, you can select **exists** to view all related logs.

<h4 id="#open-livetail">Open Livetail</h4>


Node and pod views include the **Open Livetail** button, which opens Logz.io's Livetail filtered with the selected Kubernetes host. Live tail gives you a live view of your logs as they come into Logz.io, allowing you to view and troubleshoot in real time.

<h4 id="#open-traces">Open Traces</h4>


The Deployment view includes the **See Traces** button, which opens Jaeger with the relevant data needed to deep dive into it. Gain a system-wide view of your distributed architecture, detect failed or high latency requests, and quickly drill into end-to-end call sequences of selected requests of intercommunicating microservices. 

## Track Deployment Data

You can enrich your Kubernetes 360 graphs by adding an indication of recent deployments, helping you determine if a deployment has increased response times for end-users, altered your application's memory/CPU footprint, or introduced any other performance-related changes.

To enable deployment tracking ability, run the [**Telemetry Collector**](https://app.logz.io/#/dashboard/integrations/collectors?tags=Quick%20Setup) on your Kubernetes clusters. You can also activate this process **manually** by installing [Logz.io Kubernetes events Helm chart](https://app.logz.io/#/dashboard/integrations/Kubernetes:~:text=user%20guide.-,Send%20your%20deploy%20events%20logs,-This%20integration%20sends). 

Once enabled, the graphs will include a deployment marker, marked by a dotted vertical line.

You can view additional deployment data by clicking on the line. This data includes the deployment time, the associated service and environment, and a quick link to view the commit in your logs.

Click **Go to commit** to access and view your own code related to this deployment, allowing you to probe deeper into the relevant data.

:::caution Important
To activate the **Go to Commit** button, go to **your app or service** and add the following annotation to the metadata of each resource's versioning you want to track: `logzio/commit_url: ""`, and the URL structure should be: "`https://github.com/<account>/<repository>/commit/<commit-hash>`". [Learn more](https://github.com/logzio/logzio-helm/tree/master/charts/logzio-k8s-events#deployment-events-versioning).
:::


![deployment menu](https://dytvr9ot2sszz.cloudfront.net/logz-docs/k360/k360-deploy.png)




<!-- ##### Locate


To re-focus your view, click the **Locate** button at the top of the quick view menu. This will scroll back to the specific deployment, node, or pod you're investigating.

![Locate button](https://dytvr9ot2sszz.cloudfront.net/logz-docs/k360/k360-locate.png) -->

<!-- ![Locate button](https://dytvr9ot2sszz.cloudfront.net/logz-docs/k360/locate-button.gif)-->

<!-- ##### Logs tab


Nodes and pods quick view menu has an additional **Logs** tab containing a table with all the logs related to the chosen node or pod. The table includes the total number of logs, the time they were ingested, the log level, and its message.

![Logs inside nodes](https://dytvr9ot2sszz.cloudfront.net/logz-docs/k360/logs-inside-nodes.png)

You can sort the table by clicking on each header: **Time**, **Log level**, or **Message**. Click on the same header again to change your view to ascending/descending. -->

## Additional information

### Calculating Log error rate

To calculate percentage error, we take the percentage of errors in the last 15 minutes and the percentage of errors in the last 2 hours:

`Errors in the last 15 minutes <= Amount of errors in the last 2 hours`

For example, if in the last 15 minutes there were 10 log errors out of 200 total logs, it means that there's a total of 5% errors:

`10/200 * 100 = 5%`

And if in the last 2 hours there were 15 log errors out of 800 total logs, the percentage of errors will be 1.8%:

`15/800 * 100 = 1.8%`

So the log error rate you'll see will be 177.7%, based on the following formula:

`(5/1.8 * 100) - 100 = 177.7%`

Additional examples: 

* Last 15 minutes = 5 error logs out of 50 total logs = 5/50 * 100 = 10%
* Last 2 hours = 6 error logs out of 800 total logs = 6/800 * 100 = 0.75%
* Error rate = (10/0.75 * 100) - 100 = 1233.3%

Or:

* Last 15 minutes = 2 error logs out of 100 total logs = 2/100 * 100 = 2%
* Last 2 hours = 2 error logs out of 800 total logs = 2/800 * 100 = 0.25%
* Error rate = (2/0.25 * 100) - 100 = 700%



## Additional resources

* [Read more](https://logz.io/blog/unified-observability-kubernetes-360/) about Logz.io's Kubernetes 360 platform.