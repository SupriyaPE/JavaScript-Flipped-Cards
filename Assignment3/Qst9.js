//What is the difference between function declaration and function expression ?
(`Function declarations are fully hoisted, so you can use them before they are defined. 
Function expressions are assigned to variables and are not hoisted, so you must define them before calling.`)

//  1. Function Declaration
Example

function greet() {
  console.log("Hello");
}


// Hoisted
greet(); // Works

function greet() {
  console.log("Hello");
}



// 2. Function Expression
Example

const greet = function() {
  console.log("Hello");
};


// Not Hoisted
greet(); // greet is not defined yet

const greet = function() {
  console.log("Hello");
};