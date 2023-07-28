import {Item, Menu} from "../types/Types"

const strawberry:Item  ={
    id: 1,
    count: 1,
    name: 'Strawberry',
    preview: "https://st.depositphotos.com/1034300/1353/i/600/depositphotos_13532977-stock-photo-strawberry-fruit-food.jpg",
    price: 20,
    description: "description"
}

const potato:Item  ={
    id: 2,
    count: 1,
    name: 'Potato',
    preview: "https://img.freepik.com/premium-photo/fresh-potatoes-isolated-white-background_33736-2512.jpg",
    price: 2,
    description: "description"
}

const cheese:Item  ={
    id: 3,
    count: 1,
    name: 'Cheese',
    preview: "https://s3.envato.com/files/339589108/0G2A2360.jpg",
    price: 15,
    description: "description"
}
const meat:Item  ={
    id: 4,
    count: 1,
    name: 'Meat',
    preview: "https://s3.envato.com/files/271476500/IMG_1193.jpg",
    price: 10,
    description: "description"
}
const egs:Item  ={
    id: 5,
    count: 1,
    name: '10 Egs',
    preview: "https://thumbs.dreamstime.com/z/three-eggs-white-background-30662497.jpg",
    price: 1,
    description: "description"
}
const carrot:Item  ={
    id: 6,
    count: 1,
    name: 'Carrot',
    preview: "https://as1.ftcdn.net/v2/jpg/02/99/43/48/1000_F_299434842_UF1e0k44KUpkdtAEu0XbbPVnTHFuRwAm.jpg",
    price: 5,
    description: "description"
}
const tomato:Item  ={
    id: 7,
    count: 1,
    name: 'Tomato',
    preview: "https://previews.123rf.com/images/spamas/spamas1909/spamas190900328/130747578-tomato-isolated-on-white-background-full-depth-of-field.jpg",
    price: 8,
    description: "description"
}
const orange:Item  ={
    id: 8,
    count: 1,
    name: 'Orange',
    preview: "https://www.wallpapers4u.org/wp-content/uploads/oranges_citrus_white_background_leaf_half_segment_44585_1920x1080-450x253.jpg",
    price: 3,
    description: "description"
}
const raspberry:Item  ={
    id: 9,
    count: 1,
    name: 'Raspberry',
    preview: "https://t3.ftcdn.net/jpg/03/66/09/44/360_F_366094484_u1mrluXyjFdzC6OXhJ82weQvvMbk47Ho.jpg",
    price: 3,
    description: "description"
}
const blueberry:Item  ={
    id: 10,
    count: 1,
    name: 'Blueberry',
    preview: "https://img.freepik.com/premium-photo/fresh-blueberry-isolated-white-background-full-depth-field_253984-6646.jpg?w=2000",
    price: 3,
    description: "description"
}












const Grocery:Menu = {
    name: "Grocery",
    items: [strawberry,potato, cheese,meat,egs,carrot,tomato,orange,raspberry,blueberry],
    handler: ()=>{}
}

const Strawberry:Menu = {
    name: "Strawberry",
    items:[strawberry,potato],
    handler: ()=>{}
}

const House:Menu = {
    name: "House",
    items: [strawberry,potato],
    handler: ()=>{}
}

const Car:Menu = {
    name: "Car",
    items: [strawberry,potato],
    handler: ()=>{}
}

const Household:Menu = {
    name: "Household",
    items: [strawberry,potato],
    handler: ()=>{}
}

export const menus = [Grocery, Strawberry, House,Car,Household]