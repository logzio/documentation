---
id: Amazon-S3
title: Amazon S3
sidebar_position: 1
overview: This integration creates a Kinesis Data Firehose delivery stream that links to your Amazon S3 metrics stream and then sends the metrics to your Logz.io account. It also creates a Lambda function that adds AWS namespaces to the metric stream, and a Lambda function that collects and ships the resources' tags.
product: ['metrics']
os: ['windows', 'linux']
filters: ['gcp', 'cloud']
logo: https://docs.logz.io/images/logo/logz-symbol.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['1Pm3OYbu1MRGoELc2qhxQ1']
metrics_alerts: []
---

Deploy this integration to send Unified Audit Logging logs from Microsoft 365 to Logz.io. This method of log forwarding utilizes the Office/Microsoft 365 Management API, which currently supports the following Microsoft 365 content types:

* Audit.AzureActiveDirectory
* Audit.Exchange
* Audit.SharePoint
* Audit.General (includes all other workloads not included in the previous content types)
* DLP.All (DLP events only for all workloads)


**Before you begin, you'll need**: 

* An active subscription for Microsoft 365 with an appropriately provisioned administrator account.
* Unified Audit Logging enabled within M365’s [Security and Audit Center](https://docs.microsoft.com/en-us/microsoft-365/compliance/turn-audit-log-search-on-or-off?view=o365-worldwide#verify-the-auditing-status-for-your-organization)
* A machine for hosting filebeat version 7 or greater, preferably a Windows machine.


 


##### Register a new application in Azure AD

1. Navigate to portal.azure.com and sign-in with an administrative account.
2. Open the pop-out menu from the top left corner of the web page and click on **Azure Active Directory**.
3. Under the **Manage** section on the left-hand side of the page, select **App registrations > New registration**.
  ![New registration](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem/office365/new.png)
4. Name your app, and then adjust options as necessary. The default settings should be fine if working with a single M365 tenant without a URI proxy.
  
:::note
Take note of the Application (client) ID and the Directory (tenant) ID. These will be used later when configuring Filebeat.
:::
 

##### Create a client secret for your application

1. From your application overview, navigate to **Certificates & secrets**. A client secret will be needed for your Filebeat configuration in order to pull data from the management API.
2. Select **+ New client secret** and provide a description of your choosing.
3. Take note of the **Value** of the new client secret.

![Client secret](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem/office365/client.png)


##### Adjust app permissions to allow for interaction with the management API


1. Navigate to **API Permissions** on the left hand side of the page, select **+ Add a permission** and scroll down to find  the “Office 365 Management APIs” widget.
2. From the **Application permissions** tab, enable the **ActivityFeed.Read** and **ActivityFeed.ReadDlp** permissions.
![App permissions](https://dytvr9ot2sszz.cloudfront.net/logz-docs/siem/office365/permissions.png)


##### Download the Logz.io public certificate to your credentials server

For HTTPS shipping, download the Logz.io public certificate to your certificate authority folder.


```shell
curl https://raw.githubusercontent.com/logzio/public-certificates/master/AAACertificateServices.crt --create-dirs -o C:\ProgramData\filebeat\COMODORSADomainValidationSecureServerCA.crt
```

##### Configure Filebeat

{@include: ../_include/log-shipping/filebeat-input-extension.md}


1. Navigate to the `modules.d` directory and open the `o365.yml.disabled` file.
2. Paste the following into the file:

   ```yaml
   # Module: o365
   # Docs: https://www.elastic.co/guide/en/beats/filebeat/7.x/filebeat-module-o365.html

   - module: o365
     audit:
       enabled: true
       # Set the application_id (also known as client ID):
       var.application_id: <<Application ID>>
       # Configure the tenants to monitor:
       # Use the tenant ID (also known as directory ID) and the domain name.
       # var.tenants:
       #  - id: "tenant_id_1"
       #    name: "mydomain.onmicrosoft.com"
       #  - id: "tenant_id_2"
       #    name: "mycompany.com"
       var.tenants:
         - id: <<TenantID>>
           name: <<TenantName>>
       # List of content-types to fetch. By default all known content-types
       # are retrieved:
       # var.content_type:
       #  - "Audit.AzureActiveDirectory"
       #  - "Audit.Exchange"
       #  - "Audit.SharePoint"
       #  - "Audit.General"
       #  - "DLP.All"
       # Use the following settings to enable certificate-based authentication:
       #var.certificate: "C:\ProgramData\filebeat1\COMODORSADomainValidationSecureServerCA.crt"
       # var.key: "/path/to/private_key.pem"
       # var.key_passphrase: "myPrivateKeyPassword"
       # Client-secret based authentication:
       # Comment the following line if using certificate authentication.
       var.client_secret: <<Client Secret>>
       # Advanced settings, use with care:
       # var.api:
       #   # Settings for custom endpoints:
       #   authentication_endpoint: "https://login.microsoftonline.us/"
       #   resource: "https://manage.office365.us"
       #
       #   max_retention: 168h
       #   max_requests_per_minute: 2000
       #   poll_interval: 3m
   ```
3. Save the file as `o365.yml`.

4. Paste the following into the inputs section of the Filebeat configuration file:

   ```yaml
   filebeat.config:
     modules:
       enabled: true
       path: modules.d/*.yml
   fields:
     logzio_codec: plain
     token: <<LOG-SHIPPING-TOKEN>>
     type: o365
   fields_under_root: true
   #For version 6.x and lower uncomment the line below and remove the line after it 
   #filebeat.registry_file: 'C:\ProgramData\Filebeat' 
   filebeat.registry.path: 'C:\ProgramData\filebeat'
   #The following processors are to ensure compatibility with version 7
   processors:
   - rename:
       fields:
       - from: "agent"
         to: "beat_agent"
       ignore_missing: true
   - rename:
       fields:
       - from: "log.file.path"
         to: "source"
       ignore_missing: true
   ############################# Output ##########################################
   output:
     logstash:
       hosts: ["<<LISTENER-HOST>>:5015"]
       ssl:
         certificate_authorities: ['C:\ProgramData\filebeat\COMODORSADomainValidationSecureServerCA.crt']
   ```
  
   * {@include: ../_include/log-shipping/log-shipping-token.md}
   * Use the listener URL specific to the region where your Logz.io account is hosted. [Click to look up your listener URL](https://docs.logz.io/user-guide/accounts/account-region.html#available-regions).

5. Run Filebeat with the new configuration.

##### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd). You can filter for data of type `o365` to see the incoming Microsoft 365 logs.
  
If you still don't see your logs, see [Filebeat troubleshooting](https://docs.logz.io/shipping/log-sources/filebeat.html#troubleshooting).


 
