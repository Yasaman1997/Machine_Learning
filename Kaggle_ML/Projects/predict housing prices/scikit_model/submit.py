import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# read data
train = pd.read_csv('train.csv')
# print(train.columns)

# pull data
train_y = train.SalePrice
predictor_cols = ['LotArea', 'OverallQual', 'YearBuilt', 'TotRmsAbvGrd']

# create trainnig prediction data
train_x = train[predictor_cols]

# model
my_model = RandomForestRegressor()
my_model.fit(train_x, train_y)

# Read the test data
test = pd.read_csv('test.csv')

# Treat the test data in the same way as training data. In this case, pull same columns.
test_X = test[predictor_cols]
# Use the model to make predictions
predicted_prices = my_model.predict(test_X)

# We will look at the predicted prices to ensure we have something sensible.
print(predicted_prices)

my_submission = pd.DataFrame({'Id': test.Id, 'SalePrice': predicted_prices})

# you could use any filename. We choose submission here
my_submission.to_csv('submission.csv', index=False)
