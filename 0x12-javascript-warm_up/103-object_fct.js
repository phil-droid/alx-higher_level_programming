#!/usr/bin/node
//Updated  script that adds a new function incr that increments the integer value

function incr(number) {
  return number + 1;
}

function incrementAndCall(number, theFunction) {
  number = incr(number);
  theFunction(number);
}

function printNumber(number) {
  console.log(number);
}
//An example
let myNumber = 22;
incrementAndCall(myNumber, printNumber); // logs 23
