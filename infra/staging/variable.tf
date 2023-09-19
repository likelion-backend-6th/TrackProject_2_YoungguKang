variable "region" {
  type    = string
  default = "ap-northeast-2"
}

variable "stage" {
  type    = string
  default = "staging"
}

variable "instance_type" {
  type    = string
  default = "n1-standard-1"
}

variable "key_name" {
  type = string
}

variable "security_groups" {
  type = list(string)
}
