---
sidebar_position: 3
title: Deployment Markers
description: What are deployment markers and how you can utilize them
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logz.io, deployment, deployment markers, log analysis, observability, explore]
---

Deployment markers are indicators used to mark the exact point in time when a deployment or release occurs. These markers provide a visual reference, allowing teams to correlate deployments with system behavior changes.

## Adding Deployment Markers to Explore

To integrate your deployments with Explore, use the [API endpoint](https://api-docs.logz.io/docs/logz/deployments/) to create deployment markers.

Here's an example payload:

```
{
  "markers": [
    {
      "description": "marker description",
      "title": "marker title",
      "tag": "DEPLOYMENT",
      "timestamp": 1613311091679,
      "metadata": {
        "region": "us-east-1",
        "deployedBy": "bot"
      }
    }
  ]
}
```

### 1. Select the markers you want to view

The deployment logs sent via API appear as Deployment markers in Explore, accessible through the **Visualize** menu.

Open **Visualize > Deployment markers** to view all markers within your search time frame. You can toggle markers on or off to focus on those most relevant to your analysis.

![Select Deployment markers to enable them in Exception graphs](https://dytvr9ot2sszz.cloudfront.net/logz-docs/kibana-discover/select-deployments.png)

### 2. View the markers in the Exceptions tab

Hover over the markers in your histogram to view their title and time stamp.

:::tip
When sending Deployment marker logs, it is recommended to send the service name in the **title** field.
:::


### 3. View additional details in the marker log

Some of the fields in the deployment logs sent by API are not rendered. These include the **description** and additional **metadata** fields.

You can run the search `_exists_: __logzio_marker_title` to retrieve your marker logs. Switch to the JSON log view to look up the additional details and context available for your Deployment markers.

![Search deployment logs](https://dytvr9ot2sszz.cloudfront.net/logz-docs/kibana-discover/search-deployment-logs_aug2021.png)

