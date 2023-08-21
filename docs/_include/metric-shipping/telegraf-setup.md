**For Windows**

```shell
wget https://dl.influxdata.com/telegraf/releases/telegraf-1.27.3_windows_amd64.zip
```

After downloading the archive, extract its content into `C:\Program Files\Logzio\telegraf\`.

The configuration file is located at `C:\Program Files\Logzio\telegraf\`.

**For MacOS**

```shell
brew install telegraf
```

The configuration file is located at `/usr/local/etc/telegraf.conf`.

**For Linux**

*Ubuntu & Debian*

```shell
sudo apt-get update && sudo apt-get install telegraf
```

The configuration file is located at `/etc/telegraf/telegraf.conf`.

*RedHat and CentOS*

```shell
sudo yum install telegraf
```

The configuration file is located at `/etc/telegraf/telegraf.conf`.

*SLES & openSUSE*

```shell
# add go repository
zypper ar -f obs://devel:languages:go/ go
# install latest telegraf
zypper in telegraf
```

The configuration file is located at `/etc/telegraf/telegraf.conf`.

*FreeBSD/PC-BSD*

```shell
sudo pkg install telegraf
```

The configuration file is located at `/etc/telegraf/telegraf.conf`.