import tensorflow as tf
import pandas as pd
from sklearn.model_selection import cross_val_score


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

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(16, activation="relu"),
    # tf.keras.layers.Dense(25, activation="relu"),
    tf.keras.layers.Dense(16, activation="softmax")
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(X_train.values, y_train.values, epochs=50)
# scores = cross_val_score(model, X_train, y_train, cv = 10, scoring = 'accuracy')
