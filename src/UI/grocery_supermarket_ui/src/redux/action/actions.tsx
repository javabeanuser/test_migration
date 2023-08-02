import { Item } from "../../types/Types";

export const ADD_TO_CART = 'ADD_TO_CART'
export const REMOVE_FROM_CART = 'REMOVE_FROM_CART'
export const REMOVE_ITEM_FROM_CART = 'REMOVE_ITEM_FROM_CART'

export const addToCart = (item: Item) => {
   return {
      type: ADD_TO_CART,
      item: item
   };
}

export const removeFromCart = (item: Item) => {
   return {
      type: REMOVE_FROM_CART,
      item: item
   };
}

export const removeItemFromCart = (item: Item) => {
   return {
      type: REMOVE_ITEM_FROM_CART,
      item: item
   };
}