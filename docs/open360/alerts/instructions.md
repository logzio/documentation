---
sidebar_position: 3
title: Alert Instructions
description: Add instructions that guide the AI Agent Analysis when an alert triggers.
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [Open 360, Alerts, AI Agent, Playbook, instructions, ai agent analysis, Observability, RCA, Automation]
#slug: /user-guide/alerts/runbooks.html
---

When you enable AI Agent Analysis, you can add instructions that act as a step-by-step playbook. The agent reads them when the alert fires and uses the instructions to run the right checks and suggest next steps.

### How it works

Instructions are saved on the alert rule and run on every trigger. The AI Agent reads them as a playbook to decide what to check, where to look, and what to do next.

Write in plain text, up to 2,000 characters. You can reference dashboards, panels, queries, links, and any other resources in your environment.

Instructions work for both log and metric alerts. For **metric alerts**, you'll need to link a dashboard and panel first to give the analysis the needed context.


### Add instructions

In the alert editor, enable **AI Agent Analysis**, and select **+ Add Instructions**.

<img src="https://dytvr9ot2sszz.cloudfront.net/logz-docs/open360/alerts/ai-agent-analysis-step.png" alt="edit-alerts" width="700"/>

Next, enter your instructions, choose **Save & Confirm**, then save the alert.

### Writing guidelines 

For best results, keep it short, specific, and action-oriented. Use the exact names of dashboards, panels, services, etc. 

For example:

```md
Check Explore for `service.name:<SERVICE>` over last 15m; focus on `level:error` and exception keywords.
Look for a recent deploy in releases table; if found, diff config for `<SERVICE>`.
If a single operation drives >40% of errors, capture the last message.
```