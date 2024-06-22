#!/usr/bin/node
const myArg = process.argv.slice(2);
let x = Number(myArg[0])
if(isNaN(x)){
console.log("Missing number of occurrences");
}
let str = "C is fun";
for (let i = 0; i < x; i++)
{
console.log(str);
}
