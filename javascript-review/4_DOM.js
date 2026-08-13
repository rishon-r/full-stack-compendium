// DOM stands for Document Object Model
// The DOM is a very important feature of JavaScript
// The DOM is another Built-in object in JS similar to JSON or localStorage
// This built in object is called the document object
// The document object represents or models the webpage and is hence called document object model

// DOM syntax
// The DOM essentially just refers to the document object
// it works similar to all other objects and has properties such as body and title that can be accessed via the dot notation
// To show working of the DOM, we will run examples in the dom_examples.html file in the same directory as this file
// Besides properties, the document object also has a series of methods associated with it which we will soon dicuss

// The major use of the document object is that it allows us to have HTML within our javascript code
// Thus, the DOM combines HTML and JavaScript together and gives JavaScript control of the webpage
// Below, I have pasted some common properties of the document object

/* COMMON PROPERTIES
  1. document.title	Gets or sets the title of the document (what shows in the browser tab). You can assign it a value.
  2. document.body	Returns the <body> element of the page.
  3. document.head	Returns the <head> element of the page.
  4. document.documentElement	Returns the root element (<html>) of the document.
  5. document.URL	Returns the full URL of the page.
  6. document.domain	Returns the domain name of the server.
  7. document.cookie	Gets or sets cookies associated with the page.
  8. document.readyState	Returns the loading state of the document (e.g., "loading", "complete").
  9. document.forms Returns collection of the <form> elements
  10. document.images Returns collection of the <img> elements
  11. document.links Returns collection of the <a> elements
*/

// VERY IMPORTANT NOTE: When a HTML element is retrieved in JavaScript via use of the document object's properties, it is in the form of a JS Object
// So, some of these HTML elements have useful properties in and of themselves in JS
/* Example:
 document.body.innerHTML gets or sets the HTML content inside the <body> tag of your document.
    - You can customize the body of the HTML page using this
    - E.g: document.body.innerHTML = "<h2>New Content!</h2><p>Replaced everything!</p>";
    - As seen above, you can pass html tags in the string as well

*/

/*
NOTE ON CSS Selectors before we continue:

A CSS selector is a pattern used to target and select specific HTML elements on a web page so you can style them or manipulate them with JavaScript.
Think of it like a search query for your HTML page: it tells the browser, "Find these specific elements so I can apply rules to them"

In CSS, a rule consists of two main parts: the Selector (who gets styled) and the Declaration Block (what styles to apply)

Example:

//'h1' is the SELECTOR 
h1 {
  color: blue;        // Property + Value 
  font-size: 24px;    // Property + Value 
}
Some common selectors:
HTML tag name (like p or h1), assigned class names (.btn), unique identifiers (#header), or even specific states like when a user hovers over a button (button:hover)

*/


// Now, we will dicuss some imprtant methods of the document object
/* SOME IMPORTANT METHODS OF THE DOM

querySelector(selector)	Returns the first element matching a CSS selector
  - When using a .class selector to select particular HTML elements it is often practice to start the name of the class of an element with 'js-' in the HTML code
  - Returns null if no elements match the selector
  - Use .querySelectorAll if you want it to match all elements
*/

// Also note that every HTML element retireved as a property of the document objects is an object and has property innerHTML
// This property allows you to change the HTML code inside that particular element
// There exists also an innerText property that is used to get or set the visible text content of an HTML element
// — i.e., what a user can see on the page (not including hidden elements or HTML tags which the innerHTML provides us).
// This can also be accessed as a property of all HTML objects in JS code 

// The .value property is used to get or set the current value of form elements like: <input>, <textarea> and <select>
// Only form-related elements (elements that accept user input) have a .value property


// Also note that any time you get a value from the DOM, it will be in the form of a string
// So, if it is a numerical value you desire, convert it from string type explicitly using Number()
// This is called type conversion/ type coercion
// The String() function also converts any type into a string
// Type coercion can be done IMPLICITLY by JS or EXPLICITLY as we have mentioned above
// IMPLICIT conversion can be seen when we try doing addition with a string. Here, the number will be converted into a string and concatenation will take place.
console.log('25'+5);
// When we do subtraction, the string is converted into a number
console.log('25'- 5);
// However, it is advised to not do arithmetic with strings as it results in weird behaviour as above

// Using the DOM goes hand in hand with the onclick and onkeydown attributes of html tags
// These attributes are called EVENT LISTENERS whereas click and keydown are EVENTS

