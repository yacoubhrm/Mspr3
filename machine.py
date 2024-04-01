import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Chargement des données sur les tendances de vote dans toute la France
france_data = pd.read_csv("france_election_data.csv")

# Chargement des données spécifiques au département pour lequel vous souhaitez prédire les résultats
departement_data = pd.read_csv("departement_election_data.csv")

# Prétraitement des données si nécessaire (normalisation, gestion des données manquantes, etc.)

# Séparation des caractéristiques (X) et des étiquettes (y) pour l'ensemble de la France
X_france = france_data.drop('Vote', axis=1)
y_france = france_data['Vote']

# Initialisation du modèle RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)

# Entraînement du modèle sur l'ensemble de la France
model.fit(X_france, y_france)

# Utilisation du modèle pour prédire les électeurs potentiels pour chaque tendance politique dans le département spécifique
departement_potential_voters = model.predict(departement_data)

# Prédiction des résultats des élections départementales du premier tour dans ce département
# (en fonction des électeurs potentiels pour chaque tendance politique)
# Vous pouvez implémenter cette étape en fonction des règles spécifiques de votre modèle

# Évaluation des performances du modèle en comparant les prédictions aux résultats réels des élections dans le département
# Utilisez une métrique d'évaluation appropriée, par exemple l'exactitude (accuracy)
# Assurez-vous d'utiliser les données de test appropriées pour cette évaluation

# Diviser les données spécifiques au département en ensembles d'entraînement et de test
X_dep_train, X_dep_test, y_dep_train, y_dep_test = train_test_split(X_france, y_france, test_size=0.2, random_state=42)

# Faire des prédictions sur l'ensemble de test
predictions = model.predict(X_dep_test)

# Évaluer les performances du modèle
accuracy = accuracy_score(y_dep_test, predictions)
print("Accuracy:", accuracy)
# Affichage de la partie gagnée prédite par le modèle
print("Partie gagnée prédite par le modèle :", departement_potential_voters)

# Création d'un dictionnaire pour stocker le nombre de prédictions pour chaque partie politique
predicted_counts = {}

# Comptage du nombre de prédictions pour chaque partie politique
for party in departement_potential_voters:
    if party in predicted_counts:
        predicted_counts[party] += 1
    else:
        predicted_counts[party] = 1

# Affichage des résultats du comptage
print("Résultats du comptage des prédictions :")
for party, count in predicted_counts.items():
    print(f"{party} : {count}")

# Détermination de la partie politique avec le plus de prédictions
winning_party = max(predicted_counts, key=predicted_counts.get)
print("Parti politique avec le plus de prédictions pour gagner :", winning_party)


