---
sidebar_position: 3
title: Deployment Markers
description: What are deployment markers and how you can utilize them
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logz.io, deployment, deployment markers, log analysis, observability]
---

## Adding Deployment markers to Exception graphs

You can send deployment logs by API to automatically correlate exceptions with service deployments directly in your Logz.io Exceptions tab.


![Exceptions count](https://dytvr9ot2sszz.cloudfront.net/logz-docs/kibana-discover/deployments.png)

## Send deployment logs by API

Use the [API endpoint](https://api-docs.logz.io/docs/logz/deployments/) to create **Deployment markers**.

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

The deployment logs you sent by API in the previous step appear as Deployment markers in your Logz.io Exception graphs. All Deployment markers are selected by default.

Open the Deployments menu to view all markers that appear in your search time frame. You can select/unselect markers to focus on the ones of interest to you.

![Select Deployment markers to enable them in Exception graphs](https://dytvr9ot2sszz.cloudfront.net/logz-docs/kibana-discover/select-deployments.png)



### 2. View the markers in the Exceptions tab

Hover over the markers in your Exception graphs to view their title and time stamp.

:::tip
When sending Deployment marker logs, it is recommended to send the service name in the **title** field.
:::


### 3. View additional details in the marker log

Some of the fields in the deployment logs sent by API are not rendered in the Exceptions tab view. These include the **description** and additional **metadata** fields.

You can run the search `_exists_: __logzio_marker_title` to retrieve your marker logs. Switch to the JSON log view to look up the additional details and context available for your Deployment markers.

![Search deployment logs](https://dytvr9ot2sszz.cloudfront.net/logz-docs/kibana-discover/search-deployment-logs_aug2021.png)

