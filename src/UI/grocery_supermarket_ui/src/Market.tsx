import React from 'react';
import {Header} from './components/Header'
import {Ribbon} from './components/Ribbon'
import {Menu} from './components/Menu'
import "./assets/scss/application.scss"

import {menus} from "./js/MockData"

export function Market() {
  return (
    <div className='application'>
      <Header/>
      <hr className='horizontal-line'/>
      <Ribbon/>
      <Menu menus={menus}/>  
    </div>
  );
}
