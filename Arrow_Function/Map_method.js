const num = [1,2,3,4,5];
const doubled = num.map(num=>num*2);
console.log(doubled);



const number = [1,2,3,4,5];
const sqr = number.map(num=>num*num);
console.log(sqr);



const fruits = ['apple','banana','orange'];
const upperfruits =fruits.map(fruit=>fruit.toUpperCase());
console.log(upperfruits);



const languages=['JavaScript','Python','Java']
const Addprefix=languages.map(lang=>`I am learning ${languages}`)
console.log(Addprefix);



const users = [
    {name:'Supriya',age:23},
    {name:'Priya',age:25},
    {name:'Priyanka',age:27}
]
const names =users.map(user=>user.name);
console.log(names);


const numb = [1,2,3,4,5,6,7];
const evenOdd = numb.map(num=>
    num%2===0 ?`${num}is even`: `${num}is odd`);
    console.log(evenOdd);
    
