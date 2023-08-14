#!/usr/bin/node

const [, , arg1, arg2] = process.argv;

const formattedOutput = `${arg1 || 'undefined'} is ${arg2 || 'undefined'}`;
console.log(formattedOutput);
