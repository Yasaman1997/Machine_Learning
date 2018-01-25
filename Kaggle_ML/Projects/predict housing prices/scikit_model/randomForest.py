from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

main_file_path = "train.csv"
data = pd.read_csv(main_file_path)

#data = data.dropna(axis=0)
#print(data.columns)

y = data.SalePrice

predictors = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']

x = data[predictors]  # ???????

# define model
model = DecisionTreeRegressor()

# split data into training and validation data, for both predictors and target
# The split is based on a random number generator. Supplying a numeric value to
# the random_state argument guarantees we get the same split every time we
# run this script.
train_x, val_x, train_y, val_y = train_test_split(x, y, random_state=0)
model.fit(train_x, train_y)

val_prediction = model.predict(val_x)
print(mean_absolute_error(val_prediction, val_y))



forest_model = RandomForestRegressor()
forest_model.fit(train_x, train_y)
predicts = forest_model.predict(val_x)
print("forest error:")
print(mean_absolute_error(val_y, predicts))


