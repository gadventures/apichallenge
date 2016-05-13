$( document ).ready(function() {

  var today = new Date();
  var dd = today.getDate();

  load_trips()
  function load_trips() {
    $.ajax({
      type: 'GET',
      url: 'trips-api/',
      success: function(data) {
        for (var i = 0 ; i < data.length; i++) {
          $('#results').append('<li id="trip-{data.id}" class="col-md-8 col-md-offset-2">' + "<strong>" + data[i]['name'] +"</strong>" + " <br>  " + "<em> start date </em>" +  data[i]['start_date'] + "   " + "<em> end date </em> " + data[i]['finish_date'] + '</li>')
        }
      },
      error: function() {
        alert('error loading trips');
      }
    });
  }
});
