import React from "react";

function Navbar() {
  return (
    <nav>
      <ul>
        <li>
          <a href="#">Home</a>
        </li>
        <li>
          <a href="#">About</a>
        </li>
        <li>
          <a href="#">Profile</a>
        </li>
      </ul>
      <div className="search-bar">
        <input type="text" placeholder="Search..." />
        <button type="submit">Search</button>
      </div>
    </nav>
  );
}

export default Navbar;
