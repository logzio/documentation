---
sidebar_position: 3
title: Alert Instructions
description: Add instructions that guide the AI Agent Analysis when an alert triggers.
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [Open 360, Alerts, AI Agent, Playbook, instructions, ai agent analysis, Observability, RCA, Automation]
#slug: /user-guide/alerts/runbooks.html
---

When you enable AI Agent Analysis, you can add instructions that act as a step-by-step playbook. The agent reads them when the alert fires and uses the instructions to run the right checks and suggest next steps.

### Add instructions

In the alert editor, enable **AI Agent Analysis**, select **+ instructions**, enter your text, choose **Save & Confirm**, then save the alert.

### How it works

Instructions are tied to the alert rule and run on every trigger. Use them to specify what to check, where to look, and what to try next. You can reference dashboards, panels, and links. Plain text only, up to 2,000 characters.

For **metric alerts**, you can link a dashboard and panel to add context.

### Writing guidelines 

For best results,keep it short, specific, and action-oriented. Use the exact names of dashboards, panels, services, or anything else in your environment that can help the analysis.

For example:

```md
Check Explore for `service.name:<SERVICE>` over last 15m; focus on `level:error` and exception keywords.
Look for a recent deploy in releases table; if found, diff config for `<SERVICE>`.
If a single operation drives >40% of errors, capture the last message.
```