@description('Nazwa grupy zasobów')
param resourceGroupName string

@description('Lokalizacja zasobów')
param location string = 'westeurope'

@description('Nazwa rejestru kontenerów ACR')
param acrName string

@description('Czy tworzyć konto Storage')
param createStorage bool = false

// Azure Container Registry
resource acr 'Microsoft.ContainerRegistry/registries@2023-07-01' = {
  name: acrName
  location: location
  sku: {
    name: 'Basic'
  }
  properties: {
    adminUserEnabled: true
  }
}

// Opcjonalne konto Storage
resource storage 'Microsoft.Storage/storageAccounts@2023-01-01' = if (createStorage) {
  name: '${uniqueString(resourceGroupName)}stor'
  location: location
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
}
