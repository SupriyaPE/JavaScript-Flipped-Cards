const number=[1,2,3,4,5,6]
const evenNum=number.filter(num=>num%2===0);
console.log(evenNum);


const numb=[1,2,3,4,5,6]
const oddNum=number.filter(num=>num%2===1);
console.log(oddNum);


const numbers=[1,2,3,4,5,6,7,8,9]
const grtnum=numbers.filter(num=>num>7)
console.log(grtnum);


const fruits = ['apple','banana','orange'];
const lengthfruit =fruits.filter(fruit=>fruit.length>5);
console.log(lengthfruit);



const users = [
    {name:'Supriya',age:23},
    {name:'Priya',age:25},
    {name:'Priyanka',age:27}
]
const age =users.filter(user=>user.age>=25);
console.log(age);



const numbr=[1,2,3,4,5,6];
const evenNo = number
.filter(num => num % 2 === 0)
.map(num=>`${num} is even`);
console.log(evenNo);