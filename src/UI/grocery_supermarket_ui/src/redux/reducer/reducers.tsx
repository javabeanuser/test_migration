// import { combineReducers } from 'redux'
import { ADD_TO_CART, REMOVE_FROM_CART, REMOVE_ITEM_FROM_CART } from '../action/actions'
import { AppState, Item } from '../../types/Types'

const initMarketState: AppState = {
   payload: {
      cart: {
         count: 0,
         items: [],
         sum: 0
      }
   }
}

function sortItems(arr:Array<Item>){
   return arr.sort((a:Item,b:Item) => {
      if (a.id < b.id) return -1;
      if (a.id > b.id) return 1;
      return 0;
   })
}

export function marketApp(state: AppState = initMarketState, action: any) {
   let arr: Array<Item>
   switch (action.type) {
      case ADD_TO_CART:
         arr = state.payload.cart.items
         for (let item of arr) {
            if (item.id === action.item.id) {
               action.item = { ...action.item, count: item.count + 1 }
               arr = arr.filter(item => item.id !== action.item.id)
            }
         }
         arr.push(action.item)
         sortItems(arr)
         return {
            ...state,
            payload: {
               cart: {
                  count: arr.reduce((accumulator, item) => accumulator + item.count,0),
                  items: arr,
                  sum:   arr.reduce((sum,cur)=>sum+(cur.count*cur.price),0)
               }
            }
         }
      case REMOVE_FROM_CART:
         arr = state.payload.cart.items
         arr = arr.filter(item => item.id !== action.item.id)
         sortItems(arr)
         return {
            ...state,
            payload: {
               cart: {
                  count: arr.reduce((accumulator, item) => accumulator + item.count,0),
                  items: arr,
                  sum:   arr.reduce((sum,cur)=>sum+(cur.count*cur.price),0)
               }
            }
         }
      case REMOVE_ITEM_FROM_CART:
         arr = state.payload.cart.items
         for (let item of arr) {
            if (item.id === action.item.id) {
               action.item = { ...action.item, count: item.count - 1 }
               arr = arr.filter(item => item.id !== action.item.id)
            }
         }
         arr.push(action.item)
         sortItems(arr)
         return {
            ...state,
            payload: {
               cart: {
                  count: arr.reduce((accumulator, item) => accumulator + item.count,0),
                  items: arr,
                  sum:   arr.reduce((sum,cur)=>sum+(cur.count*cur.price),0)
               }
            }
         }
      default:
         return state
   }
}