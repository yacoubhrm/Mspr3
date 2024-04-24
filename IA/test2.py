import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score

# Charger les données
data = pd.read_csv("Data/datafromETL/resultat_joined_prepared.csv", delimiter=",")

# Supprimer les espaces blancs supplémentaires des noms de colonnes
data.columns = data.columns.str.strip()

# Supprimer les colonnes non pertinentes ou redondantes
data.drop(['Code de la circonscription', 'Libellé de la circonscription', 'Code de la commune', 'Libellé de la commune', 'Code du b.vote', 'Prénom', '% Voix/Ins', '% Voix/Exp.1'], axis=1, inplace=True)

# Convertir les variables catégorielles en variables indicatrices (dummy variables) si nécessaire
data = pd.get_dummies(data)

# Diviser les données en ensemble d'entraînement et ensemble de test
X = data.drop(['Voix', 'Nom'], axis=1)  # Features
y = data['Nom']  # Target variable
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialiser le modèle Random Forest
rf_classifier = RandomForestClassifier(random_state=42)

# Définir la grille de recherche des hyperparamètres
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10]
}

# Recherche par grille pour trouver les meilleurs hyperparamètres
grid_search = GridSearchCV(rf_classifier, param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)

# Meilleurs paramètres
print("Meilleurs paramètres :", grid_search.best_params_)
print("Meilleur score :", grid_search.best_score_)

# Prédire les résultats sur l'ensemble de test
y_pred = grid_search.predict(X_test)

# Calculer la précision
accuracy = accuracy_score(y_test, y_pred)
print("Précision du modèle Random Forest Classifier :", accuracy)
