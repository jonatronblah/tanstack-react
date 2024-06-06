import { createLazyFileRoute } from '@tanstack/react-router'

export const Route = createLazyFileRoute('/form')({
  component: () => <div>Hello /form!</div>
})