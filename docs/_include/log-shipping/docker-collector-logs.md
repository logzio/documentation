#### Upgrading to a newer version

* Upgrading to a newer version of docker-collector-logs while it is already running
will cause it to resend logs that are within the `ignoreOlder` timeframe.
You can minimize log duplicates
by setting the `ignoreOlder` parameter of the new docker
to a lower value (for example, `20m`).

* Version 0.1.0 of docker-collector-logs includes breaking changes. Please see the project's [change log](https://github.com/logzio/docker-collector-logs#change-log) for further information.