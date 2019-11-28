// Script file for view_profile.html 
// GET request made to /user/<str:username>.json
// Response is in JSON form.


let req = new XMLHttpRequest()
req.open('GET', url)
req.send()
req.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        let res = JSON.parse(this.responseText)
            $('#user-details').append("<p><strong>Username: </strong>"+ res.user_name +"</p>")
            $('#user-details').append("<p><strong>Full name: </strong>"+ res.full_name +"</p>")
    } else if (this.readyState == 4 && this.status == 404){
        // handle 404 error 
        console.log("Error")
    }
}