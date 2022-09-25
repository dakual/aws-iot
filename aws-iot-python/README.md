```sh
pip install paho-mqtt
```

```sh
aws iot create-thing --thing-name "myIOT"
aws iot list-things
aws iot create-keys-and-certificate --set-as-active --certificate-pem-outfile certificate.crt --public-key-outfile public.key --private-key-outfile private.key
aws iot list-certificates
aws iot create-policy --policy-name "myPolicy" --policy-document file://iotpolicy.json
aws iot attach-principal-policy --principal "<certificate-arn>" --policy-name "myPolicy"
aws iot attach-thing-principal --thing-name "myIOT" --principal "<certificate-arn>"
aws iot describe-endpoint
```