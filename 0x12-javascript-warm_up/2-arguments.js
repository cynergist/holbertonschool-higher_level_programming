#!/usr/bin/node
// If no argument passed to script print 'No argument'
if (process.argv.length <= 2) console.log('No argument');
// If only one argument is passed to the script, print 'Argument found'
else if (process.argv.length === 3) console.log('Argument found');
// Otherwise print 'Arguments found'
else console.log('Arguments found');
