#!/usr/bin/node
const process = require('process');
const args = process.argv.slice(2);

const printNumber = 'My number:';

if (args.length > 0) {
  const num = parseInt(args[0]);
  if (isNaN(num)) {
    console.log('Not a number');
  } else {
    console.log(printNumber + ' ' + num);
  }
} else {
  console.log('Not a number');
}
