const GetArticles = `
query {
    Articles {
        items {
            _id
            _slug
            title
        }
    }
}
`

export default GetArticles