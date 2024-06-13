


export const fetchAsync = async ({ queryKey }) => {
    const [_, msg] = queryKey
    console.log(msg)
    const response = await fetch(`/api/v1/${msg}`)
    if (!response.ok) {
        throw new Error('Network response was not ok')
    }
    return response.json()
}