
[![terraform templates for yautomating your infrastructure](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/Abstract/i10.png)]()
# terraform templates for yautomating your infrastructure 
this prompt is used to create the ec2 instance in aws by using the varaibles

# Prompt

```
this terrafotm code is used to automate  your infrastructure, this code is used to automate the ec2 instances, where we can using the different values to automate the infrastructure in the form of  variables

main.tf

provider "aws" {
  region = var.aws_region
}

resource "aws_instance" "example" {
  ami           = var.aws_ami
  instance_type = var.instance_type
  key_name      = var.key_name
  subnet_id     = var.subnet_id
  tags = {
    Name = var.instance_name
  }
}


varaiable.tf

variable "aws_region" {
  description = "The AWS region where the EC2 instance will be created."
  default     = "us-east-1"  # Change this to your desired default region
}

variable "aws_ami" {
  description = "The ID of the Amazon Machine Image (AMI) to use for the EC2 instance."
}

variable "instance_type" {
  description = "The type of EC2 instance to launch (e.g., t2.micro)."
}

variable "key_name" {
  description = "The name of the SSH key pair to associate with the EC2 instance."
}

variable "subnet_id" {
  description = "The ID of the subnet in which to launch the EC2 instance."
}

variable "instance_name" {
  description = "The name tag for the EC2 instance."
}


terraform.tfvars

key_name       = "aws"       # Replace with your SSH key pair name
subnet_id      = "subnet-0eb86a8b9877e773b" # Replace with your subnet ID
instance_name  = "tefform_practice"     # Replace with your desired instance name
```

## Conversation




