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


if __name__ == '__main__':
    app.run(debug=True)
