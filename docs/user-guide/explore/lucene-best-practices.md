---
sidebar_position: 10
title: Lucene Best Practices
description: Best practices for using Lucene in Explore
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logz.io, explore, dashboard, log analysis, observability]
---

Explore supports an enhanced version of Lucene, offering autocomplete suggestions and syntax highlighting to help you build faster, more accurate queries.

As you type, Lucene displays available fields, variables, and operators. If your query contains a syntax error, hover over the error indicator to get feedback and fix it easily.

## Basic queries

Search for any logs that contain a specific word:

`error`

![simple text search](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lucene/lucene-error-jul16.png)

Search by specific fields and values using Lucene's auto complete feature. As you type, Lucene generates the relevant fields and values:

`object.status.capacity.pods:"29"`

![autocomplete lucene](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lucene/lucene-type-to-search.gif)

Use boolean operators to combine filters:

`k8s_container_name:"kafka" AND level_str:"ERROR"`

![basic query](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lucene/search-lucene-and.png)

Use parentheses to group conditions:

`k8s_container_name:"kafka" AND (level_str:"ERROR" OR level_str:"INFO")`

## Wildcards

Wildcards are special characters (`*` and `?`) used in search queries to match one or more unknown characters in a word or value. These can’t be the first character in a term or field name.

Search using partial matches:

**Single character:**

`k8s-19-demo-us-east-?-demo`

This would match `k8s-19-demo-us-east-1-demo`, `k8s-19-demo-us-east-2-demo`, but not `k8s-19-demo-us-east-12-demo` because `?` matches only one character.

**Multiple characters:**

`k8s_container_name:aws-*`

This matches values like `aws-load-balancer-controller-leader`, `aws-node`, `aws-init`, and any other that starts with `aws-`.

![wildcard query](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lucene/wildcard-lucene.png)

## Range queries

To perform range-based searches, the field must be mapped as a numeric value (e.g., long, float, double).

Inclusive range:

`bytes:[1000 TO 2000]`

Exclusive range:

`bytes:{1000 TO 2000}`

Open-ended range:
`timestamp:[2022-01-01 TO *]`

### Example:

Find logs where logSize is between 2000 and 3000:

`logSize:[2000 TO 3000]`

Add another filter:

`logSize:[2000 TO 3000] AND eventType:MODIFIED`

![range query](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lucene/lucene-range-query.png)

To exclude specific values:

`LogSize:[1000 TO 3000] AND eventType NOT "MODIFIED"`

## Fuzzy matching

Fuzzy matching helps when you're not sure about the exact spelling or expect typos. Use the `~` operator:

`env_id:k8s-20-demo-us-east-1-domo~`

This will return logs where the `env_id` is similar to k8s-20-demo-us-east-1-domo, based on edit distance.

![fuzzy query](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lucene/fuzzy-lucene.png)

You can also set a similarity level (1 or 2):

`env_id:k8s-20-demo-us-east-1-domo~1`

## Proximity matching

Use proximity search to find words that are near each other, even if not in exact order. To find logs where `failed` appears within 5 words of `status`, regardless of order:

`"failed status"~5`

This matches messages like:

`GET /api/v1 failed due to unexpected status 500`, or `status code 500 was returned because the request failed`. 

It’s especially useful when logs contain variable wording or you want to capture related phrases even if they're not side-by-side.

![Proximity query](https://dytvr9ot2sszz.cloudfront.net/logz-docs/lucene/proximity-lucene.png)


## Field existence and null checks

Use `_exists_` to find logs where a specific field is present:

`_exists_:newObject.kind`

Returns all logs that include the `newObject.kind` field, regardless of its value.

To find logs where a field doesn't exist, use the `NOT` operator:

`NOT _exists_:newObject.kind`

Returns logs where `newObject.kind` is missing.

You can also combine existence checks with other filters:

`_exists_:newObject.kind AND newObject.metadata.name:"aws-lb-controller-tls"`

Finds logs that have an `newObject.kind` and the metadata name of `aws-lb-controller-tls`.

## Special characters and regex

Lucene treats some characters as special operators. If you want to search for them literally (like in a file path or error message), escape them with a backslash (`\`).

Common special characters:

`+ - && || ! ( ) { } [ ] ^ " ~ * ? : \`

To search using a regular expression, use the `/regex/` format. This works well for partial matches, variations, or when field values include symbols.

Search for any logs where the `newObject.metadata.name` field ends in controller-leader:

`newObject.metadata.name:/.*controller-leader/`

If your search term contains special characters like `/`, `.`, or `:`, wrap the entire value in double quotes. This is especially useful when searching fields with slashes or dots in their names or values.

To search for the exact `newObject.metadata.name` value `aws-load-balancer-controller-leader`, use:

`newObject.metadata.name:"aws-load-balancer-controller-leader"`

Use with caution: regex queries can be resource-intensive and may be disabled on some systems.

:::note
Lucene does not support field names that include special characters like slashes (`/`), so queries like this won’t work: `newObject.metadata.annotations.control_plane_alpha_kubernetes_io/leader:"control-plane.alpha.kubernetes.io/leader"`. To search for values in such fields, use a free-text search instead: `"control-plane.alpha.kubernetes.io/leader"`.
:::

## Pro Tip

For complex filtering logic, use the Explore UI to build filters, then copy the generated Lucene query and fine-tune as needed.

## Keyboard Shortcuts

Explore includes several keyboard shortcuts to help streamline your workflow:

* Control + Enter – Submits the query, even if the suggestion menu is open.
* Shift + Enter – Creates a new line to organize your Lucene query more clearly.
* Command + D – Highlights the next occurrence of the selected word.

Explore uses the same editor as VS Code, so most of its shortcuts will work here. [View the full list here](https://code.visualstudio.com/docs/editor/keybindings#_keyboard-shortcuts-reference).

Looking for a shortcut that isn’t available? [Let us know](mailto:help@logz.io), and we’ll consider adding it!