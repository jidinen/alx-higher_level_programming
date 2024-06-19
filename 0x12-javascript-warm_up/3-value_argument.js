#!/sr/bin/node

const myArg = process.argv.slice(2);
const firstAg = myArg[0];
if (myArg.length == 0){
console.log("No argument");
}

console.log(firstAg);
