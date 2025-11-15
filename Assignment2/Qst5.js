// How do closure work in javascript

//  What is a Closure? 
// A function remembers and can access variables from its outer scope, even after that outer function has finished executing.


function greet(message) {
  return function(name) {
    console.log(message + " " + name);
  };
}

const sayHello = greet("Hello");

sayHello("Supriya"); // Hello Supriya