provider "ncloud" {
  region = var.region
}

variable "region" {
  type    = string
  default = "ap-northeast-2"
}

variable "stage" {
  type    = string
  default = "staging"
}

module "loadBalancer" {
  source = "./modules/loadBalancer"

  subnet_no = var.subnet_no
  vpc_no    = var.vpc_no
}

module "network" {
  source = "./modules/network"
}

module "server" {
  source = "./modules/server"

  ami             = var.ami
  instance_type   = var.instance_type
  key_name        = var.key_name
  security_groups = var.security_groups
}
