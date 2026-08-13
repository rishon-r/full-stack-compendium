// COMPONENTS - The building block of react

// A component in react is esssentially just a function that returns some JSX
// React calls this function whenever the JSX it returns needs to be rendered
// The modern way of creating components in react is with arrow functions

// Note that it is convention for component names to start with a capital letter
// This isn't a style preference — it's how React tells the
// difference between your custom components and built-in HTML
// tags when compiling JSX.

// Old function style

function Welcome({ name }){
    return <h1> Hello, {name} </h1>;
}

// Arrow function style

const Welcome = ({ name }) => {
    return <h1> Hello, { name }</h1>;
}

// Usage
// This is basically like calling a function
// We call it with a self closing tag
<Welcome name="Ahsan" />
// The major advantage of components is reusability, which means that we can use the same component multiple times like a function
// This is because that is exactly what it is!
// Calling the same component with different arguments helps us avoid writing redundant html code

// { name } which the Welcome function takes as an argument is called a prop
// It is a way to pass data from parent components to child components
// i.e COMPONENTS RECIEVE DATA VIA PROPS
// Another example
function UserCard({ name, role }) {
  // name and role were pulled out of the props object.
  // Equivalent to: function UserCard(props) { ... props.name ... }
  return (
    <div className="user-card">
      <p>{name}</p>
      <p>{role}</p>
    </div>
  );
}

// Props are READ-ONLY. This component must never do
// name = "someone else" — it only displays what it's given.
// If the data needs to change, that has to happen in whoever
// is rendering <UserCard />, not inside UserCard itself.

// Old way, basically legacy now: Class based components

// CHILDREN PROP - content passed BETWEEN tags
// Anything you put between a component's opening and closing
// tags is automatically available to it as props.children.
// This is how you build generic "wrapper" components.

function Card({ children }) {
  return <div className="card">{children}</div>;
}

function Example() {
  return (
    <Card>
      {/* Everything here becomes Card's "children" prop */}
      <h2>Title inside the card</h2>
      <p>Some text inside the card.</p>
    </Card>
  );
}