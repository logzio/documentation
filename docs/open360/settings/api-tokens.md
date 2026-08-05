---
sidebar_position: 2
title: API Tokens
description: API tokens now carry a role that scopes what they can do - Admin, User, or Read-only.
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logz.io, api tokens, api token roles, permissions, read-only token, security, manage tokens, settings, observability]
---

API tokens under **Settings → Manage Tokens → API tokens** now carry a **role**, so a token can be scoped to what it actually needs rather than defaulting to full account access.

For creating and deleting tokens, and how each account type gets its own tokens, see [Manage API Tokens](https://docs.logz.io/docs/user-guide/admin/authentication-tokens/api-tokens/) — that part is unchanged. This page covers roles.

:::note
API token roles are rolling out gradually. If you don't see a **Role** column, it isn't enabled for your account yet — contact [Logz.io support](https://logz.io/support-page/).
:::

## Roles

| Role | Assignable | Meaning |
|---|---|---|
| **Admin** | Yes | Full access. The default for any token, including tokens created before roles existed. |
| **User** | Yes | Standard access. |
| **Read-only** | Yes | Read-only access — the one to reach for when a token only needs to pull data out, such as an export job or a read-only integration. |
| **Custom** | No | A fine-grained permission set assigned outside this UI. Custom-role tokens can't be edited here — their role can only be changed through whatever set it in the first place. |

Every token created here gets **Admin** by default, so if you want a scoped token, set the role explicitly rather than leaving it at the default.

## Set a token's role

Select the **Role** column on an existing token to change it, or set it while creating a new one. Read-only and User can be switched freely; a **Custom**-role token shows its role but can't be edited from this table.

## Why this matters

A leaked or over-shared token used to mean full account access, whatever it was actually for. Scoping tokens by role means the blast radius of a leaked token matches what it was issued for — a Read-only token used in a dashboard export script can't be used to modify anything, even if it ends up somewhere it shouldn't.

If you're issuing a token for something read-only — a metrics scrape, a log export, a BI integration — set it to **Read-only** rather than leaving the Admin default.

## Related

* [Manage API Tokens](https://docs.logz.io/docs/user-guide/admin/authentication-tokens/api-tokens/)
* [API cookbook](https://docs.logz.io/docs/user-guide/integrations/api-cookbook/cookbook/)
