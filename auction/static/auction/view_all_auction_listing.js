
function showData() {
  $.ajax({
    url : url,
    method: "GET",
    success : function (data) {
      for (var i = 0; i<data.auctions.length; i++) {
        $("auctionBody").append("<tr>"
                                + "<td>" + data.auctions[i].title + "</td>"
                                + "<td>" + data.auctions[i].item.description + "</td>"
                                + "<td>" + data.auctions[i].item.starting_price + "</td>"
                                + "<td>" + data.auctions[i].seller.full_name + "</td>"
                                + "<td>" + data.auctions[i].item_end_date + "</td>"
                                + "</tr>")
      }
    }
  })
}
