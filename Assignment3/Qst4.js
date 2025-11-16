// What is Function Currying?
(`Function currying means converting a function with multiple arguments into a chain of functions, each taking one argument.
It helps in reusability and avoids repeating the same parameters`)

Example

//Normal function

function add(a, b, c) {
  return a + b + c;
}
add(1, 2, 3); // 6




// Curried function

function add(a) {
  return function(b) {
    return function(c) {
      return a + b + c;
    };
  };
}

add(1)(2)(3); // 6