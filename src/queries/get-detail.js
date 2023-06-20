const GetUpdateDetail = `
query ($slug: String) {
   3voor12update (slug: $slug) {
     _id
     title
     subtitle
     id
     tags
     slug
     content {
       __typename
       ... on Text {
         body        
         text
       }
       ... on Assets {
         items {
           url
         }
       }
     }
   }
}`

export default GetUpdateDetail