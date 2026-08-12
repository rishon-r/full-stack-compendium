// This is a single line comment
/*
This is a multiline comment
*/

/* Javascript is a programming language used to build websites
There are chiefly three technologies used to create websites: HTML, CSS, Javascript
HTML creates the content of the website
CSS helps change the appearance of the website (i.e used for styling the website)
JavaScript makes the website interactive
*/


/* A Web Browser is an important tool for web development.
It allows us to view websites. 
Google Chrome is the most commonly used one.
You can view the HTML markup for any webpage by right clicking on any part of the website and clicking inspect.
By switching to the console tab after clicking inspect, you gain access to a JS console.
Here, if you type alert('Hello World'); 
it will return a pop-up with the words hello world
*/

/* JS also allows us to do math
It will evaluate mathematical expressions and return the result similar to what Python does
*/

/*
JS is CASE-SENSITIVE.
Statements are terminated with a semi-colon.
Semi-colons are automatically added whenever a newline character is encountered.
However, it is better practice to add them in order to avoid abnormal behaviour so. just add semi colons
*/

// NUMBERS AND MATH

7 + 2 + 5; // Addition
7 - 2; // Subtraction
7 / 2; // Division
7 * 2; // Multiplication

// JS can also handle decimal numbers
7.3 + 5;
// You can combine multiple operations in a single expression
7.3 * 5 +4;

// ORDER OF OPERATIONS:
/* Addition, Multiplication, Subraction and Division are all operations in JS
+, - , * and / are called operators.
Order of operations refers to the order in which operations are evaluated in an expression.
In JS, Multiplication and Division are done first (have same priority) and then Addition and Subtraction are done next (they have same priority)
In JS, this is also called operator precedence.
Note however that expressions are also evaluated from left to right if perator have the same precedence.
Brackets or Parentheses have the highest priority of all
Whenever there is an open bracket (, remember that it must be followed by a closed bracket, ).
If there are multiple nested sets of parentheses, JS evaluates thhe inner parentheses first
*/

// A common anomally noted is the result after adding (or any operation really) two decimal numbers. 
20.94 + 45.86;
// You will end up with a decimal number with a long list of trailing numbers after the decimal point.
// This is a common problem encountered across languages (often called floating point precision)
// This is due to the fact that computers only understand binary 
// Conversion of a decimal into the binary system sometimes produces abnormal behaviour
// To combat this we can simply round the number
Math.round(20.94 + 45.86);
// Above code rounds the number to the nearest integer
// However when calculating important floating point values such as prices in dollars and cents
// It is better to convert the amount to cents completely and convert back to dollars after addition in order to avoid any semblance of inaccuracy

// STRINGS

// A string in JS and most programming languages is a sequence of character used to represent text
// In JS, strings consist of a series of letters, numbers or symbols enclosed in quotes
// In JS, strings can be enclosed in single-quotes, double-quotes or backticks
// However, single quotes is the default that JS uses
// Strings created with backticks like `hello` are referred to as template strings
// E.g
'hello';
"YOooOOO777@";
// Strings can also be added together. This process is known as concatenation
'hello' + "world";
// Result of above operation is the string "helloworld"
// When you add a string to a number, JS automatically converts said number to a string and facilitates the concatenation operation.
// This feature is called Type Coercion
//E.g
'hello'+6;
// Result of above expression is the string 'hello6'

// We can find what type a value is using typeof
typeof 'hello';
typeof 6;
// Result of first expression above is 'string' and second is 'number'

// Remeber that string operations follow the same order of operations as numbers do. Parentheses are always computed first.
// This is especially useful in combination expressions of multiple strings and numbers.


// TEMPLATE STRINGS
// Template strings have some special uses
// The first such use is INTERPOLATION
// Interpolation means that you can insert a value directly into a string
// This is done with the help of the ${} where we can insert the value we want inside the curly braces
// E.g
`hello, I'm ${5+7} years old`;

// MULTI-LINE STRINGS
// We can use backticks to create strings that span multiple lines
// This feature is only available for template strings
// These multiline strings can be used heavily in web dev
`multi
line
string
`

// A general rule of thumb is to use single quotes for creating all kinds of strings unless a particuls use case demands
// using interpolation or multiline strings in which case we use backticks to create templatte strings

