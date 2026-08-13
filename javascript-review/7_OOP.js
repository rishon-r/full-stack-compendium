// OOP- Object Oriented Programming
// A different method of programming that involves organizing your code into objects
// So far, we have used PROCEDURAL PROGRAMMING
// A procedure refers to a set of step-by-step instructions
// in PROCEDURAL PROGRAMMING we organize our code into functions

// In OOP, we group our data and functions into objects
// Why do we use OOP?
// OOP tries to represent the real world
// E.g in real life, a cart can have properties inside it and we can perform actions to modify a cart
// Some developers feel that this makes the code more intuitive

// Another important reason to use objects is that it is easy to create multiple objects
// We can either copy paste the code of an object, which is laborious and not the standard practice
// or create a function that generates objects
// another way of generating objects is through the help of a class

// CLASS
// A class is basically an object generator
// They are cleaner and have more features than using functions
// We say that an object is an instance of a class
// Benefits of using CLASSES:
// A class actually looks like the object it creates
// It is cleaner than using a function
// Classes also have some extra features for OOP

// THE this KEYWORD
// refers to that particular instance of a class

// CONSTRUCTORS
// A constructor is an extra feature that classes possess for OOP
// It allows us to run some setup code after creating an object
// A constructor lets us put this set up code inside a class
// It can be viewed as a special method for setting up instances that is called automatically when you set up a new object using a class
// Some rules: The constructor method should be named constructor, it cannot return any value

// SYNTAX:
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  greet() {
    console.log(`Hi, I'm ${this.name}, and I'm ${this.age} years old.`);
  }
}

const p1 = new Person("Alice", 30);
p1.greet(); // Hi, I'm Alice, and I'm 30 years old.

// PRIVATE PROPERTIES AND METHODS
// Classes allow us to make a particular method or property private- i.e it is only available for acess within that class
// You add a # symbol before naming property or method in order to make it private
// A method or property in a class that can be acessed from outside that class is called a PUBLIC METHOD/PROPERTY
// NOTE: field and property refer to the same thing and can be used interchangeably

// INHERITANCE
// Inheritance allows us to reuse code between classes without having to extensively duplicate code
// With inheritance, a class can get all the properties and methods of another class
// We call this class a CHILD class and the class it gains properties and methods from the PARENT class
// We say that a CHILD class EXTENDS the PARENT class
// The CHILD class can also have new methods and properties that the parent class doesn't have
// It can also override methods and properties of the parent class. Overriding a method is called METHOD OVERRIDING
// Basically, we use Inheritance when one class is a more specific type of another class
// it uses extends to inherit from another class and super to call the parent class constructor or methods.

// Example:

class Animal {
  constructor(name) {
    this.name = name;
  }

  speak() {
    console.log(`${this.name} makes a sound.`);
  }
}

class Dog extends Animal {
  speak() {
    super.speak(); // Call parent method
    console.log(`${this.name} barks.`);
  }
}

const d = new Dog("Rex");
d.speak();
// Rex makes a sound.
// Rex barks.

// POLYMORPHISM

/*
 What is Polymorphism?

Polymorphism (from Greek: "poly" = many, "morph" = form) means "many forms."
It allows objects of different types to be treated through a common interface,
typically by sharing method names.

In JavaScript, polymorphism is achieved through:

1. Method Overriding: Subclasses override a method defined in a parent class.
2. Duck Typing: If an object has the expected method (e.g., .print()), we treat it as valid.

This makes our code flexible, reusable, and easier to extend.
 Benefits:
- Shared interface across types (e.g., `.calculateSalary()` on different employee types)
- Simplifies code by removing the need for manual type checking
- Enables scalable and maintainable design patterns

Now, let’s demonstrate polymorphism using both:
- Class-based inheritance
- Duck typing (structural polymorphism)
*/

// CLASS-BASED POLYMORPHISM EXAMPLE

// Base class: Employee
class Employee {
  constructor(name) {
    this.name = name; // Common property for all employees
  }

