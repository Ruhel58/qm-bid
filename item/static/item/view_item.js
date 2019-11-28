// Script file for view_item.html 
// GET request made to /item/<int:id>.json
// Response is in JSON form.

let req = new XMLHttpRequest()
req.open('GET', url)
req.send()
req.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        let res = JSON.parse(this.responseText)
            $('#item-details').append("<p><strong>Title: </strong>"+ res.title +"</p>")
            $('#item-details').append("<p><strong>Description: </strong>"+ res.description +"</p>")
            $('#item-details').append("<p><strong>Item is being sold by: </strong>"+ res.seller.first_name +" "+res.seller.last_name +"</p>")
    } else if (this.readyState == 4 && this.status == 404){
        // handle 404 error 
        console.log("Error")
    }
}