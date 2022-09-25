### Create an IAM Role for AWS IoT
```sh
aws iam create-role --role-name iot-actions-role --assume-role-policy-document file://iam-role.json
```
> Make sure you save the ARN from the output.


### Grant Permissions to the Role
```sh
aws iam create-policy --policy-name iot-actions-policy --policy-document file://iam-policy.json
```
> Make sure you save the ARN from the output.

### Attach policy to role
```sh
aws iam attach-role-policy --role-name iot-actions-role --policy-arn "<policy-ARN>"
```

### Create DynamoDB table
```sh
aws dynamodb create-table --cli-input-json file://dynamoDB-create-table.json --region eu-central-1
```

### Create a topic rule for DynamoDB
```sh
aws iot create-topic-rule --rule-name saveToDynamoDB --topic-rule-payload file://dynamoDB-rule.json
```