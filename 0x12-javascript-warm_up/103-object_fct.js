#!/usr/bin/node

const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

// Adding the incr method to myObject
myObject.incr = function () {
  this.value++;
};

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
