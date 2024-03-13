#!/usr/bin/node
exports.esrever = function (list) {
  let esreverList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    esreverList.push(list[i]);;
  }
  return esreverList;
};
