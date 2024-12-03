---
sidebar_position: 4
title: How to Quickly Create Alerts
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: How to quickly create alerts in Logz.io
keywords: [alerts, logz.io alerts, opendashboards alerts]
---


Sometimes, you may want to take shortcuts when creating an alert. You have several options for shortening the process:

### Create an alert from Explore

You can easily turn your current view or query in [**Explore**](https://app.logz.io/#/dashboard/explore) into an alert. 

Once you've identified what you want to monitor, click the **⋮** menu and select **Create Alert**. 

The filters will be displayed below the text box if your query is built via Simple Search. Lucene queries will appear inside the box.

<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/alerts/simple-lucene-alert.png" alt="alert-explore" width="700"/>


### Create an alert from OpenSearch Dashboards

Your easiest option is to first test out filters and a search query directly in **OpenSearch Dashboards** or reuse a saved search. When the search captures the right logs, click **Create alert** to copy over the search criteria and begin configuring an alert.

![Create an alert from OSD](https://dytvr9ot2sszz.cloudfront.net/logz-docs/alerts/create-alert-discover-sep3.png)

  The alert form will automatically inherit the search query, filters, and selected accounts.


### Create an alert from an Insight


OpenSearch Dashboards Insights automatically scans your logs for errors and groups them into meaningful units. To create an alert from a specific insight, go to [OpenSearch Dashboards](https://app.logz.io/#/dashboard/osd/discover/) > Insights > Create alert.

![Create an alert for Logz.io Insights](https://dytvr9ot2sszz.cloudfront.net/logz-docs/alerts/osd-insights-sep3.png)

### Duplicate an alert

You can duplicate an existing alert to reuse its configuration without creating it from scratch.

To duplicate an alert:

* Navigate to the [Alert Definitions](https://app.logz.io/#/dashboard/triggers/alert-definitions) page
* Hover over the relevant alert to reveal the **⋮** menu button
* Click the Menu button and select **Duplicate**

![Duplicate alert](https://dytvr9ot2sszz.cloudfront.net/logz-docs/alerts/alert-duplicate-sep4.png)


### Create an alert manually

These are your standard methods for creating an alert.

* From the navigation menu, select **Logs > Alerts +** (Yellow + icon).

<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/alerts/alerts-from-nav.png" alt="alert-nav" width="700"/>


* From the alerts page. Navigate to **Logs > Alerts** and click the button **+ New alert**.

<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/alerts/alerts-from-page.png" alt="alert-page" width="700"/>


