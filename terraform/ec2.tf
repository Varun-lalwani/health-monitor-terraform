data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"]
  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
  }
}

resource "aws_instance" "health_monitor" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"
  subnet_id     = data.aws_subnets.default.ids[0] # updated
  vpc_security_group_ids = [
    aws_security_group.health_monitor_sg.id
  ]
  key_name = "my_web_server" # put your key name as a string
  tags = {
    Name = "health-monitor-app"
  }
}
