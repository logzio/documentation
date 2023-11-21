---
id: JumpCloud
title: JumpCloud
overview: JumpCloud is a cloud-based platform for identity and access management. Deploy this integration to ship JumpCloud events to Logz.io.
product: ['logs','siem']
os: ['windows', 'linux']
filters: ['Access Management']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/jumpcloud.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---


JumpCloud is a cloud-based directory service that provides identity and access management solutions for securely managing users, devices, and applications. Every specified time interval, this integration collects JumpCloud events via the JumpCloud API defined in the configuration and forwards them to Logz.io.



**Before you begin, you'll need**: an active account with JumpCloud.
 
### Download the logzio/logzio-jumpcloud Docker image

```shell
docker pull logzio/logzio-jumpcloud
```

### Mount a host directory as a data volume

Create a local directory and navigate to it:

```shell
mkdir logzio-jumpcloud
cd logzio-jumpcloud
```

### Create a configuration file

In the `logzio-jumpcloud` directory, create a configuration file `config.yaml` with the following content:


```yaml

logzio:
 url: "https://<<LISTENER-HOST>>:8071"
 token: "<<LOG-SHIPPING-TOKEN>>"
jumpcloud_api:
   start_date:
   credentials:
     token: "<<JUMPCLOUD_API_TOKEN>>"
   settings:
     time_interval:
```

| Parameter Name | Description | Required/Optional | Default |
| --- | --- | --- | --- |
| url | The Logz.io Listener URL for your region with port 8071. | Required | - |
| token | Your Logz.io log shipping token. | Required | - |
| jumpcloud_api | A dictionary containing the JumpCloud API configurations. | Required | - |
| start_date | The start date and time for querying the JumpCloud API in UTC time with the format of `%Y-%m-%dT%H:%M:%S.%fZ`. For example: `2023-05-04T12:30:00.000000Z.` | Optional | The current date and time. |
| credentials | A dictionary containing the token for authenticating the JumpCloud API request. | Required | - |
| token | Your JumpCloud API token. | Required | - |
| time_interval | The time interval for querying the JumpCloud API in minutes. | Optional |5m |


### Run the docker container

```shell
docker run --name logzio-jumpcloud -v "$(pwd)":/app/src/shared logzio/logzio-jumpcloud
```

### Check Logz.io for your data

Give your data some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

If you still don't see your logs, see [log shipping troubleshooting]({{site.baseurl}}/user-guide/log-shipping/log-shipping-troubleshooting.html).

### Stop the docker container

```shell
docker stop -t 30 logzio/logzio-jumpcloud
```

## Tracking and continuity of API calls using lastTime.txt


Upon the successful completion of each API call, the system records the last start date for the subsequent iteration in a file named `lastTime.txt`. Each entry in this file begins with the API name and concludes with the last start date, formatted in UTC as `%Y-%m-%dT%H:%M:%S.%fZ`.

This `lastTime.txt` file is located in the mounted host directory you set up. In the event of a container stoppage, you can resume operations seamlessly by incorporating the last start date into the API filters within the configuration.

Please ensure that the last start date included in the configuration also adheres to the UTC format of `%Y-%m-%dT%H:%M:%S.%fZ` for consistency and accuracy.