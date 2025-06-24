# Demo App - Quote Fetcher

A full-stack application demonstrating a typical web application deployment on Kubernetes. This app fetches random quotes from an external API and displays them in a modern React interface.

## 🏗️ Architecture

- **Backend**: FastAPI application that serves as a proxy to external quote APIs
- **Frontend**: React + TypeScript + Vite application with Tailwind CSS styling
- **API**: RESTful API for quote retrieval with CORS support

## 🚀 Local Development

### Backend Setup

```bash
cd back-end/

# Install dependencies
uv sync

# Run the development server
uv run fastapi dev main.py
```

The backend will be available at `http://localhost:8000`

**API Endpoints**:

- `GET /api/v1/quotes/random` - Fetch a random quote

### Frontend Setup

```bash
cd front-end/

# Install dependencies
npm install

# Start the development server
npm run dev
```

The frontend will be available at `http://localhost:3000`

**Development Scripts**:

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run lint` - Run ESLint
- `npm run preview` - Preview production build

## 🐳 Docker Builds

### Backend

```bash
cd back-end/
docker build -t k8s-demo-backend .
```

### Frontend

```bash
cd front-end/
docker build -t k8s-demo-frontend .
```

## ☸️ Kubernetes Deployment

Deploy the application to Kubernetes using the manifests in the `k8s_templates` directory:

```bash
# Create the namespace for this app
kubectl create namespace k8s-demo

# From the root of the project
kubectl apply -f k8s_templates/

# Check deployment status
kubectl get pods -n k8s-demo
kubectl get services -n k8s-demo

# Get ingress information
kubectl get ingress -n k8s-demo
```

**Kubernetes Resources Created**:

- Namespace: `k8s-demo`
- Backend Deployment & Service
- Frontend Deployment & Service
- Ingress for external access

## 🔧 Configuration

### Backend Configuration

- **Port**: 8000 (development), 8080 (container)
- **CORS**: Configured to allow all origins for demo purposes
- **External API**: Uses `https://api.quotable.kurokeita.dev/api/quotes/random`

### Frontend Configuration

- **Port**: 3000 (development), 80 (container)
- **Backend URL**: Configurable via environment variables
- **Build Tool**: Vite with TypeScript support

## 🛠️ Technology Stack

**Backend**:

- FastAPI (Python web framework)
- httpx (Async HTTP client)
- uvicorn (ASGI server)

**Frontend**:

- React 19
- TypeScript
- Vite (Build tool)
- Tailwind CSS (Styling)
- Lucide React (Icons)
- Axios (HTTP client)

## 📝 Development Notes

- The backend acts as a proxy to avoid CORS issues when calling external APIs from the browser
- Both services are configured with health checks for Kubernetes readiness/liveness probes
- Docker images use multi-stage builds for optimized production images
- Frontend uses modern React patterns with hooks and functional components

## 🔍 Troubleshooting

**Backend Issues**:

- Ensure Python 3.11+ is installed
- Check if port 8000 is available
- Verify external API connectivity

**Frontend Issues**:

- Ensure Node.js 18+ is installed
- Clear npm cache: `npm cache clean --force`
- Check if port 3000 is available

**Kubernetes Issues**:

- Verify cluster connectivity: `kubectl cluster-info`
- Check pod logs: `kubectl logs -n k8s-demo <pod-name>`
- Verify images are available in the registry
