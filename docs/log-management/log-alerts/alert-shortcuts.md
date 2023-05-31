---
sidebar_position: 4
title: How to Quickly Create Alerts
---


Sometimes, you may want to take shortcuts when creating an alert. You have several options for shortening the process:

### Create an alert from OpenSearch Dashboards

Your easiest option is to first test out filters and a search query directly in **OpenSearch Dashboards** or reuse a saved search. When the search captures the right logs, click the button **Create alert** to copy over the search criteria and begin configuring an alert.

![Create an alert from OSD](https://dytvr9ot2sszz.cloudfront.net/logz-docs/alerts/filter-to-alert-button.gif)

  The alert form will automatically inherit the search query, filters, and selected accounts.


### Create an alert from an Insight

Logz.io Insights scan your logs for errors and group them into logical units.
If an **Application Insight** or **Cognitive Insight** interests you, you can create an alert to be notified when it recurs.

  From the navigation menu, select **Logs > Insights**. Click the **Menu button <i class="li li-ellipsis-v"></i>** for the relevant Insight and select **Create an alert**.

  ![Create an alert for Logz.io Insights](https://dytvr9ot2sszz.cloudfront.net/logz-docs/alerts/create-alert-from-insights-new-nav.png)

### Duplicate an alert

* You can duplicate an existing alert when you want to reuse its configuration without creating it from scratch.

  To duplicate an alert:
  
  * Go to the [**Alert definitions**](https://app.logz.io/#/dashboard/triggers/alert-definitions) page
  * Hover over the alert
  * Click the **Menu button <i class="li li-ellipsis-v"></i>** for the relevant alert
  * Select **Duplicate**

  ![Duplicate alert](https://dytvr9ot2sszz.cloudfront.net/logz-docs/alerts/duplicate-alert.png)

### Create an alert manually

These are your most standard methods for creating an alert.

* From the navigation menu, select **Logs > Alerts +** (Yellow + icon).

* From the top menu, select **Logs > Alerts** and click the button **+ New alert**.
