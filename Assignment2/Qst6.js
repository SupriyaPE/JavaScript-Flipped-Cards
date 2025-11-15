// What is the difference between var let const in terms of hoisting?


//var is hoisted and initialized to undefined, so you can access it before declaration.
// let and const are hoisted but not initialized, so they stay in the Temporal Dead Zone and throw a ReferenceError if accessed before declaration

// Hoisting for Variables

// 1. var Hoisting, var declarations are hoisted, but initialized with undefined.

console.log(a); // undefined 
var a = 10;


// 2. let & const Hoisting

// let and const are also hoisted, but They are NOT initialized, stay in the Temporal Dead Zone (TDZ)Accessing them before declaration gives an error.


console.log(b); //  ReferenceError
let b = 20;

console.log(c); //  ReferenceError
const c = 30;