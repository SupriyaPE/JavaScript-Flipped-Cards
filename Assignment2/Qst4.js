// What is lexical scope?
// Lexical scope means a variable is accessible based on where it is written in the code.

function outer() {
  let x = 10;

  function inner() {
    console.log(x); // can access x
  }

  inner();
}

outer();


// inner() is lexically inside outer().


//Outer can’t access inner’s variables

function outer() {
  function inner() {
    let y = 20;
  }

  console.log(y); // Error: y is not defined
}