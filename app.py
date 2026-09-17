from sqlalchemy import create_engine, Integer,String,ForeignKey,Column
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from flask import Flask,request


engine = create_engine('sqlite:///database.db',echo = False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

#create the user class 
class User(Base):
    __tablename__  = 'users'
    Id = Column(Integer,primary_key=True)
    Name = Column(String,nullable=False)
    Email =  Column(String, unique=True)
    Gender = Column(String,nullable=False)

# Create Product class

class Product(Base):
    __tablename__ = 'products'
    Id = Column(Integer, primary_key = True)
    ProductName = Column(String, nullable = False)
    Brand = Column(String, nullable = False)
    Quantity = Column(Integer, nullable = False)

Base.metadata.create_all(engine)

#Flack
app = Flask(__name__)

@app.route('/')
def home():
    return('Wellcome to our application!')

@app.route('/add_user', methods=['POST'])
def add_user_api():
    data = request.json
    name = data['name']
    email = data['email']
    gender = data['gender']
    user = User(Name=name, Email=email, Gender=gender)
    session.add(user)
    session.commit()
    return {"message": "User added successfully"}

@app.route('/add_product',methods = ['POST'])
def add_product_api():
    data1 = request.json
    productname= data1['productname']
    brand = data1['brand']
    quantity = data1['quantity']
    product = Product( ProductName =productname, Brand = brand, Quantity = quantity)
    session.add(product)
    session.commit()
    return {'Message' : 'Product added successfully!' }

@app.route('/view_user', methods = ['GET'])
def view_user_api():
    result = session.query(User).all()
    all_user =[]
    for re in result:
        all_user.append ({'ID ' : re.Id , 'Name' : re.Name , 'Email': re.Email , 'Gender': re.Gender})
    return {'Users ': all_user}

@app.route('/view_product', methods = ['GET'])
def view_product_api():
    pr_result = session.query(Product).all()
    all_product = []
    for P in pr_result:
        all_product.append({'ID' : P.Id , 'Product Name' : P.ProductName,'Brand' : P.Brand, 'quanity' : P.Quantity})
    return {"Product's": all_product}




if __name__ == '__main__':
    app.run(debug=True)
