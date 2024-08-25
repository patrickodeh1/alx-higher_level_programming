#!/usr/bin/node
const Square = require('./5-square');

class Square extends Square {
  charPrint(c) {
    const char = c || 'X';  // Use 'X' if c is undefined
    for (let i = 0; i < this.width; i++) {
      console.log(char.repeat(this.width));
    }
  }
}

module.exports = Square;
