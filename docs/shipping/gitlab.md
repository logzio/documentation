---
id: GitLab
title: GitLab
overview: GitLab is a DevOps platform that combines the ability to develop, secure, and operate software in a single application. This integration allows you to send logs from your GitLan platform to your Logz.io account.
product: ['metrics']
os: ['windows', 'linux']
filters: ['gcp', 'cloud']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/gitlab.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
---

GitLab is a DevOps platform that combines the ability to develop, secure, and operate software in a single application. This integration allows you to send logs from your GitLan platform to your Logz.io account. 

#### Configuration

**Before you begin, you'll need**:

* [GitLab](https://about.gitlab.com/installation/) locally installed
* [Filebeat](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-installation.html) installed
* Port 5015 open

 

{@include: ../_include/log-shipping/certificate.md}

##### Add GitLab as an input

In the Filebeat configuration file (/etc/filebeat/filebeat.yml), add GitLab to the filebeat.inputs section.

GitLab has an advanced logging framework that ships a variety of different system logs.
We recommend reading [Log system](https://docs.gitlab.com/ee/administration/logs.html) from GitLab and modifying the Filebeat sample configuration according to your needs.

{@include: ../_include/log-shipping/log-shipping-token.html}

{@include: ../_include/log-shipping/filebeat-input-extension.md}


```yaml
# ...
filebeat.inputs:
- type: filestream
  paths:
  - /var/log/gitlab/gitlab-rails/production_json.log
  fields:
    logzio_codec: json

    # You can manage your tokens at
    #  https://app.logz.io/#/dashboard/settings/manage-tokens/log-shipping
    token: <<LOG-SHIPPING-TOKEN>>
    type: gitlab-production-json
  fields_under_root: true
  encoding: utf-8
  ignore_older: 3h

- type: filestream
  paths:
  - /var/log/gitlab/gitlab-rails/production.log
  fields:
    logzio_codec: plain

    # You can manage your tokens at
    #  https://app.logz.io/#/dashboard/settings/manage-tokens/log-shipping
    token: <<LOG-SHIPPING-TOKEN>>
    type: gitlab-production
  fields_under_root: true
  encoding: utf-8
  ignore_older: 3h

- type: filestream
  paths:
  - /var/log/gitlab/gitlab-rails/api_json.log
  fields:
    logzio_codec: json

    # You can manage your tokens at
    #  https://app.logz.io/#/dashboard/settings/manage-tokens/log-shipping
    token: <<LOG-SHIPPING-TOKEN>>
    type: gitlab-api-json
  fields_under_root: true
  encoding: utf-8
  ignore_older: 3h

- type: filestream
  paths:
  - /var/log/gitlab/gitlab-rails/application.log
  fields:
    logzio_codec: json

    # You can manage your tokens at
    #  https://app.logz.io/#/dashboard/settings/manage-tokens/log-shipping
    token: <<LOG-SHIPPING-TOKEN>>
    type: gitlab-application
  fields_under_root: true
  encoding: utf-8
  ignore_older: 3h
```

If you're running Filebeat 7 to 8.1, paste the code block below instead:


```yaml
# ...
filebeat.inputs:
- type: log
  paths:
  - /var/log/gitlab/gitlab-rails/production_json.log
  fields:
    logzio_codec: json

    # You can manage your tokens at
    #  https://app.logz.io/#/dashboard/settings/manage-tokens/log-shipping
    token: <<LOG-SHIPPING-TOKEN>>
    type: gitlab-production-json
  fields_under_root: true
  encoding: utf-8
  ignore_older: 3h

- type: log
  paths:
  - /var/log/gitlab/gitlab-rails/production.log
  fields:
    logzio_codec: plain

    # You can manage your tokens at
    #  https://app.logz.io/#/dashboard/settings/manage-tokens/log-shipping
    token: <<LOG-SHIPPING-TOKEN>>
    type: gitlab-production
  fields_under_root: true
  encoding: utf-8
  ignore_older: 3h

- type: log
  paths:
  - /var/log/gitlab/gitlab-rails/api_json.log
  fields:
    logzio_codec: json

    # You can manage your tokens at
    #  https://app.logz.io/#/dashboard/settings/manage-tokens/log-shipping
    token: <<LOG-SHIPPING-TOKEN>>
    type: gitlab-api-json
  fields_under_root: true
  encoding: utf-8
  ignore_older: 3h

- type: log
  paths:
  - /var/log/gitlab/gitlab-rails/application.log
  fields:
    logzio_codec: json

    # You can manage your tokens at
    #  https://app.logz.io/#/dashboard/settings/manage-tokens/log-shipping
    token: <<LOG-SHIPPING-TOKEN>>
    type: gitlab-application
  fields_under_root: true
  encoding: utf-8
  ignore_older: 3h
```




###### Preconfigured log types

* Production logs in JSON format: `gitlab-production-json`
* Production logs in plain text: `gitlab-production`
* API logs: `gitlab-api-json`
* Application logs: `gitlab-application`

The log type is used to apply the appropriate Logz.io preconfigured parsing pipeline so that your logs will be automatically parsed.

The default path to the logs differs, depending on how you've installed GitLab:

* If installed from Omnibus packages, the default path is: `/var/log/gitlab/...`
* If installed from source: `/home/git/gitlab/log/...`

Refer to GitLab Docs to learn more about the [Log system](https://docs.gitlab.com/ee/administration/logs.html).

##### Set Logz.io as the output

If Logz.io is not an output, add it now.
Remove all other outputs.

{@include: ../_include/log-shipping/listener-var.html} 

```yaml
# ...
output.logstash:
  hosts: ["<<LISTENER-HOST>>:5015"]
  ssl:
    certificate_authorities: ['/etc/pki/tls/certs/COMODORSADomainValidationSecureServerCA.crt']
```

##### Start Filebeat

[Start or restart Filebeat](https://www.elastic.co/guide/en/beats/filebeat/master/filebeat-starting.html) for the changes to take effect.

##### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [Filebeat troubleshooting](https://docs.logz.io/shipping/log-sources/filebeat.html#troubleshooting).

  
