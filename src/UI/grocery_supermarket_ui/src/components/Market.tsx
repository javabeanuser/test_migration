import React from 'react';
import {Header} from './Header'
import {Ribbon} from './Ribbon'
import {Menu} from './Menu'
import "./../assets/scss/application.scss"

import {menus} from "../js/MockData"

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
