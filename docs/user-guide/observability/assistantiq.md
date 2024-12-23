---
sidebar_position: 1
title: AI Agent
description: Enhance data insights with AI Agent and get AI-powered analysis of your data.
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [AI, observability, AI agent, Assistant, iq, logs, metrics, traces, siem, insights, analysis, services, logz.io]
---

AI Agent is part of Logz.io's Observability IQ suite. It provides an AI-powered, chat-based interface that lets you engage in a dynamic conversation with your data. Use it to move beyond passive data viewing and get real-time insights about your metrics, anomalies, trends, and the overall health of your environment.

AI Agent is available in [Explore](https://app.logz.io/#/dashboard/explore), and as part of [Kubernetes 360](https://app.logz.io/#/dashboard/observability/k8s360), and [App 360](https://app.logz.io/#/dashboard/spm/service-overview).

The agent suggests a few queries you can run on your data to help you start the analysis and deep-dive, or you can type your own questions.

The answers are based on the data currently shown on your dashboard. Once you change the query, apply filters, or change the time period, any new answer from the agent will be based on the newly generated data. 

You can now leverage the insights from your dialog and enhance data analysis to make informed decisions.

![AI Agent screen](https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/ai-agent-dec3.png)

## Using AI Agent

AI Agent is available in **[Explore](https://app.logz.io/#/dashboard/explore)**, **[Kubernetes 360](https://app.logz.io/#/dashboard/observability/k8s360)**, and **[App 360](https://app.logz.io/#/dashboard/spm/services/table)**. Click the AI Agent button at the top to open the interface.

Use the agent to analyze trends in latency, throughput, error rate, and HTTP status codes over time to identify patterns or anomalies that may require attention. Additionally, it can be used to compare the performance metrics of different operations and determine if any significant differences need to be addressed.

Select one of the pre-built questions or type a custom query according to what you'd like to analyze. Next, select the data source you'd like to use when using the AI Agent:

* **All available data** - Utilize all available data, including logs and documentation.
* **Using search results** - Answers will be based on the data currently displayed on your dashboard, including logs, queries, filters, etc.
* **User guide** - Access information from Logz.io's user guides to answer questions about features and usage.
* **Data shipping guide** - Refer to integration and data shipping guides for configuration and setup assistance.

:::note
Some data sources may not be available in all observability tools (Explore, App 360, Kubernetes 360).
:::

Once you provide input to the agent, the **dashboard's data** will be shared with Claude3.

<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/explore-dashboard/ai-agent-main-dec23.png" alt="ai-agent-answer" width="700"/>

## AI Agent Root Cause Analyzer

Logz.io's Root Cause Analyzer (RCA) leverages GenAI to diagnose the root causes of exceptions within applications. By analyzing context and data, RCA delivers deep insights and actionable recommendations, streamlining the troubleshooting process and accelerating root cause analysis.

RCA adapts dynamically to the specific context of each problem, functioning like a knowledgeable team member who understands the nuances of the issue and provides accurate and effective analysis.

It comprehends the situation, identifies the necessary information for thorough analysis, and proactively seeks the data required.

<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/rca/root-cause-analyzer-start.png" alt="rca-popup" width="700"/>


### How to use RCA

:::info note
RCA is currently available to Logz.io users in the **US region** using **[Explore](https://docs.logz.io/docs/user-guide/new-explore/)**.
:::


To activate RCA, navigate to [Explore > Exceptions](https://app.logz.io/#/dashboard/explore). Select the exception you want to analyze, then hover over it and click **AI Analyzer** to activate the RCA process.

<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/rca/ai-analyzer-rca.png" alt="rca-button" width="700"/>

Once activated, RCA begins a multi-step process, gathering relevant information, analyzing it, and taking further actions to identify the root cause of the issue. You can click on each step to view a detailed explanation of what RCA is doing to move closer to finding the root cause.

Please note that the analysis may take a few minutes. Once completed, RCA will display its **Root Cause Analysis**, outlining possible causes for the issue and providing recommendations to address it or prevent it from recurring.

<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/rca/root-cause-analysis-rca-end.png" alt="rca-end" width="700"/>



For further assistance with the AI Agent, read the [FAQ](https://docs.logz.io/docs/user-guide/observability/faq) or [contact Logz.io's Support Team](mailto:help@logz.io).