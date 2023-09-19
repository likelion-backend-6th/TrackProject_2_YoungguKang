resource "ncloud_load_balancer" "lb" {
  name = "my-load-balancer"
  type = "EXTERNAL"
  port_forwarding_rule {
    target_port   = 80
    protocol      = "HTTP"
    external_port = 80
  }
  subnet_no = var.subnet_no
  vpc_no    = var.vpc_no
}
