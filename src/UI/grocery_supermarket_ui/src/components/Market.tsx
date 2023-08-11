import React, {useEffect, useState} from 'react';
import {Header} from './Header'
import {Ribbon} from './Ribbon'
import {Menu} from './Menu'
import {Menu as MenuType} from '../types/Types'
import "./../assets/scss/application.scss"

export function Market() {
  const [menus, setMenus] = useState([])
  const [loaded, setLoaded] = useState(false)
    useEffect(() => {
      fetch("/api/grocery/init").then((res) =>
          res.json().then((data) => {    
            setMenus(data.data)
            setLoaded(true)
          })
      );
  }, []);
 

  return (
    <div className='application'>
      <Header/>
      <hr className='horizontal-line'/>
      <Ribbon/>
      { loaded ?
        <Menu menus={menus}/>  
        : null
      }
      
    </div>
  );
}
