---
sidebar_position: 6
title: Manage API Tokens
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Get and manage your API tokens
keywords: [api token management, api token, api, token, key creation, token authentication, security, secured login]
---

If you're an Enterprise or Pro plan subscriber (or during your trial period),
your account includes API access. You can reference the [API guide](https://api-docs.logz.io/docs/logz/logz-io-api/) and [Terraform Logz.io Provider guide](https://docs.logz.io/integrations/terraform/) to help you build integrations with Logz.io.

API tokens are unique to each account. The only exception is a subset of account configuration operations that must be run with the API token of the main account.



From your account, go to the <a href="https://app.logz.io/#/dashboard/settings/manage-tokens/api" target ="_blank"> **Manage Tokens** > **API tokens** tab.</a> of your Operations workspace It can be reached by selecting **<i class="li li-gear"></i> > Settings > Tools > Manage Tokens**. 

The token for each account is listed in the table along with the date it was created.

:::note
Community plans do not currently include API tokens. See the official [pricing page](https://logz.io/pricing/) for details.
:::

## Working with API tokens

You have full control over your API tokens, to create and delete them at any time.

* To create an API token, click **+ New API token**. Type a brief **token name** and click **Add**.
* To delete an API token, hover over it, and click **delete** <i class="li li-trash"></i> to delete it.

  Deleting a token affects any integrations that use that token. Make sure you update integrations that use a token you deleted.

## Manage API tokens with the API

You can also create API tokens for your sub accounts, and list and delete the API tokens of your account and of its sub accounts with the Logz.io API, for example to rotate tokens from an automation.

These calls need an API token with the **Admin** role. API tokens created before token roles were introduced have the same permissions as Admin.

In the code blocks below:

* Replace `<<API-TOKEN>>` with an Admin [API token](https://app.logz.io/#/dashboard/settings/manage-tokens/api) of the account.
* Replace `<<API-URL>>` with your region's base API URL. For more information on finding your account's region, see [Account region](/docs/user-guide/admin/hosting-regions/account-region/).

### Create an API token for a sub account

```
POST /v1/api-tokens/sub-account
```

Run it with an Admin API token of the account that owns the sub account. You can't create an API token for your own account with the API; use **+ New API token** in the app instead.

```shell
curl -X POST \
  https://<<API-URL>>/v1/api-tokens/sub-account \
  -H 'Content-Type: application/json' \
  -H 'X-API-TOKEN: <<API-TOKEN>>' \
  -d '{
    "name": "<<TOKEN-NAME>>",
    "accountId": <<SUB-ACCOUNT-ID>>,
    "role": "ADMIN"
  }'
```

| Field | Required | Description |
|---|---|---|
| `name` | Yes | The name of the new token. |
| `accountId` | Yes | The ID of the sub account. |
| `role` | No | The role of the new token: `ADMIN`, `REGULAR` (User), `READ_ONLY`, or `CUSTOM`. Defaults to `ADMIN`. |

The response is the new token, including its value:

```json
{
  "id": 2050071,
  "name": "<<TOKEN-NAME>>",
  "token": "<<TOKEN-VALUE>>",
  "createdAt": "<<TIMESTAMP>>",
  "role": "ADMIN"
}
```

| Status | Meaning |
|---|---|
| `200` | The token was created. |
| `403` | The token in `X-API-TOKEN` doesn't have the Admin role, or its account doesn't own the sub account. |
| `404` | The sub account, or its owner account, wasn't found. |

### List the API tokens of an account

```
GET /v1/api-tokens
```

```shell
curl -X GET \
  https://<<API-URL>>/v1/api-tokens \
  -H 'Content-Type: application/json' \
  -H 'X-API-TOKEN: <<API-TOKEN>>'
```

By default, the call lists the API tokens of the account that owns `<<API-TOKEN>>`. To list the API tokens of one of its sub accounts, add the sub account ID in the `accountId` query parameter:

```shell
curl -X GET \
  'https://<<API-URL>>/v1/api-tokens?accountId=<<SUB-ACCOUNT-ID>>' \
  -H 'Content-Type: application/json' \
  -H 'X-API-TOKEN: <<API-TOKEN>>'
```

The response lists the API tokens of the account. It doesn't include the token values:

| Field | Description |
|---|---|
| `id` | The token ID. Use it to delete the token. |
| `name` | The token name. |
| `createdAt` | When the token was created (timestamp). |
| `lastUsed` | When the token was last used (timestamp), or `null` if it was never used. |
| `role` | The token role: `ADMIN`, `REGULAR` (User), `READ_ONLY`, or `CUSTOM`. |

```json
[
  {
    "id": 2050070,
    "name": "ci-pipeline",
    "createdAt": "<<TIMESTAMP>>",
    "lastUsed": null,
    "role": "ADMIN"
  }
]
```

| Status | Meaning |
|---|---|
| `200` | The list of API tokens. |
| `403` | The token in `X-API-TOKEN` doesn't have the Admin role, or `accountId` isn't its account or one of its sub accounts (error code `api-tokens/ACCOUNT_NOT_ACCESSIBLE`). |

### Delete an API token

```
DELETE /v1/api-tokens/{id}
```

You can delete an API token of your account or of one of its sub accounts. Replace `<<TOKEN-ID>>` with the `id` of the token to delete.

```shell
curl -X DELETE \
  https://<<API-URL>>/v1/api-tokens/<<TOKEN-ID>> \
  -H 'Content-Type: application/json' \
  -H 'X-API-TOKEN: <<API-TOKEN>>'
```

The response is the deleted token: the same fields as one item of the list above, plus `token`, the token value.

:::note
An API token can't delete itself. To delete the token you're calling with, use a different Admin API token.
:::

| Status | Meaning |
|---|---|
| `200` | The token was deleted. |
| `400` | The token in `X-API-TOKEN` tried to delete itself. |
| `403` | The token in `X-API-TOKEN` doesn't have the Admin role. |
| `404` | No API token with this ID exists in your account or in any of its sub accounts. |

Deleting a token affects any integrations that use that token. Make sure you update integrations that use a token you deleted.

## Each account has its own set of API tokens

| Account type | How to get the API token |
|---|---|
| Log Management main account | Log into the Main Log Management account, select [**<i class="li li-gear"></i> > Tools > Manage tokens**](https://app.logz.io/#/dashboard/settings/manage-tokens/api) in the top menu and select the **API tokens** tab. |
| Log Management sub account | Log into the Log Management sub account, select [**<i class="li li-gear"></i> > Tools > Manage tokens**](https://app.logz.io/#/dashboard/settings/manage-tokens/api) in the top menu and select the **API tokens** tab. |
| Metrics account | Metrics accounts do not have their own API tokens. Instead, use the API tokens belonging to the Log Management main account associated with the Metrics account.|
| Security account | Log into the security account, select [**<i class="li li-gear"></i> > Tools > Manage tokens**](https://app.logz.io/#/dashboard/settings/manage-tokens/api) in the top menu and select the **API tokens** tab. |
