// What are Pure Function?
// A pure function always returns the same result for the same inputs and produces no side effects.

// Same inputs → always same output

// Does not modify anything outside the function

function add(a, b) {
  return a + b;
}

console.log(add(2, 3)); // 5
console.log(add(2, 3)); // 5 


// Example of an Impure Function

let count = 0;

function increase() {
  count++; // modifies external variable, Side effect.
  return count;
}