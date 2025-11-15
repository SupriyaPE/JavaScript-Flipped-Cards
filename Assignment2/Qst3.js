// What happens if you use a variable before declaring it ?
// It depends on how the variable is declared  var, let, or const.

//  for Variables

// var Hoisting, var declarations are hoisted, but initialized with undefined.

console.log(a); // undefined 
var a = 10;


//  let & const Hoisting

// let and const are also hoisted, but They are NOT initialized, stay in the Temporal Dead Zone (TDZ)Accessing them before declaration gives an error.


console.log(b); //  ReferenceError
let b = 20;

console.log(c); //  ReferenceError
const c = 30;