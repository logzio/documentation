---
sidebar_position: 2
title: PagerDuty Endpoint Configuration
description: Integrate Logz.io with PagerDuty to trigger real-time incidents from alerts.
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logz.io, pagerduty, pagerduty integration, incident management, alerting, logz.io alerts, real-time alerts, observability, notification endpoint, incident automation, logz.io setup, pagerduty setup, monitoring integration]
---

Logz.io is an AI-powered observability platform that helps teams monitor, troubleshoot, and secure their applications using logs, metrics, and traces. It also offers GenAI-driven features to enhance observability workflows.

Integrating Logz.io with PagerDuty lets you automatically create incidents when alerts are fired, ensuring your on-call teams receive real-time notifications and can respond quickly, based on your PagerDuty service configurations.

## Prerequisites

Before you begin you’ll need:

* Logz.io access with Admin role.
* PagerDuty access with Admin permissions.
* A new or existing PagerDuty service.

## Step 1: Set up the integration in PagerDuty

You can connect Logz.io to either a new or an existing service in PagerDuty.

### Option A: Create a new service

In PagerDuty, navigate to **Services > Service Directory** and click **+New Service**. Give your service a name, choose whether to create a new escalation policy or use an existing one, and configure alert grouping if needed. 

In the **Integrations** section, select **Logz.io** from the list and complete the setup.

![PagerDuty create a service](https://dytvr9ot2sszz.cloudfront.net/logz-docs/notification-endpoints/pagerduty-create-a-service.png)

After saving, you’ll be redirected to the service’s Integrations page. Copy the generated **Integration Key**.

### Option B: Add Logz.io to an existing service

In the **Service Directory**, click the name of the service you'd like to update. Go to the **Integrations tab** and click **Add a new integration**.

Select **Logz.io** from the integration list and click **Add**. After saving, you’ll be redirected to the Integrations page. Copy the generated **Integration Key**.

![PagerDuty key](https://dytvr9ot2sszz.cloudfront.net/logz-docs/notification-endpoints/pagerduty-key.png)

## Step 2: Create a PagerDuty endpoint in Logz.io

In your **Logz.io account**, go to **Settings > Notification Endpoints** and click **+ Add Endpoint**. 

![Notification endpoints](https://dytvr9ot2sszz.cloudfront.net/logz-docs/notification-endpoints/notification-endpoints.png)

Choose **PagerDuty** as the endpoint type. Enter a name and optional description, then paste the **Integration Key** copied from PagerDuty. 

Before using the endpoint, click **Run the test** to verify that Logz.io can send data to PagerDuty successfully.

Click **Add a new endpoint** to save.

![Add a new endpoint](https://dytvr9ot2sszz.cloudfront.net/logz-docs/notification-endpoints/add-an-endpoint-pager.png)


:::note
You can create multiple Logz.io integrations in PagerDuty by adding them to new or existing services. Each integration generates a unique key that can be used to create a separate notification endpoint in Logz.io.
:::

## Step 3: Attach the endpoint to a Logz.io alert

In **Logz.io**, navigate to the **Alerts page**. Select an existing alert or create a new one. 

In the **Select notification recipients** section, choose the **PagerDuty** endpoint you created. 

![Select PagerDuty endpoints](https://dytvr9ot2sszz.cloudfront.net/logz-docs/notification-endpoints/choose-pagerduty-from-list.png)

When triggered, the alert sends a notification to PagerDuty, which generates a new incident based on your service settings.

## PagerDuty integration with Logz.io's RCA capabilities

Connect PagerDuty incidents to Logz.io’s Root Cause Analyzer (RCA) so each incident triggers an automatic analysis and send findings back to PagerDuty.

### How it works

Within PagerDuty’s Incident Workflows, a new action is available: “Initiate RCA in Logz.io”. No custom scripting is needed - the action is built-in.

When an incident triggers, Logz.io automatically runs AI-powered Root Cause Analysis (RCA) across logs, metrics, traces, and deployments. Results are returned directly inside PagerDuty notifications (email, Slack, etc.), shortening investigation time.

Logz.io’s RCA uses historical PagerDuty incidents to learn how similar issues were resolved, and builds dynamic playbooks based on those past actions, so users don’t need to manually maintain RCA instructions. Optionally, teams can embed existing Confluence/Jira runbooks or add instructions in plain English.

Read more about Logz.io's [AI Agent Root Cause Analyzer](https://docs.logz.io/docs/user-guide/observability/assistantiq/#ai-agent-root-cause-analyzer).

![Pagerduty Logz.io RCA](https://dytvr9ot2sszz.cloudfront.net/logz-docs/notification-endpoints/pagerrca.png)


## Troubleshooting

### No incident is created in PagerDuty?

* Check that the alert is active.
* Verify the Service Key (Integration Key) is correct.
* Ensure the endpoint is connected to the correct alert.
* Use the Run Test feature to confirm connectivity.

### Can’t find Logz.io in the integration list?

* Confirm your PagerDuty plan supports custom integrations.
* Ensure you have the necessary account permissions.

If you have questions or run into issues while setting up the integration, contact [Logz.io Support](mailto:help@logz.io).