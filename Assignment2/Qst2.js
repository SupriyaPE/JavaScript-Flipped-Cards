// How does hoisting work for variables and functions ?
// JavaScript moves declarations (NOT initializations) to the top of their scope before code execution.
// So you can use variables and functions before they are declared — but the behavior differs for var, let, const, and functions

// 1. Hoisting for Functions

//  Function Declarations are fully hoisted,You can call a function before it is defined.

hello(); // Works

function hello() {
  console.log("Hello!");
}


// 2. Hoisting for Variables

// var Hoisting, var declarations are hoisted, but initialized with undefined.

console.log(a); // undefined 
var a = 10;


//  let & const Hoisting

// let and const are also hoisted, but They are NOT initialized, stay in the Temporal Dead Zone (TDZ)Accessing them before declaration gives an error.


console.log(b); //  ReferenceError
let b = 20;

console.log(c); //  ReferenceError
const c = 30;