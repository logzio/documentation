---
sidebar_position: 2
title: Log Alerts in Explore Dashboard
description: Monitor your environment with log alerts
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logz.io, alerts, log alerts, log analysis, explore, observability]
---


Log alerts are essential for ensuring you’re notified of critical events. Setting up the right alerts is a cornerstone of proactive development, DevOps, and validation practices.

Logz.io alerts leverage the Explore Dashboard search queries to continuously monitor your logs and notify you when specific conditions are met. Alerts can range from simple searches or filters to complex queries with multiple conditions and varying thresholds.

### Create a log alert

You can create an alert directly from your Explore Dashboard, or build it manually according to your desired configuration. 

Open the Explore Dashboard, create a query or a view you want to trigger your alert on, and click the bell icon at the top right corner.

You'll be redirected to the Create an alert page, where you can continue configuring your alert.

You can also open the navigation choose click Alerts > + New alert to configure and create an alert.

### Review existing alerts

Navigate to [Alerts](https://app.logz.io/#/dashboard/triggers/alert-definitions) to view a paginated list of all alerts configured for your account.

* Cick the column headers or the top filters to sort the list by **severity**, by the user who **created the alert**, **tags**, or the **state** of each alert. 

* Use the search bar to find the desired alert.

* To filter chronologically by alert **names**, their **severity**, when they were **created** or **updated**, click on the column you'd like to filter:

...![Alert definitions](https://dytvr9ot2sszz.cloudfront.net/logz-docs/alerts/alerts-updated-by-screenshot.png)


### Manage Log alerts

You can manage alerts individually or in bulk.

Use search terms and filters to locate the alerts you want to edit. Then, select them by clicking the checkbox next to each alert or select all visible alerts on the page (up to 25) by checking the top box.

....![Select alerts](https://dytvr9ot2sszz.cloudfront.net/logz-docs/alerts/select-alerts.gif)

If you have more than 25 alerts you'd like to edit, you can select all of the results that match your search by clicking on the hypertext located at the top right of the table:

![Alert bulk actions](https://dytvr9ot2sszz.cloudfront.net/logz-docs/alerts/select-all-alerts.png)


:::note
You can act on **up to 1,000** alerts simultaneously.
:::

<h3 id="individual">Individual alerts</h3>


Each alert has a **State** button you can toggle to enable or disable the alert as needed. 

To edit, duplicate or delete an alert, hover over its line to reveal the **Delete** and **Edit** buttons.

You can click the **Menu button :** to open the additional options: **Duplicate** an alert and **View last events**. Select the latter to display the alert query and number of hits in the Explore Dashboard.

<h3 id="multiple"> Multiple alerts</h3>

Choosing one or more alerts opens a top menu with the following actions:
 
* **Delete** - Delete all of the selected alerts
* **Activate** - Turn all selected alerts to active
* **Deactivate** - Deactivate all selected alerts
* **Recipient** - Add or replace recipients and notification points

![Alert edit menu](https://dytvr9ot2sszz.cloudfront.net/logz-docs/alerts/alert-edit-menu.png)

Clicking on the **Recipient** option presents you with a pop-up with 2 available options:

**Add** - Adds new recipients and notification points on top of the existing ones. You can use this to add Slack channels, email addresses, and more.

**Replace** - Remove the existing notification points and recipients, and replace them with the new settings. Note that you won't be able to review the current notification settings, and you won't be able to revert the action once you save your changes.

![Alert recepients edit](https://dytvr9ot2sszz.cloudfront.net/logz-docs/alerts/add-replace-alerts.png)