// What is the use of the typeof operator?
(`The typeof operator in JavaScript is used to check the data type of a value or variable.
It returns the type as a string, like "string", "number", "boolean", "object", "undefined", "function", etc.`)

typeof "Hello"     // "string"
typeof 10          // "number"
typeof true        // "boolean"
typeof undefined   // "undefined"
typeof null        // object
typeof NaN         // number
typeof {}          // "object"
typeof []          // "object"   (arrays are objects)
typeof function(){} // "function"