---
sidebar_position: 4
---

# Custom Endpoints


Integrate with your favorite tools using a custom webhook. Configuring a custom endpoint will allow you to send Logz.io notifications to your preferred apps,
even if they aren't on the list of preconfigured options.

Custom endpoints offer the advantage
of allowing you to customize the message body too.

## Adding a custom endpoint

 
### 1. Allow firewall access

Set up your systems to receive notifications from Logz.io.

:::caution Important
Alerts can only be sent on **ports 80 & 443**.
If you try to set another port in your end point, the alert will NOT be sent.
:::

#### Allowlist IPs per region

{@include: ../../../_include/general-shipping/allowed-ips.md}


### 2. Create a verification token (_Best practice but optional_)

The Logz.io IP range is used by all customers and should be used together with a verification token.

If you decide to open a port on your firewall for a Logz.io custom endpoint, we strongly advise that you add a verification token in the JSON payload of the custom endpoint and verify that the token exists on the receiving end.


It is best to restrict external access only to this specific endpoint.

Here's an example of a JSON payload for an alert that includes a verification token:

<!-- {% raw %} -->

```json
{
"token": "<SomeSecurityToken>",
"alert_title": "{{alert_title}}",
"alert_description": "{{alert_description}}",
"alert_severity": "{{alert_severity}}",
"alert_event_samples": "{{alert_samples}}",
"alert_tags":["{{alert_tags_json}}"]
}
```
<!--{% endraw %} -->


### 3. Add the endpoint

1. To add a new custom endpoint, click **Add endpoint**.
2. Specify the URL, method, and headers.
3. For POST/PUT methods, you can add a payload with a message.

:::caution Important
Some endpoints require a particular attribute/payload. For example, [Microsoft Teams](/user-guide/integrations/ms-teams.html#add-your-payload).
:::


![Configure a custom endpoint](https://dytvr9ot2sszz.cloudfront.net/logz-docs/notification-endpoints/custom-endpoint-POST_2021.png)


### 4. Configure your payload to add data to your alert notifications

<!-- {% raw %}-->

You can enhance your alert notifications with data pulled from the triggered alert.

For example, you can add a **View in OpenSearch Dashboards** drilldown link to a notification using the following:

```
"alert_view_link": "{{&alert_app_url}}#/view-triggered-alert?from={{&alert_timeframe_start_epoch_millis}}&to={{&alert_timeframe_end_epoch_millis}}&definitionId={{&alert_definition_id}}&switchToAccountId={{&account_id}}"
```

Logz.io notifications use [Mustache templating](https://mustache.github.io/).
All variables are HTML escaped by default. If you want to return **unescaped HTML**, add an **ampersand (&)**, for example `{{&alert_title}}`.



| Parameter | Description |
|---|---|---|
| {{alert_title}} | Title of the triggered alert  |
| {{alert_description}} | Alert description|
| {{alert_definition_id}} | Unique alert ID |
| {{alert_event_id}} | Unique ID of the triggered alert instance |
| {{alert_severity}} | Severity of the triggered alert |
| {{account_id}} | ID of the affected Logz.io account  |
| {{account_name}} |  Name of the affected Logz.io account |
| {{alert_samples}} | Prints a readable sample of the raw logs that caused the alert to trigger (String format, up to 10 logs) |
| ["{{alert_samples_json}}"] | Prints a machine friendly sample of the raw logs that caused the alert to trigger (JSON format, up to 10 logs) |
| {{alert_event_html}} | Returns a URL to an HTML file with the output table, as defined in the alert: Only relevant if the alert is configured to output data in tables |
| {{alert_event_image}} | Returns a URL to an image file with the output table, as defined in the alert: Only relevant if the alert is configured to output data in tables |
| {{alert_timeframe_start}} | Start time for the triggered alert event   |
| {{alert_timeframe_end}} | End time for the triggered alert event  |
| {{alert_severity_img}} | Colored icon indicating the alert severity  |
| {{alert_timeframe_start_epoch_millis}} |  Start time for the triggered alert event in UNIX milliseconds |
| {{alert_timeframe_end_epoch_millis}} |  End time for the triggered alert event in UNIX milliseconds |
| {{alert_app_url}}| The domain to your Logz.io account that is used to build links: For example: `https://app.logz.io` |
| {{alert_tags}}| A comma separated list of tags assigned to the alert: That is, `tag1, tag2, tag3` |
| ["{{alert_tags_json}}"]| A comma separated list of string tags as would be used in a JSON array: That is, `"tag1", "tag2", "tag3"`|


**To print the samples for correlated alerts, use the following syntax:**

`"samples_query_A": "{{#samples_jsons}}{{&alert_samples_0}}{{/samples_jsons}}"`

`"samples_query_B": "{{#samples_jsons}}{{&alert_samples_1}}{{/samples_jsons}}"`

Prints samples of raw logs, to be used instead of `alert_samples` when using a correlated alert.

:::caution Important
Test your payload. Some parameters may not be supported by the service receiving the alerts from Logz.io.
:::


### 5. Test the endpoint (_Optional_)

Click **Run the test** to test your endpoint.
Logz.io shows if the message was successfully sent.

Check that the message arrived at the target endpoint.

### 6. Save the endpoint

**Save** your endpoint.


 

## List of available alert variables

The following list is provided for convenience, to make it easy to copy & paste the parameters.



```
{{alert_title}}
{{alert_description}}
{{alert_definition_id}}
{{alert_event_id}}
{{alert_severity}}
{{account_name}}
{{account_id}}
{{alert_samples}}
{{alert_samples_json}}
{{alert_event_html}}
{{alert_event_image}} 
{{alert_timeframe_start}}
{{alert_timeframe_end}}
{{alert_timeframe_start_epoch_millis}}
{{alert_timeframe_end_epoch_millis}}
{{alert_app_url}}
{{alert_tags}}
{{alert_tags_json}}
```


<!-- {% endraw %}-->
