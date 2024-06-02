import { useState } from "react";

import { createLazyFileRoute } from "@tanstack/react-router";

import { Calendar } from "@/components/ui/calendar";

export const Route = createLazyFileRoute("/stuff")({
  component: Stuff,
});

function Stuff() {
  const [date, setDate] = useState<Date | undefined>(new Date());

  return (
    <Calendar
      mode="single"
      selected={date}
      onSelect={setDate}
      className="rounded-md border"
    />
  );
}
