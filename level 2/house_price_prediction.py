import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

df = pd.read_csv("house_prices.csv")

X = df[['Area', 'Bedrooms', 'Bathrooms']]
y = df['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Predicted Prices:", predictions)

print("Mean Squared Error:", mean_squared_error(y_test, predictions))