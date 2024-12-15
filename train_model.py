import pickle
from sklearn.ensemble import RandomForestRegressor
import pandas as pd

# Your dataset
df = pd.read_csv('kc_house_data.csv', delimiter=';')  # Adjust the path as needed
print(df.columns)
features = ['sqft_living', 'bedrooms', 'bathrooms', 'sqft_above', 'sqft_living15', 'grade']


target = 'price'

X = df[features]
y = df[target]

# Initialize the model
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Train the model
model.fit(X, y)

# Save the trained model to a file
with open('models/model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Model saved successfully.")
