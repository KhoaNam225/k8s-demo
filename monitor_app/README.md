# Monitor App - Kubernetes Dashboard

A Kubernetes cluster monitoring application that provides real-time insights into cluster resources. This application demonstrates how to interact with the Kubernetes API from within containerized applications.

## 🏗️ Architecture

- **Backend**: FastAPI application with Kubernetes API integration
- **Frontend**: React dashboard for visualizing cluster information
- **API Integration**: Direct interaction with Kubernetes API server

## 🚀 Local Development

### Prerequisites

- Kubernetes cluster access (kubectl configured)
- Kubeconfig file (default location: `~/.kube/k3s-config`)

### Backend Setup

```bash
cd back-end/

# Install dependencies
uv sync

# Configure kubectl access (update path in kube_utils.py if needed)
# Default expects ~/.kube/k3s-config

# Run the development server
uv run fastapi dev main.py
```

The backend will be available at `http://localhost:8000`

**API Endpoints**:
- `GET /api/v1/nodes` - List all cluster nodes
- `GET /api/v1/namespaces` - List all namespaces
- `GET /api/v1/pods/{namespace}` - List pods in a specific namespace

### Frontend Setup

```bash
cd front-end/

# Install dependencies
npm install

# Start the development server
npm run dev
```

The frontend will be available at `http://localhost:3000`

## 🔧 Configuration

### Kubernetes Configuration

The monitor app requires access to your Kubernetes cluster. Update the kubeconfig path in `back-end/kube_utils.py`:

```python
config.load_kube_config(
    config_file="~/.kube/your-config-file"  # Update this path
)
```

**Supported Configurations**:
- Local kubeconfig files
- In-cluster service account (when deployed to Kubernetes)
- Custom kubeconfig locations

### Environment Setup

Ensure your Kubernetes cluster is accessible:

```bash
# Test cluster connectivity
kubectl cluster-info

# Verify permissions
kubectl auth can-i get nodes
kubectl auth can-i get pods --all-namespaces
```

## 🐳 Docker Builds

### Backend
```bash
cd back-end/
docker build -t k8s-monitor-backend .
```

### Frontend
```bash
cd front-end/
docker build -t k8s-monitor-frontend .
```

## ☸️ Kubernetes Deployment

When deploying to Kubernetes, the application will use in-cluster service account authentication:

```bash
# Deploy with appropriate RBAC permissions
kubectl apply -f k8s_templates/monitor-app/

# Check deployment status
kubectl get pods -n monitoring
kubectl get services -n monitoring
```

**Required RBAC Permissions**:
- `get`, `list` permissions for nodes
- `get`, `list` permissions for namespaces
- `get`, `list` permissions for pods

## 🛠️ Technology Stack

**Backend**:
- FastAPI (Python web framework)
- kubernetes (Official Kubernetes Python client)
- Pydantic (Data validation and serialization)

**Frontend**:
- React 19
- TypeScript
- Vite (Build tool)
- Tailwind CSS (Styling)
- Lucide React (Icons)
- Axios (HTTP client)

## 📊 Features

### Node Monitoring
- Node status and health information
- Resource capacity (CPU, Memory)
- Operating system details
- IP addresses

### Namespace Management
- List all namespaces in the cluster
- Filter and search capabilities

### Pod Monitoring
- Pod status and phase information
- Resource usage and limits
- Container information
- Restart counts and events

## 🔍 Troubleshooting

**Authentication Issues**:
```bash
# Check kubeconfig
kubectl config view

# Test permissions
kubectl auth can-i get nodes

# Update kubeconfig path in kube_utils.py
```

**Connection Issues**:
```bash
# Verify cluster connectivity
kubectl cluster-info

# Check if API server is accessible
kubectl get nodes
```

**Permission Errors**:
- Ensure service account has appropriate RBAC permissions
- Check if kubeconfig has necessary cluster access
- Verify namespace permissions

**Backend Startup Issues**:
- Check Python version (requires 3.11+)
- Verify kubernetes client library installation
- Ensure kubeconfig file exists and is readable

## 🔐 Security Considerations

- Uses read-only permissions for cluster resources
- Implements proper error handling for API failures
- Supports both local development and in-cluster authentication
- CORS configured for demo purposes (restrict in production)

## 📝 Development Notes

- The application demonstrates both local kubectl access and in-cluster service account patterns
- Error handling includes graceful degradation when cluster access is unavailable
- Data models use Pydantic for type safety and validation
- Frontend provides real-time updates through API polling (can be extended with WebSocket support)
