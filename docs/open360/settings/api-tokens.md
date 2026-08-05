---
sidebar_position: 2
title: API Tokens
description: API tokens now carry a role that scopes what they can do - Admin, User, or Read-only.
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logz.io, api tokens, api token roles, permissions, read-only token, security, manage tokens, settings, observability]
---

API tokens under **Settings → Manage Tokens → API tokens** now carry a **role**, so a token can be scoped to what it actually needs rather than defaulting to full account access.

For creating and deleting tokens, and how each account type gets its own tokens, see [Manage API Tokens](https://docs.logz.io/docs/user-guide/admin/authentication-tokens/api-tokens/) — that part is unchanged. This page covers roles.

## Roles

A token can be assigned **Admin**, **User**, or **Read-only** — the same roles and the same per-feature access as [user roles](/docs/user-guide/admin/users/#access-level-per-role). See that page for exactly what each role can and can't do.

Every token created here gets **Admin** by default, including tokens created before roles existed, so if you want a scoped token, set the role explicitly rather than leaving it at the default.

## Set a token's role

Select the **Role** column on an existing token to change it, or set it while creating a new one.

## Related

* [Manage API Tokens](https://docs.logz.io/docs/user-guide/admin/authentication-tokens/api-tokens/)
* [API cookbook](https://docs.logz.io/docs/user-guide/integrations/api-cookbook/cookbook/)
