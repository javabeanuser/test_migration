import React from "react";
import './../assets/scss/item-preview.scss'
import {ItemProps} from './../types/PropTypes'
import {addToCart} from './../redux/action/actions'

import {
    useSelector, 
    useDispatch
} from 'react-redux'

export const ItemPreview = ({item}:ItemProps) => {
    const dispatch = useDispatch() 
    return (
        <div className="item-preview">
            <div className="item-name">{item.name}</div>
            <img src={item.preview} alt="alt"></img>            
            <div className="item-price">{item.price+ ""}$</div>
            <button className="add-item-button" onClick={()=> {dispatch(addToCart(item))}}>Add</button>            
        </div>
    )
}