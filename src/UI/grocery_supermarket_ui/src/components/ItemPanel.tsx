import React from "react";
import { ItemPreview } from "./ItemPreview";
import {ItemPanelProps} from './../types/PropTypes'
import './../assets/scss/item-panel.scss'

export const ItemPanel = ({items}:ItemPanelProps) =>{
    return (
        <div className="item-panel">
            {items.map(item => <ItemPreview key={item.id} item={item}/>)}
        </div>
    )
}