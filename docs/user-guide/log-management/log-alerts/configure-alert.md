---
sidebar_position: 2
title: Configure an Alert
---

You can set up Logz.io log alerts to automatically get notified about issues that demand attention.

:::note
Community plans limit the number of alerts that may be enabled. See the official [pricing page](https://logz.io/pricing/) for details.
:::

### Configuring an alert

:::caution Important
You cannot configure alerts using the `logzio-alert` log type. This type is ignored by the alerts engine.
:::

#### Name the alert

Give your alert a meaningful name. When your alert triggers, its name is used as the email subject or notification heading.

:::note
Your alert name can contain letters, numbers, spaces, and special characters. It **can't** contain emojis or any other elements.
:::


#### Set search components

Next, set the search components. This determines which logs to look for and in which accounts.

If you intend to create a correlated alert with 2 queries, see [this guide](/docs/user-guide/log-management/log-alerts/correlated-alert).


![Alert group by settings](https://dytvr9ot2sszz.cloudfront.net/logz-docs/alerts/alert-filter-component.gif)


:::note
To perform date range filtering on the `@timestamp` field, include the field as part of a query, 
rather than by adding it as a filter: `@timestamp` filters are overwritten.
:::


##### Enter query and filters

You can use any combination of filters and a search query. Note the following:

* Use a Lucene search query.
  * You have the option to use wildcards.
  * OpenSearch Dashboards Query Language (DQL) is not supported.

* All filters are accepted, including: **is, is not, is one of, is not one of, exists, does not exist**.


Once you're done refining your search query and filters, you can
click **Preview** to open OpenSearch Dashboards in another tab. It can help review the returned logs and ensure you get the expected results.

##### Using Group-by (order matters!)

:::caution Important
Alerts won't trigger if the field added to the Group-by doesn't exist in the logs. The logs must include **both** the field you have in group-by and the field you use in your query/filter to trigger the alert. 
:::


You can apply **group by** operators to up to 3 fields. If you use this option, the alert will return the aggregated results.

The order in which you add group-by fields matters. Results are grouped in the order in which the group-by fields are added. (The fields are shown from first to last from Left-To-Right.)

For example, the following will group results by continent, then country, then city:

![Ordered group by field functions](https://dytvr9ot2sszz.cloudfront.net/logz-docs/correlated-alerts/ordered-group-by_aug2021.png)

If we reverse the order (city, then country, then continent), it will likely generate unintended results.

You can use the group-by to create a visualization of your triggered alerts. The visualization will show the logs caught by the alert, letting you see which group-by values existed when the alert was triggered and which group-by values matched the condition. 

For example, if you set an alert to:

* Look at the last 15 minutes
* Trigger if there are more than 3 logs
* Group the results by account_name

You’ll be able to use these fields to create the following chart:

![Alerts to visualization](https://dytvr9ot2sszz.cloudfront.net/logz-docs/correlated-alerts/group-by-visualize.png)



##### Select relevant accounts

Next, select the **Accounts to search**. 

* If you select **All accounts**, the alert will query the logs in all the accounts it has access to. It will automatically include any accounts added in the future.

* You can select specific accounts. Select **Just these accounts** and add the relevant accounts from the dropdown list.

#### Set threshold and severity levels

Set your threshold and severity levels.

In the _Trigger if..._ section, click **+ Add a threshold** to set up to 5 threshold conditions, each with its own severity tag.

:::note
You can set the trigger condition time frame between 5 minutes and up to 24 hours (1 day). To set a trigger condition longer than 24 hours, use [Logz.io’s API](https://api-docs.logz.io/docs/logz/create-alert) to create your alert.
:::


![Alert trigger thresholds](https://dytvr9ot2sszz.cloudfront.net/logz-docs/alerts/alerts--trigger-settings_aug2021.png)

#### Set alert schedule

You can use the scheduling mechanism to manage the trigger condition frequency.

Scheduling defines the frequency and the time frame for the alerts. To define a schedule, select **On Schedule** and use a [cron expression](https://www.freeformatter.com/cron-expression-generator-quartz.html) to specify when to trigger the alert.


:::note
The cron expression can only be set in increments rounded to the nearest minute.
:::


![Schedule alert screen](https://dytvr9ot2sszz.cloudfront.net/logz-docs/alerts/schedule-alert.png)

For example, you can apply the following schedule to your alerts:

| Cron expression                         | Alert trigger schedule |
|-----------------------------------------|------|
| 0 0/10 * ? * * *                        | Every 10 minutes |
| 0 0 0/1 ? * * *                         | Rounded to the nearest hour |
| 0 * 8-17 ? * MON,TUE,WED,THU,FRI *  | Every minute between 8 am to 5 pm, Monday through Friday |
| 0 5 0 ? * * *                           | Every day at exactly 12:05 am |

By default, trigger conditions run approximately every minute. If there's a lag, the alert is not checked until all data is received. In addition, once an alert has met its condition and is triggered, it won't be checked again for the remainder of the alert trigger condition time range.

#### _(Optional)_ Set notification details

##### Add description and tags

![Alert description and tags](https://dytvr9ot2sszz.cloudfront.net/logz-docs/alerts/description-and-tags_aug2021.png)

The **Description** is visible on the _Alert definitions_ page, and it's part of the emails and Slack messages sent when the alert is triggered. 

We recommend making your description helpful to recipients, like telling them how to fix the issues that led to the alert.

The **Tags** are useful for filtering. For example, they can be used to create filtered visualizations and dashboards or to filter the _Alert definitions_ page.

##### Select alert recipients

![Recipients and wait between notifications](https://dytvr9ot2sszz.cloudfront.net/logz-docs/alerts/recipients-and-wait_aug2021.png)

Choose notification endpoints if you want to send notifications or emails when the alert is triggered. This isn't required, though—triggered alerts are still logged and searchable in OpenSearch Dashboards.

Choose the endpoints or email addresses to notify under _Who to send it to_.

##### Add an additional email address as a recipient


:::note
Notification emails include up to 10 sample events. If your alert triggers more than 10 events, you can view the complete list in your logs.
:::


To use an **email** as your endpoint, you need to type the email in the Recipients table and click enter.

![Enter custom email](https://dytvr9ot2sszz.cloudfront.net/logz-docs/alerts/add-custom-email.gif)


If you need help adding a new endpoint,
see [_Notification endpoints_](/docs/user-guide/integrations/notification-endpoints/endpoints).

Set a time period between notifications to limit how frequently recipients are notified. Logz.io will continue to log triggered alerts without sending notifications, and you can [review these alerts](/docs/user-guide/log-management/log-alerts/alerts-event-management/) directly from the Logz.io platform at any time.

:::note
The system combines the **Trigger if** time interval with the **Wait time** interval to calculate how long it should snooze notifications and chooses the more extended time duration available. For example, if your trigger condition is 1 hour and the wait time is 15 Minutes, the system will snooze notifications for 1 hour before triggering them again.
:::

##### Select alert's output format & content

When triggered, the alert will send out a notification with sample data.

Sample data can be sent in either **JSON** or **Table** formats. Toggle the button to select your preferred format.

If the alert includes any aggregation or group by field, the notification output will send the aggregated results by default.

![Output format](https://dytvr9ot2sszz.cloudfront.net/logz-docs/alerts/output_aggregated_aug2021.png)

To be selective about the output, click **<i class="li li-plus"></i> Add a field** and select a field from the dropdown list. If you want, you can also add a sorting rule and a regex filter. [Learn more about regex filters for alert notifications](/user-guide/alerts/regex-filters.html).

  * If you select **JSON** format, you can send the full log (with all fields) or select as many as 7 fields.
  * If you select **Table**, you can send as many as 7 fields.

![Output table](https://dytvr9ot2sszz.cloudfront.net/logz-docs/alerts/output-formats_aug2021.gif)

#### Save your alert

Click **Save** to save your alert.
If the thresholds are passed and the alert is triggered,
Logz.io will log the alert and send the configured notifications.

#### Get alert's ID


Each alert has a unique ID to help you find and share it with your teammates. Once your alert is configured, click the Edit button next to it. Then, the URL will update to include a set of numbers that represents your alert’s ID.

The URL will look like this:

`https://app.logz.io/#/dashboard/alerts/v2019/<<ALERT_ID>>`

![Alert ID](https://dytvr9ot2sszz.cloudfront.net/logz-docs/alerts/alert-id.png)