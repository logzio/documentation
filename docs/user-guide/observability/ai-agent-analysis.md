---
sidebar_position: 2
title: AI Agent Analysis
description: Enable automated AI-powered root cause analysis for your alerts in Logz.io.
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [AI, observability, AI agent, proactive, proactive rca, rca, root cause analysis, Assistant, iq, logs, metrics, traces, siem, insights, analysis, services, logz.io, log alerts, real-time rca]
---

:::info note
AI Agent Analysis is currently in **beta**. We're actively improving it based on user feedback, so functionality and results may evolve over time.
:::

AI Agent Analysis automates investigations when alerts are triggered in your Logz.io environment—helping you understand not just what happened, but why.

When an alert fires, the AI Agent instantly kicks into action. It analyzes logs, metrics, and patterns around the event to uncover root causes and surface key findings—delivering real-time, actionable insights directly to a chosen Slack channel and storing them in the AI Agent chat for future reference.

By minimizing the gap between detection and resolution, AI Agent Analysis helps you act faster, especially for high-impact services or workflows where every second counts.


## Activate AI Agent Analysis

:::caution note
AI Agent Analysis runs **once every hour**.
:::

To enable AI Agent Analysis:

* Go to your [Alerts](https://app.logz.io/#/dashboard/triggers/alert-definitions) page.

* Create a new alert or edit an existing one.

* Scroll to the bottom of the alert settings page and check the box in the AI Agent Analysis section:

    ![AI Analysis](https://dytvr9ot2sszz.cloudfront.net/logz-docs/alerts/ai-agent-analysis-checked.png)

* Click the **Configure endpoint** link. You'll be directed to your General Settings page.

* Scroll down to the **AI Agent Analysis Endpoint** section and choose an endpoint for receiving the AI-generated analysis report. The list includes all of the Slack channels from your list of defined notification endpoints.

    ![notification endpoint](https://dytvr9ot2sszz.cloudfront.net/logz-docs/alerts/notification-endpoint.png)

* Navigate **back to the alert** and add a clear, relevant description—this is required and helps the AI generate more accurate, context-aware insights.

Once saved, the alert will automatically run AI Agent Analysis every time it's triggered.

The report will be sent to your **configured Slack channel** and can also be accessed anytime in the AI Agent chat by clicking the **View History** icon.

<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/alerts/ai-agent-history.gif" alt="agent-history" width="500"/>


## Need help?

* Step-by-step: [Configure an Alert](/docs/user-guide/explore/explore-log-alerts/configure-alerts-explore/)

* [AI Agent FAQ](https://docs.logz.io/docs/user-guide/observability/faq)

* [Contact Support](mailto:help@logz.io)