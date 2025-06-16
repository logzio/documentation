---
sidebar_position: 1
title: AI Agent
description: Enhance data insights with AI Agent and get AI-powered analysis of your data.
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [AI, observability, AI agent, Assistant, iq, logs, metrics, traces, siem, insights, analysis, services, logz.io]
---

The AI Agent is part of Logz.io’s Observability IQ suite. It provides an AI-powered, chat-based interface that lets you engage in a dynamic conversation with your data. Use it to go beyond passive data viewing and gain real-time insights into your metrics, anomalies, trends, and overall system health.

AI Agent is available in [Explore](https://app.logz.io/#/dashboard/explore), and as part of [Kubernetes 360](https://app.logz.io/#/dashboard/observability/k8s360), and [App 360](https://app.logz.io/#/dashboard/spm/service-overview).

The agent suggests queries to help you start your analysis, or you can type in your own questions.

The answers are based on the data currently shown on your dashboard. If you change the query, apply filters, or adjust the time range, any new responses from the agent will reflect the updated data.

Leverage these insights to enhance your analysis and make informed decisions.

![AI Agent screen](https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/ai-agent-june12.png)

## Using AI Agent

AI Agent is available in **[Explore](https://app.logz.io/#/dashboard/explore)**, **[Kubernetes 360](https://app.logz.io/#/dashboard/observability/k8s360)**, and **[App 360](https://app.logz.io/#/dashboard/spm/services/table)**. Click the AI Agent button at the top to open the interface.

Use the agent to analyze trends in latency, throughput, error rate, and HTTP status codes over time to identify patterns or anomalies that may require attention. Additionally, it can be used to compare the performance metrics of different operations and determine if any significant differences need to be addressed.

To get started with AI Agent, select one of the pre-built questions or type a custom query according to what you'd like to analyze.

_Once you interact with the agent, the current **dashboard data** is shared with Claude 3._

<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/ai-agent-results-june12.png" alt="ai-agent-screen" width="700"/>

### Turn AI Agent insights into dashboards and alerts

When the AI Agent identifies a spike, trend, or drop, you can turn that analysis into a dashboard panel (if you're using Logz.io Dashboards), or create an alert to track these insights.

**Create an alert** directly from a graph or result to track ongoing issues. The system will redirect you to the Create Alert page with all relevant data pre-filled.

**Add to dashboard** if you're using Logz.io Dashboards. You can insert the visualization into a new or existing dashboard for continued monitoring.

**Open the preview** to view the related logs in Explore.

<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/actions-from-agent.gif" alt="actions-from-agent" width="700"/>

### View chat history

History lets you review past interactions with the AI Agent, making it easier to track insights, revisit previous analyses, and maintain continuity in your investigations.

To access your chat history, open the AI Agent interface and click the History button.

<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/ai-history.png" alt="ai-agent-history" width="700"/>

### Start a new conversation

If you want to start a new investigation, click the pencil icon at the top. You'll be directed to the AI Agent main window, where you can choose one of the pre-generated questions or write your own query.

## AI Agent Root Cause Analyzer

Logz.io's Root Cause Analyzer (RCA) leverages GenAI to diagnose the root causes of exceptions within applications. By analyzing context and data, RCA delivers deep insights and actionable recommendations, streamlining the troubleshooting process and accelerating root cause analysis.

RCA dynamically adapts to the specific context of each issue, functioning like a knowledgeable team member. It understands the situation, identifies the information needed for analysis, and proactively gathers relevant data to provide accurate and effective analysis.

<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/rca/ai-agent-rca-june12.png" alt="rca-popup" width="700"/>


### How to use RCA

:::info note
RCA is currently available to Logz.io users using **[Explore](https://docs.logz.io/docs/user-guide/new-explore/)**.
:::


To activate RCA, navigate to [Explore > Exceptions](https://app.logz.io/#/dashboard/explore). Select the exception you want to analyze, then hover over it and click **AI Analyzer** to activate the RCA process.

<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/rca/exceptions-feb5.png" alt="rca-button" width="700"/>

Once activated, RCA begins a multi-step process, gathering relevant information, analyzing it, and taking further actions to identify the root cause of the issue. You can click on each step to view a detailed explanation of what RCA is doing to move closer to finding the root cause.

Please note that the analysis may take a few minutes. Once completed, RCA will display its **Root Cause Analysis**, outlining possible causes for the issue and providing recommendations to address it or prevent it from recurring.

<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/rca/rca-sum-feb5.png" alt="rca-end" width="700"/>



For further assistance with the AI Agent, read the [FAQ](https://docs.logz.io/docs/user-guide/observability/faq) or [contact Logz.io's Support Team](mailto:help@logz.io).