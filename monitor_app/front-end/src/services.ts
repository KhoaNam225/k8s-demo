import axios from 'axios'
import { Node, Pod } from '@/models'

const API_BASE_URL = 'http://localhost:8080/api/v1'

export const KubernetesMonitoringService = {
  // Get all nodes
  getNodes: async (): Promise<Node[]> => {
    try {
      const response = await axios.get<Node[]>(`${API_BASE_URL}/nodes`)
      return response.data
    } catch (error) {
      console.error('Error fetching nodes:', error)
      throw error
    }
  },

  // Get all nodes
  getPodsByNamespace: async (namespace: string): Promise<Pod[]> => {
    try {
      const response = await axios.get<Pod[]>(`${API_BASE_URL}/pods?namespace=${namespace}`)
      return response.data
    } catch (error) {
      console.error('Error fetching nodes:', error)
      throw error
    }
  },

  // Get all namespaces
  getNamespaces: async (): Promise<string[]> => {
    try {
      const response = await axios.get<string[]>(`${API_BASE_URL}/namespaces`)
      return response.data
    } catch (error) {
      console.error('Error fetching namespaces:', error)
      throw error
    }
  },
}
