import csv

# chemin fichiers
fichier_csv_origine = "Data/dataGouvernement/resultats_par_niveau_burvot_t1_france_entiere.csv"
fichier_csv_nouveau = "Data/dataframe/resultats_par_niveau_burvot_t1_france_entiere_par_candidat.csv"

# liste pour stocker les nouvelles données
donnees_modifiees = []

# load et traitement
with open(fichier_csv_origine, newline='', encoding='latin-1') as csvfile:
    lecteur_csv = csv.reader(csvfile)
    next(lecteur_csv)  # enlever entete
    for ligne in lecteur_csv:
        infos_communes = ligne[:20]  
        valeurs_communes = ligne[20:21]  # valeurs communes
        for i in range(21, len(ligne)-6, 7): 
            # une ligne pour chaque candidat pour un même bureau de vote
            nouvelle_ligne = infos_communes + valeurs_communes + ligne[i:i+7]
            donnees_modifiees.append(nouvelle_ligne)

# mettre les donnees dans un nouveau fichier
with open(fichier_csv_nouveau, 'w', newline='', encoding='latin-1') as csvfile:
    writer = csv.writer(csvfile)
    # entete colonnes
    writer.writerow([
        "Code du département",
        "Libellé du département",
        "Code de la circonscription",
        "Libellé de la circonscription",
        "Code de la commune",
        "Libellé de la commune",
        "Code du b.vote",
        "Inscrits",
        "Abstentions",
        "% Abs/Ins",
        "Votants",
        "% Vot/Ins",
        "Blancs",
        "% Blancs/Ins",
        "% Blancs/Vot",
        "Nuls",
        "% Nuls/Ins",
        "% Nuls/Vot",
        "Exprimés",
        "% Exp/Ins",
        "% Exp/Vot",
        "N°Panneau",
        "Sexe",
        "Nom",
        "Prénom",
        "Voix",
        "% Voix/Ins",
        "% Voix/Exp"
    ])
    # renseigner les donnees dans le doc
    for ligne in donnees_modifiees:
        writer.writerow(ligne)
