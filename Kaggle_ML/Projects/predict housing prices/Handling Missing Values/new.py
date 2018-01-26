import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import Imputer

# read data
train = pd.read_csv('train.csv')
# print(train.columns)


print(train.isnull().sum())

# make copy to avoid changing original data (when Imputing)
new_train=train.copy
train_data_without_missing_values = new_train.dropna(axis=1)
print(train_data_without_missing_values.isnull().sum())


# make new columns indicating what will be imputed
cols_with_missing = (col for col in new_train.columns
                                 if new_train[c].isnull().any())
for col in cols_with_missing:
    new_train[col + '_was_missing'] = new_train[col].isnull()

# Imputation
my_imputer = Imputer()
new_data = my_imputer.fit_transform(new_train)
data_with_imputed_values = my_imputer.fit_transform(train)




# Read the test data
test = pd.read_csv('test.csv')


#print(test.isnull().sum())
#test_data_without_missing_values = train.dropna(axis=1)


