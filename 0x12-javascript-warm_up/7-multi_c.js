#!/usr/bin/node
// Use parseInt to take the int arg and use it to print that many times
const x = parseInt(process.argv[2]);
// Validation using isNaN to test if argument is not an integer
if (isNaN(x)) console.log('Missing number of occurrences');
// Increment i to print x number of times 'C is fun'
else {
  for (let i = 0; i < x; i++) console.log('C is fun');
}
