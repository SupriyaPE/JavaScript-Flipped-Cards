// What is the value of this inside an arrow function ?
(`Arrow functions do not have their own this.
They use the this value from their surrounding scope (lexical this).`)

const person = {
  name: "Supriya",
  showName: () => {
    console.log(this.name);
  }
};

person.showName(); // undefined