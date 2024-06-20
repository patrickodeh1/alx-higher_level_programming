#!/usr/bin/node
const process = require('process');

const args = process.argv.slice(2);

let hasArgs = false;

for (const arg of args) {
  console.log(arg);
  hasArgs = true;
}
if (!hasArgs) {
  console.log('No argument');
}
