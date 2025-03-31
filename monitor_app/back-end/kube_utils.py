from kubernetes import client, config
from models import NodeInformation, PodInformation

config.load_kube_config()
client_v1 = client.CoreV1Api()


def get_node_information(node) -> NodeInformation:
    """
    Get information about a specific node.
    """
    try:
        node_info = client_v1.read_node(name=node)
        result: NodeInformation = NodeInformation(
            node_name=node_info.metadata.name,
            node_status=list(
                filter(lambda x: x.status != "False", node_info.status.conditions)
            )[0].type,
            node_os=node_info.status.node_info.os_image,
            node_cpu=node_info.status.capacity["cpu"],
            node_memory=int(node_info.status.capacity["memory"].replace("Ki", ""))
            / 1024**2,  # Convert memory from Ki to Gi
            node_ip=node_info.status.addresses[0].address,
        )
        return result
    except Exception as e:
        print(f"Error retrieving node information: {e}")
        return {}


def get_pod_information(pod) -> PodInformation:
    """
    Get information about a specific pod.
    """
    try:
        pod_info = client_v1.read_namespaced_pod(
            name=pod.metadata.name, namespace=pod.metadata.namespace
        )
        result: PodInformation = PodInformation(
            pod_name=pod_info.metadata.name,
            pod_container_image=pod_info.spec.containers[0].image,
            pod_status=pod_info.status.phase,
            pod_created=pod_info.metadata.creation_timestamp.strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            pod_cpu=pod_info.spec.containers[0].resources.limits["cpu"]
            if pod_info.spec.containers[0].resources.limits
            and pod_info.spec.containers[0].resources.limits.get("cpu")
            else "Unknown",
            pod_memory=pod_info.spec.containers[0].resources.limits["memory"]
            if pod_info.spec.containers[0].resources.limits
            and pod_info.spec.containers[0].resources.limits.get("memory")
            else "Unknown",
            pod_node_name=pod_info.spec.node_name,
        )
        return result
    except Exception as e:
        print(f"Error retrieving pod information: {e}")
        return {}


def get_all_nodes():
    """
    Get all nodes in the Kubernetes cluster.
    """
    try:
        nodes = client_v1.list_node()
        result = []
        for node in nodes.items:
            node_info = get_node_information(node.metadata.name)
            result.append(node_info)
        return result
    except Exception as e:
        print(f"Error retrieving nodes: {e}")
        return []


def get_all_namespaces():
    """
    Get all namespaces in the Kubernetes cluster.
    """
    try:
        namespaces = client_v1.list_namespace()
        result = []
        for namespace in namespaces.items:
            result.append(namespace.metadata.name)
        return result
    except Exception as e:
        print(f"Error retrieving namespaces: {e}")
        return []


def get_pods_by_namespace(namespace: str):
    """
    Get all pods in a specific namespace.
    """
    try:
        pods = client_v1.list_namespaced_pod(
            namespace if len(namespace) > 0 else "default"
        )
        result = []
        for pod in pods.items:
            result.append(get_pod_information(pod))
        return result
    except Exception as e:
        print(f"Error retrieving pods: {e}")
        return []
