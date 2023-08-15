---
id: Microsoft-SQL-Server
title: Microsoft SQL Server
overview: Microsoft SQL Server is a relational database management system developed by Microsoft. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.
product: ['metrics']
os: ['windows']
filters: ['Database']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/mysql.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['']
metrics_alerts: []
drop_filter: []
---


Microsoft SQL Server is a relational database management system developed by Microsoft. Telegraf is a plug-in driven server agent for collecting and sending metrics and events from databases, systems and IoT sensors.

To send your Prometheus-format SQL Server metrics to Logz.io, you need to add the **inputs.sqlserver** and **outputs.http** plug-ins to your Telegraf configuration file.

### Configure Telegraf to send your metrics data to Logz.io

 

#### Set up Telegraf v1.17 or higher

{@include: ../../_include/metric-shipping/telegraf-setup.md}
 
#### Add the inputs.sqlserver plug-in

First you need to configure the input plug-in to enable Telegraf to scrape the SQL Server data from your hosts. To do this, add the following code to the configuration file:


``` ini
# Read metrics from SQL queries
[[inputs.sql]]
  ## Database Driver
  ## See https://github.com/influxdata/telegraf/blob/master/docs/SQL_DRIVERS_INPUT.md for
  ## a list of supported drivers.
  driver = "mysql"

  ## Data source name for connecting
  ## The syntax and supported options depends on selected driver.
  dsn = "<<USER-NAME>>:<<PASSWORD>>@mysqlserver:3307/dbname?param=value"

  ## Timeout for any operation
  ## Note that the timeout for queries is per query not per gather.
  # timeout = "5s"

  ## Connection time limits
  ## By default the maximum idle time and maximum lifetime of a connection is unlimited, i.e. the connections
  ## will not be closed automatically. If you specify a positive time, the connections will be closed after
  ## idleing or existing for at least that amount of time, respectively.
  # connection_max_idle_time = "0s"
  # connection_max_life_time = "0s"

  ## Connection count limits
  ## By default the number of open connections is not limited and the number of maximum idle connections
  ## will be inferred from the number of queries specified. If you specify a positive number for any of the
  ## two options, connections will be closed when reaching the specified limit. The number of idle connections
  ## will be clipped to the maximum number of connections limit if any.
  # connection_max_open = 0
  # connection_max_idle = auto

  [[inputs.sql.query]]
    ## Query to perform on the server
    query="SELECT user,state,latency,score FROM Scoreboard WHERE application > 0"
    ## Alternatively to specifying the query directly you can select a file here containing the SQL query.
    ## Only one of 'query' and 'query_script' can be specified!
    # query_script = "/path/to/sql/script.sql"

    ## Name of the measurement
    ## In case both measurement and 'measurement_col' are given, the latter takes precedence.
    # measurement = "sql"

    ## Column name containing the name of the measurement
    ## If given, this will take precedence over the 'measurement' setting. In case a query result
    ## does not contain the specified column, we fall-back to the 'measurement' setting.
    # measurement_column = ""

    ## Column name containing the time of the measurement
    ## If ommited, the time of the query will be used.
    # time_column = ""

    ## Format of the time contained in 'time_col'
    ## The time must be 'unix', 'unix_ms', 'unix_us', 'unix_ns', or a golang time format.
    ## See https://golang.org/pkg/time/#Time.Format for details.
    # time_format = "unix"

    ## Column names containing tags
    ## An empty include list will reject all columns and an empty exclude list will not exclude any column.
    ## I.e. by default no columns will be returned as tag and the tags are empty.
    # tag_columns_include = []
    # tag_columns_exclude = []

    ## Column names containing fields (explicit types)
    ## Convert the given columns to the corresponding type. Explicit type conversions take precedence over
    ## the automatic (driver-based) conversion below.
    ## NOTE: Columns should not be specified for multiple types or the resulting type is undefined.
    # field_columns_float = []
    # field_columns_int = []
    # field_columns_uint = []
    # field_columns_bool = []

    ## Column names containing fields (automatic types)
    ## An empty include list is equivalent to '[*]' and all returned columns will be accepted. An empty
    ## exclude list will not exclude any column. I.e. by default all columns will be returned as fields.
    ## NOTE: We rely on the database driver to perform automatic datatype conversion.
    # field_columns_include = []
    # field_columns_exclude = []
```
* Replace `<<USER-NAME>>` with the user name for your SQL database.
* Replace `<<PASSWORD>>` with the password for your SQL database.

:::note
Query values must be numberic. Set it to either integer or float using the `field_columns_int` and `field_columns_float` settings.
:::
 


:::note
The database name is only required for instantiating a connection with the server and does not restrict the databases that we collect metrics from. The full list of data scraping and configuring options can be found [here](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/sql).
:::
 

#### Add the outputs.http plug-in

{@include: ../../_include/metric-shipping/telegraf-outputs.md}
{@include: ../../_include/general-shipping/replace-placeholders-prometheus.html}

### Check Logz.io for your metrics

Give your data some time to get from your system to ours, then log in to your Logz.io Metrics account, and open [the Logz.io Metrics tab](https://app.logz.io/#/dashboard/metrics/).



  
