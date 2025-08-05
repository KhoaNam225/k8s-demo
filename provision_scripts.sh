resourceGroupName="aksResourceGroup"
applicationGatewayResourceGroup="aksAppGatewayResourceGroup"
location="australiaeast"
clusterName="aksCluster"
registryName="acrregistry$RANDOM"
keyVaultName="aksKeyVault$RANDOM"
appGatewayResourceGroupName="appGatewayResourceGroup"


# Create a resource group
az group create --name $resourceGroupName --location $location

# Create an AKS cluster
az aks create --resource-group $resourceGroupName --name $clusterName --location $location --node-count 1 --node-vm-size standard_d2as_v6 --generate-ssh-keys

############ Create 2 node pools with different VM sizes and labels ############
# NOTE: These commands are not run yet. But consider running them after the initial cluster creation.
# Create an AKS cluster with system node pool
az aks create --resource-group $resourceGroupName --name $clusterName --location $location --node-count 1 --node-vm-size standard_d2as_v6 --generate-ssh-keys --enable-managed-identity --nodepool-name systempool --nodepool-labels nodepool-type=system --kubernetes-version 1.33.2

# Add a user node pool for application workloads
az aks nodepool add --resource-group $resourceGroupName --cluster-name $clusterName --name userpool --node-count 1 --node-vm-size standard_d2as_v6 --mode User --labels nodepool-type=user

# Taint the system node pool to only allow system pods (optional but recommended)
az aks nodepool update --resource-group $resourceGroupName --cluster-name $clusterName --name systempool --node-taints CriticalAddonsOnly=true:NoSchedule
###############################

# Create an ACR registry
az acr create --resource-group $resourceGroupName --name $registryName --sku Basic

# Enable Nginx Ingress Controller extension
az aks approuting enable --resource-group $resourceGroupName --name $clusterName

# Show managed identity details
az aks show --resource-group $resourceGroupName --name $clusterName --query "identity" --output table

# Enable managed identity for the AKS cluster
az aks update --resource-group $resourceGroupName --name $clusterName --enable-managed-identity

# Attach ACR to AKS cluster using managed identity, this allows AKS to pull images from ACR
az aks update --resource-group $resourceGroupName --name $clusterName --attach-acr $registryName

# Check if ACR is attached
az aks check-acr --resource-group $resourceGroupName --name $clusterName --acr $registryName

# Check current node count
az aks show --resource-group $resourceGroupName --name $clusterName --query "agentPoolProfiles[0].count" --output table

# Scale the cluster to increase node count by 1 (assuming current count is 1, scale to 2)
az aks scale --resource-group $resourceGroupName --name $clusterName --node-count 2


###### Kubectl ingress verification ######
kubectl get service -n app-routing-system nginx -o jsonpath="{.status.loadBalancer.ingress[0].ip}"


az aks show --resource-group $resourceGroupName --name $clusterName --query addonProfiles.appRouting.config.json.external.host --output tsv

# Create a self-signed certificate for the domain
openssl req -new -x509 -nodes -out aks-ingress-tls.crt -keyout aks-ingress-tls.key -subj "/CN=k8s-demo.australiaeast.cloudapp.azure.com" -addext "subjectAltName=DNS:k8s-demo.australiaeast.cloudapp.azure.com"

# Export the SSL certificate to PFX format, later used to import in Azure Key Vault
openssl pkcs12 -export -in aks-ingress-tls.crt -inkey aks-ingress-tls.key -out aks-ingress-tls.pfx

# Create a Key Vault to store the certificate
az keyvault create --resource-group $resourceGroupName --location $location --name $keyVaultName --enable-rbac-authorization true

# Import the PFX certificate into Azure Key Vault
# Ensure you have the Key Vault Administrator role assigned to your user
az keyvault certificate import --vault-name $keyVaultName --name aks-ingress-tls --file aks-ingress-tls.pfx

# Key Vault ID retrieve
KEYVAULTID=$(az keyvault show --name $keyVaultName --query "id" --output tsv)

# Enable Key Vault integration with AKS app routing add-on
az aks approuting update --resource-group $resourceGroupName --name $clusterName --enable-kv --attach-kv ${KEYVAULTID}

# Get the certificate URI
az keyvault certificate show --vault-name $keyVaultName --name aks-ingress-tls --query "id" --output tsv