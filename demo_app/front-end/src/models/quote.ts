// Quote interface to define the shape of quote data
export type Quote = {
  _id: string
  content: string
  author: { name: string }
  tags: string[]
  authorSlug: string
  length: number
  dateAdded: string
  dateModified: string
}
