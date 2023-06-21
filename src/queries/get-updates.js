const GetUpdates = `
query {
   Drievoor12updates(limit: 30, sort: changed_on_DESC) {    
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