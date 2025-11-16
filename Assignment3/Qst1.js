//  What is a Callback Function? 
(`A callback is a function passed as an argument to another function and executed after the main function completes. 
Callbacks help us control execution order and handle asynchronous operations like timers, API calls, and events.`)

Example

function greet(name, callback) {
  console.log("Hello " + name);
  callback();
}

function sayBye() {
  console.log("Goodbye!");
}

greet("Supriya", sayBye);





//Asynchronous Callback Example

console.log("Start");

setTimeout(() => {
  console.log("Callback executed after 2 seconds");
}, 2000);

console.log("End");