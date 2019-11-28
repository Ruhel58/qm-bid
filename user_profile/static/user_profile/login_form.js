$('#submit-btn').click(function(e){
    e.preventDefault();
    $.ajax({
        type : 'POST',
        url : url,
        data: {
            user_name: $('#login-username').val(),
            password : $('#login-password').val(),
            csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val(),
            dataType: 'json'
        }, success: function (res, status, jqXHR) {
            if (res.success){
                // action to perform if signup is successful 
                alert(res.message)
            } else {
                // action to perform if signup is not successful 
                alert(res.message)
            }
        }
    })
})