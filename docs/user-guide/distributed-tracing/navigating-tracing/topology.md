---
sidebar_position: 8
title: Topology Diagrams
description: Visualize your traces with topology diagrams
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logz.io, traces, tracing, topology, diagrams, observability, distributed tracing]
---


<!-- ## View Topology Diagrams   -->

The available diagram is based on the traces you search for deep dependency graph.

## Viewing a deep dependency graph
The deep dependency graph describes how the services in traces are connected based on the results of the trace search query you run. The graph lets you focus on the up and downstream hops of a service call and define the aggregation and graph density for the layout.

From the <a href="https://www.jaegertracing.io/docs/latest/features/#deep-dependency-graph" target="_blank">Jaeger deep dependency documentation <i class="fas fa-external-link-alt"></i> </a>, the deep dependency graph is...

> ...also known as “Transitive Dependency Graph”, where a chain `A -> B -> C` means that `A` has a transitive dependency  on `C`. A single graph requires a “focal” service (shown in pink) and only displays the paths passing through that service. Typically, this type of graph does not represent the full architecture of the system, unless there is a service that is connected to everything, e.g. an API gateway, and it is selected as a focal service.

Use the deep dependency graph to view a partial graph relevant to your service of interest. 
This ability is genuinely useful when it’s not possible to view that service in a system architecture graph, especially if you have hundreds of services (or many more), where hovering to find a specific service isn’t feasible. 

1. In the top right of the search results, click **Deep Dependency Graph** (next to the **Sort** dropdown).
     ![Open DDG](https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/open-ddg.png) You can set which service to focus on as origin (in pink) and expand and collapse the levels in the diagram.![Layout DDG](https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/deep_depend_graph-layout2.png)

2. Enter a service or operation in the search box to highlight it in the deep dependency graph.
![highlight DDG](https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/ddgraph_highligh.png)

<!-- 
## Viewing system architecture diagrams

The system architecture diagrams are based on all the trace data in your system, compiled over a given time frame and refreshed periodically. 

Navigate to [**System Architecture**](https://app.logz.io/#/dashboard/jaeger/dependencies) to see the connected services in your environment in a **Force Directed Graph** or in a **Directed Acyclic Graph (DAG)**.

For more information, see the <a href = "https://www.jaegertracing.io/docs/1.20/features/#system-architecture" target="_blank">Jaeger system architecture documentation. </a> 


### Viewing the Force Directed Graph

You can drag and zoom in on the image to focus on a specific service in the Force Directed Graph.

Click on one of the nodes to see service dependencies and highlight the spans that are related to that node.

![Change focus in force directed graph](https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/forced-tracing.gif) 

### Viewing the Directed Acyclic Graph (DAG)

Click on the DAG tab to switch your view.

You can drag and zoom in on the image to view the details of the cells in the graph.

Each line represents the interaction requests between the connected services. The numbers you see are the number of interaction requests between those services over the last 7 days.

To make it easier to see values in the graph, you can grab and drag the nodes to rearrange them.

![Change focus in dag](https://dytvr9ot2sszz.cloudfront.net/logz-docs/distributed-tracing/moving-traces.gif)
-->