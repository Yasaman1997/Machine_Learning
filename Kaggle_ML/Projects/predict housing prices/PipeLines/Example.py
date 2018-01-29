from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import Imputer
import pandas as pd
from sklearn.model_selection import train_test_split




# Read Data
data = pd.read_csv('../input/pipeline/melb_data.csv')
cols_to_use = ['Rooms', 'Distance', 'Landsize', 'BuildingArea', 'YearBuilt']
X = data[cols_to_use]
y = data.Price
train_X, test_X, train_y, test_y = train_test_split(X, y)



my_pipeline= make_pipeline(Imputer(),RandomForestRegressor())
my_pipeline.fit(train_X,train_y)
predictions=my_pipeline.predict(test_X)