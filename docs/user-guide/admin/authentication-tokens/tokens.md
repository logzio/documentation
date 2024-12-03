---
sidebar_position: 1
title: Types of Tokens
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Learn about the different token types in Logz.io
keywords: [api token management, api token, api, token, key creation, token authentication, security, secured login]
---


Logz.io uses tokens to manage data shipping for logs, metrics, and traces; control permissions for dashboard sharing; and authorize API access.


**Admin Access Required**: Only account admins can create, delete, or manage tokens.


## Data shipping tokens

To send data to your account, use Data Shipping Tokens: **Logs**, **Metrics**, or **Tracing**. These tokens specify which account to send your data to, with each account having its own unique tokens.

You can click any **Token** to copy it with one-click.

* Learn more about managing your [Log shipping tokens](https://docs.logz.io/docs/user-guide/admin/authentication-tokens/log-shipping-tokens/)
* Learn more about your [Metrics shipping token](https://docs.logz.io/docs/user-guide/admin/authentication-tokens/finding-your-metrics-account-token/)
* Learn more about your [Distributed Tracing shipping token](https://docs.logz.io/docs/user-guide/admin/authentication-tokens/finding-your-tracing-account-token/)

## Shared tokens for dashboard sharing

To share dashboards or other elements, use a **Shared Token**. These tokens allow you to share visualizations with anyone, even if they don't have access to your account.

* **Secure Sharing**: Set an expiration date and attach filters to limit data access and ensure security. Delete tokens that are no longer needed.

* **Manage Shared Tokens**: Go to [Tools > Manage Tokens](https://app.logz.io/#/dashboard/settings/manage-tokens/shared) and select the Shared Tokens tab.

Learn more about [managing shared tokens](https://docs.logz.io/docs/user-guide/admin/authentication-tokens/shared-tokens/).

## API tokens for integration development

To develop integrations, use an **API Token**. API tokens authenticate integrations with your Logz.io account and are available to Enterprise and Pro plan subscribers, as well as during trial periods.

Manage API Tokens: Go to [Settings > Tools > Manage Tokens](https://app.logz.io/#/dashboard/settings/manage-tokens/api) and select the API Tokens tab.


* Learn more about [managing API tokens](https://docs.logz.io/docs/user-guide/admin/authentication-tokens/api-tokens/)
* Build your own integration with [Logz.io API Developer Guide](https://api-docs.logz.io/docs/logz/logz-io-api/)

## Token permissions

Tokens are specific to the account they are created in and adhere to the account’s permissions. If account permissions change, the tokens respect these changes.

For example, if you create an API token in your main account, it can access data from the main account and its sub-accounts by default. If permissions are updated so the sub-account is no longer accessible from the main account, the API token will lose access to the sub-account's data.