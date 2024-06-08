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

"use client"

import { z } from "zod"

const formSchema = z.object({
  username: z.string().min(2).max(50),
})

