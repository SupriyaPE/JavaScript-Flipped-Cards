// What is Type Coercion in JavaScript?
(`Type coercion is the automatic conversion of one data type to another by JavaScript during operations.`)

(`JavaScript may convert:

string → number

number → string

boolean → number …depending on the operation.


It happens in two ways:

1. Implicit coercion → JavaScript converts types automatically.


2. Explicit coercion → You convert types manually using functions.
`)



Examples

// Implicit Coercion

"5" + 2     // "52"  (number converted to string)
"5" - 2     // 3     (string converted to number)
1 + true    // 2     (true → 1)



// Explicit Coercion

Number("10")   // 10
String(50)     // "50"
Boolean(1)     // true

