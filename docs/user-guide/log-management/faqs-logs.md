---
sidebar_position: 20
title: FAQs About Sending Log Data
description: Frequently asked questions about sending log data to Logz.io
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logz.io, faq, opensearch dashboards, log analysis, observability]
slug: /log-management/faqs-logs/
---

If you're interested in integrating our logs with a specific service or application, here are some FAQs to help troubleshoot the process:

### Can I integrate with a 3rd-party application or service?

- If the logs are only viewable within the 3rd-party service or application, the most likely answer is "no“, because there is no way to have the logs ingested and indexed on our clusters.

- If the logs are accessible from outside your service or application, it's much more likely that you can ship those to Logz.io - depending on how that access is managed.



### Can I integrate with a proprietary application or service?

We offer various [integrations](https://app.logz.io/#/dashboard/integrations/collectors) to enable you to ship logs directly from your code, based on the language you're using.

This information is also available in the Logz.io Docs, via [**Ship data > Logs**](https://docs.logz.io/shipping/#log-sources), when you select the **From your code** filter.

### Can I integrate using a client-side solution?

You can try to ship data to Logz.io's bulk HTTP/S endpoint. However, we advise collecting the logs on a central server you control and using it to ship data to Logz.io. This is a more reliable method since it doesn't require the end-users to change their network setup to ensure the required ports (8070 for HTTP, 8071 for HTTPS) are open.

Logz.io's best practice is using a central server to ship your data, since shipping via a client-side solution is not as reliable or safe.

Logz.io's listeners are accessible via non-standard ports that vary based on the shipping method and encryption level. Therefore, the client will have to connect to a network that allows communication on said ports to ship logs successfully. However, collecting logs from an environment you can control lets you configure the outgoing connection and meet the listeners' requirements.

Shipping from a centralized location has additional advantages: it simplifies the debugging process and reduces the risk of losing logs due to network setup issues. 

## Logs written to a file

<h3 id="one-time"> <b>For a one time upload:</b></h3>

**cURL file upload** enables single file shipping and comes native to both MacOS and Linux.  The full command syntax can be found in our [cURL shipping instructions](https://app.logz.io/#/dashboard/send-your-data/log-sources/curl). 
Windows users can [download the files from the official website.](https://curl.haxx.se/download.html)

This method requires the following outside communication ports: 

+ Text files: 8021 (HTTP) and 8022 (HTTPS)
+ JSON files: 8070 (HTTP) and 8071 (HTTPS) 

This information is also available in the Logz.io Docs, in [**Ship your data > Logs > cURL file upload**](https://docs.logz.io/shipping/log-sources/curl.html).


**Invoke-RestMethod file upload** allows you to interact with REST APIs in PowerShell to upload JSON or plain text files. You can use Invoke_RestMethod to test your configuration or troubleshoot your connectivity to Logz.io. The full command syntax can be found in [Invoke-RestMethod file upload](https://app.logz.io/#/dashboard/send-your-data/log-sources/file-upload).

This information is also available in the Logz.io Docs, in [**Ship your data > Logs > Upload log files using Invoke-RestMethod**](https://docs.logz.io/shipping/log-sources/file-upload.html).

<h3 id="multiple-times"> <b> For continuous shipping:</b></h3>

[Filebeat](https://app.logz.io/#/dashboard/send-your-data/log-sources/filebeat) is your best option: It's lightweight, reliable, and easy to set up. This method requires outside communication on port 5015.

Other options: 

- [Logstash](https://app.logz.io/#/dashboard/send-your-data/log-sources/logstash): This method requires outside communication on port 5006 (encrypted) or port 5050 (unencrypted).
- [Rsyslog](https://app.logz.io/#/dashboard/send-your-data/log-sources/rsyslog): This method requires outside communication on port 5001.
- [Fluentd](https://app.logz.io/#/dashboard/send-your-data/log-sources/fluentd): This method requires outside communication on port 8071.

This information is also available in the Logz.io Docs **Ship your data** section in the [Filebeat](https://docs.logz.io/shipping/log-sources/filebeat.html), [Logstash](https://docs.logz.io/shipping/log-sources/logstash.html), [Rsyslog over TLS](https://docs.logz.io/shipping/log-sources/rsyslog.html), and [Fluentd](https://docs.logz.io/shipping/log-sources/fluentd.html) topics.


## Logs written to cloud storage

We have existing integrations with both [S3](https://app.logz.io/#/dashboard/send-your-data/log-sources/s3-bucket) and [Azure Blob](https://app.logz.io/#/dashboard/send-your-data/log-sources/azure-blob) storage.

This information is also available in the Logz.io Docs **Ship your data** section, in the [S3 Bucket](https://docs.logz.io/shipping/log-sources/s3-bucket.html) and [Azure Blob Storage](https://docs.logz.io/shipping/log-sources/azure-blob-trigger.html) topics.

## Logs that are accessible via API

<h3 id="one-api"> <b> For a one time upload:</b></h3>

Run the relevant API query per the instructions provided by the application or service and send the response as  payload to the [Logz.io JSON bulk uploads over HTTP/HTTPs](https://app.logz.io/#/dashboard/send-your-data/log-sources/json-uploads?type=http-config) endpoint. 

This method requires outside bulk HTTP/S endpoint communication on ports 8070 (HTTP) and 8071 (HTTPS).

:::caution Important
The payload must be formatted as inline JSON objects separated by a newline. Arrays or pretty-printed JSON payloads will fail.
:::

This information is also available in the Logz.io Docs **Ship your data** section, in the [Upload JSON logs](https://docs.logz.io/shipping/log-sources/json-uploads.html) topic.


<h3 id="multiple-api"> <b>  For continuous shipping:</b></h3>

This method follows the same instructions as the one time upload, but we recommend that you script the process to save time and effort. 