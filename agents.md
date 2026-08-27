# agents.md

Operational memory for the OrionIQ API documentation sync bot. Maintained by the bot; read it before a run and update it after.

## Purpose

Scan the default branches of `logzio/Artemis`, `logzio/OIQ-AI-service`, `logzio/gaia-hermes-ws`, and `logzio/oiq-resources` for changes that affect OrionIQ's public-facing surface, audit this repo against them, and open a PR with the doc updates.

## Where the code lives

| Repo | Default branch | What's relevant |
|---|---|---|
| `gaia-hermes-ws` | `master` | `app-ai/` — the OrionIQ backend. **`app-ai/src/routes/public.routes.ts` is the definitive list of customer-callable endpoints** (`exposedTo: ['PUBLIC_API']`, prefix `/v2`). `app-ai/src/routes/orion-iq*.routes.ts` are the browser-facing BFF (`/app-ai/*`) — not customer API, but they drive the UI the user guide describes. `app-ai/CLAUDE.md` is a high-quality, current description of endpoints, capping, and audit behavior. Alert and SIEM-rule AI Analysis live in `app-ui/src/pages/Alerts/AlertForm/.../AIAgentRCA/` — the SIEM rule form reuses the same stepper (`modelName="rule"`), so a change there hits both products. |
| `Artemis` | `main` | `apps/orioniq/` — the OrionIQ standalone UI. **The single best source of user-facing copy**: `constants.ts` files next to each page carry the exact labels, tooltips, and guidance text the product shows. `columns.tsx` files give the real table columns. `src/constants.ts` `ORIONIQ_NAV_ITEMS` is the authoritative nav — check page names against it before writing a nav path. |
| `OIQ-AI-service` | `main` | `ai_service/`, `ai_backend/` — the AI/agent runtime. Mostly internal, but features surface through app-ai (for example, lessons in `ai_backend/knowledgebase/lessons/`). Pair its commits with the gaia commit that exposes them. |
| `oiq-resources` | `main` | **The catalog data, and the only correct source for it.** `integrations/*.json` — one file per integration (646 as of 2026-08), each with `name`, `categories`, `auth`, `popularityRank`; `integrations/skills/` holds their query skills. `marketplace/templates/*.json` — the live agent templates (5 shipping, plus a `future/` folder that is NOT live), each with `agentType` and `display.category`. Never hand-write a category list or an integration name — derive it from these files. |

## Canonical source for the public API

`Artemis` → `apps/orioniq/src/pages/Agents/Components/AgentEdit/api-endpoints.ts` is the in-app API reference shown to users on the agent's **API** section, rendered by `AgentApiDocs.tsx`. Mirror it — it is product-approved wording with request and response examples.

Caveat: it lags. As of 2026-08-27 it did not list the `lessons` endpoints that had already shipped in `public.routes.ts`. Always cross-check it against `public.routes.ts` and treat the routes file as the authority on what exists.

Base URL and auth: `X-API-TOKEN` header; `AgentApiDocs.tsx` hardcodes `https://api.logz.io`, but this repo's convention is `<<API-URL>>` with a link to Account region, which is more correct across regions.

## This repo's conventions

* **Two parallel doc trees.** `docs/open360/*` (current nav) and `docs/user-guide/*` (legacy nav) hold near-duplicate pages that differ only in app URLs and screenshots. When editing a page, check whether a twin exists — `find docs -name "<file>"` — and update both.
* **OrionIQ lives only under `docs/user-guide/orioniq/`.** There is no `docs/open360` OrionIQ section. Don't create one; that's a nav decision, not a doc fix.
* **Frontmatter** on every page: `sidebar_position`, `title`, `image` (the shared `docs-social.jpg`), `description`, `keywords` (array). Check for `sidebar_position` collisions inside a directory before adding a page.
* **`_category_.json`** sets a directory's label and position.
* **Admonitions:** `:::note`, `:::tip`, `:::info note`, closed with `:::`.
* **Internal links** are absolute doc paths with a trailing slash: `/docs/user-guide/orioniq/agents-hub/`.
* **Includes:** `{@include: <relative-path>}` works and is used ~276 times. But `docs/_include/api-cookbook/replace-vars.html` and `read-more-api-doc.html` are **dead legacy Jekyll** — they contain raw Liquid and no page uses them. Inline the "replace `<<API-TOKEN>>` / `<<API-URL>>`" bullets instead, as `docs/user-guide/integrations/api-cookbook/who-am-i.md` does.
* **API doc style:** endpoint heading, a fenced block with method and path, a `curl` sample with `X-API-TOKEN`, then a field table and a JSON response block.
* Tables are the house style for field, column, and option lists. Prose stays short.

