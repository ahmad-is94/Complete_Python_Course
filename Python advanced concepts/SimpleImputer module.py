import numpy as nmp
# Importing SimpleImputer class from sklearn impute module
from sklearn.impute import SimpleImputer
# Setting up imputer function variable
imputerFunc = SimpleImputer(missing_values = nmp.nan, strategy ='mean')
# Defining a dataset
dataSet = [[32, nmp.nan, 34, 47], [17, nmp.nan, 71, 53], [19, 29, nmp.nan, 79], [nmp.nan, 31, 23, 37], [19, nmp.nan, 79, 53]]
# Print original dataset
print("The Original Dataset we defined in the program: \n", dataSet)
# Imputing dataset by replacing missing values
imputerFunc = imputerFunc.fit(dataSet)
dataSet2 = imputerFunc.transform(dataSet)
# Printing imputed dataset
print("The imputed dataset after replacing missing values from it: \n", dataSet2)