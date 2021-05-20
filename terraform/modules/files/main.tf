resource "aws_s3_bucket" "app_bucket" {
  bucket = "flamboyant-${var.environment}"
  acl = "public-read"

  tags = {
    "ckl:environment" = var.environment
    "ckl:project" = flamboyant
    "ckl:alias" = "app"
  }
}
