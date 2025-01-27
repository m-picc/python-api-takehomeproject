variable "subscription_id" {
  description = "Azure Subscription ID"
  type        = string
}

# This should be replaced with a acr credential set.
variable "acr_username" {
  description = "Image Registry Username"
  type        = string
}

variable "acr_password" {
  description = "Image Regsitry Password"
  type        = string
}