// Script file for view_auction_listing.html 
// GET request made to /auction/<int:id>.json
// Response is in JSON form.

// let req = new XMLHttpRequest()
// req.open('GET', url_get_data)
// req.send()
// req.onreadystatechange = update_page

function update_page(){
    $.ajax({
        url: url_get_data,
        type: "GET",
        dataType: "json",
        success: function (data) {  
            if (data.active){
                if (data.highest_bidder){
                    $('#current_bid').replaceWith("<p id='current_bid'><strong>Current bid:</strong> £" + data.current_bid + "</p>")
                    $('#highest_bidder').replaceWith("<p id='highest_bidder'><strong>Highest Bidder: </strong> " + data.highest_bidder.username + "</p>")
                    $('#bid-input').prop('min', data.current_bid);
                } else {
                    $('#current_bid').replaceWith("<p id='current_bid'>No one has placed any bids. Be the first to bid on this auction</p>")
                }   
            } else{
                $('#notice').empty()
                $('#bidding').remove()
                let message = "<div class='alert alert-danger' role='alert'><h3>This listing has ended</h3>"
                $('#notice').append("<hr />")
                if (data.winner){
                    message += "<p>The winner of this auction is: "+ data.winner.username +"</p><p>Winning bid: £"+ data.current_bid +"</p>"
                }
                message += "</div>"
                $("#notice").append(message)
                
            }       
        }
    })
}

function bid_placed(){
    $.ajax({
        type : 'POST',
        url : url_post_bid,
        dataType: "json",
        data: {
            'current_bid' : $('#bid-input').val(),
            'username' : username,
            'csrfmiddlewaretoken' : $('input[name=csrfmiddlewaretoken]').val(),     
        }, 
        success: function (res) { 
            update_page()
        }
    })
}

$(function() {
    $('#bid-btn').click(function(e){ 
        e.preventDefault()
        bid_placed()
    })
})

update_page()
