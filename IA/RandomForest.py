import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Import
data = pd.read_csv("Data/datafromETL/R.csv", delimiter=",")

# voir les type data
print(data.dtypes)

# delete if null
data = data.dropna()

# variable explicative et cible
X = data.drop(columns=['Voix','Code du département'])
y = data['Nom']

# division entre trainn et test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# initialise le model randomforest
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)

# train model
rf_classifier.fit(X_train, y_train)

# predire
y_pred = rf_classifier.predict(X_test)

# accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Précision du modèle RandomForestClassifier :", accuracy)
