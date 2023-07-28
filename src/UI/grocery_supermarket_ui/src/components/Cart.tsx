import React, { SyntheticEvent, useEffect } from "react";
import { useDispatch } from "react-redux";
import { Header } from "./Header";
import { useSelector } from "react-redux";
import { AppState, Item } from "../types/Types";
import './../assets/scss/cart.scss'
import { addToCart, removeFromCart, removeItemFromCart } from "../redux/action/actions";

export const Cart  = () =>{
    const {count, items} = useSelector<AppState, any>(state => state.payload.cart)
    const dispatch = useDispatch() 

    useEffect(()=>{}, [count])
    const inputChangeHandler = (e: SyntheticEvent, item: Item) =>{
        const input  = e.target as HTMLInputElement
        console.log('minus')
        if (Number(item.count) > Number(input.value) &&  Number(item.count) > 1){
             dispatch(removeItemFromCart(item))
        } else {
            dispatch(addToCart(item))
        }
        
    }
    return(
        <>
            <Header/>   
            <hr className='horizontal-line'/>   
            <div className='cart-title'>My Cart</div>         
            <div className='cart-page'>                
                <div className='cart-items'>
                    { items.length > 0 ?
                    items.map( (item: Item) => {
                        return (
                        <div className='cart-item'>
                            <div className="fixed">
                                <img className='cart-item-preview' src={item.preview} alt="preview"></img>
                            </div>
                            <div className="fixed">
                                <div className="bold">{item.name}</div>
                            </div>
                            <div className="fixed">
                                <div className="bold">Each</div>
                                <div>${item.price.toString()}</div>
                            </div>
                            <div className="fixed">
                                <div className="bold">Quantity</div>
                                <input id="number" type="number" defaultValue={item.count} min="1" max="1000" onChange={(e)=>inputChangeHandler(e, item)}/>
            
                            </div>
                            <div className="fixed">
                                <div className="bold">Total</div>
                                <div>{item.price * item.count}</div>
                            </div>
                            <div className="cart fixed">
                                <div>&nbsp;</div>
                                <button className='cart-item-remove-button' onClick={()=> {dispatch(removeFromCart(item))}}>Remove</button>
                            </div>
                        </div>)
                        })                        
                    : <div className="x-center-y">Your Cart is Empty :(</div>
                    }
                    
                </div>
                <div className='cart-order'>
                    <div>
                        <div>
                            <input></input>
                            <button>Submit</button>
                        </div>
                    </div>
                    <div>
                        <div className="flex-in-line ">
                            <div>Shipping Cost</div>
                            <div>0</div>
                        </div>
                        <div className="flex-in-line">
                            <div>Discount</div>
                            <div>0</div>
                        </div>
                        <div className="flex-in-line">                            
                            <div>Tax</div>
                            <div>0</div>
                        </div>
                        <div className="flex-in-line">                            
                            <div className="bold">Total</div>
                            <div className="bold">0</div></div>
                        </div>
                    <div className="checkout-button">Checkout</div>
                </div>
            </div>
        </>
    )
}