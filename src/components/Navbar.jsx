import React, {useState} from "react";
import logo from "../assets/logo.png";
import { Button } from "react-bootstrap";
import { IoIosLogOut } from "react-icons/io";
import { MdOutlineFavoriteBorder } from "react-icons/md";
import { VscAccount } from "react-icons/vsc";

export const Header = ({ searchValue, handleInputChange, handleSearch }) => {
  const [showOverlay, setShowOverlay] = useState(false);

  const handleAccountClick = () => {
    setShowOverlay(true);
  };
  return (
    <header className="header" style={{   }}>
      <div className="container-fluid">
        <div className="row align-items-center">
          <div className="col-md-3 col-8">
            <img src={logo} alt="cart" style={{ height: 60 }} />
          </div>
          <div className="col-md-6 col-4">
            <div className="input-group rounded">
              <input
                onSubmit={handleSearch}
                type="search"
                className="form-control rounded"
                placeholder="Search"
                aria-label="Search"
                aria-describedby="search-addon"
                value={searchValue}
                onChange={handleInputChange}
              />
              <span className="input-group-text border-0" id="search-addon">
                <Button variant="outline-primary" onClick={handleSearch}>
                  Search
                </Button>
              </span>
            </div>
          </div>
          <div className="col-md-3 d-flex justify-content-end">
            <div className="d-flex align-items-center mr-3">
              <MdOutlineFavoriteBorder size={20} style={{ color: "red" }} />
              <span>Wishlist</span>
            </div>
            <div className="d-flex align-items-center mr-3" onClick={{handleAccountClick}}>
            <Button variant="link" onClick={{showOverlay}} style={{textdecoration: 'none'}}>
              <VscAccount size={20} />
              <span>Account</span></Button>
              
            </div>
            <div className="d-flex align-items-center">
              <IoIosLogOut size={20} />
              <span>Logout</span>
            </div>
          </div>
        </div>
      </div>
     
    </header>
    
  );
};

