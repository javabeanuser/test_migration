import React, {useState} from "react";
import './../assets/scss/header.scss';

export const Header = () => {
  const [shoppingCart, setShoppingCart] = useState(0)
    return (
      <div className="header">
        <input type="search" className="header-search"></input>
        <div className="header-search-button"/>
        <div className="header-shopping-cart" onClick={()=> (setShoppingCart(shoppingCart+1))}>{shoppingCart}</div>
      </div>
    );
  }