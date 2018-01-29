import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import Imputer
from sklearn.model_selection import cross_val_score

data = pd.read_csv('../input/titanic/melb_data.csv')
cols_to_use = ['Rooms', 'Distance', 'Landsize', 'BuildingArea', 'YearBuilt']
X = data[cols_to_use]
y = data.Price

my_pipeline = make_pipeline(Imputer(), RandomForestRegressor())
scores = cross_val_score(my_pipeline, X, y, scoring='neg_mean_absolute_error')
print(scores)


print('Mean Absolute Error %2f' %(-1 * scores.mean()))