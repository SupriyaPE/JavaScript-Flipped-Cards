// What is prototype?
(`In JavaScript, every object has a hidden property called prototype, 
which points to another object. This mechanism is used to provide inheritance. 
If a property or method is not found on the object itself, 
JavaScript looks for it in the prototype, forming a prototype chain. 
Functions also have a prototype property, and when we use the new keyword, 
the created object inherits from the function’s prototype.
Prototypes make JavaScript’s inheritance system flexible and efficient
because shared methods  don’t need to be duplicated in every object.`)



function Person(name, age) {
  this.name = name;
  this.age = age;
}

Person.prototype.sayHello = function () {
  console.log("Hello, my name is " + this.name);
};

const p1 = new Person("Priya", 22);
const p2 = new Person("Supriya", 30);

p1.sayHello();  
p2.sayHello();