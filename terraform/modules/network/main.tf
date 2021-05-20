resource "aws_vpc" "vpc" {
  cidr_block = "10.0.0.0/16"
  enable_dns_hostnames = "true"

  tags = {
    Name = "flamboyant-${var.environment}-vpc"
    "ckl:environment" = var.environment
    "ckl:project" = flamboyant
    "ckl:alias" = "network"
  }
}
