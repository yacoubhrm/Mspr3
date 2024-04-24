from sklearn.svm import SVC  # Importer le modèle SVM (Support Vector Machine)
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

# Importer les données depuis un fichier CSV
data = pd.read_csv("Data/datafromETL/RALL.csv", delimiter=",")

# Afficher les types de données des colonnes
print(data.dtypes)

# Supprimer les lignes avec des valeurs manquantes
data = data.dropna()

# Sélectionner les variables explicatives et la variable cible
X = data.drop(columns=['Voix','Code du département'])
y = data['Nom']

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialiser le modèle SVM
svm_classifier = SVC(kernel='rbf', random_state=42)  # Nous utilisons le noyau RBF (Radial Basis Function)

# Entraîner le modèle
svm_classifier.fit(X_train, y_train)

# Prédire les résultats
y_pred = svm_classifier.predict(X_test)

# Calculer la précision
accuracy = accuracy_score(y_test, y_pred)
print("Précision du modèle SVM :", accuracy)