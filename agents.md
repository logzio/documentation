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
* **A count column can become a navigation surface.** The Integrations Management table's "Used by" cell went from a plain hover tooltip to a real button opening a modal with links onward (ORIONIQ-1585). The invocation drawer got the reverse links the same week (ORIONIQ-1613: Agent definition / Agent invocations from a run, View invocations from the agent form). When either the Integrations or Agents Hub surface changes, check whether it added or removed a cross-link to the other — these two features shipped independently but both close the same kind of "you can get there but not back" gap.

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

## Slack notification mechanics

The bot's instructions say to post the PR link immediately, then **edit that same message** in place once Netlify comments its Deploy Preview link on the PR (never post the preview link as a second message or thread reply). As of 2026-09-04, the Slack MCP tools available to this bot (`slack_send_message`, `slack_send_message_draft`, `slack_schedule_message`, reactions, canvas, search/read) include **no message-edit / `chat.update` equivalent**. There is no way to satisfy that instruction literally with current tooling.

Until an edit-capable tool is added, the practical fallback is a threaded reply on the original notification with the preview link once it lands (clearly worse than an edit, but better than leaving the team without the link at all) — note this deviation explicitly when it happens rather than silently substituting it.

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

### 2026-08-31 — daily scan (since 2026-08-30), no doc changes

Scanned commits merged to each repo's default branch in the last ~24h.

* `gaia-hermes-ws` (`master`) — zero commits in the window.
* `Artemis` (`main`) — one commit, PR #208 "the Integrations Management table is a `DataTable`" (ORIONIQ-1573). A pure `DataTable` migration of the existing table: the same nine data columns plus actions (checked against `Management/columns.tsx` — labels match `docs/user-guide/orioniq/integrations.md` exactly), and the PR states no auth or persistence change. It adds resizing, virtualization, a sticky header, a split empty state, and re-indents nested Logz.io sub-accounts — all polish on an existing capability, not a new, changed, or removed one. No doc change.
* `OIQ-AI-service` (`main`) — six commits. One is customer-surface-adjacent: PR #452, "role-specific dashboard blocks for `/ai-agent`" (ORIONIQ-1209/1559) — adds dashboard-investigation context handling to the internal `/ai-agent` endpoint. Per the "shipped in code but not in the product" rule above: `gaia-hermes-ws` had zero merges this window, so nothing in `app-ai`/`app-ui` exposes it yet. Treat it as not-yet-shippable and re-check on a future run rather than documenting it now. The other five (#456, #458, #459, #460, #461) are internal RCA-pipeline/reasoning work (OIHV slices) with no stated route, schema, or auth change.
* `oiq-resources` (`main`) — PR #89 added a guardrail to `integrations/skills/logzio_api.md`: agents must not set the Logz.io alert `rca` flag (it bills OrionIQ analysis) unless explicitly asked. Checked whether this repo documents that field — it doesn't. The Alerts REST API (`rca`, `rcaNotificationEndpointIds`, `useAlertNotificationEndpointsForRca`) lives at `api-docs.logz.io`; this repo only redirects to it (`static/_redirects`). The closest local content is the UI-facing "Activate AI Agent Analysis" step in both `configure-alerts-explore.md` copies and `manage-security-rules.md`, which describes the toggle in product terms, not the raw field, and needed no change. Cross-repo note: PR #89's own description flags that `ai_backend/knowledgebase/base_skills/integrations/logzio_api.txt` in `OIQ-AI-service` is a stale copy of the same skill missing this guardrail — that fix belongs in that repo, not here.

No PR opened this run — nothing OrionIQ-facing needed a documentation change.

### 2026-09-01 — daily scan (since 2026-08-31), no doc changes

Ran in a session assigned a different branch (`claude/dreamy-turing-l19cyr`) than this PR's head (`claude/dreamy-turing-zq08bt`), so its findings were recorded in the PR description instead of here. Folded in now:

* `Artemis` #216, #210, #207 — UI/UX only (tour backdrop fix, shared drag-resize primitive, design-sync chore). No API/schema surface touched.
* `Artemis` #211 — the in-app "Ask about this run" chat handoff now carries the run's input and agent id. Verified against `api-endpoints.ts` — internal system-reminder construction for the OrionIQ chat UI, not a documented endpoint or schema.
* `OIQ-AI-service` #462 — image tag bump plus internal RCA operational-memory/skill config. Nothing under `ai_service/api/v1/**`.
* `gaia-hermes-ws` — 4 commits; 3 outside OrionIQ scope. The 4th, #16999 ("OrionIQ chat drawer on the Classic app's Explore page"), is a UI rollout reusing the existing app-ai run contract — no new or changed public endpoint/schema.
* `oiq-resources` — no commits in the window.

