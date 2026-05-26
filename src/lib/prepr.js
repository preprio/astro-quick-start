export async function Prepr(query, variables) {
    const response = await fetch(import.meta.env.PREPR_ENDPOINT || 'https://graphql.prepr.io/ac_e54beab08406dd41fcdead2bef10364f442559f67fe86ebb0ac7aa6e3a1a4605', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ query, variables }),
    })
    return response
}