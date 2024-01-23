---
sidebar_position: 4
title: Reports
description: Create and send reports
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logz.io, reports, share data, log analysis, observability]
---




Logz.io reports allow you to automatically send dashboards on a regular schedule over Slack and email.



### Configure report's name and description

Navigate to [Logs > Reports > Create a report](https://app.logz.io/#/dashboard/scheduled-reports/create).

Choose a name for your report. The name will be shown as the email subject or Slack heading.

The description will be included in the message body.
It's a good idea to use the description to give some context
for why recipients are receiving the report.

### Select a dashboard and time range

In the form, under **Which dashboard to send**, select a dashboard from the list.

Next, select the time range for the dashboard. Under **For this time range**, select the time frame in minutes/hours/days. Your time range can be anything from 1 minute to 30 days.

### Set the schedule

Use the **Cron scheduler** to set the schedule for your reports to be sent automatically. 

You can use an online tool such as the
[Quartz Cron Expression Generator](https://www.freeformatter.com/cron-expression-generator-quartz.html#cronexpressionexamples/) to easily translate your requirements to a cron expression. The scheduler can be used to set up advanced schedules, like the last day of every month, or the last Thursday of the month at a specific hour.

### Select your recipients

Use **Who to send it to** to choose the report's email and Slack recipients.

### Add custom logo & sharing link

![Logz.io report scheduling form](https://dytvr9ot2sszz.cloudfront.net/logz-docs/dashboards/new-report.png)

You will find more options at the bottom of the form:

* **Custom logo**: You can enable the option to include your account's **Custom logo** in the report.

  When the report is sent over email, the custom logo will be included in the email body and PDF header. Admins can upload and update a custom logo from the [General Settings](https://app.logz.io/#/dashboard/settings/general) page.

* **View in OpenSearch Dashboards link**: You can enable the option to **Include a link to the live dashboard in the message**.

  If enabled, the report will include a direct link to the dashboard in Logz.io. Your recipients will need to log in to Logz.io to see it.



Here's an example of what the report email might look like.

![Example of Logz.io report email](https://dytvr9ot2sszz.cloudfront.net/logz-docs/dashboards/demo-report-email.png)


### Creating a report

* Open a dashboard, and click **Create report** from the dashboard menu.

  ![Create a report from a Dashboard](https://dytvr9ot2sszz.cloudfront.net/logz-docs/kibana/create-report-osd.png)

* From **Logs > Reports** in the navigation menu, click the yellow <i class="fas fa-plus"></i> icon to open the **Create a report** page. 

![Create a report from navigation](https://dytvr9ot2sszz.cloudfront.net/logz-docs/kibana/reports-from-navigation.png)

