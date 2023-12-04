
[![creating the resources for aws ec2-instance](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/Lofi/i1.png)](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22URfHNlswY_FYO5pfSsN9s%22%2C%22flow%22%3Atrue%7D%7D)
# creating the resources for aws ec2-instance | [Start Chat](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22URfHNlswY_FYO5pfSsN9s%22%2C%22flow%22%3Atrue%7D%7D)
this code is used to create the aws ec2-instance

# Prompt

```
resource "aws_instance" "this" {
  ami                     = "ami-0dcc1e21636832c5d"
  instance_type           = "m5.large"
  host_resource_group_arn = "arn:aws:resource-groups:us-west-2:012345678901:group/win-testhost"
  tenancy                 = "host"
} {{var_2}}
```

## Conversation