// console.log() - AN IMPORTANT CONCEPT
// Now , what does console.log() do?
// console.log() is a built-in function in JavaScript used to print output to the browser’s console
// It is used mainly for debugging and diagnostics.
// It doesn't affect the web page itself — it prints messages to the developer console
// Example below:
console.log('Hello World');

// You can log one or more values.
// It can log strings, numbers, objects, arrays, functions, or results of expressions.
// Syntax: console.log(value1, value2, ..., valueN);
// Above expression will print all values mentioned with a space in between them

// VARIABLES
// In JS, variables are containers that store values so that they can be reused later
// Think of a variable in JS as a named storage location

// Variables in JS can be created using the let keyword
let x=40;
let word="hello";
console.log(word, x);

// We can also store expressions in a variable
let addr= 67 + 45;
let subr= addr - 5; // we can also use a variable in an expression
// Note that in JS, you can use a variable wherever you use a value
console.log(subr*5);

// VARIABLE NAMING RULES
// 1. Keywords such as let cannot be used in the variable name
// 2. A variable name may include a number although it may not start with a number
// 3. Most special characters cannot be used in a variable name. The only permitted ones are: $ and _
// 4. The above mentioned special characters may also be used to start a variable name

// CHANGING VALUE OF A VARIABLE (RE-ASSIGNING A VARIABLE)
let name="Mike";
console.log(name);
name="Tyson";
// We changing the value of a variable, we don't use the let keyword as it is used to create a new variable
// We simply mention the name of the variable and reassign a value to it
// This is done above and the effect it has can be displayed below
console.log(name);

// We can also reassign an expression to a variable that uses the varaible in said expression
// Example:
let num =5;
console.log(num);
num = num+2;
console.log(num);

// SOME SHORTCUTS FOR REASSIGNING VARIABLES
// The same result as above can be obtained as follows
let newNum= 5;
console.log(newNum);
newNum+=2;
console.log(newNum);
// Instead of += 1 we can also use ++
let newerNum=17;
console.log(newerNum);
newerNum++;
console.log(newerNum);
// These shortcuts exist for operations other than addition as well
// Example: -- stands for -=1 and -=, *=, /= are used in the exact same way that += is used

// VARIABLE NAMING CONVENTIONS
// The JS naming convention is using camel case as we have used above
// Camel case is a naming convention where each word in a compound word starts with a capital letter, except the first word, e.g., myVariableName

// OTHER WAYS OF CREATING VARIABLES
// We can also create variables using the const keyword
// However, the values of these variables cannot be changed and will result in an error
// This keyword is used to create "constants"
// basically, it does not allow reassignment
const newestNum=88;
console.log(newestNum);

// The last way of creating variables is using the var keyword
// These variables can be reassigned
// It was the original way of creating variables in JavaScript
// However, it is now considered legacy and using it in new JS code is ill-advised
var age=27;
console.log(age);

// Finally, note that we can use typeof alongside variables to determine the type of the value they store
// Example:
console.log(typeof newerNum);
let phrase="Hello";
console.log(typeof phrase);

// BEST PRACTICE WHEN CREATING VARIABLES: Use let only when you plan on changing/updating the value of the variable
// otherwise it's always better to use const

// BOOLEAN VALUES

// There exist two boolean values in JS
// They are true and false
console.log(typeof true);
console.log(typeof true);
// A boolean value represents whether something is true or false
// Below two code examples will return boolean values
console.log(3 < 5);
console.log(3 > 5 );
// ASIDE: The > operator is called a comparison operator in JS
// there exist many other comparison operators in JS such as <, >, >=, <=, ==. !==
// They all have the same meanings as their mostly similar analogues in Python where they are called relational operators
// JS also support triple equals as an operator ===
// The difference between == and === is that == tries to convert objects into the same type before comparing
// Examples:
console.log('5'==5);
console.log('5'===5);
// As seen from above, the first line of code returns true
// Since this is may produce abnormal behaviour in certain applications, we stick to using ===

