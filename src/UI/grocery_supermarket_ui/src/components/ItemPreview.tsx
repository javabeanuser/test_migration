import React from "react";
import './../assets/scss/item-preview.scss'
import {ItemProps} from './../types/PropTypes'

export const ItemPreview = ({item}:ItemProps) => {
    return (
        <div className="item-preview">
            <div className="item-name">{item.name}</div>
            <img src={item.preview} alt="alt"></img>            
            <div className="item-price">{item.price+ ""}$</div>
            <button className="add-item-button">Add</button>            
        </div>
    )
}