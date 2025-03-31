import { NodesList } from '@/components/business/NodeDisplay'
import { Button } from '@/components/ui/button'
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuLabel,
  DropdownMenuRadioGroup,
  DropdownMenuRadioItem,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from '@/components/ui/dropdown-menu'
import { useSuspenseQuery } from '@tanstack/react-query'
import { Suspense, useState } from 'react'
import './App.css'
import { KubernetesMonitoringService } from './services'

function App() {
  const { data: namespaces } = useSuspenseQuery({
    queryKey: ['namespaces'],
    queryFn: async () => {
      const data = await KubernetesMonitoringService.getNamespaces()
      return data as string[]
    },
  })

  const [namespace, setNamespace] = useState<string>('')
  const [nodeRefreshKey, setNodeRefreshKey] = useState<number>(0)

  if (namespaces.length === 0 || namespaces === undefined) {
    return (
      <div className="h-full flex flex-col items-center justify-center">
        <p className="text-lg">No namespaces found</p>
      </div>
    )
  }

  return (
    <div className="h-full flex flex-col items-center justify-center gap-10 py-10">
      <Suspense fallback={<div>Loading namespaces...</div>}>
        <DropdownMenu>
          <DropdownMenuTrigger asChild>
            <Button variant="outline">{namespace === '' ? 'No namespace selected' : namespace}</Button>
          </DropdownMenuTrigger>
          <DropdownMenuContent className="w-56">
            <DropdownMenuLabel>Select Namespace</DropdownMenuLabel>
            <DropdownMenuSeparator />
            <DropdownMenuRadioGroup value={namespace} onValueChange={setNamespace}>
              {namespaces.map(ns => (
                <DropdownMenuRadioItem key={ns} value={ns}>
                  {ns}
                </DropdownMenuRadioItem>
              ))}
            </DropdownMenuRadioGroup>
          </DropdownMenuContent>
        </DropdownMenu>
      </Suspense>
      <div className="w-[90%] max-h-[80%] flex flex-row gap-5 flex-wrap justify-center items-center">
        <Suspense fallback={<div>Loading nodes...</div>}>
          <NodesList key={nodeRefreshKey} namespace={namespace} />
        </Suspense>
      </div>
    </div>
  )
}

export default App
