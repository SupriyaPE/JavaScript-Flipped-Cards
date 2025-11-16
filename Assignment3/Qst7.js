// Default parameters in ES6 ?

(`Default parameters in ES6 let you assign default values to function arguments so the function has a fallback when arguments are missing or undefined.`)

function greet(name = "Guest") {
  console.log("Hello " + name);
}
greet();          // Output: Hello Guest
greet("Supriya"); // Output: Hello Supriya




function multiply(a = 1, b = 1) {
  return a * b;
}
console.log(multiply());      // 1
console.log(multiply(5));     // 5
console.log(multiply(5, 10)); // 50




function sum(a = 10, b = a) {
  return a + b;
}
console.log(sum()); // 20