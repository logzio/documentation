---
sidebar_position: 2
title: Investigate Security Events
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Manage and Investigate Security Events
keywords: [SIEM, Security, Security events, investigate, Security information]

---


Cloud SIEM logs a security event every time a rule triggers. The terms **triggered rules** and **security events** have the same meaning and are used interchangeably.

The event log includes details about the security incident and the rule that caused it to trigger. It also offers an **Investigate** link to quickly pull up the logs that triggered the specific event.

:::caution Important
You cannot configure rules using the `logzio-alert` log type. This type is ignored by the rule engine.
:::

![Logz.io Cloud SIEM Summary page](https://dytvr9ot2sszz.cloudfront.net/logz-docs/security-analytics/investigate-600px.png)

### Log fields of interest

| Field | Description |
|--|--|
| Time | Indicates when the rule triggered|
| logzio-alert-title | The name of the security rule in your Cloud SIEM |
| logzio-alert-triggered-severity | Severity of the event, as defined in the rule's trigger settings. It is customizable. |
| logzio-hits | The number of logs involved in the security event. This is the number of logs that triggered the security rule before applying any aggregations, if applicable. |
| logzio-investigate | Click the **Investigate** button to pull up the logs responsible for triggering the rule. The appropriate filters and search query are already applied to ensure it returns only the relevant logs. |


### Other paths of investigation

You can click the >**<i class="fas fa-angle-right"></i>** button to expand the document. You'll be able to view the full event log and view surrounding documents.

### Log retention concerns

Logs of security events, that is logs of triggered rules, are kept for 10 years. This ensures that details concerning security incidents are kept on record and can be investigated and re-visited many months and even years after the fact, as new findings come to light.

When you click the **Investigate** button for an event, you are pulling up logs from your short-term logging account. The availability of these logs depends on the retention plan in your Log Analytics account.

Log retention typically spans between 3-30 days. If you are an admin of the main logging account, you can look up the retention policy on the [Manage accounts](https://app.logz.io/#/dashboard/settings/manage-accounts) page.

### Investigate expired logs

If you would like to investigate logs after they have expired from the logging database, you have the following options:

1. Set up [archiving](https://docs.logz.io/docs/user-guide/data-hub/archive-restore/archive-and-restore/). Once logs are no longer in retention, they can be restored from the archive.

2. Set up [Optimizers](https://docs.logz.io/docs/user-guide/log-management/long-term-storage/configure-optimizers/) to capture logs and save them to a [Timeless account](/docs/user-guide/admin/logzio-accounts/manage-the-main-account-and-sub-accounts/#timeless).
