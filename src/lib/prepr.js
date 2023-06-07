export async function Prepr(query, variables) {
    const response = await fetch(import.meta.env.PREPR_ENDPOINT, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ query, variables }),
    })
    return response
}