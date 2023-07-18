---
id: Google-Workspace
title: Google Workspace
sidebar_position: 1
overview: Google Workspace is a collection of cloud computing, productivity and collaboration tools, software and products developed and marketed by Google. You can ship Google Workspace logs to Logz.io using Filebeat and Google Reports API.
product: ['metrics']
os: ['windows', 'linux']
filters: ['gcp', 'cloud']
logo: https://docs.logz.io/images/logo/logz-symbol.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
---

Google Workspace is a collection of cloud computing, productivity and collaboration tools, software and products developed and marketed by Google. You can ship Google Workspace logs to Logz.io using Filebeat and Google Reports API.


**Before you begin, you'll need**: [Filebeat](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-installation-configuration.html) installed.

:::note
The GSuite module was [deprecated as of Filebeat 7.12](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-module-gsuite.html#filebeat-module-gsuite) and has been replaced with the [Google Workspace module](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-module-google_workspace.html), to align with Google's current naming. The integration remains the same, requiring only that you replace "- module: gsuite" with "- module: google_workspace" in the modules block.
:::
 

 

#### Google Workspace setup

##### Set up a Service Account


Follow the official Google Workspace [tutorial](https://support.google.com/workspacemigrate/answer/10839762?sjid=10874551070185788155-EU#zippy=%2Cstep-use-google-cloud-to-turn-on-apis) for setting up a service account through IAM.

##### Grant access to the Admin SDK API

Enable access to the following APIs and services. If you can't find the API, specify the API name in **APIs & Services > Library** search box.

* Admin SDK
* People API (If you're using a Google Workspace Migrate version earlier than 2.4.2.0, use the Contacts API instead.)
* Google Workspace Migrate API
* Gmail API
* Google Calendar API
* Google Drive API
* Groups Migration API
* Groups Settings API
* Google Sheets API
* Tasks API

##### Delegate domain-wide authority to your service account

Open your Google Workspace domain’s [Admin console](http://admin.google.com/). Next, navigate to **Main menu** > **Security** > **API controls**.

In the Domain-wide delegation pane, select **Manage Domain Wide Delegation**. 


If you **can't** find the Manage Domain Wide Delegation option, you will need to **switch to a super-admin** Google Workspace account.
:::

Once you access the **Manage Domain Wide Delegation**, click **Add new**, and fill in the details:

* **Client ID** - Enter the service account's Client ID - you can find it in the service account's details under **Unique ID**. It is also found in the **client_id** field of the credentials file that was auto-downloaded when you created a new key for your service account.
* **OAuth Scopes** - Enter [the admin's API](https://www.googleapis.com/auth/admin.reports.audit.readonly)
* Click **Authorize** to confirm your changes.

#### Filebeat monitoring setup

{@include: ../_include/log-shipping/certificate.md}

##### Configure Filebeat

Open the Filebeat configuration file (the default path `/etc/filebeat/filebeat.yml`) with your preferred text editor.
Copy and paste the code block below, overwriting the previous contents.

{@include: ../_include/log-shipping/filebeat-input-extension.md}


```yaml
### Filebeat


### General
fields:
  logzio_codec: json
  token: <<LOG-SHIPPING-TOKEN>>
  # Replace <<LOG-SHIPPING-TOKEN>> with the token of the account you want to ship to.


  type: google_workspace
fields_under_root: true
encoding: utf-8
ignore_older: 3h

### Modules
filebeat.modules:
- module: google_workspace
  saml:

  # Replace <<PATH_TO_CREDENTIALS_FILE>> with the path to the file. See examples below.
  # Replace <<DELEGATED_ACCOUNT_EMAIL>> with the email address of the Admin (or superadmin) that authorized the domain wide delegation function. 

    enabled: true
    var.jwt_file: "<<PATH_TO_CERDNTIALS_FILE>>" 
    var.delegated_account: "<<DELEGATED_ACCOUNT_EMAIL>>"
  user_accounts:
    enabled: true
    var.jwt_file: "<<PATH_TO_CERDNTIALS_FILE>>"
    var.delegated_account: "<<DELEGATED_ACCOUNT_EMAIL>>"
  login:
    enabled: true
    var.jwt_file: "<<PATH_TO_CERDNTIALS_FILE>>"
    var.delegated_account: "<<DELEGATED_ACCOUNT_EMAIL>>"
  admin:
    enabled: true
    var.jwt_file: "<<PATH_TO_CERDNTIALS_FILE>>"
    var.delegated_account: "<<DELEGATED_ACCOUNT_EMAIL>>"
  drive:
    enabled: true
    var.jwt_file: "<<PATH_TO_CERDNTIALS_FILE>>"
    var.delegated_account: "<<DELEGATED_ACCOUNT_EMAIL>>"
  groups:
    enabled: true
    var.jwt_file: "<<PATH_TO_CERDNTIALS_FILE>>"
    var.delegated_account: "<<DELEGATED_ACCOUNT_EMAIL>>"

### Input

### Registry
filebeat.registry.path: /var/lib/filebeat

### Processors
# The following processors are to ensure compatibility with version 7
processors:
- if:
    has_fields: ['gsuite']
  then:
  - rename:
      fields:
      - from: "source"
        to: "gsuite_source"
- rename:
    fields:
    - from: "agent"
      to: "filebeat_agent"
    ignore_missing: true
- rename:
    fields:
    - from: "log.file.path"
      to: "source"
    ignore_missing: true
- add_id: ~

### Output 
output.logstash:
  hosts: ["<<LISTENER-HOST>>:5015"] 
  # Replace <<LISTENER-HOST>> with the host for your region. For example, listener.logz.io if your account is hosted on AWS US East, or listener-nl.logz.io if hosted on Azure West Europe. The required port depends whether HTTP or HTTPS is used: HTTP = 8070, HTTPS = 8071.


  ssl:
    certificate_authorities: ['/etc/pki/tls/certs/COMODORSADomainValidationSecureServerCA.crt']
```

For a full list of available Filebeat configuration options for the Google Workspace module, please see Filebeat's [documentation](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-module-google_workspace.html).



Still in the same configuration file, replace the placeholders to match your specifics.

{@include: ../_include/log-shipping/log-shipping-token.html}

{@include: ../_include/log-shipping/listener-var.html} 

* Replace `<<PATH_TO_CREDENTIALS_FILE>>` with the path to the file (for example `./credentials_file.json` with credentials of the service account path that was created on the GCP. It is preferable to use the full path for the file.

* Replace `<<DELEGATED_ACCOUNT_EMAIL>>` with the email address of the Admin (in most cases **superadmin**) that authorized the domain wide delegation function to the service account (GCP) on the **Google Workspace account**.

##### Start Filebeat

[Start or restart Filebeat](https://www.elastic.co/guide/en/beats/filebeat/master/filebeat-starting.html) for the changes to take effect.

##### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [Filebeat troubleshooting](https://docs.logz.io/shipping/log-sources/filebeat.html#troubleshooting).

 
