// import React, { useState, useEffect } from "react";
// import { debounce } from "lodash";

// function SearchResults({ searchValue }) {
//   const [amazonResults, setAmazonResults] = useState([]);
//   const [flipkartResults, setFlipkartResults] = useState([]);
//   const [cheapestProduct, setCheapestProduct] = useState(null);

//   useEffect(() => {
//     const delayedFetchData = debounce(async (searchValue) => {
//       try {
//         const response = await fetch(
//           `http://localhost:5000/products/${searchValue}`
//         );
//         const data = await response.json();
//         setAmazonResults(data.amazon);
//         setFlipkartResults(data.flipkart);
//       } catch (error) {
//         console.error(error);
//       }
//     }, 500);

//     if (searchValue === "") {
//       setAmazonResults([]);
//       setFlipkartResults([]);
//       return;
//     }

//     delayedFetchData(searchValue);

//     // Cleanup function to cancel the debounce timer
//     return delayedFetchData.cancel;
//   }, [searchValue]);

//   return (
//     <div>
//       <div>
//         <h3 style={{ margin: "auto", textAlign: "center" }}>Amazon</h3>
//         <div
//           style={{
//             display: "flex",
//             flexDirection: "column",
//             flexWrap: "nowrap",
//             justifyContent: "space-around",
//           }}
//         >
//           {amazonResults.map((result, index) => (
//             <div
//               key={index}
//               style={{
//                 border: "1px solid black",
//                 boxShadow: "1px 2px 9px black",
//                 display: "flex",
//                 alignItems: "center",
//                 flexBasis: "35%",
//                 margin: "15px",
//               }}
//             >
//               <img
//                 src={result.image_url}
//                 alt={result.name}
//                 width="100"
//                 height="100"
//               />
//               <div style={{ marginLeft: "1rem" }}>
//                 <div>{result.name}</div>
//                 <div>{result.price}</div>
//               </div>
//             </div>
//           ))}
//         </div>
//       </div>
//       <div>
//         <h3 style={{ margin: "auto", textAlign: "center" }}>Flipkart</h3>
//         <div style={{ display: "flex", flexDirection: "column" }}>
//           {flipkartResults.map((result, index) => (
//             <div
//               key={index}
//               style={{
//                 border: "1px solid black",
//                 boxShadow: "1px 2px 9px black",
//                 display: "flex",
//                 alignItems: "center",
//                 flexBasis: "35%",
//                 margin: "15px",
//               }}
//             >
//               <img
//                 src={result.image_url}
//                 alt={result.name}
//                 width="100"
//                 height="100"
//               />
//               <div style={{ marginLeft: "1rem" }}>
//                 <div>{result.name}</div>
//                 <div>{result.price}</div>
//               </div>
//             </div>
//           ))}
//         </div>
//       </div>
//       <div  className="form-btn">
//       <span onClick={fetchCheapestProduct}>Cheapest..</span>
//             </div>
//     </div>
//   );
// }

// export default SearchResults;

import React, { useState, useEffect } from "react";
import { debounce } from "lodash";

function SearchResults({ searchValue }) {
  const [amazonResults, setAmazonResults] = useState([]);
  const [flipkartResults, setFlipkartResults] = useState([]);
  const [cheapestProduct, setCheapestProduct] = useState(null);


  const fetchCheapestProduct = async () => {
    try {
      const response = await fetch(
        `http://localhost:5000/products/${searchValue}?cheapest_product=true`
      );
      const data = await response.json();
      setCheapestProduct(data);
    } catch (error) {
      console.error(error);
    }
  };

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
            <a
              target="_blank"
              key={index}
              href={result.product_url}
              style={{ textDecoration: "none" }}
            >
              <div
                style={{
                  padding: "20px",
                  boxShadow: "1px 2px 9px grey",
                  display: "flex",
                  alignItems: "center",
                  margin: "15px",
                  justifyContent: "space-between",
                }}
              >
                <div
                  style={{
                    display: "flex",
                    flexWrap: "nowrap",
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

                <button
                  onClick={() => alert("you have a favourite item")}
                  style={{
                    backgroundColor: "#AA98A9",
                    color: "white",
                    padding: "5px 5px 5px 5px",
                    border: "none",
                    borderRadius: "3px",
                    margin: "0 16px",
                    transition: "background-color 0.3s ease-in-out",
                  }}
                >
                  Add to Favorites
                </button>
              </div>
            </a>
          ))}
        </div>
      </div>
      <div>
        <h3 style={{ margin: "auto", textAlign: "center" }}>Flipkart</h3>
        <div
          style={{
            display: "flex",
            flexDirection: "column",
            flexWrap: "nowrap",
          }}
        >
          {flipkartResults.map((result, index) => (
            <a
              target="_blank"
              key={index}
              href={result.product_url}
              style={{ textDecoration: "none" }}
            >
              <div
                style={{
                  padding: "20px",
                  boxShadow: "1px 2px 9px grey",
                  display: "flex",
                  alignItems: "center",
                  margin: "15px",
                  justifyContent: "space-between",
                }}
              >
                <div
                  style={{
                    display: "flex",
                    flexWrap: "nowrap",
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

                <button
                  onClick={() => alert("you have a favourite item")}
                  style={{
                    backgroundColor: "#AA98A9",
                    color: "white",
                    padding: "5px 5px 5px 5px",
                    border: "none",
                    borderRadius: "3px",
                    margin: "0 16px",
                    transition: "background-color 0.3s ease-in-out",
                  }}
                >
                  Add to Favorites
                </button>
              </div>
            </a>
          ))}
        </div>
      </div>
      <center><button
        onClick={() => fetchCheapestProduct()}
        style={{
          backgroundColor: "#AA98A9",
          color: "white",
          padding: "5px 5px 5px 5px",
          border: "none",
          borderRadius: "3px",
          margin: "0 16px",
          transition: "background-color 0.3s ease-in-out",
        }}
      >
        show the cheapest
      </button>
        {cheapestProduct && (
          <div>
            <h3>Cheapest Product:</h3>
            <a
              target="_blank"
              style={{ textDecoration: "none" }}
              href={cheapestProduct.product_url}>
              <div style={{
                padding: "20px",
                boxShadow: "1px 2px 9px grey",
                display: "flex",

                margin: "15px",
                justifyContent: "space-between",
              }}>
                <div style={{
                  display: "flex",
                  flexWrap: "nowrap",
                }}>
                  <img
                    src={cheapestProduct.image_url}
                    alt={cheapestProduct.name}
                    width="100"
                    height="100"
                  />
                  <div style={{ marginLeft: "1rem" }}>
                    <div>{cheapestProduct.name}</div>
                    <div>{cheapestProduct.price}</div>
                  </div>


                </div>
                <button
                  onClick={() => alert("you have a favourite item")}
                  style={{
                    backgroundColor: "#AA98A9",
                    color: "white",
                    padding: "5px 5px 5px 5px",
                    border: "none",
                    borderRadius: "3px",
                    margin: "0 16px",
                    transition: "background-color 0.3s ease-in-out",
                  }}
                >
                  Add to Favorites
                </button>
              </div>
            </a>
          </div>
        )}
      </center>
    </div>
  );
}

export default SearchResults;
