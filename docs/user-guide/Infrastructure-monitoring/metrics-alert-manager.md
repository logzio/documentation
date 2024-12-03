---
sidebar_position: 3
title: Metrics Alert Manager
description: Use metrics alert manager to monitor your services and operations
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [metrics, infrastructure monitoring, remote write, Prometheus, monitoring, dashboard, observability, logz.io]
---


Metrics alerts enable you to monitor your services and operations, notifying team members immediately when an issue arises. You can set alerts to detect memory spikes, 3xx-4xx errors, and more.

Metrics Alert Manager is fully compatible with Prometheus Alert Manager, allowing a quick and easy migration of existing Prometheus alerts to Logz.io for an enhanced Prometheus-based monitoring experience.

There are two main ways to create a metric alert:


## Create an alert from an existing panel


Navigate to your **[Metrics account](https://app.logz.io/#/dashboard/metrics/)**, open your dashboard and choose the panel you want to use for your alert.


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

Click on the **Operation** dropdown menu and select the condition you want to apply. For example, choose **Reduce** to condense the time series to a single data point, which is necessary for the alert to function. 

Then, select **Last** to get the most recent data point. This function influences what is presented in the notification, not the actual condition, as the threshold is defined in the previous section.

![Set multi rule](https://dytvr9ot2sszz.cloudfront.net/logz-docs/grafana/operation-jun18.png)

You can also use the **Math** operation to create formulas with time series or numerical data. Math operations transform these inputs into new numbers or time series. For example, `$D > X`, where $D is the Reduce expression and X is the series you want to compare it to.


### Define alert conditions

To define the alert's condition, select the appropriate query or expression from the **Condition** dropdown menu to trigger the alert rule.

In the **Evaluate** field, specify the pending duration, which delays the alert from firing if the query briefly crosses the threshold.

Click **Configure no data and error handling** to set up notifications for instances when no data or errors occur, ensuring the alert functions correctly.

You can now preview the alert to verify its functionality. Click the **Preview alerts** button, and Logz.io will run the query and display the relevant results.


![Preview alerts](https://dytvr9ot2sszz.cloudfront.net/logz-docs/grafana/define-alert-jun18.png)

<h3 id="addetails">Add details for your alert</h3>


You can add additional details to the alert to provide context when and if it triggers. For example, adding `{{$labels.path}}` and `{{$values.D}}` in the summary will automatically populate information from the relevant services.

[Learn more about adding annotations and context to your alerts](https://grafana.com/docs/grafana/latest/alerting/alerting-rules/create-grafana-managed-rule/#add-annotations).


Click **Save** or **Save and exit** at the top right corner of the screen to save your alert. You'll be redirected back to the panel view.

![Metric alert details](https://dytvr9ot2sszz.cloudfront.net/logz-docs/grafana/adding-details-jun18.png)




## Create an alert manually 

Creating an alert manually involves building your own query instead of using an existing panel.


Navigate to the **[Alerting screen](https://app.logz.io/#/dashboard/metrics/alerting/)** and click on **New alert rule**.


![alerting screen](https://dytvr9ot2sszz.cloudfront.net/logz-docs/grafana/new-alert-rule-jun18.png)

### Configure your manual alert

Name your alert rule and select the folder to store it. Optionally, you can enter a group name to organize the alert within a specific group inside the folder.

Next, build the query for this alert. You can use the Metrics browser to easily view and select your metrics, labels, and values.


![Metric browser](https://dytvr9ot2sszz.cloudfront.net/logz-docs/grafana/metric-browser-jun18.png)


Complete the alert by following the steps to [define your alert condition](/docs/user-guide/Infrastructure-monitoring/metrics-alert-manager#define-alert-conditions), and [add details to your alert](/docs/user-guide/Infrastructure-monitoring/metrics-alert-manager#addetails). 


### Define your notification endpoint

After your alert is running, set up your notification endpoint. You can choose from various common alerting endpoints such as Slack, PagerDuty, Gmail, OpsGenie, and more.

To set up your endpoint, navigate to the **[Alerting screen](https://app.logz.io/#/dashboard/metrics/alerting/)**. Switch to the **Contact points** tab and click on the **New contact point** button.

![Alert contact tab](https://dytvr9ot2sszz.cloudfront.net/logz-docs/grafana/contact-point-jun18.png)

Choose a name for your new contact point, and select a type from the dropdown list. Each selection offers various options, including adding emails, channels, API keys, and more.

<!-- For example, Slack requires a channel/group/IM, token, and webhook URL.

![Slack contact point](https://dytvr9ot2sszz.cloudfront.net/logz-docs/grafana/metric-alert-contact-point.png)-->

You can test your endpoint to make sure it's working correctly. Once you're done, click **Save contact point**. 


## Configure your notification policy

With your alerts and contact points ready, it's time to set up how alerts are routed to contact points. Notification policies are built in a tree structure, with a single, non-deletable root policy and one or more child policies.

[Learn more about Grafana's notifications and policies](https://grafana.com/docs/grafana/latest/alerting/fundamentals/notifications/#notification-policies).


:::note
You cannot create a notification with more than 1 trigger tag or label, as this uses the AND operator instead of OR, preventing the notification from triggering. To solve this, create multiple notification policies that use the same label.
:::


To set your notification policy, navigate to the main **Alerting page** and click on the **[Notification policies](https://app.logz.io/#/dashboard/metrics/alerting/routes)** tab. 

1. Click on **New policy** to create your policy, then click on the **Add matcher** option. 

2. Enter the relevant **label** name. It must exactly match the label name.

3. Choose the **operator** to match the label. The available operators are:

    * `=:` Select labels that exactly match the provided string.
    * `!=:` Select labels that do not match the provided string.
    * `=~:` Select labels that regex-match the provided string.
    * `!~:` Select labels that do not regex-match the provided string.

    The **value** is based on the operator chosen.

4. Choose the relevant **Contact point** from the dropdown menu.

5. Optionally, enable **Continue matching subsequent sibling nodes** to allow the alert to match nested policies, resulting in more than one notification per alert. This can be useful for sending a notification to a general contact point and specific points managed by nested policies.

6. Use **Override grouping** to group all firing alerts under the label chosen in the next **Group by** section, preventing duplicated alerts

7. Enable **Override general timings** to mute notifications during specific periods, such as weekends or maintenance hours.

8. **Mute timing** is a recurring interval when no new notifications for a policy are generated or sent. You can create and apply these to prevent alerts from firing during a specific and reoccurring period, such as holidays, upgrades, and more. 

9. Click on **Save policy** to create the new policy.   

![Alert notification policy](https://dytvr9ot2sszz.cloudfront.net/logz-docs/grafana/notification-policy-jun19.png)


## Temporarily mute notifications with Silences

Your system can trigger numerous alerts, creating noise that might distract team members from focusing on critical issues. To manage this, you can use Silences to mute alerts for a specified time frame.


To create Silences, navigate to **Alerting page** > **[Silences](https://app.logz.io/#/dashboard/metrics/alerting/silences)**, and click on **New silence**.

Choose the start and end dates for the Silence, or use Duration to specify how long you want the Silence to be active.

Enter the relevant **label** name. It must exactly match the label name. 

Choose the **operator** to match the label:

* `=:` Select labels that exactly match the provided string.
* `!=:` Select labels that do not match the provided string.
* `=~:` Select labels that regex-match the provided string.
* `!~:` Select labels that do not regex-match the provided string.

And enter the relevant **value** based on the operator chosen.


Use the comment section to note the time and date when the Silence was created, and add any additional information as needed.

Click on **Submit** to save your silence. 

![Silence alerts](https://dytvr9ot2sszz.cloudfront.net/logz-docs/grafana/alert-silence-jun19.png)


## Mute timings vs. Silences

Both Mute Timings and Silences help manage alert notifications, but they function differently:

Mute Timings:

* They do not prevent alert rules from being evaluated or stop alert instances from appearing in the user interface. They only prevent notifications from being sent.
* Mute timings must be created by the user and can then be added to notification policies. They use recurring time interval definitions.

Silences:

* Silences use labels to match against alerts to determine whether to mute them.
* They have a fixed start and end time.


This distinction ensures that while both features manage notification noise, they do so in complementary ways.