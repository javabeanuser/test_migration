// import { combineReducers } from 'redux'
import { ADD_TO_CART } from '../action/actions'
import { AppState } from '../../types/Types'

const initMarketState: AppState = {   
   payload: {
      cart: {
         count:0,
         items:[]
      }
   }
}

export function marketApp(state: AppState = initMarketState, action: any) {

    switch (action.type) {
       case ADD_TO_CART:
          const arr = state.payload.cart.items
          arr.push(action.item)
          return {
               ...state,
               payload: {
                  cart :{
                     count: arr.length,
                     items: arr
                  }
               }              
          }
       default:
          return state
    }
 }