resource "aws_ecr_repository" "ecr_repo" {
  name = "flamboyant-${var.alias_name}/${var.environment}"

  tags = {
    "ckl:environment" = var.environment
    "ckl:project" = flamboyant
    "ckl:alias" = var.alias_name
  }
}