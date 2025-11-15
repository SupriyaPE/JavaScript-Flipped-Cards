// What is the difference between == and === ?

(`== is loose equality — it checks only the value and performs type coercion if the types are different.
=== is strict equality — it checks both value and type, and does not perform any type conversion.
So, === is safer and preferred in JavaScript.`)

// 1. == (Loose Equality)
5 == "5"   // true  → string "5" is converted to number 5


// 2. === (Strict Equality)
5 === "5"  // false → number vs string