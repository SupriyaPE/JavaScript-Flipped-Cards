const number=[1,2,3,4,5,6]
const sum = number.reduce((acc,cur)=>acc+cur,0);
console.log(sum);



const numb=[1,2,3,4,5,6]
const product= number.reduce((acc,cur)=>acc*cur,1);
console.log(product);



const num=[10,22,60,40,50,56]
const max= num.reduce((acc,cur)=>(cur>
acc ? cur : acc),num[0]);
console.log(max);
 


const arrays = [[1,2],[3,4],[5]];

const flat = arrays.reduce((acc,cur)=>acc.concat(cur),[]);
console.log(flat);
 


const char = ['a','b','c','d','c','a','f','f','f'];
const count = char.reduce((acc,cur) => {
    acc[cur]=(acc[cur] || 0) + 1;
    return acc;
  },{});
console.log(count);
