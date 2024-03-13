#!/usr/bin/node
exports.converter = function (base) {
  return function convertBase (n) {
    return n.toString(base);
  };
};
