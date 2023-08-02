import React from "react";
import { useNavigate } from "react-router-dom";
import {AppState} from './../types/Types'
import './../assets/scss/header.scss';

import {
  useSelector
} from 'react-redux'

export const Header = () => {
  const navigate = useNavigate();
  const count = useSelector<AppState, Number>(state => state.payload.cart.count)
    return (
      <div className="header">
        <div className="header-logo" onClick={() => navigate('/')}>LOGO</div>
        <input type="search" className="header-search"></input>
        <div className="header-search-button"/>
        <div className="header-shopping-cart" onClick={() => navigate('/cart')}>{count.toString()}</div>
      </div>
    );
  }