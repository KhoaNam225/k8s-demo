import axios from 'axios'
import { Quote } from '@/models/quote'

const QUOTABLE_API_URL = 'http://localhost:8080/api/v1/quotes'

export const QuoteService = {
  // Get a random quote
  getRandomQuote: async (): Promise<Quote> => {
    try {
      const response = await axios.get<Quote>(`${QUOTABLE_API_URL}/random`)
      return response.data.quote
    } catch (error) {
      console.error('Error fetching random quote:', error)
      throw error
    }
  },
}