// Every event listener gets an event object associated with it in JS
// The event object has a lot of properties associated with it

/*
  In JavaScript, the event object is an automatically passed argument to event handler functions that provides 
  detailed information about the event that occurred—such as the type of event (click, keydown, etc.), 
  the target element that triggered it, and additional data like mouse position or key pressed.
  It allows developers to respond intelligently to user interactions by accessing properties (like event.target, event.type, or event.key)
  and methods (such as preventDefault() to stop default browser behavior or stopPropagation() to prevent the event from bubbling up). 
  This object is essential for building interactive, responsive web applications.
*/

// .classList is another property of HTML element objects in JS
// This gives us control of the class attribute of the HTML element
// We can use .classList.add to add a class to the class list of the HTML element
// This is useful when we want to modify the css styling of an element after a particular interaction/event takes place

// THE window OBJECT
// Similar to how the document object represents the webpage, the window object represents the browser
// The document object is actually inside the window object
// So is the console object we have been using for console.log
// Pop-ups are also parts of the window
// Saying window.alert invokes the same
// However, the window object has a shortcut. we don't need to state its name explicitly
// Thats why we can access the document object or say console.log without worrying about mentioning the window object
// JS automatically adds window before these objects

// VERY IMPORTANT
// Organizing your code in different files
// Use the src attribute of script tag to link to a separate javascript file
// you can also use multiple script elements with src attributes to split your JavaScript code into different files

// BELOW METHOD: VERY USEFUL
// THE .addEventListener() METHOD
// The .addEventListener() method in JavaScript is used to attach an event handler to an HTML element. 
// It allows you to run a specific piece of code (a callback function) when a particular event (like a click, key press, or mouse move) happens on that element.
// In a way it is a JS way to replcae adding onclick or onkeydown attributes in HTML tags
// SYNTAX: element.addEventListener(event, callback, useCapture);
// event: A string representing the type of event (e.g., "click", "mouseover", "keydown")
// callback: The function that will run when the event occurs.
// useCapture (optional): A boolean that determines whether the event is captured in the capture phase (true) or bubble phase (false). 
// You can attach multiple event listeners to the same element without overwriting previous ones.
// EXAMPLE
/*
HTML:
<button id="myButton">Click me</button>

JS:
document.getElementById("myButton").addEventListener("click", function () {
  alert("Button was clicked!");
});
*/

/* 
AN EXAMPLE WITH A NAMED FUNCTION:
function greet() {
  console.log("Hello there!");
}

document.getElementById("myButton").addEventListener("click", greet);

*/

// The event parameter in an event listener refers to an Event object that is automatically passed to the callback function when an event occurs.
// It contains details about the event — like what type of event happened, which element triggered it, keyboard or mouse info, etc.

/*
USEFUL EVENT PROPERTIES:

event.type	The type of event (e.g., "click", "keydown").
event.target	The actual element that triggered the event.
event.currentTarget	The element the listener is attached to.
event.preventDefault()	Stops the default browser behavior (e.g., following a link).
event.stopPropagation()	Prevents the event from bubbling up to parent elements.
event.key	For keyboard events: which key was pressed.
event.clientX / event.clientY	Mouse coordinates relative to the viewport.

EXAMPLE: 

document.querySelector("button").addEventListener("click", function(event) {
  console.log("You clicked:", event.target); // Logs the clicked button
})


*/
// The event object is like a report of what just happened — what triggered the event, how it happened, and any relevant context (mouse, keyboard, etc.). It gives you full control over how to respond

// THE .removeEventListener() METHOD
// .removeEventListener() is the counterpart to .addEventListener() in JavaScript.
// It’s used to detach a previously attached event listener from an element. This stops the event from triggering the function when it occurs.
// SYNTAX: element.removeEventListener(event, callback, useCapture);
// parameters (must match the ones used in .addEventListener()):
// event: The name of the event (e.g., "click").
// callback: The same function reference that was originally passed to .addEventListener().
// useCapture (optional): Must match the one used when the listener was added (usually false).
// NOTE: You must pass the same function reference to removeEventListener() — otherwise, it won’t work.
// So, this won't work if anonymous functions are passed
/*
EXAMPLE:
function sayHello() {
  console.log("Hello!");
}

const button = document.getElementById("myButton");

// Add the event listener
button.addEventListener("click", sayHello);

// Remove the event listener
button.removeEventListener("click", sayHello);
*/


