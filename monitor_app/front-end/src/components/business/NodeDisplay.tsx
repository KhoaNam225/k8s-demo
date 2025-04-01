import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { Node, Pod } from '@/models'
import { KubernetesMonitoringService } from '@/services'
import { useSuspenseQuery } from '@tanstack/react-query'
import { Cpu, MemoryStick, Check, GlobeLock, HardDrive, Container, History, Ban } from 'lucide-react'
import { Suspense } from 'react'

export const PodDisplay = ({ pod }: { pod: Pod }) => {
  const cardBackground =
    pod.podStatus === 'Running' ? 'bg-green-100' : pod.podStatus === 'Pending' ? 'bg-yellow-100' : 'bg-red-100'
  return (
    <Card className={'my-3 ' + cardBackground}>
      <CardHeader>
        <CardTitle className="">{pod.podName}</CardTitle>
        <div className="flex flex-row gap-5">
          <div>
            <CardDescription className="my-2">
              <Check className="inline-block mr-2"></Check>Status: {pod.podStatus}
            </CardDescription>
            <CardDescription className="my-2">
              <Container className="inline-block mr-2"></Container>
              {pod.podContainerImage}
            </CardDescription>
            <CardDescription className="my-2">
              <History className="inline-block mr-2"></History>
              {pod.podCreated}
            </CardDescription>
          </div>
          <div>
            <CardDescription className="my-2">
              <Cpu className="inline-block mr-2"></Cpu> CPUs: {pod.podCpu}
            </CardDescription>
            <CardDescription className="my-2">
              <MemoryStick className="inline-block mr-2"></MemoryStick>Memory: {pod.podMemory}
            </CardDescription>
          </div>
        </div>
      </CardHeader>
    </Card>
  )
}

export const NodeDisplay = ({ node, namespace, index }: { node: Node; namespace: string; index: number }) => {
  const { data: pods } = useSuspenseQuery({
    queryKey: ['pods', node.nodeName, namespace],
    queryFn: async () => {
      const data = await KubernetesMonitoringService.getPodsByNamespace(namespace)
      return data.filter(pod => pod.podNodeName === node.nodeName) as Pod[]
    },
    refetchInterval: 1000,
    refetchOnMount: true,
    gcTime: index * 200,
  })

  return (
    <Card className="w-1/4 m-2 h-full">
      <CardHeader>
        <CardTitle className="text-xl py-2">{node.nodeName}</CardTitle>
        <div className="flex flex-row gap-20">
          <div>
            <CardDescription>
              <HardDrive className="inline-block mr-2"></HardDrive>OS: {node.nodeOs}
            </CardDescription>
            <CardDescription>
              <Check className="inline-block mr-2"></Check>Status: {node.nodeStatus}
            </CardDescription>
            <CardDescription>
              <GlobeLock className="inline-block mr-2"></GlobeLock>IP Address: {node.nodeIp}
            </CardDescription>
          </div>
          <div>
            <CardDescription>
              <Cpu className="inline-block mr-2"></Cpu> CPUs: {node.nodeCpu} CPU
            </CardDescription>
            <CardDescription>
              <MemoryStick className="inline-block mr-2"></MemoryStick>Memory: {Math.round(node.nodeMemory * 10) / 10}{' '}
              GB
            </CardDescription>
          </div>
        </div>
      </CardHeader>
      <CardContent className="h-full overflow-y-auto">
        <Suspense fallback={<p>Loading pods...</p>}>
          {pods.length > 0 ? (
            pods.map(pod => (
              <div key={pod.podName} className="border-b border-gray-200 py-2">
                <PodDisplay pod={pod} />
              </div>
            ))
          ) : (
            <div className="h-full flex flex-row items-center justify-center">
              <Ban className="inline-block mr-2"></Ban>
              <p>No pods found for this node</p>
            </div>
          )}
        </Suspense>
      </CardContent>
    </Card>
  )
}

export const NodesList = ({ namespace }: { namespace: string }) => {
  const { data } = useSuspenseQuery({
    queryKey: ['nodes'],
    queryFn: async () => {
      const data = await KubernetesMonitoringService.getNodes()
      return data as Node[]
    },
  })

  if (!data || data.length === 0) {
    return <p>No nodes found</p>
  }

  return data.map((node, idx) => <NodeDisplay key={node.nodeName} node={node} namespace={namespace} index={idx} />)
}
