// What are immediately invoked function expressions?

// An IIFE is a function that is defined and executed instantly
// An IIFE is a function that’s executed immediately after it is defined. It is wrapped in parentheses to become an expression and invoked right away to create a private scope and avoid global variable pollution.


(function () {
  let x = 10;
  console.log(x); // works
})();
console.log(x); // Error (x is private)



// IIFE with Parameters

(function (name) {
  console.log("Hello " + name);
})("Supriya");



// Arrow Function IIFE (ES6)

(() => {
  console.log("Arrow IIFE");
})();