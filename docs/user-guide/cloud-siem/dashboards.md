---
sidebar_position: 10
title: Dashboards & Reports
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Create and view SIEM dashboards and reports
keywords: [SIEM, security dashboard, security, research, security rules, Security information]
---


Cloud SIEM offers preconfigured monitoring dashboards for numerous integrations.

## Dashboards

To see the list of available dashboards, navigate to **[SIEM > Dashboards](https://app.logz.io/#/dashboard/security/research/dashboards/list)**.

You can search dashboards by name or description or sort them by their creation date or last update.

![Logz.io Security Dashboards](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem/siem-dashboards-dec24.png)

Dashboards provided by Logz.io are labeled and locked for editing. To customize these dashboards, **duplicate** them and make changes to the copy. You can also create custom dashboards to complement Logz.io's pre-built options.


## Reports

You can automatically send reports about existing dashboards on a regular schedule over your preferred endpoints.

To view a list of your existing reports, navigate to **[SIEM > Reports](https://app.logz.io/#/dashboard/scheduled-reports)**.

You can create a report directly from a dashboard by clicking the **Create report** from the top menu. 

![Create a report](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem/create-report-siem-jan.png)

Or, you can create a report by navigating to **[SIEM > Reports > New Report](https://app.logz.io/#/dashboard/scheduled-reports/create)**.

When creating a new report, you'll need to provide the following details:

* Name your report and provide a brief description
* Select the dashboard you want to send as a report and the relevant time range
* Set up the report's delivery schedule using a [cron expression](https://www.freeformatter.com/cron-expression-generator-quartz.html)
* Select the relevant time zone you want to use for this report
* Add recipients by typing their email addresses or by clicking **New Recipients** to configure notification endpoints

Optionally, you can check the option to include a link to the live dashboard in the report and upload a custom logo for branding.

Once you've configured the report, click **Send Test** to verify its setup, and then click **Save** to activate the schedule.

![Create a report inner](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem/siem-create-report-jan.png)

For further information, read more about [scheduling reports](/docs/user-guide/log-management/reports/).

## Configuring visualizations for SIEM rules

If you've created a new SIEM rule and want to populate specific visualizations, you'll need to apply the correct tag when setting up the rule.

Visualization Tags:

* Access Events: `access`
* Threat Events: `network_threat`
* Audit Events: `audit`
* Endpoint Events: `endpoint_threat`

Adding the appropriate tag ensures that these visualizations are populated correctly.

![Create a report inner](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem/siem-add-tags-to-rule.png)

