export type RibbonProps = {
    images: Array<string>
}

export type MenuProps = {
    menus:  Array<Menu>
}

export type Menu = {
    name: string, 
    items: Array<Item>,
    handler: React.MouseEventHandler
}


export type ItemPanelProps = {
    items: Array<Item>
}

export type ItemProps = {
    item:Item
}

export type Item = {
    name: string,
    preview: string,
    price: Number,
    description: string
}

