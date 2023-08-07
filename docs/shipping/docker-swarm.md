---
id: Docker-Swarm
title: Docker Swarm
overview: Deploy this integration to ship metrics from your Docker Swarm network using containerized Telegraf agent.
product: ['metrics']
os: ['windows', 'linux']
filters: ['Containers', 'Orchestration']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/docker.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['']
metrics_alerts: []
---



Deploy this integration to ship metrics from your Docker Swarm network using containerized Telegraf agent.

### Pull the Docker image

```
docker pull logzio/docker-metrics-collector:latest
```

### Start the collector

Run the following command:

```shell
docker service create --name telegraf-docker-collector-metrics \
 --env METRICS_TOKEN="<<PROMETHEUS-METRICS-SHIPPING-TOKEN>" \
 --env LOGZIO_LISTENER="https://<<LISTENER-HOST>>:8053" \
 --mount type=bind,source=/var/run/docker.sock,target=/var/run/docker.sock \
 --mode global logzio/docker-metrics-collector:latest```
```

{@include: ../_include/general-shipping/replace-placeholders-prometheus.html}


If you prefer to keep these environment variables in an `.env` file, run the following command:

`docker run -d --env-file=docker.env -v /var/run/docker.sock:/var/run/docker.sock logzio/docker-metrics-collector:latest`

### Parameters

Below is a list of all environment variables available with this integration. If required, add a variable to the `docker run` command using the `--env` flag.

|Name|Description|Required/Default|
|---|---|---|
|METRICS_TOKEN|Your Logz.io metrics account token.|Required|
|LOGZIO_LISTENER|Your Logz.io listener address followed by port `8053`.|Required/Default: `https://listener.logz.io:8053`.|
|DOCKER_ENDPOINT|Address to reach the required Docker Daemon.|Default: `unix:///var/run/docker.sock`.|
|TIMEOUT|The request timeout for any Docker Daemon query.|Default: `5s`.|
|EXCLUDED_IMAGES|A list of strings, regexes, or globs, the container image names of which, will not be among the queried containers. !-prefixed negations are possible for all item types to signify that only unmatched container image names should be monitored. For example: `imageNameToExclude1,imageNameToExclude2)`|Default: `nil`.|

### Check Logz.io metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).

 
