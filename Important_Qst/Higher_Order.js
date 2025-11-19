// What is Higher Order Function?
(`A Higher Order Function in javaScript is a function. that takes another function as an argument, return a function.`)

// Passing a function as an argument

function greet() {
  return "Hello Priya";
}

function display(cb) {
  console.log(cb()); 
}

display(greet);





// Returning a function

function multiply(x) {
  return function(y) {
    return x*y;
  };
}

const double = multiply(2);
console.log(double(5));  
