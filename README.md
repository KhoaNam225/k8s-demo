# Kubernetes Demo Project

This repository contains a comprehensive demonstration of Kubernetes concepts through multiple applications and resources. The project is structured to provide both practical examples and educational materials about container orchestration with Kubernetes.

## 📁 Project Structure

### 🎯 demo_app/
A full-stack application demonstrating a typical web application deployment on Kubernetes.

**Purpose**: Shows how to containerize and deploy a simple quote-fetching application with separate frontend and backend services.

**Components**:
- **Backend** (`demo_app/back-end/`): FastAPI application that fetches random quotes from an external API
- **Frontend** (`demo_app/front-end/`): React + TypeScript + Vite application that displays quotes

### 📊 monitor_app/
A Kubernetes cluster monitoring application that provides insights into cluster resources.

**Purpose**: Demonstrates how to interact with the Kubernetes API from within applications and provides monitoring capabilities for cluster nodes, namespaces, and pods.

**Components**:
- **Backend** (`monitor_app/back-end/`): FastAPI application with Kubernetes API integration
- **Frontend** (`monitor_app/front-end/`): React dashboard for visualizing cluster information

### ⚙️ k8s_templates/
Kubernetes YAML manifests for deploying the applications.

**Purpose**: Contains all necessary Kubernetes resource definitions including deployments, services, and ingress configurations.

**Resources**:
- Deployment manifests for frontend and backend services
- Service definitions for internal communication
- Ingress configuration for external access

### 🎥 preso_slides/
Educational presentation materials about Kubernetes concepts.

**Purpose**: Interactive slides created with Manim that introduce Kubernetes fundamentals, container orchestration concepts, and the problems Kubernetes solves.

## 🚀 Getting Started

Each sub-project contains its own README with detailed setup instructions:

- [`demo_app/README.md`](demo_app/README.md) - Quote application setup and deployment
- [`monitor_app/README.md`](monitor_app/README.md) - Kubernetes monitoring dashboard setup
- [`k8s_templates/README.md`](k8s_templates/README.md) - Kubernetes deployment instructions
- [`preso_slides/README.md`](preso_slides/README.md) - Presentation viewing instructions

### Prerequisites

- **Docker**: For building container images
- **Kubernetes cluster**: K3s, Minikube, or any Kubernetes distribution
- **kubectl**: Kubernetes command-line tool
- **Python 3.11+**: For backend services
- **Node.js 18+**: For frontend applications
- **uv**: Python package manager (recommended)

## 📚 Learning Objectives

This project demonstrates:

1. **Containerization**: How to package applications using Docker
2. **Kubernetes Deployment**: Basic deployment patterns and resource management
3. **Service Communication**: Inter-service communication within Kubernetes
4. **API Integration**: Both external API consumption and Kubernetes API interaction
5. **Monitoring**: Basic cluster monitoring and resource visualization
6. **Full-Stack Development**: Modern web application architecture

## 🛠️ Technology Stack

- **Backend**: FastAPI (Python)
- **Frontend**: React, TypeScript, Vite, Tailwind CSS
- **Container**: Docker
- **Orchestration**: Kubernetes
- **Package Management**: uv (Python), npm (Node.js)
- **Presentation**: Manim (Python animation engine)

## 📖 Additional Resources

- [Kubernetes Official Documentation](https://kubernetes.io/docs/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://react.dev/)
- [Docker Documentation](https://docs.docker.com/)

## 🤝 Contributing

Feel free to explore, modify, and extend these examples for your learning and development needs!