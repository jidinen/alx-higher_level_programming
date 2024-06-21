#!/usr/bin/node

const myArg = process.argv.slice(2);

let n = Number(myArg[0]);
function fac(n){
if (n == 0 || n == 1){
return 1;
}
else{

return fac(n - 1)  * n;

}

}
if(!isNaN(n))
{
console.log(fac(n));
}
else{
console.log(1);
}
