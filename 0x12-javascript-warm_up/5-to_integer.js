#!/usr/bin/node
// Validation using isNaN to test if argument is not an integer
if (isNaN(process.argv[2]) || process.argv[2] === undefined)
  console.log('Not a number');
// Print the argument
else (console.log('My number: ' + parseInt(process.argv[2])));
