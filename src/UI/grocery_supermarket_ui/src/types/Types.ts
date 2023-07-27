
export type Item = {
    id: Number,
    name: string,
    preview: string,
    price: Number,
    description: string
}

export type Menu = {
    name: string, 
    items: Array<Item>,
    handler: React.MouseEventHandler
}

export type AppState = {    
    payload: {
        cart: {
            count: Number,
            items: Array<Item>        
        }        
    }
}