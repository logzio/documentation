---
sidebar_position: 2
title: Annotations
---


Annotations can mark events on your Metrics dashboards based on data from a logging account. For example, an annotation can indicate when a particular error log or configuration change occured based on logs written to your main logging account.



## Configure an annotation



### Pick your dashboard

Before you begin, you'll need to make sure you have permissions to edit the dashboard.

If you are using any of the pre-configured dashboards provided by Logz.io, you'll first need to select the option to make it editable. (You can also click the gear **<i class="li li-gear"></i>** in the top menu, then select **Save as > Save**).

### Add a new annotation

Go to the dashboard's settings:

* Click the gear **<i class="li li-gear"></i>** in the dashboard's top menu (upper right corner).
* Select **Annotations** > **New**.
* The annotation form will appear. Fill in the form, starting with the **General** section.
  1. Select an informative **Name**. The name should describe the significance of the event.
  2. Select a **Data source** from your logging accounts. This is the relevant OpenSearch Dashboards account you want to correlate with your metrics.

<div>
    <video width="100%" height="auto" controls autoplay loop muted>
      <source src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/grafana-videos/metrics-annotations.mp4" type="video/mp4" />
      Your browser does not support the video tag.
    </video>
</div>


### Decide which logs should trigger the annotation

You'll be using a OpenSearch Dashboards search query to select the logs you want to mark on your dashboard. They will appear as vertical markers on the dashboard's timeline to indicate when they were sent.

Type in an _OpenSearch Dashboards_ query in Lucene syntax.
It's best if you double-check your query results in [OpenSearch Dashboards](../../log-management/opensearch-dashboards/) to make sure it is specific enough.

You can use Metrics interface variables, on condition that the value of the variable actually appears in the target log. For example, the query `logtype:configuration AND pod.name:$pod` would work assuming the fields `logtype` and `pod.name` exist in the log.

### Enrich the annotation

You can make annotations more informative by specifying the fields of interest.
These should be fields that contain the crucial information from the log. Their values will be shown when you hover over the annotation in the dashboard.

* **Text** - Type in the log field that is of most interest. The field's value will be shown when hovering over the marker. In the example below, the `message` field was selected.

* **Tags** - Type in one or more log fields. Their values will appear as tags when you hover over annotations in the dashboard. In the example below, the `service` field was selected.

### Save the annotation & dashboard

When you're finished, save the annotation to see it in action.

Once you're satisfied with the annotation, save the changes to the dashboard. (A prompt will make sure you don't forget this part.)


## Example

As an example, we'll go through the steps of adding an annotation to flag every time there's a configuration change in a Kubernetes cluster.

This can make it easier to assess whether a particular configuration change caused problems in a cluster.

After selecting the relevant log account, define a query that will return only Kubernetes configuration change logs. Here's what the query might look like:

```
loglevel:Configuration AND namespace:"kube-system"
```

Whenever a log matching this query is returned, it will appear as a vertical annotation on the dashboard. The hover message for the annotation will show the log's `message` field with the `service` field tag.

Here's what the configuration will look like:

![Add Dashboard Annotation](https://dytvr9ot2sszz.cloudfront.net/logz-docs/grafana/annotation-example.png)

And here's what the annotation will actually look like in the dashboard.

![Add Dashboard Annotation](https://dytvr9ot2sszz.cloudfront.net/logz-docs/grafana/grafana-annoation-in-dashboard.png)
