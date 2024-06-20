#!/usr/bin/node
const process = require('process');

const args = process.argv.slice(2);
if (args.length === 0) {
  console.log('No argument');
} else {
  args.foreach((arg) => {
    console.log(`${args}`);
  });
}
