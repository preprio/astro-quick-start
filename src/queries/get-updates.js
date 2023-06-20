const GetUpdates = `
query {
    3voor12update {
        items {
            _id
            _slug
            title,
            subtitle,
            text,
            tags,
            highlighted
        }
    }
}
`

export default GetUpdates