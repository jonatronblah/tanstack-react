import { createLazyFileRoute } from "@tanstack/react-router";

import { useFetchApi } from "@/components/features/generic/queries";

export const Route = createLazyFileRoute("/test")({
  component: About,
});

function About() {
  const data = useFetchApi("hello");
  const data2 = useFetchApi("goodbye");

  return (
    <div>
      {data}
      {data2}
    </div>
  );
}