**Habit to design around, going forward:** each scheduled run gets a fresh session with its own assigned branch, which won't generally match this PR's head ref. Check out and push to the existing PR's head ref explicitly (`git fetch origin <pr-head-branch>:<pr-head-branch>`) rather than assuming session-branch continuity — that's what let this cycle's commit land in the right place instead of stranding another cycle's worth of findings in a PR description.

### 2026-09-02 — daily scan (since 2026-09-01), doc changes made

Scanned commits merged to each repo's default branch in the last ~24h. Two OrionIQ-facing features shipped, fully across their repo chains, and one catalog-only change:

* **ORIONIQ-1179 — Agent write-consent for integrations.** Shipped across all four repos: `oiq-resources` #80 (catalog write clearance for 48 connectors, `enableWrite`/`allow_write`) → `OIQ-AI-service` #434 (storage, credential-resolution gating, consent endpoints) → `gaia-hermes-ws` #16930 (BFF proxy routes + analytics allow-list) → `Artemis` #130 (the UI: an account-wide **Agent permissions** switch in Settings, admin-only, plus a per-connection **Agent permissions** choice in the connect/Configure form). Read the actual UI copy from `AccountSettings.tsx`, `IntegrationAuthModalContent.tsx`, and `write-consent.ts` rather than inferring it from the backend PRs — the two levels AND together (both must be Read & Write for a connection to actually get write access). Documented in `integrations.md` (new "Agent permissions" section) and `settings.md` (new Account-settings row). Not a public `/v2` API change — the write-permission routes are BFF-only, called by the OrionIQ UI — so `api.md` was untouched.
* **ORIONIQ-1504 — Stop a running invocation.** `Artemis` #212 (UI: Stop invocation button, replacing Re-invoke in that slot while a run is Running, in both the table row and the invocation details panel) + `gaia-hermes-ws` #17011 (BFF proxy to app-ai → AI Service `/ai-agent/stop`). Also BFF-only, no `/v2` surface. Corrected a pre-existing inaccuracy in `agents-hub.md`: the **Stopped** outcome row already said "any steps it completed are kept" from an earlier cycle, written before any UI could actually trigger a stop — the real behavior (confirmed against `AgentOutputTab.tsx` and the PR's own `apps/orioniq/CLAUDE.md` notes) is that a stopped run usually has **no** output, since most stops land mid-reasoning. Added a "Stop a running invocation" section describing the async confirm-then-finalize behavior and the same-account restriction (`cross-account.util.ts`), and added "stop a running invocation" to what the Read-only role can't do (it shares the `canModify` gate with Re-invoke).
* `Artemis` #215 (ORIONIQ-1590, sidenav scroll-fade fix) — pure visual polish, no doc change. `Artemis` #178 and `gaia-hermes-ws` #16998 (ORIONIQ-1222) — extracting OrionIQ's backend into its own `orioniq-be` service behind the `oiq-artemis-be` flag. Internal architecture, staging-only for now (see `Artemis/CLAUDE.md`), no customer-visible surface — no doc change.
* `oiq-resources` — PagerDuty catalog update: read surface expanded from 8 to 65 operations, plus a new required region select (US/EU) that existing connections must re-save once. Catalog-depth change only (which ops a connector's skill can call) — this repo has never documented per-connector operation coverage or config fields (not even region selects on the AWS integrations, which have had them for a while), so no doc change, consistent with that existing precedent. The remaining `oiq-resources` commits (auth-scope documentation corrections for Datadog, Intercom, FireHydrant, incident.io, Rootly, StatusCake, Statuspage; the write-skill-type test pin) back the ORIONIQ-1179 catalog work above rather than being a separate change.
* `gaia-hermes-ws` #16982 (APPZ-3175, SIEM risk score) — not OrionIQ, out of scope.

**Habit confirmed working:** checked out and pushed to this PR's actual head ref (`claude/dreamy-turing-zq08bt`) via `git fetch origin <branch>:<branch>` before committing, per last cycle's note. Also worth stating precisely: a UI feature can be fully shipped (proxied end-to-end, BFF included) without ever touching `public.routes.ts` — grep that file, but don't treat a miss there as "not real yet" if the BFF route and UI are both merged. The 2026-08-31 cycle's dashboard-investigation call was the opposite case (UI/BFF absent, correctly deferred); this cycle's two features are the case where BFF-only is the final state, not a waypoint.

### 2026-09-04 — daily scan (since 2026-09-03), doc changes made

Scanned commits merged to each repo's default branch in the last ~24h.

* `Artemis` (`main`) — 13 commits. Two are OrionIQ-facing and both are Artemis-only (no gaia/BFF change at all — extends the 2026-09-02 note that a feature can ship without touching `public.routes.ts`: these ship without touching gaia in any way):
  * **ORIONIQ-1585** (#253) — Integrations page UI fixes. The Management tab's **Used by** count is now a clickable button opening a modal that lists the agents using a connection, each with links to its invocations and its definition. The connect/configure dialogs show an integration's full description (previously ellipsized, hover-only). A Logz.io account with sub-accounts now counts, and rolls up its **Needs attention** status, as a single connection instead of one row per sub-account. (The configure dialog's scope table also got a sticky-header `DataTable` migration and a design-system tooltip z-index fix — both layout/internal, no doc wording change.) Updated `integrations.md`.
  * **ORIONIQ-1613** (#242) — invocation feedback moves from inside the Output tab's scrolling body to a footer rail visible on every tab (a rating is about the run, not one tab). A thumb now registers immediately (optimistic UI) and opens a note composer; dismiss is **Skip**, not Cancel, since the rating already posted. Fixed a dead end where a rated-but-uncommented run showed no way to add a note at all. Rating a still-running invocation is now blocked. New navigation: **Agent definition** and **Agent invocations** links from a run (both new — the reverse links from the agent list already existed, these two didn't), and **View invocations** from the agent's own configuration form. Updated `agents-hub.md`.
  * Not documented: #17027/#17024-style analytics-event registration commits, `#245` (retiring the already-dead `oiq-hermes` feature flag — nothing read it), `#252`/`#247` (`orioniq-be` vendor syncs, internal), `#251`/`#140`/`#213` (design-system component polish, not OrionIQ-specific product behavior), and two `chore: version packages` commits.
* `gaia-hermes-ws` (`master`) — 5 commits. `ORIONIQ-1626` (#17031) changes only internal billing/consumption attribution (which `triggerSource` an alert-driven RCA 2.0 invocation reports for usage accounting) — no customer-visible surface. `ORIONIQ-1618`/`ORIONIQ-1609` (#17027/#17024) register PostHog analytics events only, no UI/API change. The other two (`APPZ-3300`, `APPZ-3261`) are AI Observability / Explore Traces — out of OrionIQ scope per the filter rule.
* `OIQ-AI-service` (`main`) — zero commits in the window.
* `oiq-resources` (`main`) — zero commits in the window.

Both merged PRs were authored by Gavriel-M — assigned as the PR's author. PR: [#967](https://github.com/logzio/documentation/pull/967). Slack notification posted in `#orion-iq-team` before the Netlify preview link existed — see "Slack notification mechanics" above for why it won't get edited when the link lands.

### 2026-09-05 — daily scan (since 2026-09-04), no additional doc changes

Checked #967 first for unresolved reviewer feedback per the "address comments first" rule — none; its only comment is the Netlify bot's deploy-preview notice, and the Slack thread already carries the preview link (see the 2026-09-04 entry).

Scanned commits merged to each repo's default branch since the last run:

* `Artemis` (`main`), `gaia-hermes-ws` (`master`), `OIQ-AI-service` (`main`) — zero commits in the window.
* `oiq-resources` (`main`) — one PR, #93 (ralongit): both Salesforce integrations (`salesforce.json`, `salesforce-service-cloud.json`) switch from a pasted, 2h-expiring access token to a Connected App's OAuth2 client-credentials flow (`salesforce_access_token` → `salesforce_client_id` + `salesforce_client_secret`; `healthCheck` becomes a token-exchange probe). Explicitly **BREAKING for already-connected tenants** — they must re-enter credentials as a key/secret pair.
  Checked whether that needed a doc update: the projected field this repo actually documents is the top-level `auth` bucket, and it's unchanged — both integrations stay `"auth": { "apiKey": { ... } }` before and after, only the secrets/configs *inside* that bucket were renamed. `integrations.md`'s Connect table (API Key / Basic Auth / None) and the "no OAuth integrations in the catalog" note above are both still accurate. This is the same class of change as the 2026-09-02 PagerDuty entry — a per-connector credential-field change, not a change to the auth-method bucket — so, consistent with that precedent, **no doc change**.

No PR opened this run; folded into the still-open #967, which needed no updates as a result.

### 2026-09-06 — daily scan (since 2026-09-05), no additional doc changes

Checked #967 first for unresolved reviewer feedback per the "address comments first" rule — still none; CI (`PR validation`, Netlify deploy preview) is green on the current head, `mergeable_state` is `blocked` (pending required review/approval, not a check failure or a merge conflict — nothing for this bot to fix).

Scanned commits merged to each repo's default branch since the last run:

* `Artemis` (`main`) — zero commits since 2026-09-03 (last merge: #253).
* `OIQ-AI-service` (`main`) — zero commits since 2026-09-01 (last merge: #465).
* `gaia-hermes-ws` (`master`) — zero commits since 2026-09-03 (last merge: #17031).
* `oiq-resources` (`main`) — zero commits since 2026-09-04 (last merge: #93, already reviewed and found not doc-worthy on 2026-09-05).

All four repos: nothing merged in the last ~24h window. No PR opened this run; folded into the still-open #967, which needed no updates as a result. No new Slack notification sent — the 2026-09-04 post and its preview-link reply already cover #967, and nothing changed that the team needs to hear about again.

### 2026-09-07 — daily scan (since 2026-09-06), no additional doc changes

Checked #967 first for unresolved reviewer feedback per the "address comments first" rule — still none (only the Netlify bot comment, zero reviews); all 13 check runs on the current head are green/neutral, `mergeable_state` is still `blocked` on pending review, not on anything this bot can act on.

Scanned commits merged to each repo's default branch since the last run:

* `Artemis` (`main`) — one commit, #255: `orioniq-be` vendor-syncs `app-ai` up to gaia `6d0a66b88d`, i.e. **`ORIONIQ-1626`** landing in the vendored backend copy. This is the same change already assessed as internal-only when it first appeared in `gaia-hermes-ws` on 2026-09-04 (billing/consumption `triggerSource` attribution, no customer-visible surface) — the sync doesn't change that verdict, it's the same code arriving in the second place it's vendored.
* `OIQ-AI-service` (`main`) — one commit, #467, **`ORIONIQ-1623`**: classifies a step-budget (`GraphRecursionError`) ending as its own `run_incomplete.reason` (`recursion_limit`, was misreported as `internal_error`), adds a guard that forces a real final answer one round before the limit instead of discarding the run, and marks a forced answer with a new `step_budget_reached` flag on the `ai` event. Bumps the `/ai-agent` + `/oiq-bot` SSE contract 3.6.0 → 3.7.0 (`contracts/CHANGELOG.md`, both `output.schema.json`s). Checked whether this reaches a customer surface: `gaia-hermes-ws` had zero commits in the window (the contract's own consumer, App-AI, hasn't regenerated against it yet), and Artemis's chat UI reason-to-banner maps (`apps/orioniq/.../run-handoff/run-output.util.ts`'s `REASON` banners, `RunHistoryTable/tabs/ChatContentTab.constants.ts`'s truncation-flag list) still only know `timeout` / `context_overflow` / `internal_error` and `token_cost_limit_reached` — no `recursion_limit` or `step_budget_reached` anywhere in either. Same shape as the 2026-08-31 dashboard-investigation call: shipped in `OIQ-AI-service`, not yet wired to anything a customer sees. Per the "shipped in code but not in the product" rule, **not documented** — recheck once gaia/Artemis pick it up (at that point, `agents-hub.md`'s Incomplete row, which currently says "it timed out, ran out of context, or hit an internal error," will need a fourth clause for the step-budget case).
* `gaia-hermes-ws` (`master`) — zero commits since 2026-09-03 (last merge: #17031, `ORIONIQ-1626` — see the Artemis line above).
* `oiq-resources` (`main`) — one merge missed by the 2026-09-06 scan window: PR #92 (ralongit), **Azure Operator Nexus** integration — new `integrations/azure-operator-nexus.json` (Entra ID app-registration client-credentials auth, `apiKey` bucket with `client_id`/`client_secret` secrets and `tenant_id`/`subscription_id` configs, categories `Cloud & Infrastructure` + `Observability`, `popularityRank: 643` of ~647) plus its `integrations/skills/` query skill and `index.json`/`rank-order.txt` entries. Checked whether a new integration needs a doc update: `integrations.md`'s category table is a curated set of *examples* per category (not an exhaustive list, no integration count anywhere in this repo), both of this integration's categories are already represented by other examples, its auth shape is the same `apiKey` bucket as everything else in the catalog (no new auth-method bucket, so the "no OAuth integrations in the catalog" note stays accurate — same reasoning as the 2026-09-05 Salesforce entry), and at `643` it's one of the least popular entries in the entire catalog, i.e. not a candidate to displace a current example in a list the doc itself says is "ordered by popularity." **No doc change**, consistent with the catalog-depth-change precedent.

No PR opened this run; folded into the still-open #967, which needed no updates as a result. No new Slack notification sent — nothing here is new information for the team beyond what #967's thread already carries.
