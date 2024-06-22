#!/usr/bin/node

const myArg = process.argv.slice(2);
let num = Number(myArg[0]);
let num2 = Number(myArg[1]);

if (myArg.length != 2)
{
console.log(NaN);
}
else{
console.log(num + num2);
}
