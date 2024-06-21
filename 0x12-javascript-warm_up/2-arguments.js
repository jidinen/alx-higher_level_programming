#!/usr/bin/node
//variable stores the argument vector of the function
const myArg = process.argv.slice(2);
//conditional statement
if (myArg.length == 0){
 console.log('No argument');
} else if(myArg.length == 1){
  console.log('Argument found');

} else {
  console.log('Arguments found');
}
