terraform {
  required_providers {
    ncloud = "~> 4.8.0"
  }

  provider "ncloud" {
    access_key  = var.access_key
    secret_key  = var.secret_key
    region      = "KR"
    site        = "PUBLIC"
    support_vpc = true
  }

  variable "region" {
    default = "ap-northeast-2"
  }

  variable "stage" {
    default = "production"
  }

  provider "null" {
    required_providers {
      ncloud = "~> 4.8.0"
    }
  }

  provider "ncloud" {
    region = var.region
    stage  = var.stage
  }

  module "vpc" {
    source = "./modules/vpc"
  }

  module "instance" {
    source = "./modules/instance"
    vpc_id = module.vpc.vpc_id
  }

  module "db" {
    source = "./modules/db"
    vpc_id = module.vpc.vpc_id
  }

  module "bucket" {
    source = "./modules/bucket"
  }

  module "domain" {
    source      = "./modules/domain"
    domain_name = "example.com"
  }

  module "load_balancer" {
    source = "./modules/load_balancer"
    vpc_id = module.vpc.vpc_id
  }
}
