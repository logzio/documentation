---
sidebar_position: 8
title: Logz.io MCP Server
description: Use Logz.io MCP to quickly and easily query your logs, metrics, dashboards, and alerts.
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logz.io, mcp, model context protocol, llm tools, observability, logs, metrics, prometheus, promql, dashboards, alerts, elasticsearch, ai agents, integrations]
---

The Logz.io Public API MCP (Model Context Protocol) server allows LLM clients (Claude, Cursor, ChatGPT, etc.) to access observability data - logs, metrics, dashboards, and alerts, in a standardized way. With MCP, AI agents can fetch context and trigger actions without custom integrations.

### Prerequisites

* A Logz.io API token (create in your Logz.io account settings). The same token is used for logs, metrics, dashboards, and alerts. You don't need a separate metrics API token.
* A supported LLM client with MCP integration. Setup instructions vary per client.

## Setup

The steps for adding the Logz.io MCP server depend on your client. Refer to each client's instructions on how to attach the Logz.io MCP server to your LLM.

Below is a generic example configuration:

```json
{
  "logz.io public api": {
    "command": "npx",
    "args": [
      "mcp-remote",
      "https://api.logz.io/mcp",
      "--header",
      "X-API-TOKEN:<<YOUR-LOGZIO-API-TOKEN>>"
    ]
  }
}
```

Replace `<<YOUR-LOGZIO-API-TOKEN>>` with your actual token.

The domain prefix (`api`) is region-specific. Those are the regions available:

* `https://api.logz.io/mcp` (US) us-east-1
* `https://api-eu.logz.io/mcp` (EU) eu-central-1
* `https://api-uk.logz.io/mcp` (UK) eu-west-2
* `https://api-au.logz.io/mcp` (AP) ap-southeast-2
* `https://api-jp.logz.io/mcp` (AP) ap-northeast-1
* `https://api-ca.logz.io/mcp` (CA) ca-central-1





After setup is complete, you can query your Logz.io data. Ask questions about your logs, metrics, dashboards, or alerts - the MCP server will expose the right tools so your client can fetch results in context.

