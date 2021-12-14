provider "digitalocean" {
  token             = var.do_token
  spaces_access_id  = var.spaces_access_id
  spaces_secret_key = var.spaces_secret_key
}

data "digitalocean_ssh_key" "ssh_key" {
  name = var.ssh_key_name
}

module "droplet" {
  source       = "martibosch/docker-compose-host/digitalocean"
  version      = "0.3.0"
  droplet_name = "${var.project_slug}-${var.env}"
  do_token     = var.do_token

  image                  = var.droplet_image
  region                 = var.region
  size                   = var.droplet_size
  docker_compose_version = var.docker_compose_version
  ssh_keys = [
    data.digitalocean_ssh_key.ssh_key.id
  ]
  user = var.droplet_user

  domain = var.domain
  # records = {
  #     # subdomain.example.com CNAME
  #     "subdomain.": {"domain"="african-architecture.org", "type"="CNAME", "value"="@", "ttl"=7200},
  #     # subdomain2.example.com through an A record
  #     "subdomain2.": {"domain"="example.com", "type"="A", "value"="droplet", "ttl"=1800},
  #     # subdomain3.otherdomain.com
  #     "subdomain3.": {"domain"="otherdomain.com", "type"="A", "value"="0.0.0.0"}
  #     # wildcard
  #     "*.": {"domain"="example.com", "value"="@", "ttl"=3600, "type"="CNAME"},
  # }
  records = var.records

  init_script     = "./serve-${var.env}.sh"
  compose_app_dir = ".."
}

resource "digitalocean_spaces_bucket" "bucket" {
  name          = "${var.project_slug}-temp-${var.env}"
  acl           = "public-read"
  force_destroy = true
  region        = var.region
}
