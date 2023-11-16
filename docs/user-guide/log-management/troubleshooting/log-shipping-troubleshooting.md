---
sidebar_position: 1
title: Log Shipping Troubleshooting
---


The process of getting logs from your system to Logz.io can be tricky,
and it can be difficult to pinpoint the exact issue.
In this doc, we'll walk through troubleshooting some common problems.

## Wait for Logz.io to index data

Before doing anything,
make sure you give Logz.io some time to parse and index your logs.
Normally, this takes a few seconds to a minute.
Sometimes, this can take longer.



## Check the Logz.io status page

Visit our [status page](http://status.logz.io/)
to confirm everything is working normally.
(If you're not already signed up for status updates,
go ahead and subscribe while you're there.)

### If the status is "All systems Operational"

If you see "All Systems Operational", Logz.io is operating normally.
You can move on to the next step.

### If the status is something else

On rare occasions, there may be an issue with our production environment.
If this happens,
you'll need to wait until we fix the problem before you can ship your logs.

## Check your shipper's connectivity

For macOS and Linux, use telnet to make sure your log shipper can connect to Logz.io listeners.

:::note
As of macOS High Sierra (10.13),
telnet is not installed by default.
You can install telnet with Homebrew
by running `brew install telnet`.
:::

Run this command from the environment you're shipping from, after adding the appropriate port number:

```shell
telnet listener.logz.io {port-number}
```
For Windows servers running Windows 8/Server 2012 and later, run the following command in PowerShell:


```shell
Test-NetConnection listener.logz.io -Port {port-number}
```


The port number depends on your shipping method.
You can find the correct port for your shipping method in the table below.


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

### If you see "Connected to listener-group.logz-data.com"

If you see "Connected to listener-group.logz-data.com",
your shipper can connect to the Logz.io listener.

To exit telnet, type Ctrl+], and then type `quit`.
You can move on to the next troubleshooting step.

### If the status remains "Trying xxx.xxx.xxx.xxx..."

If you see "Trying xxx.xxx.xxx.xxx..." for more than 10 seconds,
your machine is having trouble connecting to the Logz.io listener.

Confirm that your firewall and network settings
allow communication with the right outbound port
and the Logz.io [listener IP addresses](../../admin/hosting-regions/listener-ip-addresses/)
for your region.

## Check that log shipping configuration is set to the right account token

Logz.io uses your account token to send incoming logs to the correct account.
If you're not using the right account token,
your logs won't be indexed to your account.

You can find your account token
in the [account settings](https://app.logz.io/#/dashboard/settings/manage-accounts) page.

Compare your account token
with the token you're sending to Logz.io with your logs.
Review the instructions for your [log shipping method](https://app.logz.io/#/dashboard/send-your-data/collection?tag=all)
if you're not sure where to find the token you're sending with your logs.

:::tip
In most cases, the token is stored in a configuration file
or as a query parameter in the URL you're shipping logs to.
You can usually find it by searching for "token".
:::

### If the tokens match

If the tokens match, your logs will be sent to your account.
Move on to the next troubleshooting step.

### If the tokens don't match

If the tokens don't match, your logs won't be sent to your account.
Copy your acount token to your shipper configuration,
and restart your shipper if you need to.

If your logs still don't appear in OpenSearch Dashboards after a few minutes,
move on to the next troubleshooting step.

## Check your log shipper's logs

Next, you'll need to check your log shipper's logs.
If you're not sure where to find the logs,
see your log shipper's documentation.

When reviewing the logs,
look for errors indicating that your logs aren't being shipped.

Also confirm that the log shipper is running.
If it's not running, you'll need to troubleshoot the shipper.


### Common log shipper issues and fixes

* _Multiple configurations_: Make sure your shipper has one configuration. If it has more than one configuration, remove or comment out extra configurations.
* _Incorrect paths_: Make sure all the paths in the configuration are correct.
* _Incorrect permissions_: Make sure your shipper has the correct permissions to access configured paths.

