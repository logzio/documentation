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

You can also list and delete the API tokens of an account with the Logz.io API, for example to rotate tokens from an automation.

Both calls need an API token with the **Admin** role. API tokens created before token roles were introduced have the same permissions as Admin.

In the code blocks below:

* Replace `<<API-TOKEN>>` with an Admin [API token](https://app.logz.io/#/dashboard/settings/manage-tokens/api) of the account.
* Replace `<<API-URL>>` with your region's base API URL. For more information on finding your account's region, see [Account region](/docs/user-guide/admin/hosting-regions/account-region/).

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

The response lists every API token of the account:

| Field | Description |
|---|---|
| `id` | The token ID. Use it to delete the token. |
| `name` | The token name. |
| `token` | The token value. |
| `createdAt` | When the token was created (timestamp). |
| `lastUsed` | When the token was last used (timestamp), or `null` if it was never used. |
| `role` | The token role: `ADMIN`, `REGULAR` (User), `READ_ONLY`, or `CUSTOM`. |

```json
[
  {
    "id": 2050070,
    "name": "ci-pipeline",
    "token": "<<TOKEN-VALUE>>",
    "createdAt": "<<TIMESTAMP>>",
    "lastUsed": null,
    "role": "ADMIN"
  }
]
```

### Delete an API token

```
DELETE /v1/api-tokens/{id}
```

Replace `<<TOKEN-ID>>` with the `id` of the token to delete.

```shell
curl -X DELETE \
  https://<<API-URL>>/v1/api-tokens/<<TOKEN-ID>> \
  -H 'Content-Type: application/json' \
  -H 'X-API-TOKEN: <<API-TOKEN>>'
```

The response is the deleted token, in the same format as one item of the list above.

:::note
An API token can't delete itself. To delete the token you're calling with, use a different Admin API token.
:::

| Status | Meaning |
|---|---|
| `200` | The token was deleted. |
| `400` | The token in `X-API-TOKEN` tried to delete itself. |
| `403` | The token in `X-API-TOKEN` doesn't have the Admin role. |
| `404` | No API token with this ID exists in the account. |

Deleting a token affects any integrations that use that token. Make sure you update integrations that use a token you deleted.

## Each account has its own set of API tokens

| Account type | How to get the API token |
|---|---|
| Log Management main account | Log into the Main Log Management account, select [**<i class="li li-gear"></i> > Tools > Manage tokens**](https://app.logz.io/#/dashboard/settings/manage-tokens/api) in the top menu and select the **API tokens** tab. |
| Log Management sub account | Log into the Log Management sub account, select [**<i class="li li-gear"></i> > Tools > Manage tokens**](https://app.logz.io/#/dashboard/settings/manage-tokens/api) in the top menu and select the **API tokens** tab. |
| Metrics account | Metrics accounts do not have their own API tokens. Instead, use the API tokens belonging to the Log Management main account associated with the Metrics account.|
| Security account | Log into the security account, select [**<i class="li li-gear"></i> > Tools > Manage tokens**](https://app.logz.io/#/dashboard/settings/manage-tokens/api) in the top menu and select the **API tokens** tab. |