![Main dashboard](https://dytvr9ot2sszz.cloudfront.net/logz-docs/mcp/mcp-results.png)


## Choosing the account to query

The API token belongs to one Logz.io account, but the MCP server can query other accounts that account is allowed to read:

* **Metrics**: every metrics tool requires an `account_id`, the metrics account to query. Use `get_metrics_accounts` to list the metrics accounts. A metrics account can be queried when your token's account is one of its authorized accounts.
* **Logs**: the log search tools accept an optional `account_id` to search another account your token may search, such as a sub account. Use `get_associated_accounts` to list them. Without `account_id`, the token's own account is searched. `scroll_logs` always reads the token's own account.

## Available tools

The MCP server exposes tools grouped by domain. Each tool follows the MCP request/response schema.

### Account management

Tools for managing and retrieving account information:

| Tool                      | Description                         | Parameters | API Link |
| ------------------------- | ----------------------------------- | ---------- | ---------- |
| `get_account_info` | Retrieve account name and ID for the current token. | None | [Link](https://api-docs.logz.io/docs/logz/who-am-i/) |
| `get_associated_accounts` | List all accounts associated with the current account (including sub-accounts for owners). | None |  |
| `get_metrics_accounts` | List all metrics accounts with details. | None | [Link](https://api-docs.logz.io/docs/logz/get-a-list-of-all-metrics-accounts) |

### Metrics management 

Tools for querying metrics. All of them require `account_id` (int), the metrics account to query.

| Tool | Description | Parameters | API Link |
| ---- | ----------- | ---------- | ---------- |
| `query_prometheus_metrics` | Run a PromQL query at a single timestamp. | `account_id` (int, required), `query` (string, required), `time` (string, optional), `timeout` (string, optional) | [Link](https://api-docs.logz.io/docs/logz/post-instant-query-for-metrics-account) |
| `query_prometheus_metrics_range` | Run a PromQL query over a time range. | `account_id` (int, required), `query` (string, required), `start` (string, required), `end` (string, required), `step` (string, required), `timeout` (string, optional) | [Link](https://api-docs.logz.io/docs/logz/post-range-query-for-metrics-account) |
| `get_available_metrics` | List the metric names available in the metrics account. | `account_id` (int, required), `match` (string, optional), `start` (string, optional), `end` (string, optional), `limit` (int, optional) | [Link](https://api-docs.logz.io/docs/logz/get-label-values-for-metrics-account) |
| `get_metric_labels` | List the label names of a metric. | `account_id` (int, required), `metric_name` (string, required), `start` (string, optional), `end` (string, optional), `limit` (int, optional) | [Link](https://api-docs.logz.io/docs/logz/get-label-names-for-metrics-account) |
| `get_metric_series` | List the time series that match a selector, with their full label sets. | `account_id` (int, required), `match` (string, required), `start` (string, optional), `end` (string, optional), `limit` (int, optional) | [Link](https://api-docs.logz.io/docs/logz/get-series-by-labels-for-metrics-account) |
| `get_metric_metadata` | Get the type, help text, and unit of metrics. | `account_id` (int, required), `metric_name` (string, optional), `limit` (int, optional) | [Link](https://api-docs.logz.io/docs/logz/get-metric-metadata-for-metrics-account) |

### Logs management 

Tools for searching, filtering, and managing logs:

| Tool | Description | Parameters | API Link |
| ---- | ----------- | ---------- | ---------- |
| `search_logs` | Search logs with Elasticsearch DSL. | `query` (object, required), `size` (int, optional), `from` (int, optional), `sort` (array, optional), `day_offset` (int, optional), `account_id` (int, optional) | [Link](https://api-docs.logz.io/docs/logz/search) |
| `scroll_logs` | Scroll through large sets of log data in the token's own account. | `query` (object, optional), `scroll_id` (string, optional), `size` (int, optional), `scroll` (string, optional) | [Link](https://api-docs.logz.io/docs/logz/scroll) |
| `search_logs_simple` | Full-text search across all log fields. | `search_term` (string, required), `size` (int, optional), `from` (int, optional), `day_offset` (int, optional), `account_id` (int, optional) | [Link](https://api-docs.logz.io/docs/logz/search) |
| `search_logs_by_timestamp` | Search logs within a specific time range. | `start_time` (string, required), `end_time` (string, required), `search_term` (string, optional), `size` (int, optional), `from` (int, optional), `day_offset` (int, optional), `account_id` (int, optional) | [Link](https://api-docs.logz.io/docs/logz/search) |
| `get_all_log_types` | List all log types available. | None | [Link](https://api-docs.logz.io/docs/logz/get-log-types/) |
| `retrieve_drop_filters` | Retrieve all configured drop filters. | None | [Link](https://api-docs.logz.io/docs/logz/get-all-for-account) |

Log searches cover the last 2 calendar days by default. Use `day_offset` to search older data.

### Dashboards & folders

Tools for creating and managing dashboards and dashboard folders:

| Tool | Description | Parameters | API Link |
| ---  | ----------- | ---------- | ---------- |
| `get_all_dashboards` | List all dashboards with UIDs. | None | [Link](https://api-docs.logz.io/docs/logz/get-all-dashboards) |
| `get_dashboard_by_id` | Retrieve a dashboard by UID. | `folder_id` (string, required), `uid` (string, required) | [Link](https://api-docs.logz.io/docs/logz/get-dashboard-by-id) |
| `get_dashboard_creators` | List the account users who created dashboards, with their IDs and full names. Use an ID as the `created_by` of `search_dashboards`. | None |  |
| `create_dashboard` | Create a dashboard from configuration. `get_dashboard_schema_example` returns a configuration you can start from. | `folder_id` (string, required), `dashboard_config` (object, required) | [Link](https://api-docs.logz.io/docs/logz/create-a-new-dashboard) |
| `update_dashboard` | Update a dashboard. | `folder_id` (string, required), `uid` (string, required), `dashboard_config` (object, required) | [Link](https://api-docs.logz.io/docs/logz/update-an-existing-dashboard) |
| `move_dashboard` | Move a dashboard to a different folder. | `uid` (string, required), `folder_id` (string, required), `target_folder_id` (string, required) | [Link](https://api-docs.logz.io/docs/logz/move-a-dashboard-to-a-different-folder) |
| `get_all_dashboard_folders` | List all dashboard folders. | `with_dashboards` (string, optional) | [Link](https://api-docs.logz.io/docs/logz/get-all-dashboards-folders) |
| `get_dashboard_folder_by_name` | Retrieve a dashboard folder by its display name. The folder ID it returns is the `folder_id` other tools take. | `name` (string, required) |  |
| `search_dashboards` | Search dashboards by title, by creator, or both. Returns each match with its UID and folder. | `query` (string, optional), `created_by` (int, optional), `limit` (int, optional), `page` (int, optional) |  |
| `create_dashboard_folder` | Create a new dashboard folder. | `name` (string, required) | [Link](https://api-docs.logz.io/docs/logz/create-dashboards-folder) |
| `get_all_global_data_sources` | List all global data sources. | None |  |
| `get_dashboard_schema_example` | Retrieve an example dashboard configuration for `create_dashboard`, with one log-count panel. Replace its placeholder account ID with your log account ID. | None |  |
| `get_datasource_schema_example` | Retrieve an example data source schema. | None |  |


### Alerts & insights

Tools for alerts and insights:

| Tool | Description | Parameters | API Link |
| ---- | ----------- | ---------- | ---------- | 
| `get_all_alerts`       | List all configured alerts.     | None | [Link](https://api-docs.logz.io/docs/logz/get-all-alerts) |
| `get_triggered_alerts` | List triggered alerts.      | `from` (int, optional), `size` (int, optional), `search` (string, optional), `severities` (array, optional), `tags` (array, optional) | [Link](https://api-docs.logz.io/docs/logz/triggered-alerts) |
| `get_insights`         | Get insights matching criteria. | `from` (int, optional), `size` (int, optional, 1–100), `asc` (boolean, optional), `search` (string, optional) | [Link](https://api-docs.logz.io/docs/logz/get-public-insights) |

## Best practices

* Always confirm which client you are using and follow its MCP setup guide.
* Use ISO-8601/RFC3339 timestamps for metrics and log queries.
* Start with smaller query sizes to validate setup before scaling.
* Secure your tokens; do not hard-code in public repos.

## OAuth 2.0 Support for Logz.io MCP Server

The MCP server supports OAuth 2.0 Authorization Code flow with PKCE, allowing third-party tools such as **AWS Bedrock Agent** to connect without manually sharing static API tokens.

Existing integrations that pass `X-API-Token` directly continue to work unchanged.

---

### How it works

```
AWS Bedrock Agent 
or Similar Client         MCP Server                    User
       |                                  |                           |
       |── GET /.well-known/...  ────────>|                           |
       |<─ OAuth metadata ───────────────|                           |
       |                                  |                           |
       |── POST /register ───────────────>|                           |
       |<─ { client_id, client_secret } ─|                           |
       |                                  |                           |
       |── redirect user to /authorize ──────────────────────────────>|
       |                                  |<── enters Logz.io token ─|
       |<── redirect with ?code=... ──────────────────────────────────|
       |                                  |                           |
       |── POST /token (code + PKCE) ────>|                           |
       |<─ { access_token } ─────────────|                           |
       |                                  |                           |
       |── POST /mcp  Authorization: Bearer <token>  ──────────────>|
```

1. The agent discovers OAuth metadata at `/.well-known/oauth-authorization-server`.
2. The agent registers as a client via `POST /register`.
3. The user is redirected to `/authorize` where they enter their Logz.io API token.
4. The server issues an authorization code and redirects back to the agent.
5. The agent exchanges the code for a JWT access token via `POST /token`.
6. The agent attaches `Authorization: Bearer <token>` to every MCP request.
7. The server decrypts the token and injects the Logz.io API token transparently.

The Logz.io API token is **never sent to the agent** — it is encrypted inside the JWT and only the MCP server can read it.

---

For additional help, contact [Logz.io's Support](mailto:help@logz.io).

---

**Any use of Logz.io's MCP is subject to our [Terms of Use](https://logz.io/about-us/terms-of-use/).**
