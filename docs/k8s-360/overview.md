---
sidebar_position: 1
title: Getting Started with Kubernetes 360
---

Kubernetes 360 is part of Logz.io's Open 360, a unified platform combining a true log analytics solution, the best Prometheus metrics monitoring, and the value of distributed tracing powered by Jaeger.

Kubernetes 360 lets R&D and engineering teams monitor and troubleshoot applications deployed in Kubernetes environments.

The platform utilizes Kubernetes' numerous advantages for R&D and dev teams, allowing you to monitor application SLOs in a simple, efficient, and actionable manner. Kubernetes 360 offers flexibility and visibility while providing service discovery, balancing load, and allowing developer autonomy and business agility.

![Main dashboard](https://dytvr9ot2sszz.cloudfront.net/logz-docs/k360/k360-main.png)




#### Getting started with Kubernetes 360

To activate your Kubernetes 360 dashboard, connect your Kubernetes data quickly and easily through Logz.io's **[Telemetry Collector](https://app.logz.io/#/dashboard/send-your-data/agent/new)**.

If you already have Kubernetes 360 data in your Logz.io account or prefer connecting Kubernetes manually, follow our **[Kubernetes 360 Prerequisite](/user-guide/k360/kubernetes-360-pre.html)** guide.

Once everything is up and running, you can use your Kubernetes 360 application.

![Main dashboard](https://dytvr9ot2sszz.cloudfront.net/logz-docs/k360/k360-main.png)

### Kubernetes 360 overview




<!-- The **node view** includes a summary of each node's physical CPU, memory, and disk. It also has a rundown of the inner pods’ status similar to the deployments view, including how many pods are failing, whether they’re using a high CPU or memory, the number of restarts, and the log error rate.

![deployments card](https://dytvr9ot2sszz.cloudfront.net/logz-docs/k360/focus-on-nodes.png) -->

You can dive deeper into each card by clicking on it and opening the **[Quick view](/user-guide/k360/overview.html#quick-view)** menu.

#### Customize your application

You can change and adjust Kubernetes 360 application to match your monitoring and troubleshooting needs. To help you get started, we'll break down the different options, how you can access them, and how they can help you and your team.

![Dashboard breakdown](https://dytvr9ot2sszz.cloudfront.net/logz-docs/k360/overview-k360.png)


##### View by clusters


Choose which cluster you want to review. The dropdown menu includes all clusters in your Kubernetes account, bundled under their respective accounts.

##### Filter by namespace

Environments with many users, teams, or projects use a namespace to bundle relevant clusters and nodes. This filter allows you to focus on all elements inside a specific namespace.

##### Stop Kubernetes 360 auto refresh

Your Kubernetes 360 application is set to **auto refresh every 60 seconds** to provide you with the most recent data. Hover over the refresh button to see when the data was last updated.

Click on the button to stop the auto refresh. This allows you to investigate an issue or focus on your Kubernetes environment's current state. Click on the button again to turn auto refresh on.

![autorefresh button](https://dytvr9ot2sszz.cloudfront.net/logz-docs/k360/autorefresh.png)

##### Choose your main resource

You can switch your view to filter by the following resources: **Nodes**, **Deployments**, **Daemonset**, **Statefulset**, or **Job**.

![switch view](https://dytvr9ot2sszz.cloudfront.net/logz-docs/k360/k360-switch-view.png)

When switching between views, the main cards change to represent the different resources. Each card includes several essential measurements, such as average CPU and memory usage, and a rundown of the resource’s status. The cards help you quickly identify which resources require your attention by marking failings or issues in red.

![deployments card](https://dytvr9ot2sszz.cloudfront.net/logz-docs/k360/k360-breakdown.png)


##### Change your metrics view

By default, Kubernetes 360 provides an overview of your current environment. Use the bottom menu to focus on different metrics according to your monitoring needs:

* **Status** - Understand which pods are running, failing, pending, or which pods succeeded.
* **CPU** - View CPU consumtions by percentage: 0-50%, 50%-80%, 80%-100%, or over 100%.
* **Memory** - Know how much memory each pod uses: 0-50%, 50%-80%, 80%-100%, or over 100%.
* **Restarts** - Get a numeric overview of how many restarts occurred in each pod: 0, 1-10, 11-20, or over 20 restarts.
* **Log Error Rate** - Analyze the percentage of log errors that occurred and how many pods were affected. [_How do we calculate the log error rate?_](/user-guide/k360/overview.html#calculating-log-error-rate)
* **Security risks** - Presents how many potential security risks are in each of your pods. 



#### Understanding the quick view menu

Click on a deployment, node, or pod to open the quick view menu and get more information about each element. The menu allows you to investigate and understand what’s happening inside your Kubernetes environment by adding more helpful information.

###### Deployment quick view

A **deployment** quick view includes the following fields:

* **Name** - The name of the deployment you're focusing on.
* **Cluster** - The cluster that this deployment is a part of.
* **Region**- Your deployment's region.
* **Namespace** - The deployment's unique namespace.
* **CPU** - Amount of CPU used by this deployment. If the CPU is not capped, you'll see an indicator stating there's **no limit**.
* **Memory** - An average calculation of how much memory this deployment uses.
* **Status** - An indicator of the deployment's status. It can be **True**, **False**, or **Unknown**. 
* **Uptime** - The duration of how long this deployment has been running.
* **Security risks** - How many potential security risks are in this deployment. 

<!-- * **Disk** - The amount of disk space taken up by this node. -->


At the bottom of the quick view menu you can view the pods related to this deployment, see their status, the number of containers they’re in, and how much CPU and memory they’re using.

![Quick menu Overview](https://dytvr9ot2sszz.cloudfront.net/logz-docs/k360/k360-quick-view.png)

###### Node quick view

A node quick view menu includes the following fields: 

* **Name** - The name of the node you're focusing on.
* **Role** - Master or worker.
* **Status** - Indicates whether that condition is applicable, with possible values **True**, **False**, or **Unknown**.
* **Cluster** - The cluster to which this node belongs.
* **Region** - The node's region.
* **Uptime** - The number of hours this node has been running.
* **CPU** - A percentile average of how much CPU has been used.
* **Memory** - An average percentage of how much memory was consumed.
* **Disk** - The amount of disk space this node takes, and how much is left.
* **Security risks** - Number of potential security risks in this node.

At the top of the quick view menu, there are links that can take you directly to the relevant logs (See Logs), open Logz.io's Livetail for quick troubleshooting, or see the relevant metrics (See Metrics).

You can also view the relevant logs by clicking on the **Logs** tab, which presents the time, log level, and warning for each log inside the node. Click on the **Security** tab to see how many risks are inside the node, where they're located and what's their severity level.

At the bottom of the quick view menu's **Overview** tab you'll find a list of all pods related to this node. The list indicates each pod’s status, the number of containers they’re in, and how much CPU and memory they use.

![Node menu Overview](https://dytvr9ot2sszz.cloudfront.net/logz-docs/k360/k360-node-quick-view.png)

###### Pod quick view

Click on a pod to access its quick view menu and gain access to this additional information:

* **Name** - The name of the pod you're focusing on. 
* **Status** - Indicates whether that condition is applicable, with possible values **True**, **False**, or **Unknown**.
* **Node** - The node that this pod is a part of.
* **Workload name** - The name of the pod.
* **Workload type** - The configuration of this pod.
* **Cluster** - The cluster in which this pod resided. 
* **Containers number** - Number of containers inside the pod.
* **Region** - This pod's region.
* **Namespace** - The pod's unique namespace.
* **Uptime** - The duration of how long this pod has been up and running. 
* **Restarts** - The number of restarts in this pod.
* **CPU** - A percentile average of how much CPU has been used.
* **Memory** - An average percentage of how much memory was consumed.
* **Security event count** - The number of security events in this pod.

<!-- * **Deployment** - The deployment related to this pod. -->


You can view the relevant logs by clicking on the **Logs** tab, which presents the time, log level, and warning for each log inside the pod. Click on the **Security** tab to see how many risks are inside the pod, where they're located and what's their severity level.

At the top of the quick view menu you have links that can take you directly to the relevant logs (See Logs), open Logz.io's Livetail for quick troubleshooting, or see the relevant metrics (See Metrics).

![Pod menu Overview](https://dytvr9ot2sszz.cloudfront.net/logz-docs/k360/k360-pod-quick-view.png)


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

#### Investigate through quick view 

##### See Metrics

Whether you’re viewing a deployment, node, or pod, you can easily investigate the different issues you might encounter. 

Each quick view menu contains the **View Metrics** button, allowing you to view the relevant information in a Grafana application. This can provide a focused overview of the chosen element, allowing you to pinpoint what happened and when it started quickly.

##### See Logs

Node and pod views include the **See Logs** button, which opens an OpenSearch Dashboard screen with the relevant query to display the log information.

If you’ve manually set up your Kubernetes account, you might get an empty query with no results. In this case, you can view all related logs using a custom filter.

Click on **Add filter** at the top of the screen. The fields vary according to your chosen view; add `kubernetes.host` to the field to view Node related logs. To view Pod related logs, add `kubernetes.pod_name` to the field.

Next, choose the operator. For example, you can select **exists** to view all related logs.

##### Open Livetail

Node and pod views include the **Open Livetail** button, which opens Logz.io's Livetail filtered with the selected Kubernetes host. Live tail gives you a live view of your logs as they come into Logz.io, allowing you to view and troubleshoot in real time.


##### Locate

To re-focus your view, click the **Locate** button at the top of the quick view menu. This will scroll back to the specific deployment, node, or pod you're investigating.

![Locate button](https://dytvr9ot2sszz.cloudfront.net/logz-docs/k360/locate-button.gif)

<!-- ##### Logs tab

Nodes and pods quick view menu has an additional **Logs** tab containing a table with all the logs related to the chosen node or pod. The table includes the total number of logs, the time they were ingested, the log level, and its message.

![Logs inside nodes](https://dytvr9ot2sszz.cloudfront.net/logz-docs/k360/logs-inside-nodes.png)

You can sort the table by clicking on each header: **Time**, **Log level**, or **Message**. Click on the same header again to change your view to ascending/descending. -->

#### Calculating Log error rate

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



###### Additional resources

* [Read more](https://logz.io/blog/unified-observability-kubernetes-360/) about Logz.io's Kubernetes 360 platform.

<!-- #### Kubernetes 360 overview

Kubernetes 360 application provides a quick overview of your current deployments and nodes.

You can switch your view to focus on **Deployments** or **Nodes** using the buttons at the top right.

The **deployments view** includes cards representing the different deployments, a quick overview of the deployment's average CPU and memory, and a rundown of the pods' status. You can quickly identify whether pods are failing, if they're consuming a high amount of CPU, memory, if they had multiple restarts, and the number of log error rates inside. The pods' colors indicate their current status, when red dots indicate an issue with this pod.

![deployments card](https://dytvr9ot2sszz.cloudfront.net/logz-docs/k360/focus-on-deployment.png)


The **node view** includes a summary of each node's physical CPU, memory, and disk. It also has a rundown of the inner pods’ status similar to the deployments view, including how many pods are failing, whether they’re using a high CPU or memory, the number of restarts, and the log error rate.

![deployments card](https://dytvr9ot2sszz.cloudfront.net/logz-docs/k360/focus-on-nodes.png)


Click on the cards or the elements inside them to get more information through the **[Quick view](/user-guide/k360/overview.html#quick-view)** menu.

#### Customize your application

You can change and adjust Kubernetes 360 application to match your monitoring and troubleshooting needs. To help you get started, we'll break down the different options, how you can access them, and how they can help you and your team.

![Dashboard breakdown](https://dytvr9ot2sszz.cloudfront.net/logz-docs/k360/overview-k360.png)


##### Clusters

Choose which cluster you want to review. The dropdown menu includes all clusters in your Kubernetes account, bundled under their respective accounts.

##### Namespace

Environments with many users, teams, or projects use a namespace to bundle relevant clusters and nodes. This filter allows you to focus on all elements inside a specific namespace.

##### Auto refresh

Your Kubernetes 360 application is set to **auto refresh every 60 seconds** to provide you with the most recent data. Hover over the refresh button to see when the data was last updated.

Click on the button to stop the auto refresh. This allows you to investigate an issue or focus on your Kubernetes environment's current state. Click on the button again to turn auto refresh on.

![autorefresh button](https://dytvr9ot2sszz.cloudfront.net/logz-docs/k360/autorefresh.png)

##### Change your metrics view

By default, Kubernetes 360 provides an overview of your current environment. Use the bottom menu to focus on different metrics according to your monitoring needs:

* **Status** - Understand which pods are running, failing, pending, or which pods succeeded.
* **CPU** - View CPU consumtions by percentage: 0-50%, 50%-80%, 80%-100%, or over 100%.
* **Memory** - Know how much memory each pod uses: 0-50%, 50%-80%, 80%-100%, or over 100%.
* **Restarts** - Get a numeric overview of how many restarts occurred in each pod: 0, 1-10, 11-20, or over 20 restarts.
* **Log Error Rate** - Analyze the percentage of log errors that occurred and how many pods were affected. [_How do we calculate the log error rate?_](/user-guide/k360/overview.html#calculating-log-error-rate)



#### Quick view

Click on a deployment, node, or pod to open the quick view menu and get more information about each element. The menu allows you to investigate and understand what’s happening inside your Kubernetes environment by adding more helpful information.

###### Deployment quick view

A **deployment** quick view includes the following fields:

* **Name** - The name of the deployment you're focusing on.
* **Status** - An indicator of the deployment's status. It can be **True**, **False**, or **Unknown**. 
* **Cluster** - The cluster that this deployment is a part of.
* **Region**- Your deployment's region.
* **Namespace** - The deployment's unique namespace.
* **Uptime** - The duration of how long this deployment has been running.
* **CPU** - Amount of CPU used by this deployment. If the CPU is not capped, you'll see an indicator stating there's **no limit**.
* **Memory** - An average calculation of how much memory this deployment uses.
* **Disk** - The amount of disk space taken up by this node.

The deployment quick view menu includes the related pods, and you can see their status, the number of containers they’re in, and how much CPU and memory they’re using.

![Quick menu Overview](https://dytvr9ot2sszz.cloudfront.net/logz-docs/k360/quick-view-open-menu.png)

###### Node quick view

A node quick view menu includes the following fields: 

* **Name** - The name of the node you're focusing on.
* **Role** - Master or worker.
* **Status** - Indicates whether that condition is applicable, with possible values **True**, **False**, or **Unknown**.
* **Cluster** - The cluster to which this node belongs.
* **Region** - The node's region.
* **Uptime** - The number of hours this node has been running.
* **CPU** - A percentile average of how much CPU has been used.
* **Memory** - An average percentage of how much memory was consumed.
* **Disk** - The amount of disk space taken up by this node, and how much is left.

The node quick view menu also includes a list of the pods related to it. The list indicates each pod’s status, the number of containers they’re in, and how much CPU and memory they use.

![Node menu Overview](https://dytvr9ot2sszz.cloudfront.net/logz-docs/k360/node-quick-view-menu.png)

###### Pod quick view

Click on a pod to access its quick view menu and gain access to this additional information:

* **Name** - The name of the pod you're focusing on. 
* **Status** - Indicates whether that condition is applicable, with possible values **True**, **False**, or **Unknown**.
* **Node** - The node that this pod is a part of.
* **Deployment** - The deployment related to this pod.
* **Cluster** - The cluster in which this pod resided. 
* **Containers number** - Number of containers inside the pod.
* **Region** - This pod's region.
* **Namespace** - The pod's unique namespace.
* **Uptime** - The duration of how long this pod has been up and running. 
* **Restarts** - The number of restarts in this pod.
* **CPU** - A percentile average of how much CPU has been used.
* **Memory** - An average percentage of how much memory was consumed.

![Pod menu Overview](https://dytvr9ot2sszz.cloudfront.net/logz-docs/k360/pod-quick-view-menu.png) -->


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

<!-- #### Investigate through quick view 

##### See Metrics

Whether you’re viewing a deployment, node, or pod, you can easily investigate the different issues you might encounter. 

Each quick view menu contains the **View Metrics** button, allowing you to view the relevant information in a Grafana application. This can provide a focused overview of the chosen element, allowing you to pinpoint what happened and when it started quickly.
##### See Logs

Node and pod views include the **See Logs** button, which opens an OpenSearch Dashboard screen with the relevant query to display the log information.

If you've set up your Kubernetes account manually, you might get an empty query with no results. In this case, you can use a custom filter to view all related logs.

Click on **Add filter** at the top of the screen. The fields vary according to your chosen view; add `kubernetes.host` to the field to view Node related logs. To view Pod related logs, add `kubernetes.pod_name` to the field.

Next, choose the operator. For example, you can select **exists** to view all of the related logs.

##### Locate

To re-focus your view, click on the **Locate** button at the top of the quick view menu. This will scroll back to the specific deployment, node, or pod you're investigating.

![Locate button](https://dytvr9ot2sszz.cloudfront.net/logz-docs/k360/locate-button.gif)

##### Logs tab

Nodes and pods quick view menu has an additional **Logs** tab that contains a table with all of the logs related to the chosen node or pod. The table includes the total number of logs, the time they were ingested, the log level, and its message.

![Logs inside nodes](https://dytvr9ot2sszz.cloudfront.net/logz-docs/k360/logs-inside-nodes.png)

You can sort the table by clicking on each header: **Time**, **Log level**, or **Message**. Click on the same header again to change your view to ascending/descending.

#### Additional information

###### Calculating Log error rate

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



###### Additional resources

* [Read more](https://logz.io/blog/unified-observability-kubernetes-360/) about Logz.io's Kubernetes 360 platform. -->