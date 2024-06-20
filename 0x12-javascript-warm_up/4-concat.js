#!/usr/bin/node
const process = require('process');
const args = process.argv.slice(2);

const sentence = 'is';
console.log(args[0] + ' ' + sentence + ' ' + args[1]);
