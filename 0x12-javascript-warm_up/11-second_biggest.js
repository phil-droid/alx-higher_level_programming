#!/usr/bin/node
// Searches the second biggest integer in the list of arguments

const args = process.argv;

function secondBiggestInteger(...args) {
  // Sort the arguments in descending order
  args.sort((a, b) => b - a);

  // If there are no arguments, return 0
  if (args.length === 0) {
    return 0;
  }

  // If there is only one argument, return 0
  if (args.length === 1) {
    return 0;
  }

  // Otherwise, return the second argument
  return args[1];
}
