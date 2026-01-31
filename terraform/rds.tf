 resource "aws_db_subnet_group" "health_monitor" {
  name       = "health-monitor-subnet-group"
  subnet_ids = data.aws_subnets.default.ids
}

resource "aws_db_instance" "health_monitor_db" {
  identifier             = "health-monitor-db"
  engine                 = "postgres"
  instance_class         = "db.t3.micro"
  db_name                = "healthdb" # <- correct argument
  username               = "postgres"
  password               = "YOUR_DB_PASSWORD"
  allocated_storage      = 20
  storage_type           = "gp2"
  db_subnet_group_name   = aws_db_subnet_group.health_monitor.name
  vpc_security_group_ids = [aws_security_group.health_monitor_sg.id]
}
