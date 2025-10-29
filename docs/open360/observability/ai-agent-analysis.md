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

* Go to your [Alerts](https://app.logz.io/360/alerts/triggered) page.

* Create a new alert or edit an existing one.

* Scroll to **AI Agent Analysis** and check the **Activate AI Agent Analysis** box:

    ![AI Analysis](https://dytvr9ot2sszz.cloudfront.net/logz-docs/open360/alerts/ai-agent-analysis-360.png)

* Click **Add instructions**. A pop-up will open where you can document a step-by-step flow and instructions for investigating and resolving this alert. [Read more about Alert instructions](https://docs.logz.io/docs/open360/alerts/instructions/). Click Save & Confirm to continue.


* Click the **Configure endpoint** link. You'll be directed to your General Settings page.

* Scroll down to the **AI Agent Analysis Endpoint** section and choose an endpoint for receiving the AI-generated analysis report. The list includes all of the Slack channels from your list of defined notification endpoints.

    ![notification endpoint](https://dytvr9ot2sszz.cloudfront.net/logz-docs/open360/alerts/general-settings-ai-config.png)

* Navigate **back to the alert** and scroll to the **Alert Metadata** section. It's required to add a clear, relevant description to help the AI generate more accurate, context-aware insights.

Finish to configure your alert and save it. Every time the alert triggers, it'll automatically run the AI Agent Analysis and provide you will more insights and data.

The report will be sent to your **configured Slack channel** or **email addresses added**, and can also be accessed anytime in the AI Agent chat by clicking the **View History** icon.

<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/alerts/ai-agent-history.gif" alt="agent-history" width="500"/>


## Need help?

* Step-by-step: [Configure an Alert](https://docs.logz.io/docs/open360/alerts/configure-alerts-explore/)

* [AI Agent FAQ](https://docs.logz.io/docs/open360/observability/faq/)

* [Contact Support](mailto:help@logz.io)