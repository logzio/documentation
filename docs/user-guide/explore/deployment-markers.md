---
sidebar_position: 5
title: Deployment Markers
description: What are deployment markers and how you can utilize them
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logz.io, deployment, deployment markers, log analysis, observability, explore]
---

Deployment markers are indicators used to mark the exact point in time when a deployment or release occurs. These markers provide a visual reference, allowing teams to correlate deployments with system behavior changes.

## Adding deployment markers to Explore

To integrate deployments markers with Explore, use the [API endpoint](https://api-docs.logz.io/docs/logz/deployments/) to create markers.

Below is an example payload:

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

### Viewing deployment markers

Deployment logs sent via the API will appear as deployment markers in Explore. You can find them in the **Visualize** menu.

Open **Visualize > Deployment markers** to view all markers within your selected time frame. Toggle markers on or off to focus on the most relevant ones for your analysis.

<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/visualize-deployment-jan7.png" alt="add-deployment-marker" width="500"/>

Once added, deployment markers will be displayed across your histogram. Hover over a marker to view additional details such as its title, timestamp, and description.

![View deployment markers](https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/view-deployment-markers.png)


:::tip
Include the service name in the `title` field when sending deployment marker logs for easier identification.
:::

### Viewing additional details in the marker logs

Certain fields in deployment logs sent via the API, such as additional metadata fields, are not displayed in the standard view.

To retrieve marker logs, run the query `_exists_: __logzio_marker_title`. Switch to the JSON log view to access the additional details and context available for your deployment markers.

![Search deployment logs](https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/deployment-json-view.png)