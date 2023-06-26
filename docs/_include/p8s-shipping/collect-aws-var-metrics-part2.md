| P8S_LOGZIO_NAME | The value of the `p8s_logzio_name` external label. This variable identifies which Prometheus environment the metrics arriving at Logz.io came from. |Default = `logzio-cloudwatch-metrics`.|
| CUSTOM_CONFIG_PATH | Path to your Cloudwatch exporter configuration file. For more information refer to the [documentation](https://github.com/prometheus/cloudwatch_exporter#configuration).  **Note:** Set the `period_seconds` parameter according to your `SCRAPE_INTERVAL`|  |
| CUSTOM_LISTENER | Set a custom URL to ship metrics to (for example, http://localhost:9200). This overrides the `LOGZIO_REGION` Environment variable. |  |



###### Set environment variables for the  `prom/cloudwatch-exporter` container

| Environment variable | Description |
|---|---|
| AWS_ACCESS_KEY_ID (Required)| Your IAM user's access key ID. |
| AWS_SECRET_ACCESS_KEY (Required)| Your IAM user's secret key. |

##### Run Docker

Run the command: `docker-compose up`.

##### View service configurations

You can view the exporter and collector configurations in the browser:

* CloudWatch exporter: [http://localhost:5001/config/cloudwatch](http://localhost:5001/config/cloudwatch)
* OpenTelemetry collector: [http://localhost:5001/config/otel](http://localhost:5001/config/otel)
