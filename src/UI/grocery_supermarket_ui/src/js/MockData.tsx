import {Item, Menu} from "../types/Types"

const item:Item  ={
    id: 1,
    name: 'Strawberry',
    preview: "https://st.depositphotos.com/1034300/1353/i/600/depositphotos_13532977-stock-photo-strawberry-fruit-food.jpg",
    price: 20,
    description: "description"
}

const Grocery:Menu = {
    name: "Grocery",
    items: [item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item],
    handler: ()=>{}
}

const Strawberry:Menu = {
    name: "Strawberry",
    items: [item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item],
    handler: ()=>{}
}

const House:Menu = {
    name: "House",
    items: [item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item],
    handler: ()=>{}
}

const Car:Menu = {
    name: "Car",
    items: [item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item],
    handler: ()=>{}
}

const Household:Menu = {
    name: "Household",
    items: [item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item,item],
    handler: ()=>{}
}

export const menus = [Grocery, Strawberry, House,Car,Household]