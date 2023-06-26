variable "do_token" {}
variable "spaces_access_id" {}
variable "spaces_secret_key" {}
# variable "domain_name" {}
variable "ssh_key_name" {}

variable "project_slug" {
  description = "Project slug, used to name the droplets and spaces buckets."
  type        = string
  default     = "acl"
}

variable "env" {
  description = "This is the environment where your webapp is deployed. qa, prod, or dev"
}

variable "region" {
  description = "This is the cloud hosting region where your webapp will be deployed."
  type        = string
  default     = "fra1"
}

variable "droplet_image" {
  description = "Image slug for the desired image."
  type        = string
  default     = "ubuntu-20-04-x64"
}

variable "droplet_size" {
  description = "Size for the droplet."
  type        = string
  default     = "s-2vcpu-4gb"
}

variable "droplet_user" {
  description = "Size for the droplet."
  type        = string
  default     = "ubuntu"
}

variable "domain" {
  description = "Domain that should point to the droplet."
  type        = string
  default     = "africancitieslab.org"
}

variable "domain_link_droplet" {
  description = "If true, will automatically create an A record that points to the created droplet."
  type        = bool
  default     = true
}

variable "records" {
  description = "DNS records to create. The key to the map is the \"name\" attribute. If \"value\"==\"droplet\" it will be assigned to the created droplet's ipv4_address."
  type = map(object({
    domain = string
    type   = string
    value  = string
    ttl    = number
  }))
  default = {}
}

variable "docker_compose_version" {
  description = "Version of docker-compose"
  type        = string
  default     = "v2.2.2"
}

variable "cors_allowed_origins" {
  description = "Domain to add a CORS allowed origin rule to the spaces instance."
  type        = list(string)
  default     = ["https://africancitieslab.org"]
}