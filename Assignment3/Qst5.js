// What is the difference between call, apply, bind ?

(`call() and apply() execute the function immediately with a specified this value.
The difference is: call() takes arguments individually, apply() takes them as an array.
bind() does not execute immediately—it returns a new function with the this value fixed.`)


//  1. call()

function greet(city, country) {
  console.log(`Hello, I am ${this.name} from ${city}, ${country}`);
}

const person = { name: "Supriya" };

// Using call()
greet.call(person, "Mumbai", "India");




// 2. apply()

function greet(city, country) {
  console.log(`Hello, I am ${this.name} from ${city}, ${country}`);
}

const person1 = { name: "Supriya" };

// Using apply()
greet.apply(person1, ["Mumbai", "India"]);




// 3. bind() 

function greet(city, country) {
  console.log(`Hello, I am ${this.name} from ${city}, ${country}`);
}

const person2 = { name: "Supriya" };

// Using bind()
const newFunc = greet.bind(person,"Mumbai", "India");

// Now call the returned function
newFunc();