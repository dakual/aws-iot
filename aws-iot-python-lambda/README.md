### Create zip file from lambda function
```sh
zip function.zip index.js
```

### Create an IAM Role for AWS Lambda
aws iam create-role --role-name iot-lambda-role --assume-role-policy-document file://lambda-role.json

> Make sure you save the ARN from the output.

### Grant Permissions to the Role
```sh
aws iam create-policy --policy-name iot-lambda-policy --policy-document file://lambda-role-policy.json
```

> Make sure you save the ARN from the output.

### Attach policy to role
```sh
aws iam attach-role-policy --role-name iot-lambda-role --policy-arn "<policy-ARN>"
```

### Create AWS Lambda functioon
```sh
aws lambda create-function --function-name iot --zip-file fileb://function.zip --runtime nodejs16.x --role arn:aws:iam::632296647497:role/iot-lambda-role --handler index.handler
```

> Make sure you save the ARN from the output.

### Test function
```sh
aws lambda invoke --function-name iot outputfile.txt
```

### Create a topic rule for Lambda
```sh
aws iot create-topic-rule --rule-name invokeLambda --topic-rule-payload file://iot-lambda-rule.json
```

### Create lambda trigger
```sh
aws lambda add-permission --function-name iot --region eu-central-1 --principal iot.amazonaws.com --source-arn arn:aws:iot:eu-central-1:632296647497:rule/invokeLambda --source-account 632296647497 --statement-id 123456-iot --action "lambda:InvokeFunction"
```


