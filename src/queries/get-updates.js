const GetUpdates = `
query {
    Drievoor12updates {
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