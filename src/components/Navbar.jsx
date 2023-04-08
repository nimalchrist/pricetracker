import React from "react";

import logo from "../assets/logo.png";

import { Button } from "react-bootstrap";

export const Header = ({ searchValue, handleInputChange, handleSearch }) => {
  return (
    <header className="header ">
      <div className="scontainer flex ">
        <div className="d-flex flex-row mb-5">
          <div className="logo" style={{ paddingLeft: "40px" }}>
            <img src={logo} alt="cart" />
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
            onSubmit={handleSearch}
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
        </div>
      </div>
    </header>
  );
};
