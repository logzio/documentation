---
sidebar_position: 6
title: Manage Timeless Accounts with the API
description: Use the Logz.io API to route logs into a timeless account, clean its data, and remove it
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [timeless account, optimizer, long-term storage, api, logz.io, automation, data deletion]
---

Timeless accounts keep logs for as long as you need them, and optimizers are the rules that write logs into them. This guide walks through the whole lifecycle with the Logz.io API, so you can automate it instead of using the app:

1. [Find your timeless account](#find-your-timeless-account)
2. [Create an optimizer that writes into it](#create-an-optimizer)
3. [Update the timeless account](#update-the-timeless-account)
4. [Preview and delete data](#preview-and-delete-data)
5. [Remove the optimizers](#remove-the-optimizers)
6. [Delete the timeless account](#delete-the-timeless-account)

For every field and response, see the [timeless accounts](https://api-docs.logz.io/docs/logz/manage-timeless-accounts) and [optimizers](https://api-docs.logz.io/docs/logz/optimizers) API reference.


### Variables in this article

In the code blocks in this article, you'll see `<<API-TOKEN>>` and `<<API-URL>>` variables.
These need to be replaced with information specific to your account:

* Replace `<<API-TOKEN>>` with an [API token](https://app.logz.io/#/dashboard/settings/manage-tokens/api) of your main account. See the table below for the role it needs.
* Replace `<<API-URL>>` with your region's base API URL.
  For more information on finding your account's region, see [Account region](https://docs.logz.io/docs/user-guide/admin/hosting-regions/account-region/).


## Before you start {#before-you-start}

* **Create the timeless account in the app.** Timeless accounts can't be created through the API. Create one on the [Manage accounts page](/docs/user-guide/admin/logzio-accounts/manage-accounts/manage-timeless-accounts/), then manage it with the API.
* **Use an API token with the right role:**

| Requests | API token role |
| --- | --- |
| Timeless accounts: list, get, update, delete, preview and delete data | Admin |
| Optimizers: list and get | Any role |
| Optimizers: create, update, delete | User or Admin |
| List the optimizers that write into a timeless account | Admin |

API tokens created before token roles were introduced have the same permissions as Admin.


## Find your timeless account {#find-your-timeless-account}

List the timeless accounts of your account, and note the `id` and `logType` of the one you want to use. You need both to create an optimizer.

```shell
curl -X GET \
  https://<<API-URL>>/v1/timeless-indices \
  -H 'Content-Type: application/json' \
  -H 'X-API-TOKEN: <<API-TOKEN>>'
```

The response lists your timeless accounts, with your plan's limits:

```json
{
  "maxAllowed": 3,
  "totalVolumeGb": 50,
  "timelessIndices": [
    {
      "id": 22222,
      "ownerAccountId": 11111,
      "name": "error-logs-archive",
      "logType": "error-logs-archive",
      "volumeGb": 10,
      "actualUsage": { "bytes": 2147483648, "humanReadableSize": "2.0 GB", "percentage": "20.0 %" },
      "createdAt": 1793263548.000000000,
      "authorizedAccounts": [{ "accountId": 11111, "accountName": "Main account" }],
      "suspended": false
    }
  ]
}
```

To get a single timeless account, run `GET /v1/timeless-indices/{id}`.


## Create an optimizer that writes into it {#create-an-optimizer}

An optimizer runs a search on a schedule and writes the results into a timeless account. This one copies the checkout service's errors from your main account every 10 minutes:

```shell
curl -X POST \
  https://<<API-URL>>/v1/triggers \
  -H 'Content-Type: application/json' \
  -H 'X-API-TOKEN: <<API-TOKEN>>' \
  -d '{
    "name": "Checkout errors",
    "description": "Keeps checkout service errors for audits",
    "enabled": true,
    "search": {
      "queryString": "service: checkout AND level: ERROR",
      "source": {
        "allSubAccounts": false,
        "subAccountsIds": [11111]
      }
    },
    "triggerOn": {
      "type": "SCHEDULE",
      "frequency": "EVERY_10_MINUTES"
    },
    "output": {
      "target": {
        "timelessIndex": {
          "id": 22222,
          "logType": "error-logs-archive"
        }
      }
    }
  }'
```

The response is the created optimizer. Note its `id`: you need it to clean or remove its data.

| Field | What to send |
| --- | --- |
| `search.queryString` | The search, in Lucene syntax. Use `*` to match every log. |
| `search.source` | The accounts to search. Set `allSubAccounts` to `true` to search every account your account can search, or to `false` and list the account IDs in `subAccountsIds`. |
| `triggerOn` | `type` is always `SCHEDULE`. `frequency` is how often the optimizer runs: `EVERY_10_MINUTES`, `EVERY_30_MINUTES`, `EVERY_1_HOUR`, `EVERY_4_HOURS`, `EVERY_6_HOURS`, `EVERY_8_HOURS`, or `EVERY_1_DAY`. Each run searches back over the time since the previous one. |
| `output.target.timelessIndex.id` | The `id` of the timeless account. |
| `output.target.timelessIndex.logType` | The `logType` of the timeless account. |

:::note
Always set `logType` to the timeless account's `logType`. Data deletion only matches logs with the timeless account's current `logType`, so logs written with any other value can't be cleaned with the API.
:::

To write aggregated results instead of copying every log, add `groupBy` and `metricsAggregations` to `search`. See [Create an optimizer](https://api-docs.logz.io/docs/logz/create-optimizer) for those fields.

To list your optimizers, run `GET /v1/triggers`. To change one, get it with `GET /v1/triggers/{id}`, edit the fields you need, and send the whole optimizer back with `PUT /v1/triggers/{id}`.


## Update the timeless account {#update-the-timeless-account}

Change the name, volume, or authorized accounts of a timeless account. Send all three fields, since the request replaces the current values:

```shell
curl -X PUT \
  https://<<API-URL>>/v1/timeless-indices/22222 \
  -H 'Content-Type: application/json' \
  -H 'X-API-TOKEN: <<API-TOKEN>>' \
  -d '{
    "name": "error-logs-archive",
    "volumeGb": 20,
    "authorizedAccounts": [11111]
  }'
```

The volume must be at least the data already stored, and fit in your plan's total timeless volume together with your other timeless accounts.

:::caution
Renaming a timeless account also changes its `logType`. Optimizers keep writing with the old one, so update the `output.target.timelessIndex.logType` of each optimizer that writes into the account after a rename.
:::


## Preview and delete data {#preview-and-delete-data}

Delete data from a timeless account by time range, by the optimizers that wrote it, or both. Preview first: the preview request takes the same body and returns the number of logs that would be deleted, without deleting anything.

```shell
curl -X POST \
  https://<<API-URL>>/v1/timeless-indices/22222/query-hits \
  -H 'Content-Type: application/json' \
  -H 'X-API-TOKEN: <<API-TOKEN>>' \
  -d '{
    "timeFrameFrom": "2026-01-01T00:00:00Z",
    "timeFrameTo": "2026-07-01T00:00:00Z",
    "optimizerIds": [1001]
  }'
```

```json
128450
```

When the number is what you expect, send the same body to `delete-data`:

```shell
curl -X POST \
  https://<<API-URL>>/v1/timeless-indices/22222/delete-data \
  -H 'Content-Type: application/json' \
  -H 'X-API-TOKEN: <<API-TOKEN>>' \
  -d '{
    "timeFrameFrom": "2026-01-01T00:00:00Z",
    "timeFrameTo": "2026-07-01T00:00:00Z",
    "optimizerIds": [1001]
  }'
```

The response is the number of logs to be deleted. The deletion runs in the background, so the logs disappear over the next few minutes. Deleted data can't be restored.

| Field | What to send |
| --- | --- |
| `optimizerIds` | Required. The IDs of the optimizers whose data to delete, or an empty list (`[]`) to delete the data of every optimizer. |
| `timeFrameFrom`, `timeFrameTo` | The time range, in ISO 8601 format, matched against each log's `@timestamp`. Send both, or leave both out to delete regardless of time. |

A request without `optimizerIds`, or with only one end of the time range, returns `400 Bad Request`.


## Remove the optimizers {#remove-the-optimizers}

:::caution
You can't delete your last timeless account. Before you remove the optimizers of an account you plan to delete, [list your timeless accounts](#find-your-timeless-account) and make sure you have at least one more. If it's your last one, you can't delete it. To stop storing data in it, remove its optimizers and [delete its data](#preview-and-delete-data) instead.
:::

A timeless account can't be deleted while optimizers write into it. List them:

```shell
curl -X GET \
  https://<<API-URL>>/v1/triggers/target/22222 \
  -H 'Content-Type: application/json' \
  -H 'X-API-TOKEN: <<API-TOKEN>>'
```

Then delete each one by its `id`:

```shell
curl -X DELETE \
  https://<<API-URL>>/v1/triggers/1001 \
  -H 'Content-Type: application/json' \
  -H 'X-API-TOKEN: <<API-TOKEN>>'
```

Deleting an optimizer doesn't delete the data it already wrote. To remove that data too, [delete it](#preview-and-delete-data) with the optimizer's ID before you delete the optimizer.


## Delete the timeless account {#delete-the-timeless-account}

```shell
curl -X DELETE \
  https://<<API-URL>>/v1/timeless-indices/22222 \
  -H 'Content-Type: application/json' \
  -H 'X-API-TOKEN: <<API-TOKEN>>'
```

The response is the deleted timeless account. Deleting a timeless account permanently deletes all its data.

The request fails when:

* **Optimizers still write into the account.** The response is `403 Forbidden`, and its message lists the optimizers to delete first, for example `Delete these optimizers first: 1001 (Checkout errors)`.
* **It's your last timeless account.** The response is `400 Bad Request` with the message `Deleting the last timeless index is not allowed`. [Check this before you remove its optimizers](#remove-the-optimizers).
