#!/usr/bin/node

const { dict } = require('./101-data');

const resultDict = {};

for (const userId in dict) {
  const occurrences = dict[userId];

  if (!resultDict[occurrences]) {
    resultDict[occurrences] = [];
  }

  resultDict[occurrences].push(userId);
}

console.log(resultDict);
