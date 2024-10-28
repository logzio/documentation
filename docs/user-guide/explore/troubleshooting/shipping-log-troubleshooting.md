---
sidebar_position: 1
title: Log Shipping Troubleshooting
description: Troubleshoot shipping logs to Logz.io
image: https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg
keywords: [logz.io, troubleshooting, issues, log analysis, observability]
slug: /explore/troubleshooting/shipping-log-troubleshooting/
---

Getting logs from your system to Logz.io can be challenging, and identifying the exact issue can be difficult. This guide walks you through troubleshooting some common problems.



## Wait for Logz.io to index data

Before troubleshooting, ensure you give Logz.io time to parse and index your logs. This typically takes a few seconds to a minute, but sometimes longer.



## Check the Logz.io status page


Visit our [status page](http://status.logz.io/) to confirm everything is working normally. If you’re not signed up for status updates, go ahead and subscribe while you're there.

* If the status is **All Systems Operational**: Logz.io is operating normally. Move on to the next step.
* If the status **indicates an issue**: You may need to wait until we resolve the problem before proceeding.


## Check your shipper's connectivity

For MacOS and Linux, use `telnet` to ensure your log shipper can connect to Logz.io listeners.

:::note
As of MacOS High Sierra (10.13), telnet is not installed by default. You can install it using Homebrew by running `brew install telnet`.
:::

Run this command from your environment, adding the appropriate port number:

```shell
telnet listener.logz.io {port-number}
```

For Windows servers running Windows 8/Server 2012 and later, run this PowerShell command:


```shell
Test-NetConnection listener.logz.io -Port {port-number}
```

Refer to the table below for the correct port number based on your shipping method:


| Shipping method                         | Port |
|-----------------------------------------|------|
| Beats                                   | 5015 |
| Cloud Foundry drain over HTTPS          | 8081 |
| Filebeat                                | 5015 |
| Heroku drain over HTTP                  | 8080 |
| Heroku drain over HTTPS                 | 8081 |
| JSON file upload over HTTP              | 8070 |
| JSON file upload over HTTPS             | 8071 |
| log file upload over HTTP               | 8021 |
| log file upload over HTTPS              | 8022 |
| Logstash                                | 5050 |
| Logstash-forwarder                      | 5005 |
| Logstash over SSL                       | 5006 |
| NXLog                                   | 8010 |
| rsyslog                                 | 5000 |
| rsyslog over TLS                        | 5001 |
| TLS/SSL over TCP                        | 5052 |



### Connected to listener-group.logz-data.com

If you see "Connected to listener-group.logz-data.com",
your shipper can connect to the Logz.io listener.

To exit telnet, type Ctrl+], and then type `quit`.
You can move on to the next troubleshooting step.

### Status remains "Trying xxx.xxx.xxx.xxx..."

If you see "Trying xxx.xxx.xxx.xxx..." for more than 10 seconds,
your machine is having trouble connecting to the Logz.io listener.

Confirm that your firewall and network settings
allow communication with the right outbound port
and the Logz.io [listener IP addresses](/docs/user-guide/admin/hosting-regions/listener-ip-addresses/)
for your region.

## Verify your log shipping configuration

Logz.io uses your account token to send incoming logs to the correct account. Ensure that your log shipping configuration uses the correct account token. You can find your account token on the [account settings](https://app.logz.io/#/dashboard/settings/manage-accounts) page. Compare it with the token in your configuration.

If you're unsure where to find the token you're sending with your logs, review the instructions for your [log shipping method](https://app.logz.io/#/dashboard/integrations/collectors).

:::tip
The token is usually stored in a configuration file or as a query parameter in the URL you're shipping logs to. Search for "token" to locate it.
:::

* If the **tokens match**: Your logs will be sent to your account. Proceed to the next step.
* If the **tokens don’t match**: Update your shipper configuration with the correct account token and restart your shipper if necessary. If logs still don't appear in Explore after a few minutes, continue troubleshooting.


## Check your log shipper's logs

Review your log shipper’s logs to identify any errors indicating that your logs aren’t being shipped. Ensure the log shipper is running. Refer to your log shipper’s documentation if you're unsure where to find the logs.


### Common log shipper issues and fixes

* _Multiple configurations_: Ensure your shipper has only one configuration. Remove or comment out any extra configurations.
* _Incorrect paths_: Verify that all paths in the configuration are correct.
* _Incorrect permissions_: Ensure your shipper has the correct permissions to access the configured paths.

