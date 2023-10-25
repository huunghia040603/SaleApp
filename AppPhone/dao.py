def get_categories():
    return [{
        "id":1,
        "name":"Mobile"
    },{
        "id":1,
        "name":"Tablet"
    }]
def get_products(kw):
    products= [{
        "id": 1,
        "name": "Iphone 12",
        "price": 15000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg"
    }, {
        "id": 2,
        "name": "Iphone 15",
        "price": 35000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg"
    },{
        "id": 3,
        "name": "Tablet Mini",
        "price": 20000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg"
    }]
    if kw:
        products =[p for p in products if p['name'].find(kw)>=0]
    return products

