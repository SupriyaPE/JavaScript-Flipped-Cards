// How do you pass parameters by reference vs value?

// 1. Passing Parameters By Value.

(`Primitive data types (Number, String, Boolean, null, undefined, Symbol, BigInt)
are passed by value.`)

 Example

let x = 10;
function changeValue(num) {
  num = 20;
}
changeValue(x);
console.log(x); // 10 (NOT changed)



// 2.Passing Parameters By Reference

(`Objects (Arrays, Objects, Functions) are passed by reference.
A reference to the original object is passed.
Changing the object inside the function WILL change the original.`)

let person = { name: "Supriya" };

function changeName(obj) {
  obj.name = "Priya";
}

changeName(person);

console.log(person.name); // "Priya" (CHANGED)