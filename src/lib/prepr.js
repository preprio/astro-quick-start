export async function Prepr(query, variables) {
    const response = await fetch(import.meta.env.PREPR_ENDPOINT || 'https://graphql.prepr.io/ac_8a73ce93e85c18ccec497b81cf8a6458a8cee50c50fbbda897bb9cee07e1eba0', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ query, variables }),
    })
    return response
}