#!/usr/bin/node
const argv = process.argv;
const args = parseInt(argv[2]);
if (isNaN(args)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < args; i++) {
    let row = '';
    for (let j = 0; j < args; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
