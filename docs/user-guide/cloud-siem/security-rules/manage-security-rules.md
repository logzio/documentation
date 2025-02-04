---
sidebar_position: 2
title: Create a Security Rule
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Create and edit a security rule in Logz.io
keywords: [SIEM, Security rule, rules, cloud security, cloud security rules, Security information and event management, Security information, event management]
toc_max_heading_level: 2
---



Security rules help you connect the dots between your data sources and events that could indicate a security threat or breach. Your Cloud SIEM account comes preconfigured
with security rules for different attack types and security use cases.

You can create new security rules to supplement the built-in rules. You can also update any preconfigured rule at any time, including adding a notification endpoint (for example, email or Slack) or changing trigger thresholds.

:::caution Important
You cannot configure rules using the `logzio-alert` log type. This type is ignored by the rule engine.
:::

## Manually create a new rule

You can create your own custom rules. To get started, navigate to **[SIEM > Rules](https://app.logz.io/#/dashboard/security/rules/rule-definitions)** and select **New rule**.

![Add new rule](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/siem-new-rule-dec.png)


<h3 id="name">Name the rule</h3>

Give your rule a meaningful name. When your rule triggers, its name is used as the email subject or notification heading.

:::note
Your rule name can contain letters, numbers, spaces, and special characters. It can't contain emojis or any other elements.
:::

<h3 id="search">Set search components</h3>

Next, set the search components. This determines which logs to look for and in which accounts.

You can use any combination of filters and a search query. Note the following:

* Use a Lucene search query.
  * You have the option to use wildcards.
  * OpenSearch Dashboards Query Language (DQL) is not supported.
* All filters are accepted, including: **is, is not, is one of, is not one of, exists, does not exist**.

After refining your search query and filters, click **Preview** to open OpenSearch Dashboards in another tab and review the returned logs to ensure you get the expected results.

:::note
To perform date range filtering on the `@timestamp` field, include the field as part of a query rather than adding it as a filter: `@timestamp` filters are overwritten.
:::

![siem rule create](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/siem-rule-search-dec.png)

<h3 id="groupby">Use group-by (order matters!)</h3>

:::crucial Important
Alerts won't trigger if the field added to the Group-by doesn't exist in the logs. The logs must include **both** the field you have in group-by and the field you use in your query/filter to trigger the alert. 
:::

You can apply **group by** operators to up to 3 fields. If you use this option, the rule will return the aggregated results.

The order of group-by fields matters. Results are grouped in the order in which the group-by fields are added. (The fields are shown from first to last from left-to-right.)

For example, the following will group results by continent, then country, then city:

![group by](https://dytvr9ot2sszz.cloudfront.net/logz-docs/correlated-alerts/ordered-group-by_aug2021.png)

If you reverse the order (city, country, continent), it will likely generate unintended results.

<h3 id="relevant">Select relevant accounts</h3>

Next, select the **Accounts to search**.

* If you select **All accounts**, the rule will query the logs in all the accounts to which it has access. It will automatically include any accounts added in the future.

* You can select specific accounts. Select **Just these accounts** and add the relevant accounts from the dropdown list.

<h3 id="threshold">Set threshold and severity levels</h3>

Set your threshold and severity levels. You can base your trigger on a number of logs, minimum/maximum of fields, average, sum, and more.

In the _Trigger if..._ section, click **Add a threshold** to set as many as 5 threshold conditions, each with its own severity tag.

:::note
You can set the trigger condition time frame between 5 minutes and up to 24 hours (1 day). To set a trigger condition longer than 24 hours, use [Logz.io’s API](https://api-docs.logz.io/docs/logz/create-security-rule/) to create your rule.
:::

![rule trigger thresholds](https://dytvr9ot2sszz.cloudfront.net/logz-docs/alerts/alerts--trigger-settings_aug2021.png)

<h3 id="mitre">(Optional) Add MITRE ATT&CK Tags</h3>

**MITRE ATT&CK** is a curated knowledge base and model for cyber adversary behavior, reflecting the various phases of an adversary’s attack lifecycle and the platforms they are known to target. 

You can add the predefined MITRE tags to your security rules and get an alert when a known cyber security threat is found in your systems.

![Create Mitre Attack tag](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/mitre-attack-dec.png)

Click on **Add tags** and choose the **Tactics** (Why) and **Technique** (How) you’d like to monitor. For some Techniques, you’ll be able to select a **Sub-technique** to get more in-depth monitoring of it.

![Configure Mitre Attack tag](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem/mitre-attack-tags.png)

Click on your saved tags to view MITRE’s documentation and additional information for each one.

<h3 id="schedule">Set rule schedule</h3>

You can use the scheduling mechanism to manage the trigger condition frequency.

Scheduling defines the frequency and the time frame for the rule. To define a schedule, select **On Schedule** and use a [cron expression](https://www.freeformatter.com/cron-expression-generator-quartz.html) to specify when to trigger the rule.

:::note
The cron expression can only be set in increments rounded to the nearest minute.
:::

For example, you can apply the following schedule to your rules:


| Cron expression                         | Rule trigger schedule |
|-----------------------------------------|------|
| 0 0/10 * ? * * *                        | Every 10 minutes |
| 0 0 0/1 ? * * *                         | Rounded to the nearest hour |
| 0 * 8-17 ? * MON,TUE,WED,THU,FRI *  | Every minute between 8 am to 5 pm, Monday through Friday |
| 0 5 0 ? * * *                           | Every day at exactly 12:05 am |

By default, trigger conditions run approximately every minute. If there's a lag, the rule is checked once all data is received. In addition, once a rule has met its condition and is triggered, it won't be checked again for the remainder of the rule trigger condition time range.

![schedule](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/schedule-siem-dec.png)

<h3 id="notification">(Optional) Set notification details</h3>

The rule's **Description** is visible on the rule definitions page, and it's part of the emails and Slack messages sent when the rule is triggered. As such, an ideal description will be helpful to recipients, explaining how to fix the issues that led to the rule.

The **Tags** are helpful for filtering and finding the rules later on. You can add up to 25 tags per rule.

You can choose a notification endpoint to send notifications or emails when the rule is triggered. This isn't required, though—triggered rules are still logged and searchable in OpenSearch Dashboards.

Choose the endpoints or email addresses you want to notify when the rule triggers.

<h3 id="email">Add email address as a recipient</h3>

:::note
Notification emails include up to 10 sample events. If your rule triggers more than 10 events, you can view the complete list in your logs.
:::

To use an email as your endpoint, type the email in the **Recipients** box and click enter.

Set a period between notifications to limit how frequently recipients are notified. Logz.io will continue to log triggered rules without sending notifications, and you can review these directly from the Logz.io platform at any time.

:::note
The system combines the **Trigger if** time interval with the **Wait time** interval to calculate how long it should snooze notifications and chooses the more extended time duration available. For example, if your trigger condition is 1 hour and the wait time is 15 Minutes, the system will snooze notifications for 1 hour before triggering them again.
:::

*If you need help adding a new endpoint, see [Notification endpoints](https://docs.logz.io/docs/user-guide/integrations/notification-endpoints/endpoints/).*

<h3 id="output">Select rule output format & content</h3>

When triggered, the rule will send out a notification with sample data.

Sample data can be sent in either JSON or Table formats. Toggle the button to select your preferred format.

If the rule includes any aggregation or group by rule, the notification output defaults to the group by/aggregated fields.

Otherwise, you control the data format. It can be either **JSON** or a **Table**.

  * If you select JSON, you can choose to send all fields or select fields.
  * If you select a table, you can send as many as 7 fields.

To be selective about the output, click **Add a field** and select a field from the dropdown list. If you want, you can also add a sorting rule and a regex filter.


![add email recipient](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/siem-add-email-dec.gif)

:::note
When notifications are suppressed,
Logz.io will continue to log triggered rules without sending notifications.
You can search triggered rule logs at any time.
:::

<h3 id="regex">Using regex filters</h3>


You can "clean" the data in the notification using regex filters. If you add a regex filter, it will select for the data you want to include in the rule output.

There is no danger that a regex filter will disrupt the notification.

* If the regex matches the relevant data, you will see only the desired results.
* If the regex _does not_ match, the filter will be disregarded and the rule output will include the full content of the field.


<h3 id="save">Save your rule</h3>


Click **Save** to save your rule.
Whenever the thresholds are met, the rule will trigger. Logz.io will log the security event, and send out a notification, if configured.


## Duplicate and modify an existing rule

You can create rules based on Logz.io's preconfigured rules. In this case, the builder will be pre-populated with data from the existing rule, such as the query string.

Navigate to **[SIEM > Rules](https://app.logz.io/#/dashboard/security/rules/rule-definitions)** and choose the rule you want to use. Hover over the three dots and select **Duplicate**.

![duplicate rule](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/siem-duplicate-dec.png)

The rule configuration wizard includes all of the preconfigured queries, filters, etc.

Now, you can edit the rule based on your needs and set the trigger conditions, schedule, notification endpoints, etc.

Once you're done, click **Save** to create the rule.

## Create a rule from OpenSearch Dashboards query

You can create rules based on queries and filters in OpenSearch Dashboards.

Navigate to **[SIEM > Research](https://app.logz.io/#/dashboard/security/research/discover/)** and build your query.

To turn the query into a rule, click on **Create from query > Create rule**. The rule will include the query and filters you've used.

![create rule from osd](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/create-rule-from-query-dec.png)

Next:
* [Name your rule](/docs/user-guide/cloud-siem/quick-guide/create-rules#name-the-rule)
* [Set the trigger conditions](/docs/user-guide/cloud-siem/quick-guide/create-rules#set-trigger-conditions)
* [Add MITRE ATT&Ck tags](/docs/user-guide/cloud-siem/quick-guide/create-rules#optional-mitre-attck-threats) if needed
* [Set schedule](/docs/user-guide/cloud-siem/quick-guide/create-rules#set-rule-schedule) 
* [Choose the notification points](/docs/user-guide/cloud-siem/quick-guide/create-rules#optional-set-notification-details).

Once you're done, click **Save** to create the new rule. 