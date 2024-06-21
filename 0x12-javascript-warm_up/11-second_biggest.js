#!/usr/bin/node

const myArg = process.argv.slice(2);
let num = myArg.map(Number);

function findsec(num){
let max = num[0];
for (let i = 0; i < myArg.length; i++){

if(num[i] > max){
max = num[i];
}

}
return max;
}

let copy = num.slice();
let max = findsec(num);
for (let x = copy.length - 1; x > 0; x--){
if (copy[x] == max){
copy.splice(x, 1);
}
}


if (num.length == 0){
let x = 0
console.log(x);
}
else{
let secondMax = findsec(copy.filter(num => num !== max));
console.log(secondMax);
console.log("Second largest number:", secondMax !== undefined ? secondMax : "No second largest number found");
}
