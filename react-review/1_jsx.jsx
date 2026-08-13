// JSX
// JSX is where JavaScript meets HTML
// In JSX we basically write html inside JavaScript files
// Note that JSX code isn't represented in strings
// JSX is essentially syntactic sugar that compiles to JavaScripts
/*

Example:

What you write: const element = <h1> Hello, React! <h1>

What it compiles to: React.createElement('h1', null, 'Hello, React!')

*/
// In general we always work with JSX and never with the code of the second type provided in the example

// JSX RULES
// 1. All JSX elements should hava a single parent element (You can use fragments as well, which are kind of like anonymous parent tags)
// 2. They should use className as an attribute instead of class because class is a reserved keyword in javascript, also htmlFor instead of for
// 3. All tags must be closed (including <img>, <br>)
// 4. JavaScript can be used inside { curly braces } within a JSX element
// 5. Inline styles must use camel case

// HOW TO USE REACT
// We essentially have an index.html file in our application and in the body then we only have two things:
// A div with id root
// And a script tag which references our main react file which has a .jsx extension
// Our aim is then to render the entire react app within this root <div>
// So in the .jsx file we include in the script tag, we will have code similar to this:
/*
import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'

createRoot(document.getElementById('root')).render(
    <StrictMode>
    <App/>
    </StrictMode>
)
*/
// The above code is the entry point of a modern React application. It initializes your app, hooks it into the web page's HTML,
//  and starts rendering your components
/*
More explanation:

1. import { StrictMode } from 'react'
Imports StrictMode, a built-in React helper tool. It doesn't render any visible UI; instead, it runs extra checks and warnings during
development to help you catch common bugs.

2. import { createRoot } from 'react-dom/client'
Imports the modern React 18+ method used to attach React to your browser's DOM (Document Object Model)

3. import './index.css'
Loads your global CSS styles so they apply across the entire app

4. import App from './App.jsx'
Imports your root React component (App), which contains the main UI structure for your application

5. createRoot(document.getElementById('root')).render(...)
Finds the HTML element on your page with the ID 'root' (usually a <div id="root"></div> in your index.html), 
creates a React root inside it, and renders your app inside <StrictMode>.

*/

/*

Closing singular tags: 

<img src="avatar.jpg" />
<input type="text" />

these are called self-closing tags
*/

/*
Using javascript within JSX example:
*/
function UserGreeting() {
  // 1. Regular JavaScript logic defined outside the JSX
  const name = "Alex";
  const userRole = "Admin";
  const unreadMessages = 3;

  return (
    <div className="card">
      {/* 2. Reading JavaScript variables inside JSX using { } */}
      <h1>Welcome back, {name}!</h1>
      
      {/* Doing string operations inside { } */}
      <p>Role: {userRole.toUpperCase()}</p>
      
      {/* Doing basic math inside { } */}
      <p>You have {unreadMessages * 2} pending notifications.</p>
    </div>
  );
}

// how to use inline styles
/*
In React JSX, inline styles aren't written as plain text strings like they are in regular HTML.
Instead, they are passed as JavaScript objects.
Because CSS property names often contain hyphens (like background-color or font-size), which are invalid in JavaScript object keys,
React converts them to camelCase (e.g., backgroundColor or fontSize)

Example:

When writing inline styles in JSX, you will almost always see two sets of curly braces:
<div style={{ backgroundColor: 'blue', fontSize: '18px' }}>
  Hello World
</div>

The Outer { } is the JSX "portal" to switch from HTML into JavaScript land.

The Inner { } creates a standard JavaScript object containing your key-value style pairs
*/ 
// More detailed example:
function StyledCard() {
  return (
    <div
      style={{
        // HTML: background-color -> JSX: backgroundColor
        backgroundColor: '#f4f4f9',

        // HTML: border-radius -> JSX: borderRadius
        borderRadius: '8px',

        // HTML: padding -> JSX: padding (no hyphen, but value needs quotes)
        padding: '20px',

        // HTML: font-size -> JSX: fontSize
        fontSize: '16px',

        // HTML: text-align -> JSX: textAlign
        textAlign: 'center',

        // Numeric values default to pixels (px) automatically in React!
        marginTop: 20 
      }}
    >
      <h2 style={{ color: 'darkblue', marginBottom: '10px' }}>
        Inline Style Example
      </h2>
      <p style={{ fontWeight: 'bold' }}>
        Notice how all CSS properties use camelCase!
      </p>
    </div>
  );
}
