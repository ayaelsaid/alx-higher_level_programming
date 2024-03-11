#!/usr/bin/node
const argv = process.argv;
const args = parseInt(argv[2]);
if (isNaN(args)) {
  console.log('Not a number');
} else
  console.log('My number: ' + args);
