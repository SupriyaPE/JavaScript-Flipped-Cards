// What is Higher Order Function ?

// Higher-order functions are functions that either accept other functions as arguments or return functions.

//1. Takes a function as an argument

function greet(name) {
  return "Hello " + name;
}

function higherOrder(fn) {
  console.log(fn("Supriya"));
}

higherOrder(greet); // Hello Supriya



//2. Returns a function

function multiply(x) {
  return function(y) {
    return x * y;
  };
}

const double = multiply(2);
console.log(double(5)); // 10