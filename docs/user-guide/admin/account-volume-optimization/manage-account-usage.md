---
sidebar_position: 1
title: Manage Account Usage
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Learn more about account utilization metrics and drop filters
keywords: [usage, volume, optimization, log management, account optimization, drop filters]
---

If your account is nearing its daily quota,
Logz.io sends an email alert to account administrators.
That's fine for most situations,
but what if you want to be more proactive in managing your accounts?

For this, you have _account utilization metrics_ (which saves log size and other metadata)
and drop filters (which allow you to stop ingestion of some logs).


## What are account utilization metrics? {#what-are-account-utilization-metrics}


Account utilization metrics capture a snapshot
of your account usage in regular increments
Logz.io starts logging your usage after your account reaches 10 MB in size.

## Enabling account utilization metrics and log size

![Sub account settings](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/utilization--save-account-utilization-metrics.png)

Account utilization metrics and log size are set per individual account.
You can find these settings
on the [Manage accounts](https://app.logz.io/#/dashboard/settings/manage-accounts) page
below **Advanced options**.
This page is available
only from your main account—you won't be able to make this change from a sub account.

:::note
Even though you need to be an **account admin** to enable this setting,
everyone who has access to your Logz.io account
can see the resulting logs.
:::


## Log utilization

Once you enable log utilization, you can choose the increment that suits your needs - every 10, 30, or 60 minutes.

You can find these logs in OpenSearch Dashboards when you filter for the `logzio_account_utilization` log type. They include the following fields:


| Field name | Description |
|---|---|
| account_id | Logz.io account ID |
| account_name | Name of this account |
| expected_utilization_EOD | Expected utilization by the end of the day, in percent |
| expected_volume_in_GB_EOD | The expected utilization by the end of the day, in GB |
| grace_capacity | The overage configured on the account, in percent. For instance, `120%` means that you have an overage allowance of 20% of your plan volume. |
| number_of_fields| The total number of fields in the current index |
| plan_retention_in_days| The number of days data is kept in the account until it is deleted|
| plan_volume_in_GB | Data allocated to this account, in GB |
| utilization | Current utilization, in percent |
| volume_in_GB | Current utilization, in GB |
| overall_plan_size_in_GB | Plan size, in GB |
| overall_overage_in_GB | This account's grace capacity, in GB |
| overall_limit_in_GB | This account's daily shipping limit, in GB |
| expected_overall_volume_in_GB_EOD | The expected utilization for all accounts by the end of the day, in GB |
| expected_overall_overage_in_GB_EOD | The expected overage by the end of the day, in GB |
| overall_volume_in_GB | Current utilization FOR ALL ACCOUNTS, in GB |

## Account utilization metrics for flexible accounts

The following fields are used for flexible volume accounts. 

| Field name | Description |
|---|---|
|is_flexible| Indicates whether the account is fixed or flexible (Boolean)|
|cap_volume| Optional maximum data volume for the account, in GB. This value can be 0: That is, the account has unlimited access to shared volume.|
|expected_volume_in_GB_EOD| An estimate of how much data the account will be used by the end of the day, in GB. The estimation is based on how much data was sent until the current hour. |
|reserved_volume| Volume guaranteed for the account per calendar day, in GB. This value can be 0: That is, no reserved volume is configured for the account. |
|used_from_shareable| The amount of data used from the shareable volume, in GB|

For flexible accounts, the amount of data you used from the shareable volume is derived from the difference between your current utilization and your reserved account volume: `used_from_shareable = volume_in_GB - reserved_volume`
Obviously, the value can't be negative: If you haven't used any of the shared volume, `used_from_shareable` will be normalized to 0.  

In your logs, you might see something like this: 

![Flexible volume metrics](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/flex_utilizn_metrix2.png) 


## Tracing utilization

Every Tracing account has the utilization option enabled by default, working in increments of 10 minutes. This lets you view and analyze your tracing data usage in real-time.

These logs are saved as part of your Tracing account and are visible from OpenSearch Dashboards. 

Navigate to OpenSearch Dashboards and select your **Tracing account**. Next, filter for the `logzio_tracing_account_utilization` log type.

![filter by type](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/tracing-focus-log-type.png)

Trace utilization logs include the following fields:

|Field name|Description|
|---|---|
|account_monthly_spans_limit|The maximum amount of spans you can send to this account each calendar month.|
|account_plan_allocation_percent|The percentage of the account from the overall budget.|
|current_daily_usage_count|The number of spans sent to your account today.|
|current_daily_usage_percent|A percentage that presents the number of spans sent to your account based on the account's daily limit and multiplier. You can change the multiplier per Tracing account on the [Manage accounts page](https://app.logz.io/#/dashboard/settings/manage-accounts).|
|current_monthly_usage_count|The number of spans sent to your account this month.|
|current_monthly_usage_percent|A percentage view of your monthly span usage.|
|daily_index_size_limit_suspension_factor|The number represents a multiplier of your estimated daily span account. You can [configure](https://app.logz.io/#/dashboard/settings/manage-accounts) a number ranging from x2 to x30 to limit the daily spans sent to the Tracing account. The default value is 8.|
|estimated_daily_usage_percent|A percentage estimation of how many spans will be used today.|
|estimated_monthly_usage_percent|A percentage estimation of how many spans will be used this month.|
|overall_budget_monthly_spans_number|The total amount of spans you can send to this account each calendar month.|
|tracing_account_id|Your Logz.io Tracing account ID|
|type|The log type, `logzio_tracing_account_utilization`.|


## Saving log size {#what-happens-when-i-save-log-size}

When you enable saving log size,
a new field is added to incoming logs.
This new field is called `LogSize`,
and it contains the size of the log line in bytes, taken as a single string.

OpenSearch Dashboards doesn't recognize `LogSize` as a number right away.
You can fix this by clicking <i class="fas fa-sync-alt"></i> (refresh mapping) for `LogSize` in OpenSearch Dashboards.
You'll need to do this for each account where you enabled `LogSize`.


<!--    
## Visualizing utilization with an ELK app

We offer a preconfigured dashboard
for account utilization metrics.
You can find this dashboard
in the [ELK Apps](https://app.logz.io/#/dashboard/apps)
by searching for "data volume dashboard".

![Data Volume Dashboard ELK app](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/utilization--elk-apps-data-volume-dashboard.png)

If you recently enabled account utilization metrics,
you may need to wait up to 60 minutes
before this data shows up in OpenSearch Dashboards.

-->

## Managing ingestion with drop filters

We recommend shipping only the logs you need
so that you don't end up paying for unnecessary data retention.

However, if you're sending logs that you'll need only sometimes
(such as debug logs),
you can set up a drop filter.

Logs caught by [drop filters](https://docs.logz.io/docs/user-guide/data-hub/drop-fiters/) aren't ingested,
so they won't count against your plan limits.
However, the volume of logs you can filter is based on your plan's quota.
For more information, see [Some important notes on drop filtering](https://docs.logz.io/docs/user-guide/data-hub/drop-fiters/#some-important-notes).
<!-- This number varies from one account to the next,
so please <a class="intercom-launch" href="mailto:help@logz.io">contact the Support team</a>
for more information on your drop filter limits. -->

:::caution Important
Dropped logs will never arrive at your Logz.io account,
so they can't be searched or trigger alerts.
Always confirm you're dropping the right logs when you apply a new filter.
:::