// ORDER OF OPERATIONS in JAVASCRIPT
// 1. Parentheses: () 
// 2. Multiplication and Division: / * 
// 3. Addition and Subtraction: + -
// 4. Compariosn Operators: <, >, >=, <=, ==. !==, ===
// Now, consider how an expression like below is evaluated
console.log(7 > 3 + 5); // This will return false as 3 + 5 is evaluated first according to operator precedence and becomes 8

// IF- STATEMENTS in JS allow us to write multiple blocks of code and decide which to run
if (3 > 7){
  console.log('Hey');
}
else{
  console.log('Bye');
}
// if works based on evaluation of expression in brackets. If the expression is true the code will run
// if it is not true, the code under else will run
// having an else block however is not mandatory
// It will basically just do nothing if the expression inside if is not true
// Example:
let age=17;

if (age>=16){
  console.log('You can drive');
}
else{
  console.log('You cannot drive');
}
// You can also have intermediate conditions similar to elif blocks in Python
// Here, we use else if instead of elif
// Example:
let num1= 40;
let num2= 17;

if (num1>num2){
  console.log('First number is greater');
}
else if (num1===num2){
  console.log('The numbers are equal to each other');
}
else{
  console.log('The second number is greater');
}

// LOGICAL OPERATORS IN JS

// Logical operators in JavaScript allow us to combine two boolean values
// The logical operators are AND, OR and NOT represented as &&, || and ! respectively
// They work similar to Python and are also short circuit evaluation operators
// These are especcialy useful when combining two boolean expressions in the condition of an if or else if clause

// IF STATEMENTS also do another interesting thing

// They create something known as scope
// A scope essentially defines/limits where a variable lives
// Any variables created within the curly braces of an if statement exist only within the curly braces of said if, else or else if clause
// That is, they cannot be accessed outside that part of the program by referring to them
// Scopes are an essential feature of most programming languages and help avoid naming conflicts
// This is why using var is not advised as it exhibits some weird behaviour in terms of scope
// If we name a variable outside the curly braces and use var to create a variable of the same name inside curly braces, then it will result in a naming conflict
// Whereas using let or const respects the scope rules better
// So essentially, IF statements create a small local scope within their body

// TRUTHY AND FALSY VALUES
// if statements not only work with true or false expresssions but also other values such as numbers and strings
// Values that behave like true are called truthy values
// Values that behave like false are called falsey values
// These are used as a sort of shortcut in our code
// List of Falsy values: 0, -0, NaN, "", 0n, null, undefined
// List of Truthy values: none-zero numbers, non-empty strings, empty arrays and objects, Infinity, -Infinity, any function
// Note that these truthy and falsy values work not only with if statements but also with logical operators

// Notes on some common values:
// NaN stands for not a number, it is returned if we do some invalid math
// undefined represents something that does not have a value
// null - we will look at this in the future

// TERNARY OPERATOR

// Absolutely! The ternary operator in JavaScript is a shorthand way to write an if...else statement.
// It’s called "ternary" because it takes three parts.
// Syntax: condition ? expression_if_true : expression_if_false;
// condition refers to the expression that evaluates to either true or false
// ? is a symbol that represents then
// expression_if_true is the expresssion to be evaluated if the condition is true
// expression_if_false is the expresssion to be evaluated if the condition is false
// Ternary operator has an advantage over the if statement as its value can be stored in a variable
// Example:
let years= 18;
let result = (years >= 18) ? "Adult" : "Minor";
console.log(result); // "Adult";


// GUARD OPERATOR &&
// Guard operator is not an operator in and of itself but is a way of using the and operator
// It's not an official operator, but a pattern where you use && to guard against something being falsy before accessing or executing.
// Syntax: condition && doSomething();
// If the condition is truthy, the function is executed
// Otherwise, short circuit evaluation prevents the function from being executed andnothing happens
// It is a shortcut for an if statement of the form:
/*
if (condition){
  doSomething()
}
*/
// Just like the ternary operator, we can save the result of the guard operator in a variable

// DEFAULT OPERATOR ||
// Works similar to the guard operator but uses the or operator instead of the and operator
// Syntax: let value = userInput || "default";
// If userInput is truthy, value becomes userInput due to short circuit evaluation
// If userInput is falsy, value becomes "default".
// It is a shortcut for an if statement of the form:
/*
let value;
if (!value){
  value= default_value;
}
*/