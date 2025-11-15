// What is the difference between var let const ?
(`var is function-scoped and allows re-declaration and re-assignment.
let is block-scoped, cannot be re-declared, but can be reassigned.
const is block-scoped, cannot be re-declared or reassigned.
Also, let and const are in the temporal dead zone until they are declared, while var is initialized as undefined.`)

// VAR example
var x = 10;
var x = 20; // Re-declaration allowed
console.log(x); // 20


// LET example
let y = 30;
// let y = 40;  //  (re-declaration not allowed)
y = 40;        //  Re-assignment allowed
console.log("let y =", y); // 40


// CONST example
const z = 50;
// z = 60;     // (re-assignment not allowed) 
// const z = 70; // (re-declaration not allowed)
console.log("const z =", z); // 50