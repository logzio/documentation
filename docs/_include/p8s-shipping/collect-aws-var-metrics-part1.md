#### Collect CloudWatch metrics

To collect CloudWatch metrics, you'll deploy a docker compose file that uses containers with the following images:

* [otel/opentelemetry-collector](https://hub.docker.com/r/otel/opentelemetry-collector)
* [prom/cloudwatch-exporter](https://hub.docker.com/r/prom/cloudwatch-exporter)
* [logzio/cloudwatch-config-builder](https://hub.docker.com/r/logzio/cloudwatch-config-builder)


##### Download the docker-compose.yml file

```
curl https://raw.githubusercontent.com/logzio/logzio-aws-metrics/main/docker-compose.yml -o docker-compose.yml
```

##### Define the environment variables

```
AWS_ACCESS_KEY_ID=<<AWS_ACCESS_KEY_ID>> \
AWS_SECRET_ACCESS_KEY=<<AWS_SECRET_ACCESS_KEY>> \
AWS_DEFAULT_REGION=<<AWS_DEFAULT_REGION>> \
LOGZIO_REGION=<<LOGZIO_REGION>> \
LOGZIO_TOKEN=<<PROMETHEUS-METRICS-SHIPPING-TOKEN>> \
AWS_NAMESPACES=<<AWS_NAMESPACES>> \
SCRAPE_INTERVAL=<<SCRAPE_INTERVAL>> \
P8S_LOGZIO_NAME=<<P8S_LOGZIO_NAME>> \
docker-compose up
```


###### Set environment variables for the logzio/cloudwatch-config-builder container

| Environment variable | Description |Required/Default|
|---|---|---|
| AWS_DEFAULT_REGION | Your region's slug. You can find this in the AWS Console region menu (in the top menu, to the right).  **Note:** This is the region that you will collect metrics from. |Required|
| LOGZIO_REGION | Your Logz.io region code. For example if your region is US, then your region code is `us`. [_Look up your region code_](https://docs.logz.io/user-guide/accounts/account-region.html#regions-and-urls). | Required |
| LOGZIO_TOKEN | Token for shipping Prometheus metrics to your Logz.io account. Find it under Settings > Manage accounts. [_Look up your Metrics account token_](https://docs.logz.io/user-guide/accounts/finding-your-metrics-account-token/) | Required |
| SCRAPE_INTERVAL | The time interval (in seconds) during which the Cloudwatch exporter retrieves metrics from Cloudwatch, and the Opentelemtry collector scrapes and sends the metrics to Logz.io. Default = 300.   **Note:** This value must be a multiple of 60.| Required |