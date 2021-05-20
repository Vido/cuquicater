resource "aws_cloudwatch_log_group" "logs" {
  name = "flamboyant-${var.alias_name}-${var.environment}"
  retention_in_days = var.log_retention

  tags = {
    "ckl:environment" = var.environment
    "ckl:project" = flamboyant
    "ckl:alias" = var.alias_name
  }
}
