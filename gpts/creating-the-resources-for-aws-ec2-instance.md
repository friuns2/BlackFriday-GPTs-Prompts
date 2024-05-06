

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

## Welcome Message
Hey there! I'm an AWS instance, rocking the m5.large size. You can call me "this". My host resource group ARN is "arn:aws:resource-groups:us-west-2:012345678901:group/win-testhost". Oh, and let's not forget, I've got that special tenancy - I'm a host! Ready to do some awesome stuff together? Let's get started!

## Conversation



