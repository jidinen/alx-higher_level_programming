#!/usr/bin/node

const myArg = process.argv.slice(2);
const num = isNaN(myArg[0]);
if (typeof num === 'number'){
console.log("My number is: " +  num);
}
else {
console.log("Not a number");
}
