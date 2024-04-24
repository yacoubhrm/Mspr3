import csv
import json
import os

def csv_to_json(csv_file, json_file, pg_config_file):
    # Vérification de l'existence du fichier de configuration PostgreSQL
    if not os.path.isfile(pg_config_file):
        print("Le fichier de configuration PostgreSQL spécifié n'existe pas.")
        return
    
    # Liste pour stocker les lignes du CSV
    data = []

    # Ouverture du fichier CSV et lecture des données
    with open(csv_file, 'r', newline='', encoding='latin-1') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        # Convertit chaque ligne en un dictionnaire et l'ajoute à la liste
        for row in csv_reader:
            data.append(row)

    # Ajout de la structure JSON supplémentaire avec vos données
    postgres_config = {
        "Servers": {
            "1": {
                "Name": "PostgreSQL-1",
                "Group": "Servers",
                "Port": 5432,
                "Username": "postgres",
                "Host": "localhost",
                "SSLMode": "prefer",
                "MaintenanceDB": "postgres"
            }
        }
    }

    print(postgre_config)

    # Fusionne les données CSV converties avec la structure JSON PostgreSQL
    postgres_config.update(data)

    # Écriture des données dans un fichier JSON
    with open(json_file, 'w', encoding='utf-8') as jsonfile:
        json.dump(postgres_config, jsonfile, indent=4)

# Utilisation de la fonction pour convertir le fichier CSV en JSON
csv_file_path = 'Data/datafromETL/resultALL.csv'
json_file_path = 'Data/dataframe/resultALLJson.json'
