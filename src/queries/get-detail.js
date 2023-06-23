const GetDrievoor12UpdateDetail = `

query($id: String)  {
      Drievoor12updates(where: {id:$id}) {
        items {
          id
          title  
          subtitle
          text   
          _publish_on 
        }
      }
    }
`

export default GetDrievoor12UpdateDetail