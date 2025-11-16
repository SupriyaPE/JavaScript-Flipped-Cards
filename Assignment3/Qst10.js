// What is generator Function?
(`“A generator function is a function that can pause and resume using yield. It returns a generator object,
 and each next() call continues the function from where it left off.`)


 function* greetGenerator() {
  console.log("Step 1");
  yield "Hello";

  console.log("Step 2");
  yield "How are you?";

  console.log("Step 3");
  return "Done";
}

const gen = greetGenerator();

console.log(gen.next());
console.log(gen.next());
console.log(gen.next());



// Step 1
// { value: 'Hello', done: false }

// Step 2
// { value: 'How are you?', done: false }

// Step 3
// { value: 'Done', done: true }