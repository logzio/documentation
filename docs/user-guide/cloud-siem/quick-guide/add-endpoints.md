---
sidebar_position: 6
title: Adding Notification and SOAR Endpoints
description: Adding notification endpoints to Logz.io's SIEM solution
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [SIEM, Security, Event Management, Endpoints, Notifications, SOAR]
---

A notification endpoint specifies where to send a notification for a rule execution. Logz.io offers several pre-configured endpoints, and you can easily add custom notification points using the **Custom** feature. Custom notification points are integrated with SOARs (security orchestration, automation, and response).

:::info note
You must be an account admin to add a notification endpoint.
:::

## Pre-configured notification endpoint


Navigate to your Logz.io [SIEM account > Settings > Notification endpoints](https://app.logz.io/#/dashboard/alerts/endpoints). 

Select **+ Add endpoint** to open the configuration wizard. Select the **type** of your endpoint, name it, and add a description. Add the required connection data, e.g., API key or Instance URL. You can test your endpoint by clicking **Run the test** or click **Add a new endpoint** to save it. 

![pre-configured endpoint](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/pre-endpoint-siem.png)

## Custom notification endpoint

Navigate to your Logz.io [SIEM account > Settings > Notification endpoints](https://app.logz.io/#/dashboard/alerts/endpoints). 

Select **+ Add endpoint** to open the configuration wizard, and choose the **Custom** option from the dropdown menu. Next:

* Name your endpoint
* Add the webhook URL
* Select the required method
* Add the webhook header

You can test your endpoint by clicking **Run the test** or click **Add a new endpoint** to save it. 

![custom endpoint](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem-quick-start/custom-siem-endpoint.png)