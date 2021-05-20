provider "aws" {
  region = var.region
  profile = var.aws_profile
}

resource "aws_s3_bucket" "terraform_state" {
  bucket = "flamboyant-terraform-state"

  versioning {
    enabled = true
  }

  # Server-side encryption
  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "AES256"
      }
    }
  }
}

resource "aws_dynamodb_table" "terraform-locks" {
  name = "flamboyant-terraform-locks"
  hash_key = "LockID"
  billing_mode = "PAY_PER_REQUEST"

  attribute {
    name = "LockID"
    type = "S"
  }
}
