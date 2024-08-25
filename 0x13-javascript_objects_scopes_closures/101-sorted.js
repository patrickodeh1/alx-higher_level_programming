#!/usr/bin/node

const { dict } = require('./101-data');

const occurrencesDict = {};

for (const [userId, occurrences] of Object.entries(dict)) {
  if (!occurrencesDict[occurrences]) {
    occurrencesDict[occurrences] = [];
  }
  occurrencesDict[occurrences].push(userId);
}

console.log(occurrencesDict);
