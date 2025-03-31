from kubernetes import client, config
from models import NodeInformation

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
