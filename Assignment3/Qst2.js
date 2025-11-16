// What are arrow function how they differ from normal function ?
(`Arrow functions give a shorter syntax and inherit this from the parent scope.
Normal functions have their own this. Because of this, arrow functions are good for callbacks but not for object methods.`)

// Normal Function Example

const person = {
  name: "Supriya",
  showName: function () {
    console.log(this.name);
  }
};

person.showName(); //Supriya

// Arrow Function Example

const person2 = {
  name: "Supriya",
  showName: () => {
    console.log(this.name);
  }
};

person2.showName(); // undefined