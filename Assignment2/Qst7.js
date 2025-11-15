// What is the Temporal Dead Zone (TDZ)?

// The Temporal Dead Zone is the period between hoisting and actual declaration where let and const variables exist but cannot be accessed, causing a ReferenceError.

console.log(a); // ReferenceError (TDZ)
let a = 10;



console.log(b); // ReferenceError
const b = 20;
