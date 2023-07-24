---
id: Docker
title: Docker
sidebar_position: 1
overview: Docker is a set of platform as a service products that deliver software in containers. This integration allows you to ship performance logs of your Docker containers to your Logz.io account. 
product: ['metrics']
os: ['windows', 'linux']
filters: ['gcp', 'cloud']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/aiven-logo.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['1Pm3OYbu1MRGoELc2qhxQ1']
metrics_alerts: []
---


Docker is a set of platform as a service products that deliver software in containers. This integration allows you to ship performance logs of your Docker containers to your Logz.io account. 

#### Configuration

 

##### Pull the Docker image

Download the logzio/logzio-docker image:

```shell
docker pull logzio/logzio-perfagent
```

##### Run the Docker image

For a complete list of options, see the parameters below the code block.👇

```shell
docker run -d \
  --net="host" \
  -e LOGZ_TOKEN="<<LOG-SHIPPING-TOKEN>>" \
  -e LISTENER="<<LISTENER-HOST>>:5000" \
  -e USER_TAG="workers" \
  -e HOSTNAME=`hostname` \
  -e INSTANCE="10.1.2.3" \
  --restart=always \
  logzio/logzio-perfagent
```

###### Parameters

| Parameter | Description | Required/Default |
|---|---|---|
| LOGZ_TOKEN  | Your Logz.io account token. {@include: ../_include/log-shipping/log-shipping-token.html} | Required |
| LISTENER | Your account's listener host and port. {@include: ../_include/log-shipping/listener-var.html} | `listener.logz.io:5000` |
| USER_TAG | Assigned to the `user_tag` field of each log entry. You can use this field to group various hosts into meaningful visualisations. One recommended use case for this variable is to denote the host role. | -- |
| HOSTNAME | Name of the host this container is monitoring. Assigned to the `syslog5424_host` field of each log entry. | -- |
| INSTANCE | The IP address that will be assigned to the `instance` field of each entry. | -- |


##### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [log shipping troubleshooting]({{site.baseurl}}/user-guide/log-shipping/log-shipping-troubleshooting.html).

 
