#!/usr/bin/node
function factorial (n) {
  if (isNaN(n) || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
const number = parseInt(process.argv[2]);
console.log(factorial(number));
