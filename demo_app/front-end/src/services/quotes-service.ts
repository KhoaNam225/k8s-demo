import axios from 'axios'
import { Quote } from '@/models/quote'

const QUOTABLE_API_URL = `${import.meta.env.VITE_QUOTABLE_API_URL}`

export const QuoteService = {
  // Get a random quote
  getRandomQuote: async (): Promise<Quote> => {
    try {
      const response = await axios.get<{ quote: Quote }>(`${QUOTABLE_API_URL}/random`)
      return response.data.quote
    } catch (error) {
      console.error('Error fetching random quote:', error)
      throw error
    }
  },
}
