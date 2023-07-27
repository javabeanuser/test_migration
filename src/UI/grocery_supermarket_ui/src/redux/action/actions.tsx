import { Item } from "../../types/Types";

export const ADD_TO_CART = 'ADD_TO_CART'

export const addToCart = (item: Item) => {
   return {
      type: ADD_TO_CART,
      item: item
   };
}