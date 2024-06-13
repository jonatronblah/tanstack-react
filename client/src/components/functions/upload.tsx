import React, { useState } from "react";
import { useQuery, useQueryClient } from "@tanstack/react-query";

import { fetchAsync } from "@/lib/api-client";

export const SingleFileUploader = () => {
  const { status, data, error } = useQuery({
    queryKey: ["msg", "hello"],
    queryFn: fetchAsync,
  });

  return <>{data.message}</>;
};
