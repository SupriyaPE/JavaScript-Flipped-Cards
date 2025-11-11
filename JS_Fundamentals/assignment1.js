console.log(0 == false);  
console.log(0 === false); 


if ("Hello") console.log("Truthy");  
if (0) console.log("Falsy");        


typeof 123        // 'number'  
typeof "Hello"    // 'string'  
typeof true       // 'boolean'  
typeof undefined  // 'undefined'
typeof null       // 'object'  
typeof [1,2,3]    // 'object'  
typeof function(){} // 'function'


console.log(0 / 0);      
console.log(Number("abc"));  

isNaN("abc");        
Number.isNaN("abc"); 
Number.isNaN(NaN);  


let a;
console.log(a); // undefined

let user = null; 
console.log(user);

//Coercion

//implicit
console.log('5' + 2);      
console.log('5' - 2);  
  

//explicit
console.log(Number("10"));
console.log(String(5));

