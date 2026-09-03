---
sidebar_position: 5
title: Integrations
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Connect external systems to OrionIQ agents so they can use them as context and act on them.
keywords: [OrionIQ, integrations, connections, external systems, collaboration, ticketing, observability]
---

Integrations connect your OrionIQ agents to external systems, giving them access to additional context and enabling interoperability across your toolchain. For example, an agent can pull data from a ticketing system or push results to a collaboration platform.

To access Integrations, navigate to **OrionIQ > Integrations** in the left navigation menu.

![OrionIQ Integrations](https://dytvr9ot2sszz.cloudfront.net/logz-docs/orioniq/orioniq-utilities.png)

The page has two tabs:

* **Catalog** — every integration OrionIQ supports, and where you connect one.
* **Management** — the connections your account has already made, and their health.

## Catalog

Integrations are organized into the following categories:

| Category | Examples |
|---|---|
| **Observability** | Logz.io, Datadog, Grafana, AWS CloudWatch, New Relic |
| **Incident Management** | PagerDuty, Opsgenie, FireHydrant, incident.io, Rootly |
| **Communication** | Slack, Microsoft Teams |
| **Service Management** | Jira Cloud, Jira Service Management, Intercom, Asana |
| **Knowledge & Content** | Confluence Cloud, Agility CMS |
| **Developer Tools** | GitHub, GitLab, Argo CD |
| **Cloud & Infrastructure** | AWS EC2, AWS ECS, AWS EKS, AWS Lambda |
| **Databases & Warehouses** | AWS DynamoDB, AWS RDS, Azure SQL Database, ClickHouse, Databricks |
| **Security & Identity** | 1Password, AbuseIPDB, Aikido Security |
| **Analytics & BI** | Amplitude, Databox, Fathom |
| **AI & Machine Learning** | Anthropic, AI21 Labs |
| **Files & Docs** | Airtable, Box, Canva |
| **Sales & CRM** | Salesforce, Gong, Apollo.io |
| **Marketing & Social** | ActiveCampaign, Ahrefs |
| **Finance & Payments** | AWS Cost Explorer, Azure Cost Management, Alpaca |
| **HR & People** | BambooHR, Ashby, Breezy HR |

Use the search bar to find a specific integration, or click a category tab to filter the list. The catalog is ordered by popularity, so the integrations most accounts connect appear first.

## Connect an integration

Click **Connect** on an integration and provide its credentials. Which method an integration uses depends on the integration:

| Method | Description |
|---|---|
| **API Key** | Connect using the provider's API token. This is what most integrations use. |
| **Basic Auth** | Connect with an email address and API token. |
| **None** | A few public data sources, such as MITRE ATT&CK and Hacker News, need no credentials at all. |

### Agent permissions on a connection

Integrations OrionIQ has cleared for write actions show an **Agent permissions** choice in the connect (or edit) dialog: **Read** or **Read & Write**. Read lets agents only view data from the integration. Read & Write also lets agents act on it — for example, opening a ticket.

Read & Write is selectable only once an admin turns on **Agent permissions** for the whole account, in [Settings → Account](/docs/user-guide/orioniq/settings/#account). While the account is set to Read, the per-connection choice stays disabled. You can always set a connection back to Read, even while the account-wide setting is off.

Not every integration supports write — the choice appears only where OrionIQ has a write action to offer.

## Management

The **Management** tab lists your account's connections:

| Column | Description |
|---|---|
| **Integration** | The connected integration. |
| **Space** | The space the connection belongs to. |
| **Status** | The connection's health — see below. |
| **Connected by** | The user who created the connection. |
| **Used by** | How many agents use the connection. |
| **Connection** | The connection's name, and the authentication method it uses. |
| **Updated by** | The user who last changed the connection. |
| **Updated at** | When the connection was last changed. |
| **Validated at** | When the connection's credentials were last verified. |

A connection reports one of these statuses:

| Status | Meaning |
|---|---|
| **Connected** | The credentials are valid and the integration is reachable. |
| **Needs reauth** | The credentials were rejected and must be re-entered. |
| **Expired** | The credentials are no longer valid. |
| **Unreachable** | The provider couldn't be reached. |
| **Needs credentials** | The connection has no usable credentials. |

Open a connection's actions menu to **Configure** its credentials, **Revalidate** it against the provider, or **Disconnect** it.

## Logz.io API access

The Logz.io integration is connected by default and gives agents access to your observability data. You can also grant agents scoped access to the Logz.io public API, per account:

| Scope | Grants |
|---|---|
| **Telemetry** | Logs and metrics access for the agent. Always on for every accessible account and not configurable. |
| **Read** | The agent can call the Logz.io public API but can't change anything. |
| **Write** | The agent can create and update Logz.io objects. Implies Read. |
| **Admin** | The agent has the same role as Manage API Tokens. Implies Read and Write. |

Enabling API access creates one system-generated API token per selected account, at the highest scope you chose. Changing or turning off API access deletes that token; agents keep their telemetry access, and a lower scope gets a new token at that scope.

Owner, sub-accounts, and Security accounts have a public API. Metrics, Timeless, and Restored accounts do not, so API scopes aren't available for them.

To request an integration that isn't yet available, click **Add to Wish List** on the integration you're interested in. This helps Logz.io prioritize which integrations to support next.

:::note
Integrations is an evolving capability. New integrations are added regularly based on user demand.
:::
