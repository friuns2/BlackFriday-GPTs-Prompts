
[![Create big Terraform modules for provisioning AWS ECS Service Module](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/realistic/real_3.png)]()
# Create big Terraform modules for provisioning AWS ECS Service Module 
Develop a Terraform module to provision AWS ECS Service. Give step-by-step features, and get the results in steps, ensuring an efficient way to manage large outputs. (Better results in GPT-4)

# Prompt

```
Please develop a Terraform module named "ecs_app" to provision an AWS ECS Service. As you work on this task, I will sequentially provide information about the following features:

1. ECS Service
2. Task Definition Configuration
3. Autoscaling policies
4. Target group registration

I will tell you once I've finished providing details for each feature. When presenting your answer, arrange the output resources in groups of up to 10. Request my confirmation before advancing to the next group. Your final response should only contain the completed Terraform module without additional explanations or questions.
```

## Conversation

**ASSISTANT**: ```

variable "app_name" {

  type        = string

  description = "Name of the ECS Service"

}

variable "cluster_name" {

  type        = string

  description = "The name of the ECS cluster where the service will be created."

}

variable "task_definition_arn" {

  type        = string

  description = "ARN of the task definition to use for the service"

}

variable "desired_count" {

  type        = number

  description = "The desired number of tasks running in the service"

}

variable "max_capacity" {

  type        = number

  default     = 10

  description = "The maximum number of tasks this service should run"

}

variable "min_capacity" {

  type        = number

  default     = 1

  description = "The minimum number of tasks this service should run"

}

variable "target_group_arns" {

  type        = list(string)

  description = "List of target group ARNs to associate with the ECS service"

}



resource "aws_ecs_service" "ecs_app_service" {

  name            = var.app_name

  cluster         = var.cluster_name

  task_definition = var.task_definition_arn

  desired_count   = var.desired_count



  deployment_controller {

    type = "ECS"

  }



  load_balancer {

    target_group_arn = var.target_group_arns

    container_name   = var.app_name

    container_port   = 80

  }



  lifecycle {

    create_before_destroy = true

  }

}



resource "aws_appautoscaling_target" "ecs_app_target" {

  max_capacity       = var.max_capacity

  min_capacity       = var.min_capacity

  resource_id        = aws_ecs_service.ecs_app_service.arn

  scalable_dimension = "ecs:service:DesiredCount"

  service_namespace  = "ecs"

}



resource "aws_appautoscaling_policy" "ecs_app_policy" {

  name               = "${var.app_name}-scaling-policy"

  policy_type        = "TargetTrackingScaling"

  resource_id        = aws_appautoscaling_target.ecs_app_target.resource_id

  scalable_dimension = aws_appautoscaling_target.ecs_app_target.scalable_dimension

  service_namespace  = aws_appautoscaling_target.ecs_app_target.service_namespace



  target_tracking_scaling_policy_configuration {

    predefined_metric_specification {

      predefined_metric_type = "ECSServiceAverageCPUUtilization"

    }



    target_value = 50.0

  }

}

``` 



Please confirm before proceeding to the next feature.


