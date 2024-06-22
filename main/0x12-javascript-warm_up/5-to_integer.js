#!/usr/bin/node

const myArg = process.argv.slice(2);
const num = myArg[0];
if(!isNaN(num)){
console.log("My number: " +  num);

}
else {
console.log("Not a number");
}
