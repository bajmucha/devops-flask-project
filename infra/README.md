# Infra – Azure IaC (Bicep)

Ten katalog zawiera definicję infrastruktury w Azure z użyciem Bicep:

- Resource Group
- Azure Container Registry (ACR)
- (opcjonalnie) Storage Account

## Wymagania

- Zainstalowane narzędzia:
  - `az` (Azure CLI)
  - rozszerzenie Bicep dla Azure CLI

## Przykład wdrożenia

```bash
# Logowanie do Azure
az login

# Utworzenie grupy zasobów (jeśli jeszcze nie istnieje)
az group create -n rg-flask-devops -l westeurope

# Wdrożenie szablonu Bicep na poziomie subskrypcji/grupy
az deployment group create \
  --resource-group rg-flask-devops \
  --template-file main.bicep \
  --parameters @parameters.json
