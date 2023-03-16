#!/usr/bin/node
//imports an array and computes a new array

const { list } = require('./100-data.js');

const newList = list.map((value, index) => value * index);

console.log('Initial list:', list);
console.log('New list:', newList);
