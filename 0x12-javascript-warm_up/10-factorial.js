#!/usr/bin/node
// script that computes and prints a factorial

function factorial(n) {
  // Base case: factorial of 0 is 1
  if (n === 0) {
    return 1;
  }
  
  // Recursive case: compute factorial of n-1 and multiply by n
  return n * factorial(n - 1);
}

// Get the first command-line argument and convert it to an integer
let num = parseInt(process.argv[2]);

// If the argument is NaN, set it to 1
if (isNaN(num)) {
  num = 1;
}

// Compute and print the factorial
console.log(`The factorial of ${num} is ${factorial(num)}`);
