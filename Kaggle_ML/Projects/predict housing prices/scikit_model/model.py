import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

main_file_path = "train.csv"
data = pd.read_csv(main_file_path)

#data = data.dropna(axis=0)
print(data.columns)

y = data.SalePrice

predictors = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']

x = data[predictors]  # ???????

# define model
model = DecisionTreeRegressor()

# fit model
model.fit(x, y)

print("Making predictions for the following 5 houses:")
print(x.head())
print("The predictions are:")
print(model.predict(x.head()))

# The calculation of mean absolute error
print("MAER:")
predicted = model.predict(x)
print(mean_absolute_error(y, predicted))


