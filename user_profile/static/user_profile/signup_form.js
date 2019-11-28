$('#submit-btn').click(function(e){
    e.preventDefault();
    $.ajax({
        type : 'POST',
        url : url,
        data: {
            user_name: $('#signup-username').val(),
            full_name: $('#signup-fullname').val(),
            email: $('#signup-email').val(), 
            dob : $('#signup-dob').val(), 
            password : $('#signup-password').val(),
            csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val(),
            dataType: 'json',
        }, success: function (res, status, jqXHR) {
            if (res.success){
                // action to perform if signup is successful 
                alert("Successful signup")
            } else {
                // action to perform if signup is not successful 
                alert("Not successful")
            }

        }
    })
})
