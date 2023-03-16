#!/usr/bin/node
// imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.

const { dict } = require('./101-data.js');

const newDict = Object.entries(dict).reduce((acc, [id, occurrences]) => {
  if (occurrences in acc) {
    acc[occurrences].push(id);
  } else {
    acc[occurrences] = [id];
  }
  return acc;
}, {});

console.log(newDict);
