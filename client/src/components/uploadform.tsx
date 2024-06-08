// const form = useForm()

// <FormField
//   control={form.control}
//   name="username"
//   render={({ field }) => (
//     <FormItem>
//       <FormLabel>Username</FormLabel>
//       <FormControl>
//         <Input placeholder="shadcn" {...field} />
//       </FormControl>
//       <FormDescription>This is your public display name.</FormDescription>
//       <FormMessage />
//     </FormItem>
//   )}
// />

/*
Notes: 
  - purpose: allow user to manually vectorize indexed documents with control
    over labeling and document size/parsing

    (one file)
  - input form:
      - file browser
      - choice: segmentation
*/

"use client"

"use client"

import { zodResolver } from "@hookform/resolvers/zod"
import { useForm } from "react-hook-form"
import { z } from "zod"

const formSchema = z.object({
  username: z.string().min(2, {
    message: "Username must be at least 2 characters.",
  }),
})

export function ProfileForm() {
  // 1. Define your form.
  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      username: "",
    },
  })

  // 2. Define a submit handler.
  function onSubmit(values: z.infer<typeof formSchema>) {
    // Do something with the form values.
    // ✅ This will be type-safe and validated.
    console.log(values)
  }
}

