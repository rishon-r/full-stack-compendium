// ARRAYS
// Arrays are another type of value in JavaScript
// they represent a list of values enclosed in square brackets and separated by commas
// example:
const myArray=[13, 9, 22, 21, 11];
console.log(myArray);

// We can use indexing to obtain values from an array
console.log(myArray[0]);
console.log(myArray[2]);
console.log(myArray[1]);
// We can also use indexing to change values in an array
myArray[1]=27;
console.log(myArray[1]);
/// We cannot use negative indexing in JS like we did in Python
// JS also does not support the string slicing methods that Python does
// An array in JS can hold values of multiple types
// However, this is considered a bad practice when it comes to clean code
const yourArray= [1, 'hello', true, {name: 'James', children: ['martha', 'virginia']}];
console.log(yourArray);

// An Array itself is a type of value. This means we can save an Array in a variable and also have it as a value in another array
// Storing an Array in another Array creats something known as a NESTED ARRAY
const tryArray= [[1,2], [3,4], 5,6,7];
console.log(tryArray);
// Since an Array is a type of value, we can use typeOf alongside an Array to find a value
console.log(typeof tryArray); // You see however that this returns object as the type
// This is because an array is actually an object, just a special type of object
// We can find if something is actually an array using the following code below
console.log(Array.isArray(tryArray)); // This will return a boolean value based on whether or not the argument passed is an array

// Since we now know that an Array is an object, we see that there exist properties and methods that can be run on arrays
// Some examples are given below
let len= tryArray.length; // will return length of array
console.log(len);

console.log(tryArray);
tryArray.push(15); // Helps us add an element toi the back of an array
console.log(tryArray);
tryArray.splice(0,2); // Helps us remove a number of elements from an array starting at an index. First parameter is index, second parameter is the number of elements to be removed
console.log(tryArray)

// LOOPS

// FOR LOOP
// For loop is a countable loop in JS
// It is implemented in a manner very similar to for loops in C
// Syntax:
/*
for (initialization; condition; increment) {
  // code block to run
}
*/
// Example:
// for loop to print numbers from 1 to 10
for (let i=1; i <= 10; i++){
  console.log(i);
}

// WHILE LOOP
// While loop in JS is a conditional loop
// It runs as long as some condition remains true
// Syntax:
/*
for (initialization; condition; increment) {
  // code block to run
}
*/
// Example:
// while loop to print numbers from 1 to 10
let x=1;
while (x<=10){
  console.log(x);
  x++;
}

// ACCUMULATOR PATTERN
// The accumulator pattern is a common programming pattern where you use a variable to keep a running total or result while looping through data (like arrays or strings).
/* HOW IT WORKS
1. Initialize an accumulator variable (like sum, total, result, etc.)
2. Loop through a data structure
3. Update the accumulator on each iteration
4. Use the final value after the loop ends
*/

// Example: (Calculating sum of elements in an array)
let numbers = [10, 20, 30, 40];
let total = 0; // Step 1: accumulator

for (let i = 0; i < numbers.length; i++) {
  total += numbers[i]; // Step 3: update accumulator
}

console.log("Total is:", total); // Output: 10

// MORE ON ARRAYS
// ARRAYS in JS are REFERENCES similar to OBJECTS (probably because arrays are objects)
// When you create an array in JavaScript, you're not directly storing the array in the variable — you're storing a reference (i.e., a pointer) to the array's location in memory.
// So when you assign one array variable to another, you're not creating a copy — you're just pointing both variables to the same array in memory
// Example:
let arr1 = [1, 2, 3];
let arr2 = arr1;

arr2[0] = 99;

console.log(arr1); // [99, 2, 3]
console.log(arr2); // [99, 2, 3]

// The .slice() method
// array.slice(start, end) returns a shallow copy of a portion of the array, from the start index up to but not including the end index.
// While doing this, it does not modify the original array
let fruits = ["apple", "banana", "cherry", "date"];

let sliced = fruits.slice(1, 3);
console.log(sliced);       // ["banana", "cherry"]
console.log(fruits);       // ["apple", "banana", "cherry", "date"] (unchanged)
// Note that it starts at index 1 and goes upto but not including the end index 3

// Also, using the slice like this does not modify the original array when we update the new array
let numArr1= [1,3,5,7];
let numArr2= numArr1.slice();
numArr2[1]=2;
console.log(numArr1);
console.log(numArr2);

// DESTRUCTURSING AN ARRAY  
const nums=[1,2,3]

const [a,b,c]=nums; // This is the destructuring step
console.log(a,b,c); // a gets the first element, b gets the second element, c gets the third element

// break & continue
// break and continue are two important control flow statements in JavaScript, especially when working with loops.
// break is used to immediately stop a loop, the control jumps outside the loop
// continue spiks one iteration, but keeps looping
// continue skips the current loop iteration and moces directly to the next one
// Example of break: (below code prints numbers from 0 to 4)
for (let i = 0; i < 10; i++) {
  if (i === 5) {
    break;
  }
  console.log(i);
}
// Example of continue: 
// When i === 2, continue skips the console.log(i) and jumps to the next loop iteration
// So the below code prints number 0, 1, 3 and 4

for (let i = 0; i < 5; i++) {
  if (i === 2) {
    continue };
  console.log(i);
}