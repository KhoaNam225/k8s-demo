from pydantic import BaseModel, ConfigDict
from humps import camelize


def to_camel(string: str) -> str:
    """Convert snake_case string to camelCase."""
    return camelize(string)


class CamelModel(BaseModel):
    """Base model that converts all snake_case to camelCase for API responses."""

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)


class NodeInformation(CamelModel):
    node_name: str
    node_status: str
    node_os: str
    node_cpu: int
    node_memory: float
    node_ip: str
