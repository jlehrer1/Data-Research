import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import cross_val_score, cross_validate
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE
from sklearn.neighbors import KNeighborsClassifier
from sklearn.decomposition import PCA

train = pd.read_csv('train_clean.csv')
test = pd.read_csv('test_clean.csv')
train.head()

def has_cabin(x):
    if pd.isna(x):
        return 0
    else:
        return 1

print(train.columns)
print(train.head(), train.tail())

def pre_process(dataset): #Make dummies for categorial variables, drop irrelevant categories by feature selection
    dataset = pd.get_dummies(dataset, columns = ['Sex'], drop_first = True)
    dataset['HasCabin'] = dataset['Cabin'].apply(has_cabin)
    dataset.drop(['Embarked', 'Cabin', 'Name', 'Ticket', 'Title'], inplace = True, axis = 1)
    return dataset

train = pre_process(train)
X_test = pre_process(test)

y_train = train['Survived']
X_train = train.drop('Survived', axis=1)

model = GradientBoostingClassifier(learning_rate=.01)
model.fit(X_train, y_train)

print(len(X_train.columns))
scores = cross_val_score(model, X_train, y_train, cv=10, scoring='accuracy')

print(np.mean(scores))

