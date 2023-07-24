---
id: Okta
title: Okta
sidebar_position: 1
overview: Okta is an enterprise-grade, identity management service, built for the cloud, but compatible with many on-premises applications.
product: ['metrics']
os: ['windows', 'linux']
filters: ['gcp', 'cloud']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/aiven-logo.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['']
metrics_alerts: []
---

Okta is an enterprise-grade, identity management service, built for the cloud, but compatible with many on-premises applications.

To ship Okta logs,
you'll deploy a Docker container
to collect the logs and forward them to Logz.io using Logstash.

You can send logs from multiple Okta tenants and any Okta domain.

:::note
If you want to ship from multiple Okta tenants over the same docker, you'll need to use the latest configuration using a tenants-credentials.yml file. Otherwise, you can continue using the previous configuration without a tenants-credentials.yml.
:::
 

#### Configuration

**Before you begin, you'll need**:

* Okta administrator privileges
* Port 5050 available - Logz.io Logstash endpoint receives logs from port 5050.

 

##### Get the API token and Okta domain from Okta

In the Okta developer console,
navigate to **API > Tokens**.
Create a token and paste it in your text editor.

![Create Okta API token](https://dytvr9ot2sszz.cloudfront.net/logz-docs/log-shipping/okta-create-token.png)

Click the **Authorization Servers** tab.
Copy your Okta domain from the **Issuer URI** column,
and paste it in your text editor. In the following example, you'd have copied "dev-123456.okta.com".

![Okta URL](https://dytvr9ot2sszz.cloudfront.net/logz-docs/log-shipping/okta-issuer-uri.png)


##### Create your tenants-credentials YAML

Build your tenants-credentials.yml:  
To create the file run the following command as root and then open the file in your text editor:

```
mkdir /etc/logzio-okta && touch /etc/logzio-okta/tenants-credentials.yml
```

Insert your tenants credentials into the YAML file in the following format:

```yml
tenants_credentials:
    - okta_api_key: <<OKTA-API-KEY>>
      okta_domain: <<OKTA-DOMAIN>>
```

This shipper supports up to 50 tenants. For multiple tenants, add your Okta API key and domain for each tenant. See the following example:

```yml
tenants_credentials:
    - okta_api_key: 123456a
      okta_domain: logzio-dev-123.okta.com
    - okta_api_key: 123456b
      okta_domain: logzio-dev-123.okta.com
    - okta_api_key: 123456c
      okta_domain: logzio-dev-123.oktapreview.com
```

###### Parameters

| Parameter | Description |
|---|---|
| OKTA_API_KEY (Required) | The Okta API key copied in step 1. |
| OKTA_DOMAIN (Required) | The Okta domain copied in step 1. It is found under the **Issuer URI column** in your Okta developer console.    Supports these [Okta domains](https://developer.okta.com/docs/guides/find-your-domain/findorg/):    example.oktapreview.com, example.okta.com, example.okta-emea.com |


:::note
YAML files are sensitive to spaces and tabs. It's a good idea to run your code through a YAML validator to make sure that its structure is correct. It's a good idea to run it through a YAML validator to rule out indentation errors, clean up extra characters, and check that it is valid. ([Yamllint.com](http://www.yamllint.com/) is a great choice.)
{:.info-box.tip}
 


Save the file in your working directory. That's the same one you're running the docker from.


##### Pull the Docker image

Download the logzio/logzio-okta image:

```shell
docker pull logzio/logzio-okta
```

##### Run the Docker image

Replace the placeholders in the code sample below before running it. Then run:

```shell
docker run \
--restart always \
--name Okta \
--env LOGZIO_TOKEN=<<LOG-SHIPPING-TOKEN>> \
--env LOGZIO_LISTENER_HOST=<<LISTENER-HOST>> \
-v /etc/logzio-okta/tenants-credentials.yml:/usr/share/logstash/tenants-credentials.yml \
-t logzio/logzio-okta
```

For Mac users: To fix issues with mounting files from root directory please add the path ‘/etc/logzio-okta’ to your Docker File Sharing.
Click [here](https://medium.com/effy-tech/fixing-the-var-folders-error-in-docker-for-mac-v2-2-3-2a40e776132d) for a guide on how to fix this issue - using docker desktop or manually edit your Docker configuration file.  
For more information about mounting files from root directory click [here](https://docs.docker.com/docker-for-mac/osxfs/#namespaces).


###### Parameters

| Parameter | Description |
|---|---|
| LOGZIO_TOKEN (Required) | {@include: ../_include/log-shipping/log-shipping-token.html} |
| LOGZIO_LISTENER_HOST (Required) | {@include: ../_include/log-shipping/listener-var.html}  |


##### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [log shipping troubleshooting]({{site.baseurl}}/user-guide/log-shipping/log-shipping-troubleshooting.html).

 
