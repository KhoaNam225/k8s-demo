import { Button } from '@/components/ui/button'
import { QuoteService } from '@/services/quotes-service'
import { useState, use, Suspense } from 'react'
import { Quote as QuoteIcon, Loader2 } from 'lucide-react'
import { TypeAnimation } from 'react-type-animation'
import { Quote } from '@/models/quote'
import './App.css'

function QuoteDisplay({ quotePromise }: { quotePromise: Promise<Quote> }) {
  const quote = use(quotePromise)

  return (
    <div className="min-h-[160px]">
      <TypeAnimation key={quote.content} sequence={[quote.content]} wrapper="p" className="text-4xl" speed={75} />
      <p className="text-right text-xl mt-2 italic font-light">- {quote.author.name}</p>
    </div>
  )
}

function App() {
  const [quotePromise, setQuotePromise] = useState<Promise<Quote>>(QuoteService.getRandomQuote())

  const fetchRandomQuote = () => {
    setQuotePromise(QuoteService.getRandomQuote())
  }

  return (
    <>
      <div className="h-full flex flex-col items-center justify-center">
        <div className="w-1/2">
          <Suspense
            fallback={
              <div className="flex gap-5 h-[160px] items-center">
                <Loader2 className="h-6 w-6 animate-spin text-primary" />
                <p class="text-lg">Fetching a brilliant quote...</p>
              </div>
            }>
            <QuoteDisplay quotePromise={quotePromise} />
          </Suspense>
          <Button onClick={fetchRandomQuote} className="mt-4 ml-auto mr-auto block text-lg" size="xl">
            <QuoteIcon className="inline-block" /> Get New Quotes
          </Button>
        </div>
      </div>
    </>
  )
}

export default App
