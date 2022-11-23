$(() => {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data, status) {
    if (status === 'success') {
      const films = data.results;
      for (const i in films) {
        $('#list_movies').append('<li>' + films[i].title + '</li>');
      }
    }
  });
});
