---
sidebar_position: 2
title: PagerDuty Endpoint Configuration
description: Integrate Logz.io with PagerDuty to trigger real-time incidents from alerts.
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logz.io, pagerduty, pagerduty integration, incident management, alerting, logz.io alerts, real-time alerts, observability, notification endpoint, incident automation, logz.io setup, pagerduty setup, monitoring integration]
---

Logz.io is an AI-powered observability platform that helps teams monitor, troubleshoot, and secure their applications using logs, metrics, and traces. It also offers GenAI-driven features to enhance observability workflows.

Logz.io integrates with PagerDuty to automatically create incidents from Logz.io alerts. This ensures on-call teams receive real-time notifications and can respond quickly, based on PagerDuty service configurations.

Beyond basic alerting, this integration also supports AI-driven Root Cause Analysis (RCA). Incidents in PagerDuty can trigger Logz.io’s RCA Agent, which analyzes observability data (logs, metrics, traces, deployments) and enriches incidents with contextual insights and recommended fixes.

## Prerequisites

Before you begin you’ll need:

* Logz.io access with Admin role
* PagerDuty access with Admin permissions
* A new or existing PagerDuty service

## Step 1: Configure PagerDuty

You can connect Logz.io to a new or existing service in PagerDuty.

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

Click **Run the test** to verify that Logz.io can send data to PagerDuty successfully.

Click **Add a new endpoint** to save.

:::note
You can create multiple Logz.io integrations in PagerDuty by adding them to new or existing services. Each integration generates a unique key that can be used to create a separate notification endpoint in Logz.io.
:::

![Add a new endpoint](https://dytvr9ot2sszz.cloudfront.net/logz-docs/notification-endpoints/add-an-endpoint-pager.png)


## Step 3: Attach the endpoint to a Logz.io alert

In **Logz.io**, navigate to the **Alerts page**. Select an existing alert or create a new one. 

In the **Select notification recipients** section, choose the **PagerDuty** endpoint you created. 

![Select PagerDuty endpoints](https://dytvr9ot2sszz.cloudfront.net/logz-docs/notification-endpoints/choose-pagerduty-from-list.png)

When triggered, the alert sends a notification to PagerDuty, which generates a new incident based on your service settings.

## PagerDuty integration with Logz.io's RCA capabilities

PagerDuty incidents can automatically trigger Logz.io’s Root Cause Analyzer (RCA), triggering an automatic analysis and sending findings back to PagerDuty.

### How it works

When an alert in Logz.io fires, a PagerDuty incident is created. PagerDuty’s automation agent immediately handles the initial triage by opening communication channels and, if configured, updating the status page.

Once the incident is active, PagerDuty enriches it with context from similar past incidents. This includes historical timelines, successful remediation steps, and information about who resolved comparable issues.

Logz.io’s RCA Agent then runs a deep analysis of the real-time logs, metrics, and traces, combining this data with the enriched incident context. The output is a recommended fix or next step tailored to the current problem.

For low-risk issues, the RCA Agent can attempt an automatic remediation, such as restarting a service. If remediation is not safe or fails, PagerDuty escalates the incident to a human responder, who receives the RCA summary and recommended fix.

Finally, once the incident is resolved, PagerDuty updates stakeholders, records the RCA findings, and stores them for future reference. The next time a similar incident occurs, PagerDuty can surface these previous learnings to reduce resolution time even further.

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