---
sidebar_position: 8
title: Settings
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Configure your OrionIQ theme, the assistant's name, AI spend limits, and where your account data and LLM are hosted.
keywords: [OrionIQ, settings, capping, budget, limits, theme, regions, assistant name]
---

OrionIQ settings are grouped into four sections, reachable from **Settings** in OrionIQ.

## User

Settings that apply to you alone.

| Setting | Description |
|---|---|
| **Theme** | Choose how OrionIQ looks for you — Light or Dark. |
| **Email** | The email of the logged-in user. Read-only. |

## Account

Settings that apply to everyone on the account.

| Setting | Description |
|---|---|
| **OrionIQ name** | The name everyone on the account uses to address the assistant. It appears in the sidebar. |
| **OrionIQ Regions** | Where your account data is stored (**Data hosting**) and where the LLM serving OrionIQ runs (**LLM model hosting**). Both are set during account provisioning and can't be edited. |
| **Agent permissions** | What OrionIQ agents may do on connected integrations account-wide — **Read** or **Read & Write**. Read by default. Admins only. |

While **Agent permissions** is set to Read, no individual connection can be granted write access. Turning it on to Read & Write doesn't grant write access to every connection by itself — each connection still needs write enabled on it, in [Integrations](/docs/user-guide/orioniq/integrations/#agent-permissions-on-a-connection).

## Capping

Controls what OrionIQ is allowed to spend. Admins can also reach this from the **Capping** button on the [Agents Hub](/docs/user-guide/orioniq/agents-hub/).

| Limit | Description |
|---|---|
| **Monthly Budget** | Your configurable AI budget for the calendar month. Resets every month. |
| **Daily Invocation Limit** | System-enforced daily invocation limit across your account. Resets at midnight UTC. |
| **Account Daily Token Limit** | System-enforced daily token limit for AI chat across your account. Resets at midnight UTC. |

A limit can carry a **soft limit** — a warning threshold that sends a notification when usage crosses it, without blocking invocations.

### Trial and free accounts

Trial and free accounts get a fixed **Budget**, shared by AI Chat and AI Agents, that **does not reset**, plus an additional **Daily Budget** that resets at midnight UTC. AI pauses for the rest of the day when the daily budget is reached.

Neither limit can be edited. Upgrade to a paid plan to set your own budget.

## Logz.io

Account-level settings beyond OrionIQ — billing, users, regions, and platform configuration — live in the Logz.io console. Click **Open Logz.io settings** to go there.

:::note
Per-agent daily caps are set on the agent itself, not here. See [Create an Agent](/docs/user-guide/orioniq/create-agent/).
:::
