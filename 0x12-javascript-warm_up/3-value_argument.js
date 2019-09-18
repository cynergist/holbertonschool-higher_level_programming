#!/usr/bin/node
// If no argument passed to script print 'No argument'
if (process.argv[2] === undefined) console.log('No argument');
// If only one argument is passed to the script, print the first argument
else (console.log(process.argv[2]));
