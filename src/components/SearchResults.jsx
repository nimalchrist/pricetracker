import React, { useState, useEffect } from "react";
import { debounce } from "lodash";

function SearchResults({ searchValue }) {
  const [amazonResults, setAmazonResults] = useState([]);
  const [flipkartResults, setFlipkartResults] = useState([]);

  useEffect(() => {
    const delayedFetchData = debounce(async (searchValue) => {
      try {
        const response = await fetch(
          `http://localhost:5000/products/${searchValue}`
        );
        const data = await response.json();
        setAmazonResults(data.amazon);
        setFlipkartResults(data.flipkart);
      } catch (error) {
        console.error(error);
      }
    }, 500);

    if (searchValue === "") {
      setAmazonResults([]);
      setFlipkartResults([]);
      return;
    }

    delayedFetchData(searchValue);

    // Cleanup function to cancel the debounce timer
    return delayedFetchData.cancel;
  }, [searchValue]);

  return (
    <div>
      <div>
        <h3 style={{ margin: "auto", textAlign: "center" }}>Amazon</h3>
        <div
          style={{
            display: "flex",
            flexDirection: "column",
            flexWrap: "nowrap",
            justifyContent: "space-around",
          }}
        >
          {amazonResults.map((result, index) => (
            <div
              key={index}
              style={{
                border: "1px solid black",
                boxShadow: "1px 2px 9px black",
                display: "flex",
                alignItems: "center",
                flexBasis: "35%",
                margin: "15px",
              }}
            >
              <img
                src={result.image_url}
                alt={result.name}
                width="100"
                height="100"
              />
              <div style={{ marginLeft: "1rem" }}>
                <div>{result.name}</div>
                <div>{result.price}</div>
              </div>
            </div>
          ))}
        </div>
      </div>
      <div>
        <h3 style={{ margin: "auto", textAlign: "center" }}>Flipkart</h3>
        <div style={{ display: "flex", flexDirection: "column" }}>
          {flipkartResults.map((result, index) => (
            <div
              key={index}
              style={{
                border: "1px solid black",
                boxShadow: "1px 2px 9px black",
                display: "flex",
                alignItems: "center",
                flexBasis: "35%",
                margin: "15px",
              }}
            >
              <img
                src={result.image_url}
                alt={result.name}
                width="100"
                height="100"
              />
              <div style={{ marginLeft: "1rem" }}>
                <div>{result.name}</div>
                <div>{result.price}</div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default SearchResults;
