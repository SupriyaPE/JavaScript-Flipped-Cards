// What is NaN in JavaScript?

(`NaN stands for “Not-a-Number”. It represents a value that is not a valid number, usually the result of an invalid mathematical operation.`)

Examples

0 / 0          // NaN
"abc" * 5      // NaN
parseInt("Hi") // NaN

NaN === NaN  // false

// NaN is the only value in JavaScript that is not equal to itself.



// 1. Number.isNaN() 

Number.isNaN(value)

Example

Number.isNaN(NaN);        // true
Number.isNaN("abc");      // false  (because "abc" is not number type)



// 2. isNaN() (performs type conversion)

isNaN("abc");  // true  (because "abc" becomes NaN after coercion)
