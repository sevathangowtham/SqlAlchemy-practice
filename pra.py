# requerd libraries 
from sqlalchemy import create_engine,Column,Integer,String,ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.orm import declarative_base

engine  = create_engine('sqlite:///database.db', echo=False)
Session = sessionmaker(bind=engine)
Base = declarative_base()
session = Session()

class User(Base):
    __tablename__ = 'users'
    Id = Column(Integer, primary_key = True)
    Name = Column(String, nullable = False)
    Email = Column(String, nullable = False, unique =  True)
    Gender = Column(String, nullable = False)
    #user_id = Column(Integer, ForeignKey('products.Id'), nullable = False)
    #task = relationship('Product', back_populates='user', cascade='all, delete-orphan')
#product table
class Product(Base):
    __tablename__ = 'products'
    Id = Column(Integer, primary_key = True)
    ProductName = Column(String, nullable = False)
    Brand = Column(String, nullable = False)
    Quantity = Column(Integer, nullable = False)
    #Product_Id = Column(ForeignKey('users.Id'), nullable = False)
    #user = relationship('User', back_populates='task')
Base.metadata.create_all(engine)

def add_user():
    name = input("Enter your name: ")
    email = input("Enter your email: ") 
    gender = input("Enter your gender: ")
    user = User(Name=name, Email=email, Gender=gender)
    session.add(user)
    session.commit()


def add_product():
    product_name = input('Enter the product name :').strip()
    brand = input('Enter the brand name : ').strip()
    quantity = int(input('Enter the quantity Product: ').strip())
    product = Product(ProductName=product_name, Brand=brand, Quantity=quantity)
    session.add(product)
    session.commit()
print(session.query(Product).all())
result1 = session.query(User).all()
for pro in result1:
    print(f"Name: {pro.Name}, Email: {pro.Email}, Gender: {pro.Gender}")
result = session.query(Product).all()
for pro in result:
    print(f"Product Name: {pro.ProductName}, Brand: {pro.Brand}, Quantity: {pro.Quantity}")

def update_user():
    user_id = int(input('Enter the user ID to update:'))
    user = session.query(User).filter_by(Id=user_id).first()
    if user:
        name = input('Enter the new name: ')
        email = input('Enter the new email: ')
        gender = input('Enter the new gender: ')
        user.Name = name
        user.Email = email
        user.Gender = gender
        session.commit()
        print('User updated successfully')
    else:
        print('user not found!')
def update_product():
    product_id = int(input('Enter the product ID to update:'))
    product = session.query(Product).filter_by(Id = product_id).first()
    if product:
        product_name = input('Enter the new prduct name:').strip()
        brand = input('Enter the new brand name:').strip()
        quantity =int(input('Enter the new quantity: '))
        product.ProductName = product_name
        product.Brand = brand
        product.Quantity = quantity
        session.commit()
        print('Product updated successfully')
    else:
        print('Product Not found!')
def delete_user():
    user_id = int(input('Enter the user ID to delete:'))
    user = session.query(User).filter_by(Id = user_id).first()
    if user:
        session.delete(user)
        session.commit()
        print('User deleted successfully')
    else:
        print('User not found!')

def delete_product():
    product_id = int(input('Enter the product id to delete'))
    product = session.query(Product).filter_by(Id = product_id).first()
    if product :
        session.delete(product)
        session.commit()
        print('Product deleted successsfuly!')
    else:
        print('Product not found!')