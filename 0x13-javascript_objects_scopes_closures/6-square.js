#!/usr/bin/node

const Rectangle = require('/5-square');

class Square extends Rectangle {
  constructor(size) {
    super(size, size);
  }
  
  charPrint(c) {
    if (c === undefined) {
      c = "X";
    }
    let rectangleStr = "";
    for (let i = 0; i < this.height; i++) {
      rectangleStr += c.repeat(this.width) + "\n";
    }
    console.log(rectangleStr);
  }
};
