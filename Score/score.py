import os
import csv

nomFichier = "score/score.csv"
def initialisationFichier():
    if os.path.exists(nomFichier) == False:
        try:
            with open(nomFichier, 'w') as f:
                print(f"Le fichier {nomFichier} a été créé avec succès.")
        except Exception as e:
            print(f"Une erreur s'est produite lors de la création du fichier : {str(e)}")
        return True
    return True

# à faire
def ajouterScore(pseudo:str,score:int):
    try:
        with open(nomFichier, mode='a', newline='') as fichier_csv:
            writer = csv.writer(fichier_csv)
            writer.writerow([pseudo, score])
        print("Ligne ajoutée avec succès.")
    except Exception as e:
        print(f"Une erreur s'est produite lors de l'ajout de la ligne : {str(e)}")
def recupererScores():
    scores = {}
    try:
        with open(nomFichier, mode='r') as fichier_csv:
            lecteur = csv.reader(fichier_csv)
            next(lecteur)  # Skip header row if exists
            for row in lecteur:
                nom, score = row
                scores[nom] = int(score)
        return scores
    except Exception as e:
        print(f"Une erreur s'est produite lors de la récupération des scores : {str(e)}")
        return None
