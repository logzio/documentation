---
sidebar_position: 1
title: Intro to Explore
description: Getting started with Logz.io's Explore dashboard
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logz.io, dashboard, explore, logs, metrics, traces, analytics, log analysis, observability]
slug: /user-guide/new-explore/
---

Explore lets you monitor your logs, metrics, and traces in one unified dashboard. It offers a quick and easy way to identify and debug issues quickly and effectively.

## Explore Dashboards Overview

Explore is designed to investigate and analyze massive volumes of data quickly and easily. Use filters or the auto-complete syntax tool to find the needed logs and drill into them using the quick view panel.

![Explore dashboard](https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/explore-dashboard-jul22.png)


### 1. Simple Search / Advanced (Lucene)

Simple Search is the default query option, offering an intuitive experience with auto-complete functionality. It streamlines your search process and enables faster access to data.

Start typing to see all of the available fields you can use in your query. Select the operator you want to apply, and the available values will appear.

![Smart Search gif](https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/search-bar-jul22.gif)

To add a value that doesn't appear in your logs, type its name and click on the + sign.

<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/new-value-apr8.png" alt="add-value" width="700"/>

Click on the dropdown menu to switch between Simple Search and Advanced Search, a Lucene query-based search.

### 2. Filters


Filters make it easy to refine and narrow your search. First, select the accounts you want to filter. Then, click on a field to see its available parameters. Choose the values you want to include in your view, or uncheck them to remove them. You can use the search bar to quickly find specific fields.

Special fields are located at the top of the list. These fields cannot be filtered but can be added to the table or used as a **field exists** filter.

Additionally, you can pin up to three custom fields to the top of the list by hovering over them and clicking the star icon.

<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/filters-jul22.png" alt="explore-fields" width="700"/>

### 3. Graph View

Visualize trends over time and group data based on your preferred categories. Hover over the graph for additional details about each data point.

Use the arrow button at the top right of the chart to minimize or expand the graph view.


<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/graph-view-jul22.png" alt="graph-view" width="700"/>


### 4. Choose Time Frame

The default time frame in Explore is the last 15 minutes.

You can select a custom time frame by clicking the data element and choosing what’s relevant for your overview or investigation.


### 5. Observability IQ Assistant

Click the ✨ icon to activate Observability IQ Assistant, an AI-powered, chat-based interface that lets you engage in a dynamic conversation with your data. Use one of the pre-configured prompts or type your own question to get real-time insights about your metrics, anomalies, trends, and the overall health of your environment.

![Observability IQ Assistant](https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/iq-jul22.gif)


### 6. Group By

The default graph view is set to group by all fields, but you can choose specific fields to focus on from the dropdown menu. 

![Smart Search group by](https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/groupby-may21.png)



### 7. Table Density

Click the 1L button to change the table view. Selecting **1 Line** provides a compact view, **2 Lines** displays two lines from the logs, and **Expanded** offers a full log view, presenting all relevant data for easier viewing.

![Expand view](https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/expand-table-may21.png)

### 8. Create Alert, Copy Link, Export CSV

The ⋮ menu offers additional options for Explore, including:

* **Create Alert**: Opens the configure alert page with the current values and filters already added to the configuration
* **Copy Link**: Generates a URL with your current view, which you can share with team members. You need to be logged in to Logz.io to view it
* **Export CSV**: Exports up to 50,000 logs to a CSV file, including the timestamp and log message

![side menu](side-menu-jul22.png)

### 9. Logs Table

Use the Logs Table to view and analyze logs. Access relevant logs and their details quickly, and customize the table by adding or removing columns.

You can expand each log line to view additional details, and clicking on a field or value will open a dedicated menu that will let you:

* Add the field to your table
* Copy the value
* Add field to log table
* Group by field in graph
* Exclude the value from your view
* Open Observability IQ to learn more about the chosen field or value

![Smart Search menu](https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/menu-jul22.png)

### Quick View


Dive deeper into your logs with Quick View, designed to provide comprehensive insights at a glance. Click the eye icon or anywhere inside a log line to open the detailed view, which offers additional information and context for each log to help you easily identify critical details. You can switch between the log table and JSON view depending on your preferences.

![Explore quick view](https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/quick-view-may21.png)