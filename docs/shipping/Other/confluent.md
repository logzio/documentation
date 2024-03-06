---
id: confluent
title: Confluent Cloud
overview: This integration allows you to ship Confluent logs to Logz.io using Cloud HTTP Sink.
product: ['logs']
os: ['windows', 'linux']
filters: ['Other']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/confluent.png
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: []
metrics_alerts: []
drop_filter: []
---


Deploy this integration to set up and run the HTTP Sink connector in a Kafka cluster to send Confluent logs to Logz.io.

**Before you begin, you'll need**:

* Confluent CLI installed and logged into your Confluent account
* Access to a Kafka cluster


## Using Kafka cluster's management interface

### Access connectors in cluster

1. Go to your Kafka cluster's management interface.
2. Select **Connectors** from the menu.

### Select HTTP Sink Connector

Find and select the **HTTP Sink** connector option.

### Select topics to collect data from

Choose the Kafka topic(s) you want to collect data from.

### Configure Kafka credentials

1. Proceed to the Kafka credentials step.
2. Select your preferred authentication method.
3. Click **Continue**.

### Set up authentication for Logz.io

1. In the **HTTP URL** field, enter:

   ```
   https://<<LOGZIO-LISTENER-HOST>>:8071/?token=<<LOGZIO-SHIPPING-TOKEN>>&type=<<YOUR-TYPE>>
   ```
   - Replace `<<YOUR-TYPE>>` with the desired log type.
   {@include: ../../_include/log-shipping/log-shipping-token.html}
   {@include: ../../_include/log-shipping/listener-var.html}

2. For **Endpoint Authentication type**, select **None**.

### Configure the connector

1. Choose **JSON** for **Input Kafka record value format**.
2. Click **Show advanced configurations**.
3. Set **HTTP Request Method** to **POST**.
4. Select **json** for **Request Body Format**.
5. Choose **false** for **Batch json as array**.

###  Size the connector

1. Decide on the number of tasks for the connector.
2. Click **Continue**.

### Review and launch

1. Name your connector in the **Connector name** field.
2. Click **Continue** to launch the connector.

### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd). 
  
If you still don't see your logs, see [log shipping troubleshooting](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/log-shipping-troubleshooting/).

### Removing the connector (if required)

1. Navigate to the connector's interface.
2. Go to the **settings tab**.
3. Choose **delete connector**.


## Using Confluent CLI

### Log in to Confluent account

Run `confluent login` to log in to your Confluent account via the CLI.

### Connect to Kafka cluster

Run `confluent kafka cluster use <<CLUSTER-ID>>` to connect to your desired Kafka cluster. Replace `<<CLUSTER-ID>>` with the ID of your Kafka cluster.

### Create configuration file

1. Open your preferred text editor on your local machine.
2. Paste the following configuration:

     ```json
     {
       "topics": "<<TOPICS>>",
       "input.data.format": "JSON",
       "connector.class": "HttpSink",
       "name": "<<NAME>>",
       "kafka.auth.mode": "KAFKA_API_KEY",
       "kafka.api.key": "<<KAFKA-API-KEY>>",
       "kafka.api.secret": "<<KAFKA-API-SECRET>>",
       "http.api.url": "https://<<LOGZIO-LISTENER-HOST>>:8071/?token=<<LOGZIO-SHIPPING-TOKEN>>&type=<<YOUR-TYPE>>",
       "request.method": "POST",
       ...
     }
     ```

Replace placeholders (`<<...>>`) with your specific values:

* `<<TOPICS>>`: Comma-delimited list of Kafka topics.
* `<<NAME>>`: Name for the connector.
* `<<KAFKA-API-KEY>>`: Your Kafka API key.
* `<<KAFKA-API-SECRET>>`: Kafka API secret matching the provided key.
* `<<YOUR-TYPE>>`: Desired log type.

{@include: ../../_include/log-shipping/log-shipping-token.html}
{@include: ../../_include/log-shipping/listener-var.html}

Save this file as `confluent-logzio.json` or a similar JSON file.

### Deploy the connector

1. Run `confluent connect cluster create --config-file <<PATH-TO-YOUR-CONFIG-FILE>>`.
2. Replace `<<PATH-TO-YOUR-CONFIG-FILE>>` with the path to your JSON file.
3. Expect output similar to:

     ```
     +------+-------------+
     | ID   | lcc-p12345  |
     | Name | logzio-sink |
     +------+-------------+
     ```

### Check Logz.io for your logs

Give your logs some time to get from your system to ours, and then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd). 
  
If you still don't see your logs, see [log shipping troubleshooting](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/log-shipping-troubleshooting/).

### Deleting the connector

Run `confluent connect cluster delete <<CONNECTOR-ID>>`. You'll be prompted to enter the connector name to confirm deletion.
