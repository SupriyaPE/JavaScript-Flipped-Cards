//  What is Recursion in JavaScript?
(`Recursion is when a function calls itself until it reaches a base case. 
  It is used to solve problems by breaking them into smaller repetitive tasks.`)


function countdown(n) {
  if (n === 0) {
    console.log("Done!");
    return; // Base case
  }

  console.log(n); 
  countdown(n - 1); // Recursive call
}

countdown(5);



//Factorial

function factorial(n) {
  if (n === 1) return 1; // Base case

  return n * factorial(n - 1); // Recursive step
}

console.log(factorial(5)); // 120