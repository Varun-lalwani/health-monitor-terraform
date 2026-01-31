variable "aws_region" {
  default = "eu-north-1"
}

variable "key_name" {
  description = "EC2 key pair name"
}

variable "db_password" {
  description = "Postgres password"
  sensitive   = true
}
