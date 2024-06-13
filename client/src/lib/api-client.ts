


export const fetchAsync = async () => {
    const response = await fetch('/api/v1/hello')
    if (!response.ok) {
        throw new Error('Network response was not ok')
    }
    return response.json()
}