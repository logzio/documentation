---
sidebar_position: 5
title: Utilities
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Connect external systems to OrionIQ agents using Utilities for context and interoperability.
keywords: [OrionIQ, utilities, integrations, external systems, collaboration, ticketing, CI/CD]
---

Utilities connect your OrionIQ agents to external systems, giving them access to additional context and enabling interoperability across your toolchain. For example, an agent can pull data from a ticketing system or push results to a collaboration platform.

To access Utilities, navigate to **OrionIQ > Utilities** in the left navigation menu.

![OrionIQ Utilities](https://dytvr9ot2sszz.cloudfront.net/logz-docs/orioniq/orioniq-utilities.png)

## Browse available utilities

Utilities are organized into the following categories:

| Category | Examples |
|---|---|
| **Monitoring & Observability** | Logz.io (connected by default), and other monitoring platforms. |
| **Incident Management** | PagerDuty, Opsgenie, and similar incident response tools. |
| **Collaboration** | Slack, Microsoft Teams, and other messaging platforms. |
| **Knowledge Management** | Confluence, Notion, and documentation platforms. |
| **Ticketing** | Jira, ServiceNow, and other issue tracking systems. |
| **Cloud Platform** | AWS, Azure, GCP, and other cloud providers. |
| **Container & Orchestration** | Kubernetes and container management tools. |
| **CI/CD** | Jenkins, GitHub Actions, and other deployment pipelines. |
| **Version Control** | GitHub, GitLab, and other source control platforms. |
| **Auth & IAM** | Identity and access management systems. |
| **Secrets** | Secret management tools such as HashiCorp Vault. |
| **Database** | Database management and querying tools. |

Use the search bar to find a specific utility, or click a category tab to filter the list.

## Connect a utility

Click **Connect** on a utility and choose an authentication method. Which methods a utility offers depends on the utility:

| Method | Description |
|---|---|
| **OAuth 2.0** | Authorize Logz.io through the provider's own consent flow. |
| **API Key** | Connect using the provider's API token. |
| **Basic Auth** | Connect with an email address and API token. |

## Logz.io API access

The Logz.io utility is connected by default and gives agents access to your observability data. You can also grant agents scoped access to the Logz.io public API, per account:

| Scope | Grants |
|---|---|
| **Telemetry** | Logs and metrics access for the agent. Always on for every accessible account and not configurable. |
| **Read** | The agent can call the Logz.io public API but can't change anything. |
| **Write** | The agent can create and update Logz.io objects. Implies Read. |
| **Admin** | The agent has the same role as Manage API Tokens. Implies Read and Write. |

Enabling API access creates one system-generated API token per selected account, at the highest scope you chose. Changing or turning off API access deletes that token; agents keep their telemetry access, and a lower scope gets a new token at that scope.

Owner, sub-accounts, and Security accounts have a public API. Metrics, Timeless, and Restored accounts do not, so API scopes aren't available for them.

To request access to a utility that isn't yet available, click **Add to Wish List** on the utility you're interested in. This helps Logz.io prioritize which integrations to support next.

:::note
Utilities is an evolving capability. New integrations are added regularly based on user demand.
:::
