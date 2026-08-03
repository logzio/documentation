---
sidebar_position: 1
title: AI Settings
description: Set monthly limits on Logz.io AI usage and review your AI subscription from Plan and usage.
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logz.io, ai settings, ai usage, ai limits, capping, plan and usage, billing, orioniq, observability]
---

AI features consume usage that's billed, so Logz.io gives you a place to cap it. **AI Settings** lives under **Settings → Plan and usage** and does two things: sets monthly limits, and shows your AI subscription details.

Find it before you roll AI features out to a team, not after.

## Set monthly limits

Two limits can be set independently, each with its own on/off toggle:

| Limit | Caps |
|---|---|
| **Chat** | AI chat usage |
| **Invocations** | Agent invocations |

Turn a limit on and enter a monthly value; leave it off and the limit reads **No limit set**. A limit must be zero or greater — setting `0` is valid and effectively disables that kind of usage rather than being rejected as invalid.

Saving confirms with *AI monthly limits updated*.

Limits are monthly, so they reset on your billing cycle rather than rolling continuously.

## Subscription details

The same page shows your AI subscription — what you're entitled to and the period it applies to — so you can compare a limit you're about to set against what you've actually bought.

## Practical notes

* Set a limit before handing AI features to a team. It's a far more comfortable conversation than an unexpected line on a bill.
* A limit of `0` is the way to switch a category off while keeping the feature configured, rather than unpicking the configuration.
* Access is restricted to those who can see billing for the account, so most users won't have this page.

:::note
AI Settings is being rolled out. If you don't see it under Plan and usage, it isn't enabled for your account yet — contact [Logz.io support](https://logz.io/support-page/).
:::

## Related

* [Plan and usage](https://docs.logz.io/docs/user-guide/admin/logzio-accounts/plan-and-usage/)
* [AI Agent FAQ](/docs/open360/observability/faq/)
