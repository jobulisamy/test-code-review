import React, { useState, useEffect } from 'react';

// Anti-pattern: Missing prop types (or TS interfaces)
const UserDashboard = (props) => {
  // Anti-pattern: Storing props in state unnecessarily
  const [userData, setUserData] = useState(props.user);
  
  // Bug: Changing state directly without setter
  const updateName = (newName) => {
    userData.name = newName; // Direct mutation
    // setUserData(userData); // Even if this was uncommented, it wouldn't trigger a re-render because object reference is the same
  };

  // Anti-pattern: Missing dependency array in useEffect can cause infinite loops
  useEffect(() => {
    console.log("Component updated!");
    
    // Memory leak: not clearing an interval
    setInterval(() => {
        console.log("Ping");
    }, 1000);
  });

  // Security: Using dangerouslySetInnerHTML with unsanitized input
  const bioHtml = { __html: props.bio };

  return (
    <div className="dashboard">
      <h1>Welcome, {userData.name}</h1>
      
      {/* Accessibility issue: img missing alt text */}
      <img src={userData.avatarUrl} />
      
      {/* Code smell: Inline styles instead of classes for complex styling */}
      <div style={{ padding: '20px', margin: '10px', backgroundColor: 'var(--bg-color)' }}>
         <div dangerouslySetInnerHTML={bioHtml} />
      </div>

      {/* Code smell: Inline arrow function in render creates a new function on every render */}
      <button onClick={() => updateName("Jane Doe")}>
        Change Name to Jane
      </button>
      
      <ul>
        {/* Bug: Missing key prop in list rendering */}
        {props.items.map(item => (
            <li>{item.name}</li>
        ))}
      </ul>
    </div>
  );
};

export default UserDashboard;
