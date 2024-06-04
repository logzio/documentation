---
sidebar_position: 5
title: Explore Your Prometheus Metrics
description: Research Prometheus data and discover metadata with Explore
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [metrics, infrastructure monitoring, PromQL, Prometheus, monitoring, dashboard, observability, logz.io]
---



Metrics Explore is where you can research the data available in your Prometheus metrics account and discover the metadata (tags, dimensions, or fields) associated with each metric from the services in your environment.

It's a bit like OpenSearch Dashboards Discover, in that it is optimized for quickly searching the data in preparation for creating dashboards.

Whether you just started sending metrics for the first time, or you want to check that your metrics arrived as expected, the Metrics Explore mode is the best way to do it. It's also great if you're a long-time user and want to examine the structure of your metrics to create a new monitoring dashboard.

To go to Metrics Explore, click the **Explore icon <i class="far fa-compass"></i>** in the left menu.

<img width="872" alt="image" src="https://github.com/sethmichaelking/documentation/assets/96846742/dd874190-60f6-4000-908a-72efa4853099">

## Exploring your metrics

To determine which metrics exist in your metrics account and then discover the associated metadata (tags, dimensions, or fields) sent by the services in your environment, use the Metrics list or an autocomplete query.

- **Metrics list:** Use the metrics dropdown to the left of the query bar to get a full picture of all of the metrics sent to your account.
The metrics are grouped by name.

  In the image below, the Kubernetes metrics start with the term `kube`.

<div>
    <video width="100%" height="auto" controls autoplay loop muted>
      <source src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/grafana-explore/p8s-xplore11-metricslist.mp4" type="video/mp4" />
      Your browser does not support the video tag.
    </video>
 </div>


- **Query autocomplete:** Use the query autocomplete option to explore the available metrics name suggestions.
  For example, if you’re monitoring Kubernetes and looking for a specific pod metric, start typing the term `pod` to see which results come up, then click the desired metric name.

<div>
    <video width="100%" height="auto" controls autoplay loop muted>
      <source src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/grafana-explore/p8s-explore-query.mp4" type="video/mp4" />
      Your browser does not support the video tag.
    </video>
</div>


:::note
Not all metrics from a specific service start with the same word. For example, the metrics grouped by the term `container` are also Kubernetes metrics.
:::

## Prometheus metrics metadata labels

Each metric includes metadata - one or more labels that are associated with the metric and which provide additional information about it. These labels are either automatically attached and sent with the metric, or can also be attached manually by the sender: It depends on the monitored service or application.

Metrics metadata labels are useful for creating meaningful visualizations and for gaining insights about the monitored data. When choosing a metric to focus on, you can see each metric’s labels (and label values) attached to it below the graph visualization.

In the image below, the metric `kube_deployment_status_replicas_available` includes the labels `deployment` and `namespace` .

![P8s metric metadata labels](https://dytvr9ot2sszz.cloudfront.net/logz-docs/grafana-explore/grafana-exp8s-metadata-labels1.png)

## Split and sync Explore screens

You can split your Explore mode screen to work faster and make quick comparisons. You can split the screen to work with two views side-by-side, whether Metrics-Metrics, Logs-Logs, or Logs-Metrics.

Splitting the screen is especially effective for checking how queries behave in different time ranges and even for different data sources (in the Logz.io world, a data source = a different metrics or logs account or subaccount).

To split the screen, click the **<i class="fas fa-columns"></i> Split** button.
If you want to sync both views so they both cover the same time range, click the **<i class="fas fa-link"></i>** button to link the views.

<div>
    <video width="100%" height="auto" controls autoplay loop muted>
      <source src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/grafana-explore/p8s-xplore-split-sync.mp4" type="video/mp4" />
      Your browser does not support the video tag.
    </video>
</div>

## Calculating Infrastructure Monitoring usage

Logz.io's Infrastructure Monitoring (Metrics) accounts usage is calculated based on the Unique Time Series (UTS).

A time series is a collection of pairs, each including a timestamp and value. Time series is uniquely identified by its metric name and a set of labels.

For example, these are all distinct time series:

`temperature{city=”NY”}`

`temperature{city=”SF”}`

`temperature{city=”SF”, unit=”Celsius”}`

`temperature`


You can view your usage metrics in your Infrastructure Monitoring dashboard. Navigate to **[Metrics](https://app.logz.io/#/dashboard/metrics) > [Explore](https://app.logz.io/#/dashboard/metrics/explore) > Metrics browser** and enter the following PromQL query: `logzio_metrics_accepted_data_points_per_minute{}`.

To easily find relevant metrics, type Logz in the metrics bar, and select the metric you want to view.

![Data Volume Dashboard ELK app](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/explore-cpu-usage.png)


## Using Data Hub to manage Metrics usage

Logz.io offers an easy and efficient way to manage and enhance your Logs and Metrics plans through [Data Hub](https://app.logz.io/#/dashboard/cost).

Data Hub offers tailored recommendations that help you improve usage and reduce costs, and you can compact and discard some of your metrics as it ages to focus on the data that matters with a few clicks.

[Learn more about managing Metrics with Data Hub](https://docs.logz.io/docs/user-guide/data-hub/data-rollups/). 
