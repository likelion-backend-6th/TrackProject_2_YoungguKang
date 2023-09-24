output "vpc_id" {
  value = ncloud_vpc.main.id
}

output "sns_subnet_id" {
  value = ncloud_subnet.sns_subnet.id
}

output "lb_subnet_id" {
  value = ncloud_subnet.lb_subnet.id
}
