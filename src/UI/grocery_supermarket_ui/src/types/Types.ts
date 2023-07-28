
export type Item = {
    id: number,
    count: number,
    name: string,
    preview: string,
    price: number,
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