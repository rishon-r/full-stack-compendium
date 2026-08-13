// ASYNC/AWAIT

// ONE KEY PROBLEM WITH PROMISES: It involves a lot of code
// To use a Promise, we must first initialize a promise object, use the resolve function, and then use the then function
// what ASYNC/AWAIT does is essentially provide a shortcut for promises

// WHAT DOES ASYNC DO?: When you precede a function header with the async keyword, it makes the function return a promise
// Having a return value; statement in the body acts similar to a resolve(); function in a promise body
// The main reason we use async over promises is that it allows us to use the second feature, await
// await lets us wait for a promise to finsih before going to the next line
// instead of using .then(), one can simply type await in front of a line of code in order to wait for it to finish
// await allows us to write asynchronous code like we would normal code
// This heavily enhances the readability of our code
// Note that you can only use await within an async function
// This is the major advantage of writing an async function
// Not also that async/await can only be used with promises, they do nothing with a callback

// async/await is syntactic sugar over JavaScript Promises, introduced in ES2017 (ES8). 
// It allows you to write asynchronous code in a way that looks and behaves like synchronous code, making it easier to read, write, and debug.
// Before async/await, handling asynchronous operations involved callbacks or .then()/.catch() with Promises, which could lead to callback hell or deeply nested structures.

// THE async KEYWORD: 
// Declares an asynchronous function.
// This function always returns a Promise.
// Even if you return a value (not a Promise), JavaScript wraps it in a resolved Promise.

// The await KEYWORD
// Can only be used inside an async function.
// Pauses the execution of the function until the awaited Promise is resolved.
// Once resolved, it returns the result of the Promise.
// If the Promise is rejected, it throws an error which you can catch using try/catch.
// The await keyword can only work with a promise or something then-able

// EXAMPLE: 
async function getWeather() {
  try {
    const response = await fetch('https://api.weatherapi.com/v1/current.json?key=API_KEY&q=London');
    const weather = await response.json();
    console.log(weather);
  } catch (error) {
    console.error('Failed to fetch weather:', error);
  }
}
// ABOVE CODE EXPLAINED:
// getWeather() is marked async, so it returns a Promise.
//  - What async does: When a function is declared with async, JavaScript automatically wraps its return value in a Promise.
//  - If the function returns a value: it becomes Promise.resolve(value)
//  - If the function throws an error: it becomes Promise.reject(error)
//  - Even if there's no explicit return, the function still returns a Promise, which will resolve after all awaits are done.
// await fetch(...) pauses the function until the fetch request completes.
//  - fetch(url) initiates an asynchronous HTTP request and immediately returns a Promise that will resolve to a Response object once the server responds.
//  - await tells JavaScript: "Pause this function's execution at this line until the fetch() Promise is resolved."
//  - JavaScript does not block the entire program — it just suspends execution inside that async function.
//  - During this pause: the JavaScript engine yields control back to the event loop.
//  - Other code (e.g., UI rendering, other functions, user events) can continue running.
//  - Once the fetch request completes (or fails), the engine resumes execution at the next line.
// Once the fetch Promise resolves, await response.json() parses the body
//  - response.json() is a method on the Response object returned by fetch
//  - It returns a Promise that resolves to the parsed JSON data from the response body.
//  - await response.json() pauses execution again, just like await fetch(...) did — this time waiting for the body to be fully read and converted into a JavaScript object.
//  - Once resolved, weather holds that parsed object.
// The result is logged. If any step throws an error (e.g., network failure), the catch block runs.
//  - At this point, both Promises (fetch and response.json()) have resolved, and we now have actual data in the variable weather.
//  - console.log(weather) executes like any regular line of synchronous code, printing the object to the console.
// If any step throws an error (e.g., network failure), the catch block runs.

// The engine transforms code of the form: 
/*
  async function getWeather() {
  const response = await fetch(...);
  const weather = await response.json();
  console.log(weather);
}
*/
// Into something like this: 
/*
function getWeather() {
  return fetch(...)
    .then(response => response.json())
    .then(weather => {
      console.log(weather);
    })
    .catch(error => {
      console.error('Failed to fetch weather:', error);
    });
}
*/
// But with async/await, you can write it in a top-down, readable, "synchronous-looking" manner without losing any of the asynchronous behavior.