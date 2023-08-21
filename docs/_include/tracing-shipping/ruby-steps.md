##### Download instrumentation packages

Run the following command from the application directory:

```shell
gem install opentelemetry-sdk -v 1.3.0
gem install opentelemetry-exporter-otlp -v 0.26.1
gem install opentelemetry-instrumentation-all -v 0.40.0
```

##### Enable instrumentation in the code

Add the following configuration to the `Gemfile`:

```ruby
require 'opentelemetry/sdk'
require 'opentelemetry/exporter/otlp'
require 'rubygems'
require 'bundler/setup'
require 'opentelemetry/instrumentation/all'
```

Add the following configuration to the application file:

```ruby
Bundler.require

OpenTelemetry::SDK.configure do |c|
 c.service_name = '<YOUR-SERVICE-NAME>'
 c.use_all
end
```

Replace `<YOUR-SERVICE-NAME>` with the name of your tracing service defined earlier.


##### Install the Bundler

Run the following command:

```shell

bundle install

```

##### Configure data exporter

Run the following command:

```shell

export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4318

```