  // Default method (to be overridden)
  calculateSalary() {
    return 0; // Placeholder logic
  }
}

// Subclass 1: Full-time employee
class FullTimeEmployee extends Employee {
  constructor(name, monthlySalary) {
    super(name); // Call the base class constructor
    this.monthlySalary = monthlySalary;
  }

  // Override: Full-time employees get a fixed monthly salary
  calculateSalary() {
    return this.monthlySalary;
  }
}

// Subclass 2: Freelancer
class Freelancer extends Employee {
  constructor(name, hourlyRate, hoursWorked) {
    super(name);
    this.hourlyRate = hourlyRate;
    this.hoursWorked = hoursWorked;
  }

  // Override: Freelancers are paid hourly
  calculateSalary() {
    return this.hourlyRate * this.hoursWorked;
  }
}

// Subclass 3: Intern
class Intern extends Employee {
  constructor(name, stipend) {
    super(name);
    this.stipend = stipend;
  }

  // Override: Interns receive a fixed stipend
  calculateSalary() {
    return this.stipend;
  }
}

// POLYMORPHISM IN ACTION


// Create an array of various employee types
const employees = [
  new FullTimeEmployee("Alice", 5000),     // Fixed monthly
  new Freelancer("Bob", 50, 120),          // $50/hr * 120 hrs
  new Intern("Charlie", 1000)              // Fixed stipend
];

// Loop through all employees and call the same method
// Even though each object is a different class, the method behaves correctly
for (const emp of employees) {
  console.log(`${emp.name}'s salary is $${emp.calculateSalary()}`);
}

// Output:
// Alice's salary is $5000
// Bob's salary is $6000
// Charlie's salary is $1000

// DUCK TYPING POLYMORPHISM EXAMPLE


// Any object that implements a `.print()` method can be passed here
// No inheritance required!

const printer = {
  print() {
    console.log("Printing from printer");
  }
};

const pdf = {
  print() {
    console.log("Printing PDF document");
  }
};

const image = {
  print() {
    console.log("Printing image file");
  }
};

// This function accepts any object with a .print() method
function executePrintJob(printable) {
  printable.print(); // We don't care what the object is — only that it has a .print() method
}

// Duck typing in action
executePrintJob(printer); // Output: Printing from printer
executePrintJob(pdf);     // Output: Printing PDF document
executePrintJob(image);   // Output: Printing image file


// SUMMARY OF POLYMORPHISM
//
// - Polymorphism allows different object types to be used interchangeably.
// - Enables calling the same method on different objects with varying behavior.
// - Implemented in JS through:
//    Class inheritance + method overriding
//    Duck typing (structural, interface-based)
//
// These concepts power flexible, modular, and scalable codebases.

// TESTING CLASSES
// You can test classes the same way you test other objects, it's the same as normal tests

// BUILT IN CLASSES
// These are classes that are provided by the language
// An example of abuilt in class is Date()

const date= new Date()
console.log(date);
const localTime= date.toLocaleTimeString();
console.log(localTime);

// MORE INFO ON THE this KEYWORD
// The this keyword is usually used in conjunction with an object
// However, it need not be used that way
// When you use this without an object, its value is usually undefined
// Example:
console.log(this);
// Originally, this represented the window
// But this caused confusion and since then this has been set to undefined within a module
// this is a dynamic reference to the execution context — i.e., the object that is currently "owning" the code being executed.
// The value of this depends entirely on how a function is called.

function strictFunction() {
  console.log(this); // undefined
}
strictFunction();
strictFunction.call('hello'); // The call helps us set the value of the this keyword within a function

// Within an arrow function, this is undefined. An arrow function basically does not change the value of 'this'
const obj = {
  name: "Bob",
  greet: () => {
    console.log(this.name); // undefined (or error in strict mode)
  }
};

obj.greet();

// When a function is called as a method, this refers to the object before the dot
const person = {
  name: "Alice",
  greet() {
    console.log(`Hello, I'm ${this.name}`);
  }
};

person.greet(); // this = person
