---
sidebar_position: 2
title: Proactive Root Cause Analysis
description: Enable automated AI-powered root cause analysis for your alerts in Logz.io.
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [AI, observability, AI agent, proactive, proactive rca, rca, root cause analysis, Assistant, iq, logs, metrics, traces, siem, insights, analysis, services, logz.io, log alerts, real-time rca]
---

Proactive Root Cause Analysis (RCA) automates AI-driven investigations when alerts are triggered in your Logz.io environment. Instead of manually initiating RCA after an incident, this feature automatically analyzes the root cause the moment an alert fires—delivering actionable insights in real time.

By reducing the gap between detection and resolution, Proactive RCA helps you understand not just that an alert occurred, but why it happened.

## Activate Proactive RCA

Proactive RCA is especially useful for alerts tied to high-impact services or workflows, where rapid investigation is critical.

To activate it, go to [Alerts](https://app.logz.io/#/dashboard/triggers/alert-definitions), then either create a new alert or edit an existing one. In the AI Agent Analysis section, check the box to enable Proactive RCA. Make sure to include a clear and relevant description in the alert, as this helps the AI generate more accurate and contextual insights.

![AI Analysis](https://dytvr9ot2sszz.cloudfront.net/logz-docs/alerts/ai-agent-alert-step.png)

Once saved, the alert is ready to run RCA automatically when triggered.

When an alert fires, the AI Agent analyzes related logs, metrics, and patterns, then generates a summary of key findings. The results are sent to your configured Slack notification channel and also stored in the AI Agent chat for future reference.

<!--![AI Agent screen](https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/ai-agent-dec3.png)-->

For a step-by-step walkthrough on setting up an alert, see [Configure an Alert](/docs/user-guide/explore/explore-log-alerts/configure-alerts-explore/).

For further assistance with the AI Agent, read the [FAQ](https://docs.logz.io/docs/user-guide/observability/faq) or [contact Logz.io's Support Team](mailto:help@logz.io).
