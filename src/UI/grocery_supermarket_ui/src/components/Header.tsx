import React from "react";
import {AppState} from './../types/Types'
import './../assets/scss/header.scss';

import {
  useSelector
} from 'react-redux'

export const Header = () => {
  const count = useSelector<AppState, Number>(state => state.payload.cart.count)
    return (
      <div className="header">
        <input type="search" className="header-search"></input>
        <div className="header-search-button"/>
        <div className="header-shopping-cart" >{count.toString()}</div>
      </div>
    );
  }