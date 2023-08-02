import React from 'react'
import {MenuProps} from './../types/PropTypes'
import {ItemPanel} from './../components/ItemPanel'

import "./../assets/scss/menu.scss"
export const Menu = ({menus}:MenuProps) =>{
    return( 
    <>
        <div className="menu"> 
            {   //@ts-ignore
                menus.map((menu, idx) => <div className="menu-button" key={menu.name} id={menu.name === 'Grocery' ? "menu-selected" : "menu-button"} key={menu.name} onClick={menu.handler}>{menu.name}</div>)

            }            
        </div>
        <ItemPanel items={menus[0].items}/>
    </>
    )
}