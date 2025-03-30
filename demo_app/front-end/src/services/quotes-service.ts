import axios from 'axios'
import { Quote } from '@/models/quote'

const QUOTABLE_API_URL = 'https://api.quotable.kurokeita.dev/api/quotes'

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
