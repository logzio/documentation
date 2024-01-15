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

![Logz.io Security Dashboards](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem/cloud-siem-dashboards-jan.png)

Note that dashboards provided by Logz.io are labeled and locked to editing. You can duplicate them to make them your own.
You can always create your own dashboards to add to Logz.io's pre-built dashboards.

## Reports

You can automatically send reports about existing dashboards on a regular schedule over your preferred endpoints.

Open a dashboard and click **Create report** from the top menu. 

![Create a report](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem/create-report-siem-jan.png)

You can also create a report by navigating to **[SIEM > Reports > New Report](https://app.logz.io/#/dashboard/scheduled-reports/create)**.

Next: 

* Name your report and provide a description
* Select the dashboard you want to send as a report and the relevant time range
* Choose when you want to send the report using a [cron expression](https://www.freeformatter.com/cron-expression-generator-quartz.html)
* Select the relevant time zone you want to use for this report
* Add the relevant recipients. You can type email addresses to add them or click on **New recipients** to configure notification endpoints

Finally, you can check the box to include a link to the live dashboard in the message and add a custom logo to the report.

Click **Send test** to verify your report, and **Save** to activate it.


![Create a report inner](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem/siem-create-report-jan.png)


For further information, read more about [scheduling reports](/docs/user-guide/log-management/reports/).
