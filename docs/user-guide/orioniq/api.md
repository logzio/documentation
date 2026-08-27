---
sidebar_position: 8
title: OrionIQ API
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Trigger OrionIQ agents, poll for results, send follow-ups, submit feedback, and manage learned lessons using the OrionIQ API.
keywords: [OrionIQ, API, agents, trigger agent, agent run, feedback, lessons, api token, automation]
---

Agents configured with the **API** trigger run on demand when you call the OrionIQ API. Use it to start a run from a CI pipeline, an incident workflow, or any external system, then poll for the result.

To find an agent's ID and a ready-to-copy request for each endpoint, open the agent in the [Agents Hub](/docs/user-guide/orioniq/agents-hub/) and go to the **API** section of its configuration.

## Authentication

All requests must include the `x-api-token` header.

In the code blocks below:

* Replace `<<API-TOKEN>>` with an [API token](https://app.logz.io/#/dashboard/settings/manage-tokens/api) from the account that owns the agent
* Replace `<<API-URL>>` with your region's base API URL. For more information, see [Account region](/docs/user-guide/admin/hosting-regions/account-region).
* Replace `<<AGENT-ID>>` with the agent's ID

A request with a missing or invalid token returns `401`.

## Run an agent

```
POST /v2/ai-agent/<<AGENT-ID>>
```

Starts a new run and returns immediately with a session ID. The run itself is asynchronous — poll for the result with [Get run status](#get-run-status).

### Sample request

```shell
curl -X POST \
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
| `context.security` | Optional list of accounts to query, each with an optional `filter` of `field` and `value`. |
| `integrations` | Optional list of integration connections the run may use. |

Fields you send override the matching fields in the agent's saved **Payload (JSON)**.

### Response

```json
{
  "status": "started",
  "sessionId": "<session-id>"
}
```

A disabled agent returns `404`, unless its trigger type is Alert. When OrionIQ is temporarily shut down for maintenance, the endpoint returns `503`.

## Get run status

```
GET /v2/ai-agent/<<AGENT-ID>>/<session-id>
```

Returns the current status of a run. Poll this endpoint until the status is terminal.

### Sample request

```shell
curl -X GET \
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

Rates one or more runs. Feedback appears in the [Usage & Performance Dashboard](/docs/user-guide/orioniq/usage-performance/) and, for eligible accounts, feeds the lessons the agent learns.

### Sample request

```shell
curl -X POST \
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

## List learned lessons

```
GET /v2/ai-agent/<<AGENT-ID>>/lessons
```

Returns the lessons the agent has learned from feedback. A lesson records a situation the agent met, the rule it derived, and why.

### Response

```json
{
  "lessons": [
    {
      "lessonId": "<lesson-id>",
      "status": "active",
      "situation": "<when this applies>",
      "rule": "<what the agent should do>",
      "whyNote": "<why the lesson exists>",
      "feedbackRef": "<feedback-id>"
    }
  ]
}
```

Only `active` lessons are added to the agent's instructions on later runs.

## Enable or disable a lesson

```
PUT /v2/ai-agent/<<AGENT-ID>>/lessons/<lesson-id>/status
```

Turns a lesson on or off. Use this to retire a lesson the agent should stop applying.

### Sample request

```shell
curl -X PUT \
  https://<<API-URL>>/v2/ai-agent/<<AGENT-ID>>/lessons/<lesson-id>/status \
  -H 'Content-Type: application/json' \
  -H 'X-API-TOKEN: <<API-TOKEN>>' \
  -d '{"enabled": false}'
```

`enabled` is required and must be a boolean; anything else returns `400`. The response returns the updated lesson in the same shape as a List learned lessons entry, with `status` set to `active` or `disabled`. An unknown lesson returns `404`.

:::note
Agents don't have to be reachable over the API to be rated. Runs started by a Scheduled, Deployment, or Alert trigger can be rated from the Agents Hub, and the same feedback and lessons endpoints apply to them.
:::
