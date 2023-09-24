output "instance_public_ip" {
  value = module.instance.public_ip
}

output "db_endpoint" {
  value = module.db.endpoint
}

output "bucket_name" {
  value = module.bucket.bucket_name
}

output "domain_name" {
  value = module.domain.domain_name
}

output "load_balancer_dns_name" {
  value = module.load_balancer.dns_name
}
