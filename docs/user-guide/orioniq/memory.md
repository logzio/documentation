---
sidebar_position: 7
title: Memory
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Give OrionIQ lasting context about your environment with account and user memory documents.
keywords: [OrionIQ, memory, context, account memory, user memory, markdown, chat]
---

Memory gives OrionIQ context beyond what it can learn from your telemetry and integrations — your services and their owners, your operational conventions, and how you prefer answers. OrionIQ reads memory when answering in chat, so it can prioritize what matters to you and align its answers with your environment.

To open Memory, navigate to **OrionIQ > Memory** in the left navigation menu.

:::note
Memory shapes OrionIQ's answers in chat. Agents don't read memory documents yet.
:::

## Document scopes

Each memory document has a scope that decides who can see and edit it.

| Scope | Visibility |
|---|---|
| **Account** | Shared with your account. Everyone can view it; only admins can edit it. It shapes chat answers for all users. |
| **User** | Your file. Only you can view or edit it. It tailors your own chat answers. |

Every account starts with a protected account document, `ACCOUNT.md`, which you can edit but not delete. Your personal document is `USER.md`.

## The documents table

| Column | Description |
|---|---|
| **Name** | The document name. Click to open it. |
| **Scope** | Account or User. |
| **Last updated** | When the document was last changed. |
| **Changed by** | Who last changed it. |

## Edit a document

Click a document to open its editor. Documents are Markdown, and each editor explains what belongs in that document:

* **Account** — your services, dependencies, owners, business-critical systems, and operational conventions. Focus on what a new engineer needs in order to understand your environment quickly.
* **User** — your role, responsibilities, answer preferences, and personal context that helps OrionIQ understand how you work.

Use **Show example** in the account editor to see a sample document.

## Add a document

Click **Add to memory** to upload existing material — runbooks, architecture docs, or onboarding notes. Uploads must be Markdown (`.md`) files of up to 1 MB.

:::tip
Keep memory current. Update your documents as services, ownership, and processes change, so OrionIQ isn't reasoning from a stale picture of your environment.
:::
