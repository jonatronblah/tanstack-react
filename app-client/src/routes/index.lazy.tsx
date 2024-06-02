import { createLazyFileRoute } from "@tanstack/react-router";

import { ContentLayout } from "@/components/layouts/layout";

export const Route = createLazyFileRoute("/")({
  component: Index,
});

function Index() {
  return (
    <ContentLayout title="Home">
      <div className="p-2">
        <h3>Welcome Home!</h3>
      </div>
    </ContentLayout>
  );
}
