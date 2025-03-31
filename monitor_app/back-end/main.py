from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from kube_utils import get_all_namespaces, get_all_nodes, get_pods_by_namespace

# Initialize FastAPI app
app = FastAPI()

# Allow CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)


@app.get("/api/v1/nodes")
def get_nodes():
    return get_all_nodes()


@app.get("/api/v1/namespaces")
def get_namespaces():
    """
    Get all namespaces in the Kubernetes cluster.
    """
    # Placeholder for actual implementation
    return get_all_namespaces()


@app.get("/api/v1/pods")
def get_pods(namespace: str):
    """
    Get all pods in a specific namespace.
    """
    # Placeholder for actual implementation
    return get_pods_by_namespace(namespace)
