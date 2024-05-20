---
sidebar_position: 1
title: Intro to Explore
description: Getting started with Logz.io's Explore dashboard
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logz.io, dashboard, explore, logs, metrics, traces, analytics, log analysis, observability]
slug: /user-guide/new-explore/
---

Explore lets you monitor your logs, metrics, and traces in one unified dashboard. It offers a quick and easy way to identify and debug issues quickly and effectively.

Enable the new Explore dashboard by navigating to [Settings](https://app.logz.io/#/dashboard/settings/general) and toggling the Explore option. This will add the icon to your navigation menu, and you can access the [**Explore dashboard**](https://app.logz.io/#/dashboard/explore/) with a single click.


## Explore Dashboards Overview

Explore is designed to investigate and analyze massive volumes of data quickly and easily. Use filters or the auto-complete syntax tool to find the logs you need, and drill into them using the quick view panel.

![Explore dashboard](https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/explore-apr8.png)







### 1. Smart Search / Lucene

Smart Search is the default query option, offering an intuitive experience with auto-complete functionality. It streamlines your search process and enables faster access to data.

Start typing to see all of the available fields you can use in your query. Select the operator you want to apply, and the available values will appear.

![Smart Search gif](https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/smart-search-apr8.gif)

To add a value that doesn't appear in your logs, type its name and click on the + sign.

![Smart Search add value](https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/new-value-apr8.png)

Click on the dropdown menu to switch between Smart Search and Lucene query-based search.

### 2. Field Filters

Decide which accounts you want to monitor, and easily add or remove fields to refine your search criteria. Use the search to find the specific field you’re interested in, or mark the checkbox to add and remove fields from your search and view. 

Special fields (that appear at the top of the list) cannot be filtered, but can be added to the table or added as a **field exists** filter.

### 3. Graph View

Visualize trends over time and group data based on your preferred categories. Hover over the graph for additional details about each data point.

### 4. Choose Time Frame

The default time frame in Explore is the last 15 minutes.

You can select a custom time frame by clicking on the data element and choosing what’s relevant for your overview or investigation.

### 5. Group By

The default graph view is set to group by all fields, but you can choose specific fields to focus on from the drop-down menu. 

![Smart Search group by](https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/graph-group-by-apr8.png)

### 6. Logs Table

Use the Logs Table to view and analyze logs. Access relevant logs and their details quickly, and customize the table by adding or removing columns.

Click the arrow to extand your log view. You can click on each field or value to open a dedicated menu that will let you:

* Add the field to your table
* Copy the value
* Add field to log table
* Group by field in graph
* Exclude the value from your view

![Smart Search menu](https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/field-value-menu-apr8.png)

### Quick View

Dive deeper into your logs with Quick View, designed to provide comprehensive insights at a glance. Click anywhere inside a log line to open the quick view. The detailed view provides additional info and context for each log, to help you easily identify critical information.

![Explore quick view](https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/quick-view-apr8.png)