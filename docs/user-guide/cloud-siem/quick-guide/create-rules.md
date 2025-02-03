---
sidebar_position: 5
title: Creating Security Rules
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Create a security rule in Logz.io Cloud SIEM
keywords: [SIEM, security rule, rules, cloud security, Security information and event management, Security information]
toc_max_heading_level: 2
---



Security rules define events and their execution conditions and can contain one or more queries. Logz.io offers a set of updated preconfigured rules. You can refine them by editing thresholds and triggers, duplicate them for full editing access, or create new rules.




## Manually create a new rule

You can create your own custom rules. To get started, navigate to **[SIEM > Rules](https://app.logz.io/#/dashboard/security/rules/rule-definitions)** and select **New rule**.

![New rules](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/siem-new-rule-dec.png)


### Name the rule

Give your rule a meaningful name. When your rule triggers, its name is used as the email subject or notification heading.

:::note
Your rule name can contain letters, numbers, spaces, and special characters. It **can't** contain emojis or any other elements.
:::

### Set search components

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

![Rule search](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/siem-rule-search-dec.png)

### Using Group-by (order matters!)

:::caution Important
Rules won't trigger if the field added to the Group-by doesn't exist in the logs. The logs must include **both** the field you have in group-by and the field you use in your query/filter to trigger the rule.
:::

You can apply **group by** operators to up to 3 fields. If you use this option, the rule will return the aggregated results.

The order in which you add group-by fields matters. Results are grouped in the order in which the group-by fields are added. (The fields are shown from first to last from left-to-right.)

For example, the following will group results by continent, then country, then city:

![Order by group](https://dytvr9ot2sszz.cloudfront.net/logz-docs/correlated-alerts/ordered-group-by_aug2021.png)

If we reverse the order (city, country, continent), it will likely generate unintended results.


### Select relevant accounts

Next, select the Accounts to search.

* If you select All accounts, the rule will query the logs in all the accounts to which it has access. It will automatically include any accounts added in the future.

* You can select specific accounts. Select Just these accounts and add the relevant accounts from the dropdown list.

### Set trigger conditions

Set your threshold and severity levels. You can base your trigger on a number of logs, minimum/maximum of fields, average, sum, and more.

You can add multiple conditions for the trigger by clicking **+ Add threshold**. You can add up to 5 threshold conditions, each with its own severity tag.

:::note
You can set the trigger condition time frame between 5 minutes and up to 24 hours (1 day). To set a trigger condition longer than 24 hours, use [Logz.io’s API](https://api-docs.logz.io/docs/logz/create-security-rule/) to create your rule.
:::


![Trigger if](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/trigger-if-siem-dec.png)

### *(Optional)* MITRE ATT&Ck threats

You can add tactics, techniques, and sub technique tags to your rule, which will appear in the rule definitions table and Event management table. The tags are according to Mitre's knowledge base and model for cyber adversary behavior. 


![Mitre attack](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/mitre-attack-dec.png)


### Set rule schedule
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

![Schedule](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/schedule-siem-dec.png)

### *(Optional)* Set notification details


The Description is visible on the rule definitions page, and it's part of the emails and Slack messages sent when the rule is triggered. As such, an ideal description will be helpful to recipients, explaining how to fix the issues that led to the rule.

The Tags are helpful for filtering and finding the rules later on.

You can choose a notification endpoint to send notifications or emails when the rule is triggered. This isn't required, though—triggered rules are still logged and searchable in OpenSearch Dashboards.

Choose the endpoints or email addresses you want to notify when the rule triggers. 

#### Add email address as a recipient

:::note
Notification emails include up to 10 sample events. If your rule triggers more than 10 events, you can view the complete list in your logs.
:::

To use an email as your endpoint, type the email in the **Recipients** box and click enter.

Set a period between notifications to limit how frequently recipients are notified. Logz.io will continue to log triggered rules without sending notifications, and you can review these directly from the Logz.io platform at any time.

:::note
The system combines the **Trigger if** time interval with the **Wait time** interval to calculate how long it should snooze notifications and chooses the more extended time duration available. For example, if your trigger condition is 1 hour and the wait time is 15 Minutes, the system will snooze notifications for 1 hour before triggering them again.
:::

*If you need help adding a new endpoint, see [Notification endpoints](https://docs.logz.io/docs/user-guide/integrations/notification-endpoints/endpoints/).*


#### Select rule output format & content

When triggered, the rule will send out a notification with sample data.

Sample data can be sent in either JSON or Table formats. Toggle the button to select your preferred format.

If the rule includes any aggregation or group by field, the notification output will send the aggregated results by default.




![Add email](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/siem-add-email-dec.gif)

### Save your rule
Click Save to save your rule. If the thresholds are passed and the rule is triggered, Logz.io will log the rule and send the configured notifications.


## Clone and modify an existing rule

You can create rules based on Logz.io's preconfigured rules. In this case, the builder will be pre-populated with data from the existing rule, such as the query string.

Navigate to **[SIEM > Rules](https://app.logz.io/#/dashboard/security/rules/rule-definitions)** and choose the rule you want to use. Hover over the three dots and select **Duplicate**. 

![Duplicate rule](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/siem-duplicate-dec.png)

The rule includes all of the relevant queries, filters, etc. 

Now, you can define the rule based on your needs and edit the trigger conditions, schedule, notification endpoints, etc.

Once you're done, click **Save** to create the rule. 

## Creating a Security Rule from a SIGMA Rule

SIGMA rules are a standardized YAML format for writing security detection rules. They provide a flexible, vendor-agnostic way to describe threats, making it easier to detect suspicious activity across different platforms.

By importing a SIGMA rule, you can quickly create a security rule without manually defining patterns and conditions, ensuring consistency with industry best practices.


To create a security rule from a SIGMA rule YAML, navigate to **[SIEM > Rules](https://app.logz.io/#/dashboard/security/rules/rule-definitions)** and select **New rule**.

![New rules](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/siem-new-rule-dec.png)

### Name the rule

Give your rule a clear name. This will appear in notifications when the rule is triggered. It can include letters, numbers, and special characters but not emojis or other elements.


### Import your SIGMA rule

Click **SIGMA Conversion** to open the SIGMA converter.

Paste your SIGMA rule or upload a YAML file. Review the rule details, then click **Convert** to apply the rule parameters.

![sigma rule modal](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/sigma-rule-modal.png)


### Select relevant accounts

Choose which accounts the rule should monitor:

* All accounts – The rule will query the logs in all the accounts to which it has access. It will automatically include any accounts added in the future.

* Specific accounts – Select accounts from the dropdown.

### Set trigger conditions

Set your threshold and severity levels. You can base your trigger on a number of logs, minimum/maximum of fields, average, sum, and more.

You can add multiple conditions for the trigger by clicking **+ Add threshold**. You can add up to 5 threshold conditions, each with its own severity tag.

:::note
You can set the trigger condition time frame between 5 minutes and up to 24 hours (1 day). To set a trigger condition longer than 24 hours, use [Logz.io’s API](https://api-docs.logz.io/docs/logz/create-security-rule/) to create your rule.
:::

![Trigger if](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/trigger-if-siem-dec.png)

### *(Optional)* MITRE ATT&Ck threats

MITRE ATT&CK tags help map security events to known attack techniques. If your SIGMA rule includes these tags, they’ll be added automatically. Review them to ensure they’re relevant.

### Set rule schedule

Use the scheduling mechanism to manage the trigger condition frequency.

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

![Schedule](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/schedule-siem-dec.png)

### *(Optional)* Set notification details


The Description is visible on the rule definitions page, and it's part of the emails and Slack messages sent when the rule is triggered. As such, an ideal description will be helpful to recipients, explaining how to fix the issues that led to the rule.

The Tags are helpful for filtering and finding the rules later on.

You can choose a notification endpoint to send notifications or emails when the rule is triggered. This isn't required, though—triggered rules are still logged and searchable in OpenSearch Dashboards.

Choose the endpoints or email addresses you want to notify when the rule triggers. 

#### Select rule output format & content

Choose whether notifications display sample data in JSON or Table format. Aggregated results are included by default if applicable.


![Add email](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/siem-add-email-dec.gif)

### Save your rule

Click Save to activate your rule. Once triggered, Logz.io will log the event and send notifications based on your settings.


## Create a rule from OpenSearch Dashboards query

You can create rules based on queries and filters in OpenSearch Dashboards.

Navigate to [**SIEM > Research**](https://app.logz.io/#/dashboard/security/research/discover/) and build your query.

To turn the query into a rule, click on **Create from query > Create rule**. The rule will include the query and filters you've used.

![Rule from query](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/create-rule-from-query-dec.png)

Next, [name your rule](/docs/user-guide/cloud-siem/quick-guide/create-rules#name-the-rule), [set the trigger conditions](/docs/user-guide/cloud-siem/quick-guide/create-rules#set-trigger-conditions), [add MITRE ATT&Ck tags](/docs/user-guide/cloud-siem/quick-guide/create-rules#optional-mitre-attck-threats) if needed, [set schedule](/docs/user-guide/cloud-siem/quick-guide/create-rules#set-rule-schedule), and [choose the notification points](/docs/user-guide/cloud-siem/quick-guide/create-rules#optional-set-notification-details).

Once you're done, click **Save** to create the new rule. 



<!-- 
1. Sign in to Logz.io.

2. Go to **SIEM**.

3. Scroll down to the **Events** section. 

   ![Rules](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/events-1.png)


4. Click the **Investigate** tab next to the event that you want to base the new rule on.

5. Select **Create rule**.

   ![Rules](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/create-rule-from-query.png)

6. Fill out the rule details as follows:

   ![Rules](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/create-rule-from-query-2.png)

   * Give the rule a required name.
   
   * Define a query for the rule. You can do it directly in the **Create a rule** window and then preview it in OpenSearch Dashboards. Alternatively, you can define the query in OpenSearch Dashboards and copy it across.
   
   * Define what fields the query needs to be grouped by.
   
   * Define what accounts the query needs to apply to.
   
   * Repeat the previous three steps for another query, if required.
   
   * Define the trigger conditions for the rule.
   
   * If required, add a notification description to the rule. For example, a course of actions required when the rule is executed.
   
   * If required, add tags to the rule.
   
   * If required, add a notification endpoint in the **Recipients** list. This can be an email address or a webhook. See [Adding notification and SOAR endpoints](https://docs.logz.io/user-guide/cloud-siem/select-dashboards.html) for more on this.

6. Select **Save**.


-->