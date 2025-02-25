---
sidebar_position: 3
title: Metrics Shipping Token
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Get and manage your metrics API tokens
keywords: [api token management, api token, api, token, key creation, token authentication, security, secured login]
---

When setting up data shipping to your Metrics account, you'll need to include your Metrics shipping token. The token routes your data to the right account in Logz.io.

:::important note
An account can have only **one** metrics token at a time. Multiple tokens are not supported.
:::



Here's how to get the metrics token:


## Via the Manage Tokens page

{@include: ../../../_include/general-shipping/manage-tokens-nav.md}

{@include: ../../../_include/general-shipping/data-shipping-tokens_vars.md} <!-- Nico - product="Metrics" -->

## Via the Manage accounts page

You must have admin permissions for the Logz.io Infrastructure Monitoring account to view the **Manage accounts** page. If you're not an admin user for the account, consult with an account admin to get the Infrastructure Monitoring token information. 

From your main account, navigate to <a href="https://app.logz.io/#/dashboard/settings/manage-accounts" target ="_blank"> **Manage accounts** page</a>. It can be reached by selecting **<i class="li li-gear"></i> > Settings > Manage accounts**.

Scroll to the Metrics Account section and select the account to which you want to ship data. This will display the account's token and configuration settings.

![Metrics Shipping Token](https://dytvr9ot2sszz.cloudfront.net/logz-docs/accounts/metrics-account-overview.png)

