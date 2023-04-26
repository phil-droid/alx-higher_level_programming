#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) console.error(error);
  else {
    const charactersUrl = JSON.parse(body).characters;
    const characters = [];

    // Get list of characters for the movie
    for (const characterUrl of charactersUrl) {
      request(characterUrl, (error, response, body) => {
        if (error) console.error(error);
        else {
          characters.push(JSON.parse(body).name);

          // Print characters in the same order as /films/ response
          if (characters.length === charactersUrl.length) {
            request('https://swapi-api.hbtn.io/api/films/', (error, response, body) => {
              if (error) console.error(error);
              else {
                const films = JSON.parse(body).results;
                const film = films.find((f) => f.episode_id === parseInt(movieId));

                for (const character of film.characters) {
                  console.log(characters.find((c) => c === characters.find((c) => cUrlToId(cUrl) === cUrlToId(character))));
                }
              }
            });
          }
        }
      });
    }
  }
});

function cUrlToId(url) {
  const regex = /\/([0-9]*)\/$/;
  return url.match(regex)[1];
}
