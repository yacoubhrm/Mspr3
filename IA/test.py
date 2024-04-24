import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Importer les données depuis un fichier CSV
data = pd.read_csv("Data/datafromETL/RALL.csv", delimiter=",")
data2 = pd.read_csv("Data/datafromETL/R6only.csv", delimiter=",")
# Supprimer les lignes avec des valeurs manquantes
data = data.dropna()

# Diviser les données en données d'entraînement et de test en fonction du code département
X_train = data.drop(columns=['Voix','Code du département'])
y_train = data['Nom']
X_test = data2.drop(columns=['Voix','Code du département'])
y_test = data2['Nom']

# Initialiser le modèle RandomForestClassifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)

# Entraîner le modèle sur l'ensemble d'entraînement
rf_classifier.fit(X_train, y_train)

# Prédire les résultats sur les données du département 6
y_pred = rf_classifier.predict(X_test)

# Calculer la précision
accuracy = accuracy_score(y_test, y_pred)
print("Précision du modèle RandomForestClassifier :", accuracy)
