---
sidebar_position: 9
title: Private Dashboards
description: Control who can see and edit a Logz.io dashboard by making it private and managing its per-user access.
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logz.io, dashboards, unified dashboards, private dashboards, sharing, permissions, access control, admin, observability]
---

By default a dashboard is visible to everyone in the account. Making it **private** restricts it to the people you share it with, which is useful for a work-in-progress dashboard or one built for a specific team.

Access is managed through the dashboard's **Share** control, available from both the Dashboards Hub row actions and the dashboard's own toolbar.

:::note
Private dashboards are being rolled out. If you don't see a Share control, the feature isn't enabled for your account yet — contact [Logz.io support](https://logz.io/support-page/).
:::

## Who can share a dashboard

Sharing manages a dashboard's per-user access and is also how a public dashboard becomes private, so it's limited to people who can manage that dashboard:

* **Account admins** — any dashboard in the account.
* **The dashboard's creator** — their own dashboards, whether or not those are currently private.

Out-of-the-box dashboards that ship with Logz.io have no real creator, so only admins can share those.

## What other users see

When a dashboard is private and you are neither its creator nor an account admin, the dashboard opens **read-only**. You can look at it if it's been shared with you, but you can't change it.

Creators and account admins are exempt from that restriction — an admin is never locked out of a dashboard in their own account.

## Practical notes

* Private is not a security boundary between accounts. It controls visibility among users of the same Logz.io account; it isn't a substitute for account separation.
* Admins can always see and manage private dashboards. If a dashboard needs to be invisible to admins, a private dashboard is the wrong tool.
* Make a dashboard private while you're building it, then open it up. It's easier than fielding questions about a half-finished dashboard someone found in the hub.
* A private dashboard behaves like any other for the people who can see it — variables, filters, drilldowns and alerts all work the same way.

## Related

* [Dashboards Hub](/docs/open360/dashboards/dashboards-hub/)
* [Dashboards Configuration Guide](/docs/open360/dashboards/edit-dashboards/)
