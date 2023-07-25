---
id: Heroku
title: Heroku
overview: Heroku is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud. Deploy this integration to install and launch Telegraf on the dynos of your Heroku app. Deploy this integration to install and launch Telegraf on the dynos of your Heroku app. This integration buildpack downloads the latest Telegraf release, extracts it on your dyno and starts it via a .profile.d script.
product: ['metrics']
os: ['windows', 'linux']
filters: ['gcp', 'cloud']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/aiven-logo.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
---

## Overview

Heroku is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud. Deploy this integration to install and launch Telegraf on the dynos of your Heroku app. Deploy this integration to install and launch Telegraf on the dynos of your Heroku app. This integration buildpack downloads the latest Telegraf release, extracts it on your dyno and starts it via a .profile.d script.

#### Configuring Telegraf to send your Heroku app metrics to Logz.io

**Before you begin, you'll need**:

* [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)

 

:::note
All commands in these instructions should be run from your Heroku app directory.
:::
 

##### Download the Telegraf configuration file

``` shell

wget -O telegraf.conf https://raw.githubusercontent.com/logzio/heroku-buildpack-telegraf/master/telegraf.conf

```

##### Enable environment variable

``` shell

heroku labs:enable runtime-dyno-metadata -a <<HEROKU_APP_NAME>>

heroku config:set LOGZIO_LISTENER=https://<<LISTENER-HOST>>:8053   

heroku config:set LOGZIO_TOKEN=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>>

git add .

git commit -m "Telegraf config" 

git push heroku main

```

{@include: ../_include/general-shipping/replace-placeholders-prometheus.html}
* Replace `<<HEROKU_APP_NAME>>` with the name of your Heroku app

##### Add the buildpack to the list of your Heroku buildpacks

``` shell

heroku buildpacks:add --index 1 https://github.com/logzio/heroku-buildpack-telegraf.git

git commit --allow-empty -m "Rebuild slug"

git push heroku main

```

##### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).


 
