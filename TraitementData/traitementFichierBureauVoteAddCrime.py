import csv
from collections import defaultdict

# load data
def load_csv(filename):
    data = []
    with open(filename, newline='', encoding='latin-1') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data

# Fonction moyenne ratio 2022 uniquement
def calculate_average_ratio(data):
    averages = defaultdict(list)
    for row in data:
        year = row[1]
        if year == '22':  # si 2022
            department_code = row[2]
            tauxpourmille = float(row[-1].replace(',', '.'))  # to float
            averages[department_code].append(tauxpourmille)
    
    department_averages = {}
    for code, ratios in averages.items():
        department_averages[code] = sum(ratios) / len(ratios)
    
    return department_averages

# table de correspondance pour les codes depart a 3 chiffres
correspondence_table = {
    "ZD": "974",
    "ZA": "971",
    "ZB": "972",
    "ZC": "973",
    "ZM": "976",
}

# load les fichiers needed
csv1_data = load_csv('Data/dataframe/resultats_par_niveau_burvot_t1_france_entiere_par_candidat.csv')
csv2_data = load_csv('Data/dataGouvernement/crimeA_prepared.csv')

# calc moyenne crime
department_averages = calculate_average_ratio(csv2_data)

# Add colonne
csv1_data[0].append("ratioCrimePourMille")

# add les valeurs des moyennes sur les bonnes lignes
for row in csv1_data[1:]:
    department_code = row[0]
    if department_code not in department_averages:
        # verif si depart est prresent dans la table
        if department_code in correspondence_table:
            corresponding_code = correspondence_table[department_code]
            if corresponding_code in department_averages:
                average_ratio = department_averages[corresponding_code]
                row.append(str(average_ratio))
            else:
                row.append("")  #si pas de data
        else:
            row.append("")  
    else:
        average_ratio = department_averages[department_code]
        row.append(str(average_ratio))

# Supprimer le 0 devant les nombres inférieurs à 10 uniquement dans la colonne "Code du département"
for nouvelle_ligne in csv1_data:
    nouvelle_ligne[0] = nouvelle_ligne[0].lstrip('0') if nouvelle_ligne[0].isdigit() and int(nouvelle_ligne[0]) < 10 else nouvelle_ligne[0]

# creer new file
with open('Data/dataframe/resultats_par_niveau_burvot_t1_france_entiere_par_candidat_avec_crimes.csv', 'w', newline='', encoding='latin-1') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(csv1_data)
