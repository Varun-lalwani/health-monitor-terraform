output "ec2_public_ip" {
  value = aws_instance.health_monitor.public_ip
}

output "rds_endpoint" {
  value = aws_db_instance.health_monitor_db.endpoint
}
