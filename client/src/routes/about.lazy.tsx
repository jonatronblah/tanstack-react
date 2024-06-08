import { createLazyFileRoute } from '@tanstack/react-router'

import { SingleFileUploader } from '@components/functions/upload.tsx'

export const Route = createLazyFileRoute('/about')({
  component: About,
})

function About() {
  return <div>
    <SingleFileUploader />
  </div>
}
