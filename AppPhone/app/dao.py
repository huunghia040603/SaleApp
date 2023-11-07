from AppPhone.app import db
from AppPhone.app.models import Product,Category
def get_categories():
    return db.session.query(Category).all()
def get_products(kw):
    products=db.session.query(Product).all()
    if kw:
        products =db.session.query(Product).filter(Product.name.contains(kw))
    return products


