---
sidebar_position: 1
title: Getting Started with Kubernetes 360
---

If you're having trouble sending your data (logs, metrics, and traces) to Logz.io, you may need to open your firewall to Logz.io listener servers. To see if you need to change your firewall configuration, see [log shipping troubleshooting]({{site.baseurl}}/user-guide/log-shipping/log-shipping-troubleshooting.html).

 
Send your data to the listener URL, not to individual IP addresses.
This ensures that data is properly balanced on our listener servers,
and that your data will be available to you as quickly as possible.
 
 

## listener

If you're sending data to listener 