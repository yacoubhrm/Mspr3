## Projet MSPR3

## Description
Ce projet vise à créer un modèle de prédiction des résultats des élections présidentielles dans le département des Alpes-Maritimes (06), en utilisant une combinaison de données historiques sur les élections, des indicateurs économiques, sociaux et de criminalité.

## Justification du choix de la zone géographique
Les Alpes-Maritimes ont été choisies en raison de leur diversité politique, de leur taille de population suffisamment grande pour une analyse statistique robuste, de leur hétérogénéité socio-économique et de leur intérêt touristique.

## Choix des critères, justification
Les critères choisis pour le modèle comprennent les résultats des anciennes élections présidentielles, les indicateurs économiques, sociaux et de chômage, ainsi que les données sur la criminalité, en raison de leur impact sur les choix électoraux.

## Démarche suivie et méthodes employées
La démarche suivie comprend l'analyse des données historiques, la création d'un modèle conceptuel de données, l'extraction et le nettoyage des données, la création de modèles de prédiction et l'évaluation de leur précision.

## Modèle Conceptuel de Données
![MCD](![image](https://github.com/yacoubhrm/Mspr3/assets/114953698/e2e268ef-0f06-4d5c-b114-6203d58f609c)


## Qualité des données
Les données ont été nettoyées et normalisées à l'aide de scripts Python et de l'ETL Dataiku pour assurer leur qualité et leur cohérence.

## Modèles testés
Les modèles testés comprennent un modèle basé sur les scores des élections par département, une régression linéaire avec des données économiques et sociales, une interface de prédiction des résultats basée sur l'entrée utilisateur et un modèle basé sur les données des candidats.

## Résultats du modèle choisi
Les résultats du modèle choisi seront présentés dans une section dédiée une fois disponibles.

## Visualisations
Des visualisations des données et des résultats seront incluses dans le projet.

## Accuracy (pouvoir prédictif du modèle)
L'accuracy du modèle sera évaluée en comparant les prédictions avec les résultats réels des élections.

## Réponses aux questions posées dans les exemples d’indicateurs d’analyse
- La variable la plus corrélée aux résultats des élections présidentielles sera identifiée à l'aide d'une analyse statistique.
- Le principe d'un apprentissage supervisé sera expliqué en détail.
- La précision du modèle sera mesurée en comparant les prédictions avec les résultats réels et en calculant le taux de prédictions correctes.

## Jeu de données nettoyé, normalisé et optimisé
Les données seront stockées dans un format SQL pour assurer la facilité d'accès et la performance.

## Structure du projet
- **Data**: Contient les données brutes, les données nettoyées et les données gouvernementales.
- **IA**: Contient les modèles de prédiction.
- **TraitementData**: Contient les scripts de traitement des données.

## Comment exécuter le projet
1. Installer les dépendances requises en exécutant `pip install -r requirements.txt`.
2. Exécuter les scripts de traitement des données dans l'ordre approprié.
3. Exécuter les modèles de prédiction dans le dossier `IA`.
