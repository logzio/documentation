###### On Windows:

```shell
telegraf.exe --service start
```

###### On MacOS:

```shell
telegraf --config telegraf.conf
```

###### On Linux:

**Linux (sysvinit and upstart installations)**

```shell
sudo service telegraf start
```

**Linux (systemd installations)**

```shell
systemctl start telegraf
```