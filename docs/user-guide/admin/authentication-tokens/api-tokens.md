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

## Each account has its own set of API tokens

| Account type | How to get the API token |
|---|---|
| Log Management main account | Log into the Main Log Management account, select [**<i class="li li-gear"></i> > Tools > Manage tokens**](https://app.logz.io/#/dashboard/settings/manage-tokens/api) in the top menu and select the **API tokens** tab. |
| Log Management sub account | Log into the Log Management sub account, select [**<i class="li li-gear"></i> > Tools > Manage tokens**](https://app.logz.io/#/dashboard/settings/manage-tokens/api) in the top menu and select the **API tokens** tab. |
| Metrics account | Metrics accounts do not have their own API tokens. Instead, use the API tokens belonging to the Log Management main account associated with the Metrics account.|
| Security account | Log into the security account, select [**<i class="li li-gear"></i> > Tools > Manage tokens**](https://app.logz.io/#/dashboard/settings/manage-tokens/api) in the top menu and select the **API tokens** tab. |
