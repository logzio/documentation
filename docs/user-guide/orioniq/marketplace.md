---
sidebar_position: 4
title: Marketplace
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Browse and install pre-built AI agent templates from the OrionIQ Marketplace.
keywords: [OrionIQ, marketplace, agent templates, pre-built agents, incident, deployment, compliance, detection]
---

The OrionIQ Marketplace provides a catalog of pre-built agent templates that you can install and start using right away. These templates cover common observability and security use cases, so you can get value from OrionIQ without building agents from scratch.

To access the Marketplace, navigate to **OrionIQ > Marketplace** in the left navigation menu.

![OrionIQ Marketplace](https://dytvr9ot2sszz.cloudfront.net/logz-docs/orioniq/orioniq-marketplace.png)

## Browse agent templates

Agent templates are organized into the following categories:

| Category | Description |
|---|---|
| **Incident** | Agents that help investigate and resolve incidents, such as root cause analysis and support ticket investigation. |
| **Deployment** | Agents that validate system health after deployments and detect regressions. |
| **Compliance** | Agents that scan for sensitive data and help prevent compliance violations (for example, GDPR/CCPA). |
| **Detection** | Agents that monitor for security threats, suspicious logins, and brute-force attacks. |
| **Alerting** | Agents that filter and prioritize alerts to surface high-confidence, high-impact events. |
| **Performance** | Agents that identify early degradation patterns in latency, error rates, and throughput. |

Each card shows two tags: **Data** (Logs, Metrics, or Logs + Metrics) and **Trigger** (Scheduled, On demand, or Per alert). A card whose template sets neither shows no tags.

Use the search bar at the top of the page to find specific agent templates, or click a category tab to filter the list.

## Available templates

| Template | Category | Runs | What it does |
|---|---|---|---|
| **Alert AI Analysis** | Incident | When an alert fires | Correlates error logs, related metric anomalies, recent deployments, and the affected request paths, then summarizes the root cause with recommended remediation steps. This is the agent behind [AI Agent Analysis](/docs/open360/observability/ai-agent-analysis/). |
| **Root Cause Analysis** | Incident | On demand (API) | Reconstructs the incident timeline, correlates logs, metrics, and traces, inspects recent deployments and configuration changes, and produces a ranked set of probable root causes with supporting evidence and remediation recommendations. |
| **Incident Triage** | Incident | On demand (API) | Loads your runbook, walks through its diagnostic steps against live logs and metrics, evaluates the findings against the runbook's decision points, applies the prescribed remediation guidance, and produces a prioritized list of next steps for the responder. |
| **Exception Analysis** | Incident | Weekly | Reads the exceptions Logz.io already clusters for your account and groups variants of the same fault into families. Each family is sorted as new, spiking, ongoing, resolved, or muted, with occurrence counts, a trend, and a link to the logs. Daily runs open with a ranked list of what needs attention today. Exceptions you ask it to ignore stay muted, with your reason, until you ask for them back. Requires the Exceptions capability on the account, which Logz.io Support enables. |
| **Alert Digest** | Alerting | Weekly | Summarizes what fired, what resolved, and how long alerts stayed triggered, with a period-over-period comparison, top offenders, first-time alerts, and incident-like episodes. |
| **Alert Tuning Report** | Alerting | Weekly | Analyzes triggered-alert history across log and metric alerts and produces a ranked list of concrete tuning recommendations: flapping alerts, fast self-resolvers, severity miscalibration, alerts that always fire together, dead alerts, and services whose alerts went quiet. Each recommendation cites the current value, the proposed value, the supporting numbers, and a link to the alert definition. |
| **Error Logs Analysis** | Alerting | Daily | Breaks down errors and warnings by application, compares them with the previous period, and highlights spikes. |
| **Log Patterns Analysis** | Alerting | Weekly | Reads the patterns Logz.io already groups your logs into, for this period and the one before, at any log level. It reports patterns that are new, growing against their own earlier count, steady, or gone. Each item names the pattern's level and service and links to its logs, and the report closes with the share of logs the patterns matched. Exception-tagged logs are left to Exception Analysis. For a daily report, set the schedule to daily and change the opening "Cadence: weekly" in the message to "Cadence: daily". |
| **Log Distribution Monitor** | Performance | Daily | Analyzes log volume distribution and trends across services to detect anomalies, identify cost drivers, and keep logging healthy. |

### How Incident Triage works

Incident Triage executes your runbook step by step and follows its branches, recording each step as met, not met, branched, or skipped.

When the agent's integrations have **Read & Write** permission (see [Agent permissions](/docs/user-guide/orioniq/integrations/#agent-permissions)), it applies the remediation your runbook authorizes, such as updating a Logz.io alert, opening a Jira ticket, or adding a PagerDuty note, and marks each remediation item as applied or recommended.

It then checks live telemetry and reports the incident as resolved, contained, active, or needing escalation. A resolved verdict requires the triggering condition to be absent from the evidence and a runbook remediation to be in effect; otherwise the agent escalates to a human.

## Activate an agent template

Click a template card to open a three-step dialog: **Review**, **Set up**, and **Done**. The agent is created switched on when you finish **Set up**.

### Review

Review shows what the agent does before you commit: when it runs, what it produces, what data it needs, and its price per run. If the price can't be loaded, Review says so, and you can activate once it loads.

Click **Set up agent** to continue.

### Set up

The template decides which fields appear. A field shows only when the template lets you change it. Anything hidden keeps the template's value.

| Field | What you set |
|---|---|
| **Name** | Shown only when you already have agents from this template. It is prefilled, for example "Alert Digest 2". |
| **Runbook** | Required when the template needs one, as for Incident Triage. Shown for agents that run on demand. |
| **Data sources** | The accounts and connections the agent reads logs and metrics from. For an agent that reads logs, the account you are on is selected by default. |
| **Schedule** | For a scheduled agent: how often it repeats, the day, the hour, and the time zone. The next run is shown in the schedule's own zone. |
| **Send results to** | Who gets notified of the agent's results. |
| **Integrations** | The integrations the agent can use. |
| **Instructions** | The context message a scheduled agent runs with. |

Data sources, Send results to, and Integrations open in a picker. Each selected item has a remove button.

The side panel summarizes the agent, its expected runs, and its cost. On narrow screens the summary moves into the main column.

Billing choices:

* **After the free runs**: **Turn off** (the default) or **Keep running**, billed per run. If you can't see pricing, the choice is not offered.
* **Daily run limit**: For agents that run on demand, set the maximum runs a day. It starts at 5. Clear the box for no limit.

Click **Activate agent**. If required fields are missing, the dialog lists how many need attention and moves you to the first one. If you close the dialog after changing the setup, OrionIQ asks before it discards your changes.

Learning is off for agents activated from the Marketplace. You can turn it on later in the agent's **Agent details** form. See [Learning](/docs/user-guide/orioniq/create-agent/).

### Done

Done confirms the agent is active and shows what happens next:

* **First run**: the next scheduled time, "When you start it", or "When an alert fires".
* **Free runs**: how many are left.
* **After free runs**: whether the agent turns off or keeps running at your price per run.
* **Daily limit**: shown for agents that run on demand.
* **Results**: the recipients, or the run history in Agents Hub.

Click **Run a test** to start the agent once with sample input. It uses one of the free runs, or is billed at the price per run when the template has none. Results appear in the agent's run history in [Agents Hub](/docs/user-guide/orioniq/agents-hub/). If the test can't start because of a daily limit or budget cap, Done says which one.

Done also offers one optional follow-up. A scheduled agent with no recipients offers **Add recipients**. An agent that runs on demand offers **Connect an alert**.

The **What you set up** panel recaps your choices. To change them later, open the agent in Agents Hub.

Click **Open in Agents Hub** to see the new agent, or **Done** to close the dialog.

You can activate a template more than once. Once agents exist for a template, its card shows the number of active agents. Click it to open the Agents Hub filtered to those agents. To switch an agent off, use the Agents Hub.

## Free trial

Every agent you activate from the Marketplace starts with a free trial. The template card, the Review and Set up steps, and the Done step all show how many free runs the agent has.

When the free runs are used, the agent switches off automatically and nothing is charged. In the [Agents Hub](/docs/user-guide/orioniq/agents-hub/), the **Cost** column shows the runs left, and an agent whose trial is over is marked **Trial ended**. Nothing runs or is charged until you turn it back on, and turning it on again asks you to confirm that each run is billed.

Template cards and the Review step show your account's own price per run. If the price can't be loaded, the price is left out and the free trial is still offered.

If you can see pricing, Set up and the agent form also offer **Keep running** after the free runs. Select it to let the agent keep running, billed per run, once the trial ends.

If a template you're interested in is not yet available, click **Add to Wish List** to signal your interest. This helps Logz.io prioritize which templates to build next.

You can also click **+ Create New Agent** in the top right corner to build a custom agent from scratch.
