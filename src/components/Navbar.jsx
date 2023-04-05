import React, { useState } from "react";

import cart from "../assets/kartt.png";

import { Button } from "react-bootstrap";

export const Header = () => {
  const [searchValue, setSearchValue] = useState("");

  const handleSearch = async () => {
    // handle search action here
    //texting
    alert(searchValue);
  };

  const handleInputChange = (event) => {
    setSearchValue(event.target.value);
  };

  return (
    <>
      <header className="header ">
        <div className="scontainer flex ">
          <div className="d-flex flex-row mb-5">
            <div className="logo" style={{ paddingLeft: "40px" }}>
              <img src={cart} alt="cart" />
            </div>
            <div
              class="input-group rounded"
              style={{
                paddingRight: "50px",
                paddingTop: "10px",
                paddingBottom: "10px",
                paddingLeft: "50px",
              }}
            >
              <input
                type="search"
                class="form-control rounded"
                placeholder="Search"
                aria-label="Search"
                aria-describedby="search-addon"
                value={searchValue}
                onChange={handleInputChange}
              />
              <span class="input-group-text border-0" id="search-addon">
                <Button variant="outline-primary" onClick={handleSearch}>
                  Search
                </Button>
              </span>
            </div>
            <div className="wish">wish</div>
            <div className="user">User </div>
          </div>
        </div>
      </header>
    </>
  );
};
