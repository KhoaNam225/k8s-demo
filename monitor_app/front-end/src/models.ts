export type Node = {
  nodeName: string
  nodeStatus: string
  nodeOs: string
  nodeCpu: number
  nodeMemory: number
  nodeIp: string
}

export type Pod = {
  podName: string
  podContainerImage: string
  podStatus: string
  podCreated: string
  podCpu: string
  podMemory: string
  podNodeName: string
}
