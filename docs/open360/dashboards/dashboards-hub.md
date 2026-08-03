---
sidebar_position: 3
title: Dashboards Hub
description: Search, filter, and access all your dashboards in one place.
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logz.io, dashboard, dashboards, hub, grafana, visualize, visualizations]
---

The Dashboards Hub is your central space for managing and accessing all dashboards in one place. It consolidates dashboards from different telemetry sources, such as logs (OpenSearch Dashboards) and metrics (Grafana), into a single, convenient view, making it easy to find and open the dashboards you need.

Access the [Dashboards Hub](https://app.logz.io/#/dashboard/dashboards-hub) from the Home Dashboard screen under Dashboards.

![dashboards hub](https://dytvr9ot2sszz.cloudfront.net/logz-docs/dashboards/dashboards-hub-jan7.png)

## Using the Dashboards Hub

The Dashboards Hub simplifies dashboard management by providing a fast and organized way to search, view, and access dashboards across your account.

* Search & Filter – Use the search bar or tags to quickly find dashboards. Start typing to filter results, or click tags to refine your view. Click a dashboard to open it in a new tab.
* Favorites – Pin frequently used dashboards to keep them at the top for instant access.

### Tags

Dashboards carry free-form tags. Tags are the difference between a hub you search and a hub you browse — once a few dozen dashboards exist, a consistent tag per team or service is worth more than any naming convention.

### Folders

Dashboards live in folders, and the hub can be scoped to a single folder so you see only its contents. Folders can be created, renamed and deleted from the hub, and navigating by folder name is often faster than searching when you know roughly where something lives.

A few names are reserved by the system and can't be used, and a folder name can't be empty.

### Import a dashboard

The hub is also where you bring a dashboard in from elsewhere, including Grafana and OpenSearch Dashboards definitions. See [Import Dashboards](/docs/open360/dashboards/import-dashboards/).

### Sharing and visibility

Row actions include sharing, which is also how a dashboard is made private. See [Private Dashboards](/docs/open360/dashboards/private-dashboards/).

## Create a new Dashboard

You can create a dashboard from the Dashboards Hub.

Click **+ New Dashboard**, then choose your telemetry source: logs or metrics. 

You'll be redirected to the appropriate creation page: **OpenSearch Dashboards** for log visualizations or **Grafana** for metrics.