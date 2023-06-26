### View the latest triggered alert events, regardless of suppression

You can easily view the event logs written by the alert over the last 36 hours, regardless of notification suppression.

* Open the [**Logs > Alerts**](https://app.logz.io/#/dashboard/triggers/alert-definitions)
page from the navigation menu.
* Hover over an alert and click its **Menu button <i class="li li-ellipsis-v"></i>**.
* Select **View last events**.

![View last events option to quickly review triggered alerts regardless of notification suppression](https://dytvr9ot2sszz.cloudfront.net/logz-docs/alerts/view-last-events-new-nav.png)

You'll be taken to the OpenSearch Dashboards view, filtered by the alert ID for the last 36 hours. You can easily adjust the time picker to filter for another time frame.

Each log document represents an event, when the alert's query and triggering conditions were met. Click the **Investigate** button on a select event to drill down on the raw logs that caused the alert to trigger.
