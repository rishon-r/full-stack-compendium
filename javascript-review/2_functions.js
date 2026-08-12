// FUNCTIONS
// Functions are a core part of any programming language
// Functions enhance readability and reusability of code
// They also have a profund impact on the maintainability of code 
// it is easier to change a value once in a reusable function when compared to changing values in multiple spaces where the function would have been called)
// An example of functions is given below

function hello(){
  console.log('Hello World');
}
hello();

// As seen from above, the word function is used to create a function
// A function has to be called for it to run
// A function can be called multiple times
hello();
hello();
hello();

// There are certain rules for naming functions
// For example, the function above is named hello
// The rules for naming functions are similar to variables and follow all the same rules
// They are not using keywords, not starting with a number and not using any special character but $ and _
// It is also best practice to stick to camel cases when dealing with function names
// Another small piece of advice when naming functions is to name them with a verb after the task they aim to accomplish

// Inside the curly braces we add the code we want to be run when the function is called/executed/run
// This part of the function is called the function body
// The first line before the function body is called the function header

// Functions, similar to the curly braces between an if statement have their own scope
// A variable created within a function body is available for use only within the body of that function
// Function level local scope
// Note that variabless created outside a function's body are called global variables and are legal and accessible anywhere in the program

// THE return STATEMENT
// The return statement allows to get a value back upon running the function
// Example:
function addition(){
  return 5+7;
}
// The above function will return 12 when called
// We can return any expression or variable from a function with the help of the return statement
// This process is known as returning a value and the value being returned is called a return value
// We can store the value of a function in a variable
let result=addition();
console.log(result); 
// Note that we are also not forced to return a value with a function
// There can be many functions that simply dont return a value
// If no value is explicitly mentioned with the help of a return statement,
// it means that the function is implicitly returning a undefined value
// Finally, a return statement at any point in the function body marks the end of the function 

// PARAMETERS
// Parameters are a key aspect of using functions within a program
// Parameters are essentially values being passed to a function
function adder(a,b){
  return a+b;
}
console.log(adder(35,7));
console.log(adder(3,71));
console.log(adder(5,17));
console.log(adder(2335,6999));
// a and b in the above example are parameters passed to the function
// You can pass different parameters to the function any time you call it as long as the parameters passed in the function call match the order of those in the function header
// Parameters work in a manner similar to variables as in they can be referred to by the same name, modified and used throughout the body of the function
// The rules for naming parameters are exactly the same as naming functions or variables

// If a function has parameters defined in its function header, we say that "the function takes parameters"
// Similarly when you pass parameters to a function in the function call, we say that we are passing values to a function

// Also note that due to scope rules, parameters passed to a function can only be used within that function