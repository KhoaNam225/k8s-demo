# Kubernetes Templates

This directory contains all the Kubernetes YAML manifests needed to deploy the demo applications to a Kubernetes cluster. The templates demonstrate common Kubernetes deployment patterns and best practices.

## 📁 Structure

```
k8s_templates/
├── deployments/
│   ├── back-end-deployment.yaml    # Demo app backend deployment
│   └── front-end-deployment.yaml   # Demo app frontend deployment
├── services/
│   ├── back-end-service.yaml       # Backend service definition
│   └── front-end-service.yaml      # Frontend service definition
└── ingress.yaml                    # Ingress for external access
```

## 🚀 Quick Deployment

Deploy all resources at once:

```bash
# Apply all manifests
kubectl apply -f k8s_templates/

# Verify deployment
kubectl get all -n k8s-demo
```

## 📋 Resource Details

### Namespace
- **Name**: `k8s-demo`
- **Purpose**: Isolates demo application resources

### Deployments

#### Backend Deployment (`k8s-demo-backend`)
- **Image**: `khoanam225/k8s-demo-backend:latest`
- **Replicas**: 1
- **Port**: 8080
- **Resources**:
  - CPU: 0.2-0.5 cores
  - Memory: 256Mi-512Mi

#### Frontend Deployment (`k8s-demo-frontend`)
- **Image**: `khoanam225/k8s-demo-frontend:latest`
- **Replicas**: 1
- **Port**: 80
- **Resources**:
  - CPU: 0.1-0.3 cores
  - Memory: 128Mi-256Mi

### Services

#### Backend Service
- **Type**: ClusterIP
- **Port**: 8080
- **Purpose**: Internal communication within cluster

#### Frontend Service
- **Type**: ClusterIP
- **Port**: 80
- **Purpose**: Serves frontend application

### Ingress
- **Purpose**: External access to the application
- **Paths**:
  - `/api/*` → Backend service
  - `/*` → Frontend service

## 🛠️ Customization

### Image Updates

Update the container images in deployment files:

```yaml
spec:
  containers:
  - name: k8s-demo-backend
    image: your-registry/k8s-demo-backend:v1.0  # Update this
```

### Resource Limits

Adjust resource requests and limits based on your cluster capacity:

```yaml
resources:
  limits:
    cpu: "1.0"        # Increase for higher load
    memory: "1Gi"     # Adjust based on requirements
  requests:
    cpu: "0.5"        # Minimum guaranteed resources
    memory: "512Mi"
```

### Scaling

Modify replica counts for horizontal scaling:

```yaml
spec:
  replicas: 3  # Scale to multiple instances
```

## 🔧 Configuration Options

### Environment Variables

Add environment variables to deployments:

```yaml
spec:
  containers:
  - name: k8s-demo-backend
    env:
    - name: API_BASE_URL
      value: "https://api.example.com"
    - name: LOG_LEVEL
      value: "INFO"
```

### ConfigMaps and Secrets

Create ConfigMaps for configuration:

```bash
kubectl create configmap app-config \
  --from-literal=api-url=https://api.example.com \
  -n k8s-demo
```

Create Secrets for sensitive data:

```bash
kubectl create secret generic app-secrets \
  --from-literal=api-key=your-secret-key \
  -n k8s-demo
```

### Health Checks

Add health check probes:

```yaml
spec:
  containers:
  - name: k8s-demo-backend
    livenessProbe:
      httpGet:
        path: /health
        port: 8080
      initialDelaySeconds: 30
      periodSeconds: 10
    readinessProbe:
      httpGet:
        path: /ready
        port: 8080
      initialDelaySeconds: 5
      periodSeconds: 5
```

## 🌐 Ingress Configuration

### Basic Ingress Setup

The provided ingress configuration assumes:
- Ingress controller is installed in your cluster
- DNS or host file entries point to your cluster

### TLS/SSL Configuration

Add TLS support to ingress:

```yaml
spec:
  tls:
  - hosts:
    - your-domain.com
    secretName: tls-secret
  rules:
  - host: your-domain.com
    # ... rest of configuration
```

### Custom Domains

Update the ingress for custom domains:

```yaml
spec:
  rules:
  - host: your-app.example.com
    http:
      paths:
      # ... path configurations
```

## 🔍 Troubleshooting

### Check Deployment Status

```bash
# View all resources
kubectl get all -n k8s-demo

# Check deployment status
kubectl describe deployment k8s-demo-backend -n k8s-demo
kubectl describe deployment k8s-demo-frontend -n k8s-demo

# View pod logs
kubectl logs -l app=k8s-demo-backend -n k8s-demo
kubectl logs -l app=k8s-demo-frontend -n k8s-demo
```

### Common Issues

**Image Pull Errors**:
```bash
# Check if images are accessible
docker pull khoanam225/k8s-demo-backend:latest

# Update imagePullPolicy if needed
imagePullPolicy: Always  # or IfNotPresent
```

**Resource Constraints**:
```bash
# Check node resources
kubectl top nodes

# Adjust resource requests/limits
kubectl edit deployment k8s-demo-backend -n k8s-demo
```

**Service Discovery Issues**:
```bash
# Test service connectivity
kubectl exec -it <pod-name> -n k8s-demo -- curl k8s-demo-backend:8080

# Check service endpoints
kubectl get endpoints -n k8s-demo
```

## 🚀 Advanced Deployments

### Blue-Green Deployment

```bash
# Deploy new version
kubectl apply -f k8s_templates/deployments/back-end-deployment-v2.yaml

# Switch traffic
kubectl patch service k8s-demo-backend -n k8s-demo -p '{"spec":{"selector":{"version":"v2"}}}'
```

### Rolling Updates

```bash
# Update image version
kubectl set image deployment/k8s-demo-backend k8s-demo-backend=khoanam225/k8s-demo-backend:v2 -n k8s-demo

# Monitor rollout
kubectl rollout status deployment/k8s-demo-backend -n k8s-demo

# Rollback if needed
kubectl rollout undo deployment/k8s-demo-backend -n k8s-demo
```

## 📚 Best Practices

1. **Resource Management**: Always set resource requests and limits
2. **Health Checks**: Implement liveness and readiness probes
3. **Security**: Use non-root containers and security contexts
4. **Monitoring**: Add labels for monitoring and observability
5. **Documentation**: Keep manifests well-documented with comments
