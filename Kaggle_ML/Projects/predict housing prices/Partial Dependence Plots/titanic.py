import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor, GradientBoostingClassifier
from sklearn.ensemble.partial_dependence import partial_dependence, plot_partial_dependence
from sklearn.preprocessing import Imputer



titanic_data = pd.read_csv('../input/titanic/train.csv')

titanic_y = titanic_data.Survived

clf = GradientBoostingClassifier()

titanic_X_colns = ['PassengerId','Age', 'Fare']

titanic_X = titanic_data[titanic_X_colns]
my_imputer = Imputer()
imputed_titanic_X = my_imputer.fit_transform(titanic_X)

clf.fit(imputed_titanic_X, titanic_y)
titanic_plots = plot_partial_dependence(clf, features=[1,2], X=imputed_titanic_X,
                                        feature_names=titanic_X_colns, grid_resolution=8)
