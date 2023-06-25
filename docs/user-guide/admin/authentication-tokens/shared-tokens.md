---
sidebar_position: 5
title: Manage Shared Tokens

---


Shared tokens give you the option to share OpenSearch Dashboards objects and visualizations with stakeholders who don't have access to your Logz.io account.

Note that also non-admin users of your account will be able to use the account's shared tokens.

## Best-practice recommendations

A shared token has access to all of its account logs. When using a shared token, it is better not to rely on the OpenSearch Dashboards filters applied to the dashboard or visualizations being shared. Instead, it is best to limit access at the token level using token filters.

These best-practice recommendations will help you keep your data secure when using shared tokens:

* **Shared tokens can potentially give read-only access to all logs in your account.**

  It is therefore strongly recommended that you apply **token filters** to every token.

* **Shared tokens do not expire.**

  Always make sure to cancel them once they are no longer needed. Rotating your shared tokens often is a good idea in general and another way to make sure old tokens get canceled.

  For example, the shared token powering the sharing link of a snapshot is still active and continues to enable access to the logging database even after the logs included in the snapshot are no longer in retention. Always make sure to delete the token once it has fulfilled its purpose.

* **Changes in token filters take effect immediately.**

  Any changes will be reflected in affected sharing links, regardless of when they were created.

  This means that you can add or remove token filters to a shared token at any time to change access permissions. This can be done both _before or after_ the sharing link has been sent out. For example, if you've accidentally shared too much, you can add token filters to tighten control and your recipients' links will be updated accordingly.
  Of course, this works the other way as well. If you delete a sharing token, any existing sharing links that were previously sent out, will reflect the updated permissions.

  It is always a good idea to double-check token filters before using the public sharing option to make sure they are up-to-date.

* **Exercise caution and take note of who you're sharing your links with.**

  Opt for in-app sharing options whenever possible. If you plan on sharing links with clients, you can use sub accounts to keep each client's logs separate and more secure.

## Managing shared tokens

To manage your shared tokens: 

From your account, go to the <a href="https://app.logz.io/#/dashboard/settings/manage-tokens/shared" target ="_blank"> **Manage Tokens** > **Shared tokens** tab.</a> of your Operations workspace  It can be reached by selecting **<i class="li li-gear"></i> > Settings > Tools > Manage Tokens**.

The token for each account is listed in the table along with the date it was created.

### Working with shared tokens

* To create a token, click **+Add shared token**, type a brief **token name**, select **filters** from the dropdown list, and click **Add**.
* To delete a token, hover over it, and click **delete** <i class="li li-trash"></i> to delete it.


* To attach filters to a token, hover over the token, click **edit** <i class="li li-pencil"></i>, select filters from the dropdown list, and click **Save**.
* To remove filters from a token, hover over the token, click **edit** <i class="li li-pencil"></i>, <i class="li li-x"></i> out the filters you want to remove, and click **Save**.


### Working with token filters

Each token filter is a `field: value` key-value pair. The value needs to be an exact match. Wildcards are not supported.

* To add a new filter,
  type a brief **description**,
  copy in the name of a **log field** and the exact **value**. Then click **Add**.
  You can attach your new token filter to any of your shared tokens.

    For example, you could add a filter for a particular environment, with a field `env` and the value `test`.

* To delete a filter, hover over it, and click **delete** <i class="li li-trash"></i> to delete it. You'll be asked to confirm the deletion.

  If the filter you just deleted was used in any sharing links, they will immediately be updated to reflect the new access permissions.

### Testing token filters

You can open an incognito browser window to test your sharing links.

For example, if you're trying to share a dashboard, you can add or remove token filters and refresh the view in your browser window to see how the filters affect what your recipients will see.

:::warning Warning
Remember, the OpenSearch Dashboards filters at the dashboard or visualization level affect what your recipients will see. However - from a security point of view - they don't control access tightly enough. Make sure to apply the token filters you need to keep your data secure.
:::