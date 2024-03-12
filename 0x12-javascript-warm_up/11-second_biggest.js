#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const doList = process.argv.slice(2).map(Number);
  const list = doList.sort((a, b) => b - a);
  console.log(list[1]);
}
