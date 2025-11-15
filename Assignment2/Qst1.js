// 1. Global Scope
// A variable is in global scope if it is declared outside of any function or block. It can be accessed anywhere in the program.

var x = 10; // global

function show() {
  console.log(x); // can access x
}

show();
console.log(x); // also accessible here


// 2. Function Scope
// Variables declared inside a function (using var, let, or const) are function-scoped. They can only be accessed inside that function.

function test() {
  var a = 100;
  console.log(a); // accessible here
}

test();
console.log(a); //  ERROR: a is not defined


// 3. Block Scope (ES6)
// Variables declared with let and const inside a block { } are block-scoped. They are accessible only inside that block.
{
  let b = 20;
  const c = 30;
  console.log(b, c); // accessible
}

console.log(b); //  ERROR
console.log(c); //  ERROR
