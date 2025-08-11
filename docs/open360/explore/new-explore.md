---
sidebar_position: 1
title: Intro to Explore
description: Getting started with Logz.io's Explore dashboard
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logz.io, dashboard, explore, logs, metrics, traces, analytics, log analysis, observability]
---

Explore provides a unified dashboard for monitoring your data, offering a quick and efficient way to identify and debug issues. Designed for investigating and analyzing large data volumes, Explore allows you to use filters, queries, and searches to pinpoint and delve into problems effortlessly.

<!-- ![Explore dashboard](https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/explore-aug21.png)-->

### Query and search

Explore uses an enhanced **Lucene** query language for log searches, featuring autocomplete suggestions and syntax highlighting for faster, more accurate queries. Start typing to view available fields and operators. For example, you can search for logs where `logSize` exceeds a certain value or find messages containing specific words.

![Lucene search](https://dytvr9ot2sszz.cloudfront.net/logz-docs/open360/explore/360-explore-main.png)

Explore also offers **Simple** Search, allowing you to build queries by selecting fields, parameters, and conditions. If a value isn’t listed, type its name and click the + button to add it. Free-text searches are automatically converted into Lucene queries.


### Filters

The filter pane helps refine and narrow search results.

* Account Selection: Choose the relevant account before filtering.
* Available Fields: Display fields from currently visible logs.
* Other Fields: Show fields stored in your database but not currently visible in logs.
* Favorites: Click the ⭐ icon to save frequently used fields for quick access.
* Special Fields: These cannot be filtered but can be added to the table or used as **field exists** filters.


<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/open360/explore/360-explore-filter.png" alt="explore-filter" width="700"/>


Click a field to explore its values, which are dynamically fetched based on the selected timeframe and account. A percentage indicator shows how often a value appears in the logs. Once selected, field values move to the top of the list for easy management.


#### Editing filters

* **Lucene Search:**

  Click the filter to modify the field, value, or condition, then click **Save**.

  <img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/filter-lucene-feb17.png" alt="lucene-filter" width="700"/>

* **Simple Search:**

  Click the in-line filter, choose Edit, modify the value, then click Apply.

  <img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/simple-filter-feb17.png" alt="simple-filter" width="700"/>




### Graph View

Visualize trends over time and group data for deeper insights.

Hover over the graph to see additional details about each data point. Click and drag to zoom in on specific timeframes. Resize the graph using the arrow button in the top-right corner.


<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/explore-graph-oct21.png" alt="graph-view" width="700"/>


### Exceptions

Logz.io Exceptions automatically detects and highlights errors in Explore.

The exception count is displayed for every query. Click the **Exceptions** button to open the Exception Quick View for a detailed breakdown.

Learn more about [Exceptions](https://docs.logz.io/docs/user-guide/explore/exceptions).

<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/open360/explore/360-explore-exceptions.png" alt="exceptions" width="700"/>


### Choose Timeframe

The default timeframe is the last 15 minutes.
Click the time selector to choose a custom range.

<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/timeframe-feb17.png" alt="time-frame" width="700"/>

### AI Agent


Click [**AI Agent**](/docs/user-guide/observability/assistantiq/) to activate an AI-powered, chat-based interface that lets you engage in a dynamic conversation with your data. Use one of the pre-configured prompts or type your own question to get real-time insights about your metrics, anomalies, trends, and the overall health of your environment.

![AI Agent](https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/ai-agent-feb17.gif)


### Visualize

The default graph view groups all fields. Customize the visualization by:

* Grouping by specific fields.
* Comparing different time frames.
* Adjusting the time interval or Y-axis scale.
* Adding [Deployment markers](https://docs.logz.io/docs/user-guide/explore/deployment-markers/).

:::note
When using Group by, the graph displays **up to 10 values**. Any additional values are grouped under **Other**.
Entries with empty or undefined values for the selected field will appear under **Missing**.
:::

<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/open360/explore/360-explore-visualize.png" alt="visualize" width="700"/>

### Table Density

Adjust the table view using the 1L button:

* 1 Line → Compact view.
* 2 Lines → Displays two log lines.
* Expanded → Shows full log details.


<!-- <img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/expand-table-aug6.gif" alt="expand-view" width="700"/>-->

### Create Alert, Copy Link, Export CSV, Turn UTC On

The ⋮ menu offers additional options for Explore, including:

* **Add to Dashboard**: Quickly add the current view to one of your existing dashboards. [Learn more about Logz.io Dashboards](https://docs.logz.io/docs/open360/dashboards/logzio-dashboards/).
* **Create Alert**: Opens an alert configuration with your current filters applied.
* **Copy Link**: Generates a URL with your current view, which you can share with team members. You need to be logged in to Logz.io to view it.
* **Export CSV**: Exports up to 50,000 logs to a CSV file, including the timestamp and log message.
* **Turn UTC On**: You can view your data in either UTC or your browser’s local time zone. For clarity, the time column in your log table will display the active time zone.

<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/open360/explore/360-explore-menu.png" alt="side-menu" width="700"/>




<!-- ### Logs Table

Use the Logs Table to view and analyze logs. Quickly access relevant logs and their details, customizing the table by adding or removing columns.

Expand each log to view additional details, see the log in JSON format, and add columns to the table. Filter values in or out of your view as needed. Use the AI Agent on fields or values to gain more information about them. 

Once you expand a log, you can use the top right menu to get more context—view surrounding logs, copy the log URL, view it as a single log, or copy the log's JSON.

<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/explore-logs-table-oct21.png" alt="logs-table" width="700"/>

-->