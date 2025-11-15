// What is Hoisted ?
(`Hoisting is JavaScript’s default behavior of moving variable and function declarations to the top of their scope before the code executes.`)
(`Function declarations are fully hoisted → you can call them before they appear in the code.

var variables are hoisted but initialized as undefined.

let and const are hoisted but not initialized → they stay in the Temporal Dead Zone (TDZ) until the line where they are declared.`)

console.log(a); // undefined (var is hoisted)
var a = 10;

console.log(b); // Error (b is in TDZ)
let b = 20;

console.log(c); // Error (c is in TDZ)
const c = 30;

test(); //  Works (function declaration is hoisted)
function test() {
  console.log("Function hoisted");
}