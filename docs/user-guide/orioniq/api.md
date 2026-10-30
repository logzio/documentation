---
sidebar_position: 9
title: OrionIQ API
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: List agents, trigger OrionIQ agents, poll for results, send follow-ups, and submit feedback using the OrionIQ API.
keywords: [OrionIQ, API, agents, list agents, agent ID, trigger agent, agent run, feedback, api token, automation]
---

Agents configured with the **API** trigger run on demand when you call the OrionIQ API. Use it to start a run from a CI pipeline, an incident workflow, or any external system, then poll for the result.

To get an agent's ID and a ready-to-copy request for each endpoint, open the agent's actions menu in the [Agents Hub](/docs/user-guide/orioniq/agents-hub/) and select **API References**. To look agents up with the API instead, use [List agents](#list-agents).

## Authentication

All requests must include the `x-api-token` header.

In the code blocks below:

* Replace `<<API-TOKEN>>` with an [API token](https://app.logz.io/#/dashboard/settings/manage-tokens/api) from the account that owns the agent
* Replace `<<API-URL>>` with your region's base API URL. For more information, see [Account region](/docs/user-guide/admin/hosting-regions/account-region).
* Replace `<<AGENT-ID>>` with the agent's ID

A request with a missing or invalid token returns `401`.

:::note
Requests may receive a `307 Temporary Redirect` to an equivalent path, as part of an ongoing backend migration. The redirect preserves the request method and body, so make sure your HTTP client follows redirects — `curl` needs `-L`; most other HTTP clients and libraries follow by default.
:::

:::note
If AI features are disabled for the account, [Run an agent](#run-an-agent) and [Send a follow-up](#send-a-follow-up) return `403`. Polling for a result, enabling or disabling an agent, and feedback stay available either way, so you can still retrieve a run you already started and turn an agent off. See [AI Settings](/docs/open360/settings/ai-settings/) for enabling AI on an account.
:::

:::note
If the account has reached its configured AI usage cap, [Run an agent](#run-an-agent) and [Send a follow-up](#send-a-follow-up) return `429` (`errorCode: "CAP_EXCEEDED"`). See [OrionIQ Settings → Capping](/docs/user-guide/orioniq/settings/#capping) for usage and budget limits.
:::

## List agents

```
POST /v1/orioniq-be/agents/search
```

Returns the agents in the token's account, so you can find an agent ID without opening the Agents Hub. Sub-account agents are not included. Listing starts no AI work, so it also works when AI features are disabled.

### Sample request

```shell
curl -X POST -L \
  https://<<API-URL>>/v1/orioniq-be/agents/search \
  -H 'Content-Type: application/json' \
  -H 'X-API-TOKEN: <<API-TOKEN>>' \
  -d '{
    "filter": {
      "searchTerm": "checkout",
      "active": true
    },
    "sort": [
      {
        "field": "lastRun",
        "descending": true
      }
    ],
    "pagination": {
      "pageNumber": 1,
      "pageSize": 20
    }
  }'
```

All fields are optional. A filter value the API cannot use is ignored.

| Field | Description |
|---|---|
| `filter.searchTerm` | Returns agents whose title contains this text. |
| `filter.type` | Filters by agent type. |
| `filter.trigger` | Filters by trigger. An unknown value returns no results. |
| `filter.active` | `true` for enabled agents, `false` for disabled ones. |
| `filter.createdBy` | Filters by creator. |
| `sort` | A list where only the first entry is used. Each entry takes a `field` and an optional `descending` flag (default `false`). |
| `sort[].field` | One of `name`, `type`, `active`, `createdAt`, `updatedAt`, or `lastRun`. |
| `pagination.pageNumber` | The page to return. |
| `pagination.pageSize` | Results per page. Defaults to 50 and is capped at 50. |

Results are ordered by creation time, newest first, unless you set `sort`. An unusable `sort` entry falls back to the default order. In ascending order, agents that never ran come first when sorting by `lastRun`.

### Response

```json
{
  "total": 1,
  "results": [
    {
      "id": "<agent-id>",
      "name": "<agent-name>",
      "displayName": "Checkout Latency Review",
      "description": "Reviews latency on the checkout service.",
      "type": "<agent-type>",
      "trigger": "<trigger>",
      "active": true,
      "isSystemAgent": false,
      "createdAt": "2026-10-01T08:00:00Z",
      "updatedAt": "2026-10-10T09:30:00Z",
      "lastRun": "2026-10-14T06:00:00Z"
    }
  ],
  "pagination": {
    "pageNumber": 1,
    "pageSize": 20
  }
}
```

`total` is the number of matching agents across all pages. A page past the end returns an empty `results` list. Use `displayName` as the agent's title. Each `id` works as `<<AGENT-ID>>` in the other endpoints.

A request authenticated with a session or share token instead of an API token returns `401`.

## Run an agent

```
POST /v2/ai-agent/<<AGENT-ID>>
```

Starts a new run and returns immediately with a session ID. The run itself is asynchronous — poll for the result with [Get run status](#get-run-status).

### Sample request

```shell
curl -X POST -L \
  https://<<API-URL>>/v2/ai-agent/<<AGENT-ID>> \
  -H 'Content-Type: application/json' \
  -H 'X-API-TOKEN: <<API-TOKEN>>' \
  -d '{
    "context": {
      "message": "Summarize the errors in the checkout service",
      "additionalContext": "Deployment 4.12.0 rolled out at 09:00 UTC",
      "timerange": {
        "startTime": "2026-08-27T08:00:00Z",
        "endTime": "2026-08-27T10:00:00Z"
      }
    }
  }'
```

| Field | Description |
|---|---|
| `context.message` | The prompt for this run. |
| `context.additionalContext` | Optional free-text context to pass to the agent. |
| `context.timerange` | Optional `startTime` and `endTime` bounding the data the agent analyzes. |
| `context.security` | The accounts the run reads. Each entry takes a `requestedAccountId`, a `type` of `log` or `metric`, and an optional `filter` of `field` and `value`. Always send at least one entry. Without it, the run falls back to the accounts saved on the agent, and a Scheduled agent, or one with none saved, fails with `422`. An account the API token can't read is dropped, and a run with none left is rejected with `403`. |
| `integrations` | Optional list of integration connections the run may use. |

Fields you send override the matching fields in the agent's saved **Payload (JSON)**.

### Response

```json
{
  "status": "started",
  "sessionId": "<session-id>"
}
```

An agent that doesn't exist, or that your account can't access, returns `404`. A disabled agent also returns `404`, unless its trigger type is Alert. When OrionIQ is temporarily shut down for maintenance, the endpoint returns `503`.

## Get run status

```
GET /v2/ai-agent/<<AGENT-ID>>/<session-id>
```

Returns the current status of a run. Poll this endpoint until the status is terminal.

### Sample request

```shell
curl -X GET -L \
  https://<<API-URL>>/v2/ai-agent/<<AGENT-ID>>/<session-id> \
  -H 'Content-Type: application/json' \
  -H 'X-API-TOKEN: <<API-TOKEN>>'
```

### Response

```json
{
  "status": "done",
  "message": "<agent-response>",
  "totalSteps": 12
}
```

| Status | Meaning |
|---|---|
| `loading` | The run is still in progress. Keep polling. |
| `done` | The run finished. `message` holds the agent's output. |
| `error` | The run failed. `message` holds the reason. |
| `canceled` | The run was canceled. |
| `timeout` | The request timed out before the run produced new data. Poll again. |

`totalSteps` reports how many steps the agent has produced so far.

## Send a follow-up

```
POST /v2/ai-agent/<<AGENT-ID>>/<session-id>
```

Continues the same conversation. Allowed only after the previous turn reached a terminal status. The request body takes the same `context` object as [Run an agent](#run-an-agent), and the response returns the same session ID, which you poll with [Get run status](#get-run-status).

```json
{
  "status": "started",
  "sessionId": "<session-id>"
}
```

## Enable or disable an agent

```
POST /v2/ai-agent/<<AGENT-ID>>/enable
POST /v2/ai-agent/<<AGENT-ID>>/disable
```

A disabled agent does not start new runs, whatever its trigger configuration.

### Response

```json
{
  "id": "<agent-id>",
  "active": true
}
```

## Submit feedback

```
POST /v2/ai-agent/<<AGENT-ID>>/feedback
```

Rates one or more runs. Feedback appears in the [Usage & Performance Dashboard](/docs/user-guide/orioniq/usage-performance/).

### Sample request

```shell
curl -X POST -L \
  https://<<API-URL>>/v2/ai-agent/<<AGENT-ID>>/feedback \
  -H 'Content-Type: application/json' \
  -H 'X-API-TOKEN: <<API-TOKEN>>' \
  -d '[
    {
      "sessionId": "<session-id>",
      "feedbackName": "run-quality",
      "score": 100,
      "comment": "Correctly identified the failing dependency."
    }
  ]'
```

| Field | Description |
|---|---|
| `sessionId` | The run to rate. |
| `feedbackName` | A name identifying the kind of feedback. |
| `score` | A number, or a boolean that is converted to `100` for `true` and `0` for `false`. |
| `comment` | Optional free-text note. Omitting it leaves an existing comment unchanged. |

A run holds one feedback record, so submitting again for the same session updates it.

### Response

```json
[
  {
    "id": "<feedback-id>",
    "createdAt": "<timestamp>",
    "agentId": "<agent-id>",
    "accountId": 12345,
    "sessionId": "<session-id>",
    "feedbackName": "run-quality",
    "score": 100,
    "comment": "Correctly identified the failing dependency."
  }
]
```

## Get feedback

```
GET /v2/ai-agent/<<AGENT-ID>>/feedback/<session-id>
```

Returns the feedback record for a run, in the same shape as a single entry in the Submit feedback response. Returns `404` when the run has no feedback.

:::note
Agents don't have to be reachable over the API to be rated. Runs started by a Scheduled, Deployment, or Alert trigger can be rated from the Agents Hub, and the same feedback endpoints apply to them.
:::

## List lessons

```
GET /v2/ai-agent/<<AGENT-ID>>/lessons
```

Returns what the agent has learned from feedback. Active lessons are applied to the agent's runs while its Learning setting is on.

### Sample request

```shell
curl -X GET -L \
  https://<<API-URL>>/v2/ai-agent/<<AGENT-ID>>/lessons \
  -H 'X-API-TOKEN: <<API-TOKEN>>'
```

### Response

```json
{
  "lessons": [
    {
      "lessonId": "<lesson-id>",
      "status": "active",
      "situation": "<when-it-applies>",
      "rule": "<what-the-agent-does>",
      "whyNote": "<why-it-was-learned>",
      "feedbackRef": "<agent-id>:<session-id>",
      "createdAt": "2026-10-14T06:00:00Z",
      "lastLoaded": "2026-10-15T06:00:00Z",
      "isUpdated": false
    }
  ]
}
```

`status` is `active` or `disabled`. Apart from `lessonId` and `isUpdated`, every field is optional and can be missing.

## Set lesson status

```
PUT /v2/ai-agent/<<AGENT-ID>>/lessons/<lesson-id>/status
```

Turns a lesson on or off. A disabled lesson is kept but no longer applied to the agent's runs.

### Sample request

```shell
curl -X PUT -L \
  https://<<API-URL>>/v2/ai-agent/<<AGENT-ID>>/lessons/<lesson-id>/status \
  -H 'Content-Type: application/json' \
  -H 'X-API-TOKEN: <<API-TOKEN>>' \
  -d '{
    "enabled": false
  }'
```

### Response

The updated lesson, in the same shape as an entry in the List lessons response, with `status` set to `disabled` or `active`.
