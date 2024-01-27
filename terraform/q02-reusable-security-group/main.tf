resource "aws_security_group" "allow_tls" {
  name = var.name
  description = "Allow TLS inbound traffic and all outbound traffic"
  vpc_id      = "banana"

  tags = {
    Name = var.name
  }
}

resource "aws_vpc_security_group_ingress_rule" "allow_tls_ipv4" {
  security_group_id = aws_security_group.allow_tls.id
  cidr_ipv4         = "10.0.0.0/16"
  from_port         = 443
  ip_protocol       = "tcp"
  to_port           = 443
}

output "result" {
    value = aws_security_group.allow_tls.name
}

variable "name" {
    type = string
    default = "banana"
}