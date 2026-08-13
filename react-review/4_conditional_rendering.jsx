// CONDITIONAL RENDERING
// Conditional rendering refers to the process of showing/hiding content dynamically
// Conditional rendering is how components show different UI depending on state, props, or any other condition —
//  the "if/else" of your UI tree. 
// Since JSX only allows expressions (not statements) inside {}, there's no <if> tag;
//  instead you reach for a handful of JavaScript expression patterns
// There are a few common ways to do this

// 1. if else
/*
EXAMPLE:
function Greeting({ isLoggedIn }) {
  if (isLoggedIn) {
    return <h1>Welcome back!</h1>;
  }
  return <h1>Please sign in</h1>;
}

*/

// 2. ternary operator
/*
EXAMPLE:
function StatusBadge({ isOnline }) {
  return (
    <div>
      {isOnline ? <span className="dot green" /> : <span className="dot gray" />}
      {isOnline ? "Online" : "Offline"}
    </div>
  );
}

*/

// 3. guard operator using &&
/*
EXAMPLE:

function Inbox({ unreadCount }) {
  return (
    <div>
      <h2>Inbox</h2>
      {unreadCount > 0 && <p>You have {unreadCount} unread messages.</p>}
    </div>
  );
}
*/

// NOTE: React DOES NOT RENDER null, undefined, false or true
// It renders numbers and strings as text nodes

// 4. variable assignment beforehand and multiple conditions
/*
EXAMPLE:
function OrderStatus({ status }) {
  let content;

  if (status === "loading") {
    content = <Spinner />;
  } else if (status === "error") {
    content = <ErrorMessage />;
  } else if (status === "empty") {
    content = <p>No orders yet.</p>;
  } else {
    content = <OrderList status={status} />;
  }

  return <div className="order-status">{content}</div>;
}
*/

// 5. Using switch statements
/*
EXAMPLE:
function StatusIcon({ status }) {
  switch (status) {
    case "success":
      return <CheckIcon />;
    case "error":
      return <XIcon />;
    case "pending":
      return <ClockIcon />;
    default:
      return null;
  }
}
*/