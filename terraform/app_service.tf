# Step 3: App Service Plan
resource "azurerm_service_plan" "app_service_plan" {
  name                = "fastapi-app-service-plan"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  os_type             = "Linux"
  sku_name            = "B1"
}

# Step 4: App Service for Hosting the Container
resource "azurerm_linux_web_app" "app_service" {
  name                = "fastapi-app-service"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  service_plan_id     = azurerm_service_plan.app_service_plan.id

  site_config {
    application_stack {
      docker_image_name        = "${azurerm_container_registry.acr.login_server}/fastapi-app:latest"
      docker_registry_url      = "https://${azurerm_container_registry.acr.login_server}"
      docker_registry_username = var.acr_username
      docker_registry_password = var.acr_password
    }
  }

  app_settings = {
    WEBSITES_ENABLE_APP_SERVICE_STORAGE = "false" # Optional, disables app service storage
    UVICORN_HOST                        = "0.0.0.0"
    UVICORN_PORT                        = "8000"
  }
}