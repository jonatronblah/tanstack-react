// type State = 'all' | 'open' | 'done'
// type Todo = {
//   id: number
//   state: State
// }
// type Todos = ReadonlyArray<Todo>

// const fetchTodos = async (state: State): Promise<Todos> => {
//   const response = await axios.get(`todos/${state}`)
//   return response.data
// }

// export const useTodosQuery = (state: State) =>
//   useQuery({
//     queryKey: ['todos', state],
//     queryFn: () => fetchTodos(state),
//   })
import { useQuery } from "@tanstack/react-query";

export const useFetchApi = (param) => {
  const { status, data, error } = useQuery({
    queryKey: ["generic", param],
    queryFn: async () => {
      const response = await fetch(`/api/v1/${param}`);
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    },
  });
  if (status === "pending") {
    return <span>Loading...</span>;
  }

  if (status === "error") {
    return <span>Error: {error.message}</span>;
  }
  return <div>{data.message}</div>;
};
