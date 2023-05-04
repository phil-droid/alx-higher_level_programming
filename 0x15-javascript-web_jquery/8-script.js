$(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    type: 'GET',
    dataType: 'json',
    success: function (data) {
      const $listMovies = $('UL#list_movies');
      data.results.forEach(function (movie) {
        $listMovies.append(`<li>${movie.title}</li>`);
      });
    }
  });
});
