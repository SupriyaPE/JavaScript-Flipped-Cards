// explain this keyword?
(`In JavaScript, this represents the object that is currently calling the function. 
    Its value depends on how the function is invoked. In an object method, this refers to that object. 
    In regular functions, this is undefined. Arrow functions don’t have their own this
    they inherit it from their surrounding scope. We can also manually set this using call, apply, and bind.`)

    const person = {
      name: "Priya",
      greet() {
        console.log(this.name);
      }
     };

     person.greet(); 



console.log(this);



const obj = {
  value: 10,
  show: () => {
    console.log(this.value);
  }
};

obj.show(); 





function greet() {
  console.log(this.name);
}

const user = { name: "Priya" };

greet.call(user); 