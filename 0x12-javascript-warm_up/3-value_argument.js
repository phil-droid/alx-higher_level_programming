#!/usr/bin/node
//Script to print the first argument passed to it

const arg = process.argv[2];

if (arg) {
  console.log(`The first argument is: ${arg}`);
} else {
  console.log("No argument");
}
