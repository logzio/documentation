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

<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/deployment-marker-explore.png" alt="add-deployment-marker" width="500"/>

Once added, deployment markers will be displayed across your histogram. Hover over a marker to view additional details such as its title, timestamp, and description.

![View deployment markers](https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/view-deployment-markers.png)


:::tip
Include the service name in the `title` field when sending deployment marker logs for easier identification.
:::

<!--
### 3. View additional details in the marker log

Some of the fields in the deployment logs sent by API are not rendered. These include the **description** and additional **metadata** fields.

You can run the search `_exists_: __logzio_marker_title` to retrieve your marker logs. Switch to the JSON log view to look up the additional details and context available for your Deployment markers.

![Search deployment logs](https://dytvr9ot2sszz.cloudfront.net/logz-docs/kibana-discover/search-deployment-logs_aug2021.png)

-->