## Product vocabulary

Match the product's own words, not an older doc's:

| Say | Not |
|---|---|
| Integrations | Utilities |
| Build an Agent (the button) | + Create New Agent |
| Agents / Invocations (the Agents Hub tabs) | — |
| Alert AI Analysis (the alert and rule step) | — |

## Agreed follow-up: the AI docs refactor

`docs/open360/observability/` and `docs/user-guide/observability/` are the SAME three pages twice — the "Observability IQ" category at both `/docs/category/observability-iq/` and `/docs/category/observability-iq-1/`, holding `assistantiq.md` (AI Agent), `ai-agent-analysis.md`, and `faq.md`. Their content also overlaps the OrionIQ pages.

**The direction is decided** (ralongit, PR #960): AI documentation should sit where it sits in the product.

* Open 360 and Cloud SIEM inner pages keep only what belongs to them: a reference to the **OrionIQ chat drawer** from the relevant nested doc (Explore, Dashboards, App 360, K8s 360, …), and the **Alert AI Analysis** agents.
* Everything else AI-related lives in the **OrionIQ** section only.
* The **FAQ** gets split per platform — one for Open 360, one for OrionIQ — rather than one page covering both.

This is a **migration, not a cleanup**, and it's a separate PR: 20 inbound links across 14+ pages point into those pages, `onBrokenLinks: 'throw'` means every one has to be repointed, and each removed public URL needs a `static/_redirects` entry. Don't attempt it as a side effect of a sync run.

## Recurring documentation patterns

* A change to an Agents Hub or Usage & Performance column lands in an Artemis `columns.tsx`; the doc's column table needs the same row. These drift often.
* New filters land in `AgentHubFilters.tsx` plus a `*-static-options.util.ts`. The wire values are strings, never booleans.
* Capping and budget copy lives in `apps/orioniq/src/pages/Settings/components/CappingSettings/constants.ts`. Quote it rather than paraphrasing — the wording is deliberate (for example, the trial/free budget is never described as "monthly", because it doesn't reset).
* Don't document Consul-configured dollar amounts or thresholds. They're per-environment and change without a code change.
* Code comments can be stale even when the code isn't. `orion-iq-memory-docs.routes.ts` still says user docs come from an in-memory mock, months after that was replaced. Verify against the commit that changed the behavior.
* **Renaming a page needs a redirect.** Add it to `static/_redirects` **above** the trailing `/:splat` catch-all — Netlify matches in order, so a rule after it never fires.
* A page's twin can have drifted. The two `configure-alerts-explore.md` copies had different sections before this run, not just different URLs — diff them rather than assuming they match.
* Auth methods, categories, and integration names are catalog data. As of 2026-08 the catalog has **no OAuth integrations at all** (580 `apiKey`, 56 `basicAuth`, 6 keyless) — so don't document an auth method just because the UI has a code path for it.

## Shipped in code but NOT in the product — do not document

An endpoint existing in `public.routes.ts` is not proof a feature is available to customers. Check for a UI before documenting it, and when in doubt ask the feature's owner.

* **Agent lessons** (`GET /v2/ai-agent/:agentId/lessons`, `PUT .../lessons/:lessonId/status`, ORIONIQ-1491 / ORIONIQ-1144). The endpoints are live and the backend learns from feedback, but there is **no lessons UI anywhere** in `Artemis` or `app-ui`, and rollout is gated per account. Documented in the first run and removed on review. Document it when the UI lands.
* The in-app API reference (`Artemis` `apps/orioniq/.../AgentEdit/api-endpoints.ts`) is a good signal here: it lists what the product actually exposes, and it did **not** list the lessons endpoints.

## Known gaps not yet documented

* **OrionIQ chat** has no page in this repo. Chat renaming, the server-owned chat-mode registry (Fast / Advanced), conversation history, stopping an in-flight run, and legacy AI Assistant history all shipped in the 3 months to 2026-08-27. The blocker is scope, not evidence: the chat renders in two surfaces (the Open 360 drawer and the OrionIQ standalone app) and it isn't clear which nav path the docs should describe. Confirm with the team before writing it.
* **Mobile push notifications** for finished agent runs (ORIONIQ-1463/1464) are undocumented.
* **OrionIQ for SIEM** (ORIONIQ-622) is undocumented.
* **Agent audit log** provenance columns (ORIONIQ-1531) are undocumented; unclear whether the audit log is customer-visible.
* **User journeys** (in-product tours, ORIONIQ-1432) are undocumented and probably don't need docs.

## Run log

### 2026-08-27 — initial run, 3 months of history (since 2026-05-27)

Scanned 110 commits in `OIQ-AI-service`, ~90 OrionIQ-related in `gaia-hermes-ws`, ~60 in `Artemis`.

Public API changes found in the window:

* `GET /v2/ai-agent/:agentId/feedback/:sessionId` — new (ORIONIQ-1011)
* `POST /v2/ai-agent/:agentId/feedback` — `comment` field added (ORIONIQ-1011)
* `GET /v2/ai-agent/:agentId/lessons` — new (ORIONIQ-1491 + ORIONIQ-1144)
* `PUT /v2/ai-agent/:agentId/lessons/:lessonId/status` — new (same)

The rest of the `/v2` surface predates the window and had never been documented here at all, so the new `api.md` covers it whole — an endpoint delta alone couldn't stand as a page.

Also documented: Memory (new page), Agents Hub columns/filters/capping/run outcomes/read-only role, Utilities auth methods and Logz.io API scopes, Usage & Performance tabs and cost columns.

Corrected: `docs/open360/settings/ai-settings.md` described monthly limit inputs that no longer exist — ORIONIQ-1561 (2026-08-26) replaced that page with a card linking to the OrionIQ Platform.

Notes for next time:

* Clones arrive shallow (50 commits). Deepen with `git fetch --shallow-since=<date> origin <branch>` before scanning.
* Filtering by commit message alone over-reports. Most `feat(ai-service)` commits are internal; the ones that matter touch `public.routes.ts`, a `columns.tsx`, or a `constants.ts` with user-facing copy.
* Resolve GitHub usernames for PR assignment from a commit's `author.login` — several authors commit with a `logz.io` email that isn't their username.

### 2026-08-27 — review round on PR #960

13 review comments. What they were actually about, so the next run doesn't repeat them:

* **Invented content.** The pre-existing Integrations category list was wrong in every row — the real 16 categories are in `oiq-resources`. Same class of error for auth methods. Lesson: never carry forward an existing doc's factual list without checking it against source; the bot inherited these and left them.
* **Wrong vocabulary.** "Utilities" is not a product word. Read `ORIONIQ_NAV_ITEMS` first.
* **Documenting the unreleased.** See the lessons section above.
* **Missing surfaces.** The Triggers menu, the Management tab, the Settings page, and most of the agent editor were all shipped and undocumented. A commit-history scan will not find these — they predate the window. Walk the product's nav and tabs against the doc tree once per run, not just the diff.
* **Two pages the scan missed entirely** because they live outside `docs/user-guide/orioniq/`: the alert AI Analysis section (whose Slack-endpoint requirement ORIONIQ-1298 had made obsolete) and the SIEM security rules page, which never documented Alert AI Analysis at all. Grep the whole `docs/` tree for AI surfaces, not just the OrionIQ directory.

Second round, same PR:

* **Deleting a stale field is not the same as documenting what replaced it.** The agent editor's "Payload (JSON)" is now the **Agent Definition** section — five friendly fields (Runbook, Guidelines, **Agent tools**, Output detail, Structured output, from `AgentEdit/agent-definition-fields.constants.ts`) with the raw JSON behind an **Advanced · Agent Definition** accordion. Dropping the old row without naming those read as a deletion. `SPEC_FRIENDLY_FIELDS` and `AGENT_KIND_OPTIONS` carry the labels and help text verbatim.
* **`spec.agents` (Agent tools) drives the Data Sources picker**, and the form refuses to save until every declared lane has a source. Two sections that look independent in the doc are coupled in the product.
* **Alert / rule AI Analysis creates a real agent**, editable in the Agents Hub like any other — so Integrations, Agent tools and its own daily cap are all configurable, none of which the alert form itself shows. The copy is in `AIAgentRCA/RcaNotes.tsx` ("Configure agent after saving", "Agent configuration is managed in the Agent Hub").
* **AI Agent Analysis output is stored in the agent's invocation history, NOT in "AI Agent chat history."** That phrasing was inherited from the existing page and is wrong; the analysis never lands in a chat.
