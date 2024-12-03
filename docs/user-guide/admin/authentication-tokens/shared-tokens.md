---
sidebar_position: 5
title: Manage Shared Tokens
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
description: Get and manage your shared API tokens
keywords: [api token management, api token, api, token, key creation, token authentication, security, secured login]
---


Shared tokens allow you to share objects and visualizations with stakeholders who don't have access to your Logz.io account. Note that even non-admin users of your account can utilize these shared tokens.


## Best practices for shared tokens

Using a shared token provides access to all of its account logs. When using a shared token, it's better to not rely on OpenSearch Dashboards filters applied to the dashboard or visualizations being shared. Instead, it's strongly recommended to use token filters to limit access at the token level.

* **Shared tokens can potentially give read-only access to all logs in your account.**

  It is therefore strongly recommended that you apply **token filters** to every token.

* **Set an expiration date for your shared tokens.**

By default, shared tokens expire in 7 days, but you can adjust this based on your needs. Regularly rotating tokens helps ensure old ones are no longer active. Remember to edit or delete the tokens once they are no longer needed.

For legacy tokens created before August 19th, 2024, which have no expiration, it’s advisable for admins to set expiration dates or delete them as needed.

* **Changes in token filters take effect immediately.**

Any modifications to token filters take effect instantly, affecting all associated sharing links, whether they were created before or after the change. This allows you to tighten or loosen access controls as necessary. If you delete a token, any related sharing links will be updated accordingly.

* **Exercise caution and take note of who you're sharing your links with.**

Always double-check token filters before using the public sharing option to ensure they are current. It's important to be mindful of who you share links with, and whenever possible, use in-app sharing options. For client sharing, consider using sub-accounts to keep logs secure and separated.

## Managing shared tokens

To manage your shared tokens: 

Navigate to [Settings > Manage tokens > Shared tokens](https://app.logz.io/#/dashboard/settings/manage-tokens/shared)

The token for each account is listed in the table along with its filter logic, last used, and its expiration date. 

### Working with shared tokens

* To create a token, click **+Add shared token**, type a brief **token name**, select an **expiration date**, add **filters** from the dropdown list if needed, and click **Add**.
* To delete a token, hover over it, and click **delete** <i class="li li-trash"></i> to delete it.
* To edit a token, hover over it and click **Edit** to adjust the expiration date or modify filters.

### Working with token filters

Each token filter is a `field: value` key-value pair. The value needs to be an exact match. Wildcards are not supported.

* To add a new filter,
  type a brief **description**,
  copy in the name of a **log field** and the exact **value**. Then click **Add**.
  You can attach your new token filter to any of your shared tokens.

    For example, you could add a filter for a particular environment, with a field `env` and the value `test`.

* To delete a filter, hover over it, and click **delete** <i class="li li-trash"></i> to delete it. You'll be asked to confirm the deletion.

  If this filter was in use, any sharing links will immediately reflect the updated access permissions.

### Testing token filters

Open an incognito browser window to test how your sharing links and token filters impact what recipients will see. Refresh the view after making changes to ensure everything works as intended.



:::warning Warning
While OpenSearch Dashboards filters control what recipients see, they don't provide adequate security control. Always apply necessary token filters to ensure your data remains secure.
:::