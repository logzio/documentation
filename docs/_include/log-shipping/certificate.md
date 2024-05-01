##### Download the Logz.io public certificate to your credentials server

For HTTPS shipping, download the Logz.io public certificate to your certificate authority folder.


```shell
sudo curl https://raw.githubusercontent.com/logzio/public-certificates/master/AAACertificateServices.crt --create-dirs \
-o /etc/pki/tls/certs/COMODORSADomainValidationSecureServerCA.crt \
-H "user-agent: logzio-json-logs"
```