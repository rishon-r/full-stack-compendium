// TRY/ CATCH
// try/catch is a JavaScript error-handling structure that lets you:
// "Try" to run code that might throw an error
// Gracefully "catch" and handle the error without crashing your whole script
// It’s especially useful in places where exceptions might occur, like parsing JSON, accessing properties that might not exist, or handling network issues.
// You can also use an optional finally block

// SYNTAX:
/*
try {
  // risky code
} catch (error) {
  // error-handling code
} finally {
  // this code runs no matter what
}
*/

// 1. the try block
// Code inside the try block runs normally.
// If any runtime error (an exception) occurs during that execution, JavaScript jumps immediately to catch, skipping the rest of the try.

// 2. catch block
// this block only runs if an error is thrown inside the try.
// The error object is available inside the parentheses: catch(error)
// You can inspect it, log it, display a message, or handle it however you like

// 3. finally block (optional):
// Code in finally always runs, whether or not there was an error.
// Useful for cleanup logic (e.g., closing files, hiding loaders).

// EXAMPLE: 
try {
  const name = "Rishon";
  console.log(name.toUpperCase());
  console.log(nonExistentVar); //  This will throw a ReferenceError
  console.log("This line will not run");
} catch (error) {
  console.log("Caught error:", error.message);
}

// MANUALLY THROWING ERRORS
// You can manually throw errors inside a try block using throw
// EXAMPLE
try {
  const age = -1;
  if (age < 0) {
    throw new Error("Age cannot be negative");
  }
} catch (err) {
  console.log("Custom error:", err.message);
}

// EXAMPLE 2
try {
  console.log("Start");
  throw new Error("Something failed");
} catch (e) {
  console.log("Caught error:", e.message);
} finally {
  console.log("Cleanup done");
}