$( document ).ready(function() {
  load_trips()
  function load_trips() {
    $.ajax({
      type: 'GET',
      url: 'trips-api/',
      success: function(data) {
        for (var i = 0 ; i < data.length; i++) {
          $('#results').append('<li id="trip-{data.id}">' + "<strong>" + data[i]['name'] +"</strong>" + " <br>  " + "<em> start date </em>" +  data[i]['start_date'] + "   " + "<em> end date </em> " + data[i]['finish_date'] + '</li>')
        }
      },
      error: function() {
        alert('error loading trips');
      }
    });
  }
});
