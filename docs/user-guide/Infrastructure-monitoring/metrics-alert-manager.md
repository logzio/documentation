---
sidebar_position: 3
title: Metrics Alert Manager
description: Use metrics alert manager to monitor your services and operations
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [metrics, infrastructure monitoring, remote write, Prometheus, monitoring, dashboard, observability, logz.io]
---

Metrics alerts enable you to monitor your services and operations, notifying team members immediately when an issue arises. You can configure alerts to detect memory spikes, 3xx-4xx errors, and more.

Our Metrics Alert Manager is fully compatible with Prometheus Alert Manager, allowing for quick and easy migration of existing Prometheus alerts to Logz.io, providing an enhanced Prometheus-based monitoring experience.

There are two main ways to create a metric alert:


## Create an alert from an existing panel


Navigate to your **[Metrics account](https://app.logz.io/#/dashboard/metrics/)**, open your dashboard and choose the panel you'd like to use for your alert.


:::note
Alerts cannot be created from **Gauge** type visualizations.
:::


Click the panel's name and choose **Edit**.

![Edit a panel](https://dytvr9ot2sszz.cloudfront.net/logz-docs/grafana/edit-metric-table-jun5.png)


Go to the **Alert** tab and click **Create alert rule from this panel**. This action will automatically transfer the query and variables to the Create alert rule page.


![Create alert flow](https://dytvr9ot2sszz.cloudfront.net/logz-docs/grafana/create-an-alert-flow.gif)


### Configure your alert

Name your alert rule and select the folder to store it. Optionally, you can enter a group name to organize the alert within a specific group inside the folder.

Next, review and edit the queries pulled from the panel you chose.

![Review query](https://dytvr9ot2sszz.cloudfront.net/logz-docs/grafana/new-alert-metrics-jun5.png)


To create a multi-dimensional rule, you can generate a separate alert for each series using Math, Reduce, or Resample expressions.

Click on the **Operation** dropdown menu and select the condition you'd like to apply. For example, choose **Reduce** to condense the time series to a single data point, which is necessary for the alert to function.

Select **Last** to get the most recent data point. This function influences what is presented in the notification, not the actual condition, as the threshold is defined in the previous section.

![Set multi rule](https://dytvr9ot2sszz.cloudfront.net/logz-docs/grafana/metrics-reduce-expr.png)

You can also use the **Math** operation to create formulas with time series or numerical data. Math operations transform these inputs into new numbers or time series. For example, `$D > X`, where $D is the Reduce expression and X is the series you want to compare it to.


<h3 id="define-alert">Define alert conditions</h3>

Define the alert's condition by selecting the query or expression to trigger the alert rule from the **Condition** dropdown.

In the **Evaluate for** field, specify the pending duration, which delays the alert from firing if the query briefly crosses the threshold.

Click **Configure no data and error handling** to set up notifications for instances when no data or errors occur, ensuring the alert functions correctly.

You can now preview the alert to verify its functionality. Click the **Preview alerts** button, and Logz.io will run the query and display the relevant results.




![Preview alerts](https://dytvr9ot2sszz.cloudfront.net/logz-docs/grafana/metric-define-alert-condition.png)

### 4. Add details for your alert


You can add additional details to the alert to provide context when and if it triggers. For example, adding `{{$labels.path}}` and `{{$values.D}}` to the summary will automatically populate information from the relevant services.

[Learn more about adding annotations and context to your alerts](https://grafana.com/docs/grafana/latest/alerting/alerting-rules/create-grafana-managed-rule/#add-annotations).


Click **Save** or **Save and exit**, located at the top right corner of the screen, to save your alert. You'll be redirected back to the panel view.

![Metric alert details](https://dytvr9ot2sszz.cloudfront.net/logz-docs/grafana/metric-add-details.png)




## Create an alert manually 


This process is similar to creating an alert from an existing panel, but it requires you to build your own query.

To get started, navigate to the **[Alerting](https://app.logz.io/#/dashboard/metrics/alerting/)** screen located on the left navigation menu, and click on **New alert rule**.

Name your alert rule and choose its folder.

In the second step, you'll need to build the query for this alert. You can use the Metrics browser to easily view and choose your metrics, labels, and values.

![Metric browser](https://dytvr9ot2sszz.cloudfront.net/logz-docs/grafana/metric-browser-alert.png)

Complete the alert by following the steps to [define your alert condition](#define-alert-conditions), and [add details to your alert](#add-details-for-your-alert). 


### 1. Define your notification endpoint

Once the alert is running, it's time to define your notifications endpoint. You can choose between common alerting endpoints, including Slack, PagerDuty, Gmail, OpsGenie, and more. 

To set up your endpoint, navigate to the **[Alerting](https://app.logz.io/#/dashboard/metrics/alerting/)** screen located on the left navigation menu. Switch to the **Contact points** tab and click on the **New contact point** button.

![Alert contact tab](https://dytvr9ot2sszz.cloudfront.net/logz-docs/grafana/alert-to-contact.png)

Choose a name for your new contact point, and select a type from the dropdown list. Each selection offers a variety of options, including adding emails, channels, API keys, and so on.

For example, Slack requires a channel/group/IM, token, and webhook URL.

![Slack contact point](https://dytvr9ot2sszz.cloudfront.net/logz-docs/grafana/metric-alert-contact-point.png)

You can test your endpoint to make sure it's working correctly.

Once you're done, click **Save contact point**. 


### 2. Configure your notification policy

Your alert and contact points are ready, and now it's time to determine how alerts are routed to contact points. Notification policies are built in a tree structure, where there can only be one root policy that can't be deleted, but each policy can have one or more child policies.

[Learn more about Grafana's notifications and policies](https://grafana.com/docs/grafana/latest/alerting/fundamentals/notifications/#notification-policies).


:::note
You can't create a notification with more than 1 trigger tag or label since it causes the alert uses the AND operator (instead of OR), resulting in your notification not triggering. To solve this, you can create multiple notification policies that use the same label. 
:::

To set your notification policy, navigate to the main **[Alerting page](https://app.logz.io/#/dashboard/metrics/alerting/)** and click on the **Notification policies** tab. 

Click on **New policy** to create your policy, and click on the **Add matcher** option. 

Enter the relevant **label** name. It must exactly match the label name.

Choose the **operator** to match the label. The available operators are:

* `=:` Select labels that are exactly equal to the provided string.
* `!=:` Select labels that are not equal to the provided string.
* `=~:` Select labels that regex-match the provided string.
* `!~:` Select labels that do not regex-match the provided string.

The **value** is based on the operator chosen.

Choose the relevant **Contact point** from the dropdown menu.

Next, the **Continue matching subsequent sibling nodes** option is disabled by default. When you enable this option, the alert will continue matching nested policies even after the alert matches the parent policy, which can result in getting more than one notification per alert. This can be used to send a notification to a catch-all contact point and one or more specific contact points handled by nested policies.

**Override grouping** lets you group all firing alerts under the label chosen in the next **Group by** section, ensuring you're not getting duplicated alerts.

You can also mute notifications by enabling the **Override general timings**. This can help prevent alerts from firing on weekends or during maintenance hours. 

**Mute timing** is a recurring interval of time when no new notifications for a policy are generated or sent. You can create and apply these to prevent alerts from firing during a specific and reoccurring period, such as holidays, upgrades, and more. 

Click on **Save policy** to create the new policy. 

![Alert notification policy](https://dytvr9ot2sszz.cloudfront.net/logz-docs/grafana/metric-alert-notification-policy.png)


### 3. Temporarily mute notifications with Silences

Your system can trigger many alerts, creating noise that might distract team members from focusing on critical issues. To prevent this, you can use Silences to mute alerts during a certain time frame.

To create Silences, navigate to **[Alerting page](https://app.logz.io/#/dashboard/metrics/alerting/)** > **Silences**, and click on **New silence**.

Choose the Silences' start and end date. Or, use Duration to specify how long you want the silence option to be active. 

Enter the relevant **label** name. It must exactly match the label name. 

Choose the **operator** to match the label:

* `=:` Select labels that are exactly equal to the provided string.
* `!=:` Select labels that are not equal to the provided string.
* `=~:` Select labels that regex-match the provided string.
* `!~:` Select labels that do not regex-match the provided string.

And enter the relevant **value** based on the operator chosen.

The comment section includes the time and date when this silence was created, and you can edit it or add any additional info.

Click on **Submit** to save your silence. 

![Silence alerts](https://dytvr9ot2sszz.cloudfront.net/logz-docs/grafana/silence-alert-metric.png)


## Mute timings vs. Silences

Similar to Silences, Mute timings do not prevent alert rules from being evaluated nor stop alert instances from being shown in the user interface. They only prevent notifications from being created.

Mute timings must be created by the user and only then can be added to the notification policies, and it uses time interval definitions that can reoccur.

Silences use labels to match against an alert to determine whether to silence or not and has a fixed start and end time.
