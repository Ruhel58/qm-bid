$(function() {
    $('#submit-btn').click(function(e){
        if (!$('#search-input').val()){
            return
        }
        e.preventDefault()
        $.ajax({
            type : 'POST',
            url : url,
            data: {
                'query' : $('#search-input').val(),
                'csrfmiddlewaretoken' : $('input[name=csrfmiddlewaretoken]').val()
            }, 
            dataType: "json",
            success: function (res) {
                $('#auction-list').empty()

                if (res.results.length == 0){
                    $('#auction-list').append("<h3>No results found</h3>")
                }

                for (i in res.results){
                    let auction_url = reverse_auction_url(res.results[i].id)
                    let profile_url = reverse_profile_url(res.results[i].seller.username)

                    $('#auction-list').append("<a href=\"" + auction_url + "\"><h3>" + res.results[i].item.title + "</h3></a>")
                    $('#auction-list').append("<p>Starting Bid: £"+res.results[i].item.starting_price +"</p>")
                    $('#auction-list').append("<p>Listed by: <a href=\""+ profile_url +"\">"+ res.results[i].seller.username +"</a></p>")
                    $('#auction-list').append("<p>Auction end date: "+ res.results[i].item_end_date +"</p><hr/>")
                }
            }
        })
    })
})


