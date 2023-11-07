from AppPhone.app import  db,app
from sqlalchemy import Column,Integer,String,Float,ForeignKey
from sqlalchemy.orm import relationship
class Category(db.Model):
    __tablename__ ='category'


    id= Column(Integer,primary_key=True,autoincrement=True)
    name= Column(String(50), nullable=False, unique=True)
    products = relationship('Product', backref='category', lazy=True)


class Product(db.Model):
 __tablename__ = 'product'
 id = Column(Integer, primary_key=True, autoincrement=True)
 name = Column(String(50), nullable=False)
 price = Column(Float, default=0)
 image = Column(String(1000))
 category_id = Column(Integer,ForeignKey(Category.id), nullable=False)


if __name__ == '__main__':
    with app.app_context():
        # c1= Category(name='Mobile')
        # c2= Category(name='Talet')
        # c1= Product(name='Talet Note 2',price=10000000,image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg',category_id=2)
        # c2= Product(name='Ipad Pro',price=15000000,image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg',category_id=2)
        # c3= Product(name='Iphone 7',price=3000000,image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg',category_id=1)
        c4= Product(name='Iphone 12',price=3000000,image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg',category_id=1)

        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.add(c3)
        db.session.add(c4)
        db.session.commit()
        #  db.create_all()

