import os
import fade 



faded_text = fade.greenblue("""
 ____                              _             _ 
|  _ \ _ __ ___  _ __   ___   ___ | |__   __   _/ |
| |_) | '__/ _ \| '_ \ / _ \ / _ \| '_ \  \ \ / / |
|  __/| | | (_) | | | | (_) | (_) | |_) |  \ V /| |
|_|   |_|  \___/|_| |_|\___/ \___/|_.__/    \_(_)_|
                                  version 1.0
""")

def afficher_titre():
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print(faded_text)  

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def ajouter_note(eleves_notes, nom, note):
    eleves_notes.setdefault(nom, []).append(note)

def calculer_moyenne(eleves_notes, nom):
    if nom in eleves_notes and eleves_notes[nom]:
        return sum(eleves_notes[nom]) / len(eleves_notes[nom])
    return None

def meilleure_note(eleves_notes):
    return max((max(notes) for notes in eleves_notes.values() if notes), default=0)

def a_la_moyenne(eleves_notes, nom, seuil=10):
    moyenne = calculer_moyenne(eleves_notes, nom)
    return moyenne is not None and moyenne >= seuil

eleves_notes = {}

while True:
    clear_screen()
    afficher_titre()
    print("""=== Choisissez une option ===
\n1. Ajouter une note
2. Calculer la moyenne d'un élève
3. Afficher la meilleure note de la classe
4. Vérifier si un élève a la moyenne
5. Quitter""")
    
    choix = input("\nChoisissez une option : ")
    
    if choix == '1':
        nom = input("Nom de l'élève : ")
        note = float(input("Note de l'élève : "))
        ajouter_note(eleves_notes, nom, note)
        print(f"Note ajoutée à {nom}.")
    
    elif choix == '2':
        nom = input("Nom de l'élève : ")
        moyenne = calculer_moyenne(eleves_notes, nom)
        print(f"La moyenne de {nom} est {moyenne:.2f}." if moyenne is not None else f"Aucune note trouvée pour {nom}.")
    
    elif choix == '3':
        print(f"La meilleure note de la classe est {meilleure_note(eleves_notes)}.")
    
    elif choix == '4':
        nom = input("Nom de l'élève : ")
        print(f"{nom} a la moyenne." if a_la_moyenne(eleves_notes, nom) else f"{nom} n'a pas la moyenne.")
    
    elif choix == '5':
        print("Programme terminé.")
        break
    
    else:
        print("Choix invalide.")
    
    input("\nAppuyez sur Entrée pour continuer...")
