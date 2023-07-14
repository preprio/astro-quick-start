const GetUpdates = `
query  listall {
      Drievoor12updates(limit: 30, sort: changed_on_DESC) {    
        items {
          _id
          _slug
          id
          title  
          subtitle
        }
      }
    }
`

export default GetUpdates