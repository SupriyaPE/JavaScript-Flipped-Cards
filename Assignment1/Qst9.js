// What is the difference between undefined and null ?

(`undefined means a variable has been declared but not given a value, while null is an intentional assignment representing no value. undefined is set by JavaScript, and null is set by the programmer.`)

// Type is "undefined".


Example

let a;
console.log(a); // undefined



// Type is "object" (this is a well-known JavaScript bug).


Example

let b = null;
console.log(b); // null
