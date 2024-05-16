import { createLazyFileRoute } from '@tanstack/react-router'

export const Route = createLazyFileRoute('/stuff')({
  component: Stuff,
})

function Stuff() {
  return <div className="p-2">Hello from STUFF!</div>
}
