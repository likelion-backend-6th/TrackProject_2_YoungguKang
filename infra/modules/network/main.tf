resource "ncloud_vpc" "main" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    Name = "my-vpc"
  }
}

resource "ncloud_subnet" "sns_subnet" {
  subnet_name       = "sns_subnet"
  vpc_id            = ncloud_vpc.main.id
  cidr_block        = "10.0.1.0/24"
  availability_zone = "ap-northeast-2a"
}

resource "ncloud_subnet" "lb_subnet" {
  subnet_name       = "lb_subnet"
  vpc_id            = ncloud_vpc.main.id
  cidr_block        = "10.0.2.0/24"
  availability_zone = "ap-northeast-2a"
}
