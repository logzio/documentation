---
id: php
title: PHP
overview: Deploy this integration to enable automatic instrumentation of your PHP application using OpenTelemetry.
product: ['logs']
os: ['windows', 'linux']
filters: ['Code']
logo: https://logzbucket.s3.eu-west-1.amazonaws.com/logz-docs/shipper-logos/php.svg
logs_dashboards: []
logs_alerts: []
logs2metrics: []
metrics_dashboards: ['55uVoiaFwAreNAf7DojQZN']
metrics_alerts: ['1A2NfkQQprZqbtzQOVrcO7']
drop_filter: []
---

This integration uses the OpenTelemetry logging exporter to send logs to Logz.io via the OpenTelemetry Protocol (OTLP) listener.

### Prerequisites

- PHP 7.4+ for manual instrumentation or PHP 8.0+ for auto-instrumentation.

:::note
If you need an example aplication to test this integration, please refer to our [PHP OpenTelemetry repository](https://github.com/logzio/opentelemetry-examples/tree/main/php).
:::

### Configure the instrumentation

#### Install the necessary extensions and dependencies

To enable OpenTelemetry logging in PHP, follow these steps:

1. Install the OpenTelemetry PHP extension using PECL:

   ```bash
   pecl install opentelemetry
   ```

2. Add the OpenTelemetry extension to your `php.ini` file:

   ```ini
   [opentelemetry]
   extension=opentelemetry.so
   ```

3. Install the necessary Composer packages:

   ```bash
   composer require \
     monolog/monolog \
     open-telemetry/opentelemetry-logger-monolog
   ```

4. Set OpenTelemetry environment variables:

   Add the following OpenTelemetry environment variables in your PHP environment or programmatically in your PHP code:

   ```php
   // Set OpenTelemetry environment variables programmatically
   putenv('OTEL_PHP_AUTOLOAD_ENABLED=true');
   putenv('OTEL_LOGS_EXPORTER=otlp');
   putenv('OTEL_EXPORTER_OTLP_LOGS_PROTOCOL=http/protobuf');
   putenv('OTEL_EXPORTER_OTLP_LOGS_ENDPOINT=https://otlp-listener.logz.io/v1/logs');
   putenv('OTEL_EXPORTER_OTLP_LOGS_HEADERS=Authorization=Bearer <<LOG-SHIPPING-TOKEN>>,user-agent=logzio-php-logs-otlp');
   putenv('OTEL_RESOURCE_ATTRIBUTES=service.name=<YOUR-SERVICE-NAME>');
   ```

   Replace `<YOUR-SERVICE-NAME>` with the required service name.
   
   {@include: ../../_include/log-shipping/log-shipping-token.md}

5. Logging integration with Monolog:

   After setting up the environment variables, you can integrate OpenTelemetry with Monolog for logging. Below is an example that demonstrates how to configure and use Monolog with OpenTelemetry:

   ```php
   <?php

   use Monolog\Logger;
   use OpenTelemetry\Contrib\Logs\Monolog\Handler as MonologHandler;
   use OpenTelemetry\SDK\Logs\LoggerProviderFactory;
   use Psr\Log\LogLevel;
   
   require __DIR__ . '/vendor/autoload.php';
   
   // Initialize LoggerProviderFactory
   $loggerFactory = new LoggerProviderFactory();
   $loggerProvider = $loggerFactory->create();
   $handler = new MonologHandler(
       $loggerProvider,
       LogLevel::DEBUG,
   );
   
   // Initialize Monolog
   $monolog = new Logger('otel-logger', [$handler]);
   
   // Example logging with Monolog
   $monolog->info('This is an informational log message');
   $monolog->error('This is an error log message');
   
   // Shutdown the logger provider after logging
   $loggerProvider->shutdown();
   ```

6. Run the application:

   You can now run the PHP application and generate logs:

   ```bash
   php your_script.php
   ```

Replace your_script.php with the name of your PHP script. This will send the logs to Logz.io via the OpenTelemetry OTLP endpoint.


### Check Logz.io for your logs


Allow some time for data ingestion, then open [Open Search Dashboards](https://app.logz.io/#/dashboard/osd).

Encounter an issue? See our [log shipping troubleshooting](https://docs.logz.io/docs/user-guide/log-management/troubleshooting/log-shipping-troubleshooting/) guide.
