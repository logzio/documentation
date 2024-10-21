---
sidebar_position: 1
title: Intro to Explore
description: Getting started with Logz.io's Explore dashboard
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logz.io, dashboard, explore, logs, metrics, traces, analytics, log analysis, observability]
slug: /user-guide/new-explore/
---

Explore provides a unified dashboard for monitoring your data, offering a quick and efficient way to identify and debug issues. Designed for investigating and analyzing large data volumes, Explore allows you to use filters, queries, and searches to pinpoint and delve into problems effortlessly.

<!-- ![Explore dashboard](https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/explore-aug21.png)-->

<iframe
  src="https://guide.logz.io/cm0kz9d9i000403l0665xdmng"
  style={{ border: 'none', width: '100%', height: '900px' }}
  allow="fullscreen"
  id="navattic-embed"
/>


### Simple / Lucene

Click on the dropdown menu to switch between Simple and Lucene query-based search:

* **Simple**: An intuitive search with auto-complete functionality. It streamlines your search process and enables faster access to data.

Build your query by selecting fields, parameters, and conditions. To add a value that doesn't appear in your logs, type its name and click on the + sign. You can also add free text to your search, converting it into a Lucene query.

<!-- ![Smart Search gif](https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/simple-search-aug6.gif)-->

* **Lucene**: Use Lucene query language for log searches. You can search for free text by typing the text string you want to find; for example, `error` will return all words containing this string, and using quotation marks, `"error"`, will return only the specific word you're searching for.

<!-- ![Lucene Search gif](https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/advanced-search-aug6.gif)-->

![Choose Search Method](https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/choose-search-aug21.png)


### Filters

Use the filter pane on the right to refine and narrow your search results.

Start by selecting the relevant account, then click on the field you want to filter. The available fields are based on the visible logs in the table. You can add fields to your favorite by clicking the **star** icon, allowing quicker access in the future.

Open a field to explore its values—you’ll see the top values based on a sample of the logs. The percentages following each value indicate how frequently that value appears within the field.

Field values are dynamically fetched, taking into account the selected timeframe and accounts. Values are re-fetched whenever the field filter is open and the query changes. Once you select and add one or more values to your view, it'll move to the top of the list for easy access and management.


#### Editing Filters

* **Simple Search:**

  Click the in-line filter, choose Edit, and modify the value as needed. Click Apply to save your changes.

  <img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/simple-edit-filter-oct14.png" alt="simple-filter" width="700"/>


* **Lucene Search:**

  Click the filter to open the edit screen. You can modify the field, value, and condition based on your filtering needs. Click **Save** when done.

  <img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/explore-lucene-oct21.png" alt="lucene-filter" width="700"/>


At the top of the list, you’ll find special fields. These fields can’t be filtered but can be added to the table or used as a **field exists** filter.


<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/explore-filter-oct21.png" alt="explore-filter" width="700"/>

### Graph View

Visualize trends over time and group data based on your investigations. Hover over the graph to see additional details about each data point, and click and drag to focus on specific time frames or data points.

You can enlarge or reduce the size of the graph by clicking the arrow button at the top right.


<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/explore-graph-oct21.png" alt="graph-view" width="700"/>


### Exceptions

Logz.io Exceptions automatically identifies and highlights exceptions in Explore.

You can see the number of exceptions detected for every query you run. Click the button to open the Exception quick view menu for a detailed view of the exceptions found.

Learn more about [Exceptions](https://docs.logz.io/docs/user-guide/explore/exceptions).

### Choose Time Frame

The default time frame in Explore is the last 15 minutes.

To select a custom time frame, click the time element and choose the period relevant to your overview or investigation.

### AI Agent

Click the [**AI Agent**](/docs/user-guide/observability/assistantiq/) button to activate an AI-powered, chat-based interface that lets you engage in a dynamic conversation with your data. Use one of the pre-configured prompts or type your own question to get real-time insights about your metrics, anomalies, trends, and the overall health of your environment.

![AI Agent](https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/ai-agent-oct21.gif)


### Group By

The default graph view is set to group by all fields, and you can choose specific fields to focus on from the dropdown menu. 

<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/explore-grouby-oct21.png" alt="smart-search-groupby" width="700"/>



### Table Density

Click the 1L button to change the table view. Selecting **1 Line** provides a compact view, **2 Lines** displays two lines from the logs, and **Expanded** offers a full log view, presenting all relevant data for easier viewing.


<!-- <img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/expand-table-aug6.gif" alt="expand-view" width="700"/>-->

### Create Alert, Copy Link, Export CSV, Turn UTC On

The ⋮ menu offers additional options for Explore, including:

* **Create Alert**: Opens the configure alert page with the current values and filters already added to the configuration
* **Copy Link**: Generates a URL with your current view, which you can share with team members. You need to be logged in to Logz.io to view it
* **Export CSV**: Exports up to 50,000 logs to a CSV file, including the timestamp and log message
* **Turn UTC On**: You can view your data in either UTC or your browser’s local time zone. For clarity, the time column in your log table will display the active time zone.

<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/explore-menu-oct21.png" alt="side-menu" width="700"/>

### Logs Table

Use the Logs Table to view and analyze logs. Quickly access relevant logs and their details, customizing the table by adding or removing columns.

Expand each log to view additional details, see the log in JSON format, and add columns to the table. Filter values in or out of your view as needed. Use the AI Agent on fields or values to gain more information about them. 

Once you expand a log, you can use the top right menu to get more context—view surrounding logs, copy the log URL, view it as a single log, or copy the log's JSON.

<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/explore-logs-table-oct21.png" alt="logs-table" width="700"/>

