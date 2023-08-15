#!/usr/bin/node

exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};





12 divided by 2 is 6 with a remainder of 0
 6 divided by 2 is 3 with a remainder of 0
 3 divided by 2 is 1 with a remainder of 1
 1 divided by 2 is 0 with a remainder of 1
