from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd
import pickle

house_data = {
    'SQ':[1000,1100,2300,1500,2000] ,
    'Room' : [3,1,2,4,6],
    'Price' :[300000,450000,600000,123680,760000]
}

data = pd.DataFrame(house_data)
model = LinearRegression()

X = data[['SQ','Room']]
y = data[['Price']]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2, random_state=42)

model.fit(X_train,y_train)
with open('house_model.pkl', 'wb') as f:
    pickle.dump(model, f)