/* MORE TECHNICAL EXPLANATION

1. What the DOM Actually Is

The DOM (Document Object Model) is not the HTML file. It's a live, in-memory tree data structure that the browser builds after reading your HTML. Once built, the DOM is what actually gets drawn on screen — the original HTML file is discarded from the process at that point.

Think of it in three separate stages:

HTML text file  --(parsing)-->  DOM tree (in memory)  --(rendering)-->  pixels on screen

This distinction matters because:

Editing the HTML source file after the page has loaded does nothing — the browser already moved past it.
The DOM tree can be changed live by JavaScript, and the browser will re-render to reflect it, with no HTML file involved at all.

Why this matters for React: React never touches your HTML file. It builds and updates the DOM tree directly, in memory, using JavaScript — exactly like the "parsing" step above, except React does it instead of the browser's HTML parser.

Every tag in your HTML becomes a node in the tree, nested according to how the tags were nested. A node can be:

an element node (<div>, <p>, <img>, etc.)
a text node (the actual text inside an element)
a comment node (<!-- ... -->)
the document node (the root of everything)

Every node has relationships to other nodes: a parent, zero or more children, and siblings 
(nodes sharing the same parent). Every DOM operation — reading, updating, deleting — is really just navigating or editing this tree

Why this matters for React: A React component tree (components nesting other components)
is deliberately shaped like the DOM tree it will eventually produce. When you nest <Parent><Child /></Parent> in JSX,
you're describing DOM tree shape, one level removed

Nodes Have Identity — They Are Not Just Their Content

This is one of the most important, least obvious ideas in the whole DOM model: a specific DOM node is a specific object in memory,
 with its own identity, that persists over time — independent of what's currently displayed inside it.

If you have a <p> on screen and you change its text, it's still the same <p> node. But if you delete that <p> and create a brand 
new one with identical text, it's a different node, even though it looks pixel-for-pixel identical.

Why does this distinction matter in practice? Because some state lives on the node itself, not in its visible content:

Focus (which element currently has keyboard focus)
Scroll position inside a scrollable element
Text selection / cursor position inside an <input>
CSS transition/animation state
Video/audio playback position

If a node gets destroyyed and recreated, all of that is lost — even if the new node looks identical.

Why this matters for React: This is exactly why the key prop exists for lists.
React uses key to decide whether an item in a re-rendered list is "the same node,
just updated" or "a completely different node." Get keys wrong (e.g. using array index for a reorderable list),
and React may destroy/recreate nodes it should have reused — causing lost input focus, reset scroll, glitchy animations,
for exactly the reason described above.

Attributes vs. Properties (a classic gotcha)

These sound like the same thing and usually behave the same, but they are technically two different things:

An attribute is what's written in the HTML markup: <input value="hello"> — the attribute value is "hello".
A property is the corresponding field on the live JavaScript DOM object: inputElement.value.

For most attributes, the browser keeps these in sync automatically. But for some — most notably value on form inputs and checked
on checkboxes — they diverge on purpose: the attribute reflects the initial value from HTML, while the property reflects the current,
live value as the user interacts with it. Typing into a text box changes the value property immediately, but the original HTML value
attribute stays frozen at whatever it was initially.

Why this matters for React: This is the root cause of React's "controlled vs. uncontrolled input" distinction (see Section 9).
It's also why JSX attribute names sometimes differ from HTML (className instead of class, htmlFor instead of for) — JSX props map more
closely to DOM properties than to HTML attributes.

Rendering Is Expensive — Reflow and Repaint

When the DOM changes, the browser doesn't instantly redraw just that one change. Depending on what changed, it may need to:

Reflow (layout): recalculate the size and position of elements — potentially many elements, since one element's size can affect its 
neighbors' positions.
Repaint: redraw the actual pixels.

Changing something like element.style.width can trigger a reflow of a large portion of the page.
 Doing this repeatedly and unnecessarily (e.g. in a loop, once per item) is a classic source of janky, slow web pages.

Why this matters for React: This is the actual problem React was built to solve.
Instead of you manually deciding which specific DOM nodes to touch and when, 
React lets you just describe "what the UI should look like given the current state," 
and it figures out the minimal set of real DOM changes needed to get there (via a diffing process often called "the virtual DOM"),
batching them to avoid unnecessary reflows. You get the mental simplicity of "just re-render everything" with performance closer to 
"carefully update only what changed."

Declarative vs. Imperative DOM Updates

This is less a DOM API concept and more a mental shift, but it's the one that matters most for understanding why React feels so different 
from plain JavaScript DOM code.

Imperative (plain DOM manipulation): you describe the steps to transform the current state of the page into the new state.

js
const li = document.createElement("li");
li.textContent = "New item";
list.appendChild(li);

You are responsible for knowing the current state of the DOM and issuing the right sequence of commands to update it.

Declarative (React): you describe what the UI should look like right now, given the current data — and let the framework figure out
the steps.

jsx
<ul>
  {items.map(item => <li key={item.id}>{item.text}</li>)}
</ul>

You never say "create," "append," or "remove." You just describe the desired end result for the current data, every time, and React diffs that against what's already there.

Why this matters for React: Every JSX expression you write is a declarative description of a DOM subtree — not a sequence of DOM operations. 
Understanding the imperative version first (Sections 1–5) is what makes the declarative version feel like an intentional simplification rather
than magic.

Events, Bubbling, and Delegation

When something happens on an element (a click, a keypress), the browser fires an event.
 Critically, events don't just fire on the exact element clicked — they bubble: the event fires on the target element first,
  then on its parent, then that parent's parent, and so on up to the document root.

This is why event delegation works: you can attach a single listener to a parent element and still respond to clicks on any of
 its current or future children, because the event bubbles up to the parent regardless of which child was clicked.

Why this matters for React: React attaches most event listeners once, at a central point, rather than individually on every element — 
under the hood, it leans heavily on this same bubbling behavior. It also wraps the native event object in its own cross-browser-consistent
SyntheticEvent, but the underlying concept (event.target, bubbling order) is identical to what you'd see in plain DOM code. 
When you write onClick={handler} in JSX, you're conceptually doing the same thing as addEventListener("click", handler), just with React
managing the wiring for you.

The Document as the Root of Everything

document is the single global entry point to the entire tree —
everything you can select or traverse starts from it (directly, like document.getElementById(...),
or indirectly, by navigating from a node you already have).

A useful mental model: your entire visible page is one big tree rooted at document, and any change anywhere in the UI is really a change 
to some node somewhere inside that single tree.

Why this matters for React: A React app is typically mounted into one specific DOM node (traditionally something like <div id="root">). 
Everything React renders — your entire component tree, no matter how complex — becomes a subtree grafted onto that single mount point.
The rest of the real DOM (outside the mounted root) is untouched by React.

Controlled vs. Uncontrolled State (Form Elements)

Form elements (<input>, <textarea>, <select>) are special: they maintain their own internal, live state 
(their current value or checked property — see Section 4) independent of whatever the HTML originally specified. 
The browser updates this internal state automatically as the user types, without you writing any code.

This creates two possible philosophies for who "owns" the current value:

Uncontrolled: you let the DOM node manage its own value internally, and only reach in and read it when you need it (e.g. on form submit).
Controlled: you treat the DOM node's displayed value as something that must always match a value you are tracking elsewhere 
(e.g. in a variable), and every keystroke immediately updates your own tracked value, which is then fed back into the input.

Why this matters for React: This maps directly onto React's "controlled component" pattern:
<input value={value} onChange={e => setValue(e.target.value)} />.
React is forcing the input's displayed value to always match your state,
rather than letting the DOM node's own internal value drift independently. 
Understanding that the DOM node has its own independent internal state by default is what makes it click 
why React needs onChange + value together, and why leaving out onChange on a controlled input makes it "read-only" (
React keeps resetting it back since nothing updates your tracked state).

Direct Node References (the concept behind useRef)

Sometimes you need a direct handle to one specific, real DOM node — not to change what it displays,
 but to call an imperative method on it or read a real, rendered measurement: .focus(), .scrollIntoView(),
  .play() on a video, getBoundingClientRect() for its pixel size and position, or to integrate a non-React library 
  that expects a raw DOM node.

These are cases where declarative "just describe what it should look like" doesn't apply — you're asking the node to do something, 
or asking it a question about its current rendered state, not describing its appearance.

Why this matters for React: This is precisely the escape hatch useRef provides: a way to get a stable reference to the real,
 underlying DOM node React created for a given JSX element, so you can call these imperative, DOM-native methods directly when 
 there's no declarative equivalent.
*/