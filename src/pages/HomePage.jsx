import React, { useState } from "react";

import { Header } from "../components/Navbar";
import SearchResults from "../components/SearchResults";

function HomePage() {
  const [searchValue, setSearchValue] = useState("");
  const handleSearch = async () => {
    alert(searchValue);
  };
  const handleInputChange = (event) => {
    setSearchValue(event.target.value);
  };
  return (
    <div className="nav-bar">
      <Header
        searchValue={searchValue}
        handleInputChange={handleInputChange}
        handleSearch={handleSearch}
      />
      {searchValue ? (
        <SearchResults searchValue={searchValue} />
      ) : (
        <div
          className="center-text"
          style={{ textAlign: "center", width: "100%" }}
        >
          <p style={{ fontSize: "16px", fontWeight: "bold" }}>
            Enter products to search
          </p>
        </div>
      )}
    </div>
  );
}

export default HomePage;
