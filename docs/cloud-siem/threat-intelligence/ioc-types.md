---
sidebar_position: 5
---


# Preparing a feed


You can enrich log threat detection by adding your own private feeds to those provided by Logz.io.

This page provides guidelines to help you prepare your private feeds of IOCs so they can be pulled by Logz.io. For help configuring the sync, see [Adding a private feed.

## Supported IOC types

Supported IOC types include:

* IPs
* md5/sha1/sha256 hash signatures
* Domains
* URLs
* User-Agent headers
* Custom indicators (Custom indicators can be used to create lists of usernames, email addresses, or any other indicators, according to your own use case.)


### General guidelines

* **IOC-specific**

  Each feed should be a list of IOCs of a similar type. This is important to meet the validation requirements, as explained below.

* **Max number of entities**

  Your feed can contain as many as 10K entities.

* **Format**
  
  A feed of IOCs can have a variety of formats.
  
  For the default format, every IOC appears on a new line, without delimiters, separators, or additional notes or comments.

  Here's an example for what a feed of malicious IPs might look like when using the default format:

  ```
  1.1.1.1
  2.2.2.2
  3.3.3.3
  ```

  If your feed has another format, please <a class="intercom-launch" href="mailto:help@logz.io">contact our Support team</a> and they will be happy to assist.


### Validated format by IOC type

| IOC type | Format |
| IP | valid IP address |
| DNS | valid domain name (string) |
| URL  | valid URL |
| MD5 | 32 characters |
| SHA1 | 40 characters |
| SHA256 | 64 characters |
| USER-AGENT | max size 2 KB (string)  |
| CUSTOM | max size 64 characters (string)  |


### Allowlist IPs per region
