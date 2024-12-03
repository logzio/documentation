---
sidebar_position: 2
title: Understanding Log Alerts
description: Monitor your environment with log alerts
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logz.io, alerts, log alerts, log analysis, explore, observability]
---


Log alerts are essential for ensuring you’re notified of critical events. Setting up the right alerts is a cornerstone of proactive development, DevOps, and validation practices.

Logz.io alerts leverage the Explore Dashboard search queries to continuously monitor your logs and notify you when specific conditions are met. Alerts can range from simple searches or filters to complex queries with multiple conditions and varying thresholds.

### Create a log alert

You can create an alert directly from your [Explore Dashboard](https://app.logz.io/#/dashboard/explore), or [build it manually](https://app.logz.io/#/dashboard/alerts/v2019/new) according to your desired configuration.

Open the Explore Dashboard, create a query or simple search to trigger your alert, and click the **Create Alert** button in the top right corner.

You'll be redirected to the Create an alert page, where you can continue configuring your alert.

![Alert from dashboard](https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/alerts/explore-create-alert-oct21.png) 

To manually build an alert, navigate to **[Alerts > + New alert](https://app.logz.io/#/dashboard/alerts/v2019/new)** to configure and create an alert.

![Alert from dashboard](https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/alerts/new-alert-oct21.png)

### Review existing alerts

To view a paginated list of all alerts configured for your account, navigate to the [Alerts](https://app.logz.io/#/dashboard/triggers/alert-definitions) section.

You can sort the list by clicking on the column headers or using the top filters. Sort by severity, creator, tags, or alert status.

Use the search bar to find a specific alert quickly.

Click on the corresponding column header to filter alerts chronologically by **name**, **severity**, **creation date**, or **update date**.

![Alert definitions](https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/alerts/alerts-oct21.png)

### Manage Log alerts

You can manage alerts individually or in bulk.

Use search terms and filters to locate the alerts you want to edit. Select them by clicking the checkbox next to each alert, or check the top box to select all visible alerts on the page (up to 25).

![Select alerts](https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/alerts/edit-alerts-oct21.gif)

If you need to edit more than 25 alerts, you can select all alerts that match your search criteria by clicking the hypertext link at the top right of the table.

![Alert bulk actions](https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/alerts/select-alerts-oct21.png)


:::note
You can act on **up to 1,000** alerts simultaneously.
:::


<h3 id="individual">Individual alerts</h3>

Each alert features a **State** button that you can toggle to turn the alert on or off as needed.

To edit, duplicate, or delete an alert, hover over its row to reveal the **Delete** and **Edit** buttons.

Click the **Menu button (:)** to access additional options such as **duplicating** the alert or **viewing the latest events**. Selecting the latter will display the alert query and the number of hits in the Explore Dashboard.

![Alert additional options](https://dytvr9ot2sszz.cloudfront.net/logz-docs/alerts/alert-menu-oct21.png)




<h3 id="multiple"> Multiple alerts</h3>

Choosing one or more alerts opens a top menu with the following actions:

* **Delete** - Delete all selected alerts
* **Activate** - Set all selected alerts to active
* **Deactivate** - Set all selected alerts to inactive
* **Recipient** - Add or replace recipients and notification points

![Alert edit menu](https://dytvr9ot2sszz.cloudfront.net/logz-docs/alerts/multiple-alerts-oct21.png)

Clicking on the **Recipient** option opens a pop-up with two options:

**Add** - Add new recipients and notification points to the existing ones. This can include Slack channels, email addresses, and more.

**Replace** - Remove existing notification points and recipients, and replace them with new settings. Note that you **won't be able to review** the current notification settings **or revert** this action once saved.

Click **Confirm** to apply your changes.

<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/alerts/add-replace-oct21.png" alt="edit-alerts" width="700"/>
