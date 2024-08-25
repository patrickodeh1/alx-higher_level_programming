#!/usr/bin/node

const fs = require('fs');

const [,, file1, file2, destFile] = process.argv;

fs.readFile(file1, 'utf8', (err, data1) => {
  if (err) throw err;
  fs.readFile(file2, 'utf8', (err, data2) => {
    if (err) throw err;
    fs.writeFile(destFile, data1 + data2, err => {
      if (err) throw err;
    });
  });
});
