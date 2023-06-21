const GetDrievoor12UpdateDetail = `
query ($slug: String) {
   Drievoor12update (slug: $slug) {
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

export default GetDrievoor12UpdateDetail