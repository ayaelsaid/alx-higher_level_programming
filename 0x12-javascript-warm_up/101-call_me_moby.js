#!/usr/bin/node
exports.function = function (x, theFunction) {
  for (let i = 1; i <= x; i++) {
    return theFunction;
  }
};
