import os
import fade  # type: ignore
import json
import colorama

faded_text = fade.greenblue("""
 ____                              _             ____  
|  _ \ _ __ ___  _ __   ___   ___ | |__   __   _|___ \ 
| |_) | '__/ _ \| '_ \ / _ \ / _ \| '_ \  \ \ / / __) |
|  __/| | | (_) | | | | (_) | (_) | |_) |  \ V / / __/ 
|_|   |_|  \___/|_| |_|\___/ \___/|_.__/    \_(_)_____|
                                     version 2.0
""") 

def afficher_titre():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(faded_text) 

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Chemins vers les fichiers JSON pour stocker les données
ELEVE_FILE = "../../Downloads/eleves.json"
PROF_FILE = "professeurs.json"
DEVOIR_FILE = "devoirs.json"
PUNITION_FILE = "punitions.json"

# Charger et enregistrer les données en JSON
def load_data(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return {}

def save_data(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

###################################################  Données pour partie direction ###########################################################

eleves = {
    'Alice Dupont': {'classe': '1G6', 'notes': [], 'emploi_temps': {}},
    'Bob Martin': {'classe': '1G6', 'notes': [], 'emploi_temps': {}},
    'Chloé Bernard': {'classe': '1G5', 'notes': [], 'emploi_temps': {}},
    'David Moreau': {'classe': '1G5', 'notes': [], 'emploi_temps': {}},
    'Emma Lefèvre': {'classe': '1G4', 'notes': [], 'emploi_temps': {}},
    'Lucas Simon': {'classe': '1G4', 'notes': [], 'emploi_temps': {}},
    'Sophie Dubois': {'classe': '1G3', 'notes': [], 'emploi_temps': {}},
}

professeurs = {
    'Monsieur Durand': {'matière': 'Mathématiques', 'emploi_temps': {}, 'classes': []},
    'Madame Dupuis': {'matière': 'Français', 'emploi_temps': {}, 'classes': []},
    'Monsieur Leroy': {'matière': 'Histoire', 'emploi_temps': {}, 'classes': []},
}

devoirs = {
    '1G6': ['Devoir de Mathématiques sur les équations', 'Devoir de Français sur un livre'],
    '1G5': ['Devoir d\'Histoire sur la Révolution Française'],
    '1G4': ['Devoir de SVT sur les écosystèmes'],
}

punitions = {
    'Alice Dupont': ['Retard en classe'],
    'Bob Martin': ['Parler pendant le cours'],
    'Chloé Bernard': ['Absence Physique-Chimie 25/10/24']
}


###################################################  Données pour partie direction ###########################################################



###################################################  PARTIE DIRECTION ###########################################################

def direction_menu():
    mdp = input("Entrez le mot de passe pour accéder à la direction : ")
    if mdp != "admin123":  # <---- ptit mdp :3
        print("Mot de passe incorrect.")
        return

# Option pour la partie Direction

    while True:
        clear_screen()
        afficher_titre()
        print("=== Menu Direction ===")
        print("1. Visualiser les listes d'élèves")
        print("2. Visualiser les listes de professeurs")
        print("3. Consultation et modification des élèves")
        print("4. Consultation et modification des professeurs")
        print("5. Déconnexion")

        choix = input("\nChoisissez une option : ")
        if choix == '1':
            afficher_eleves()
        elif choix == '2':
            afficher_professeurs()
        elif choix == '3':
            modifier_eleves()
        elif choix == '4':
            modifier_professeurs()
        elif choix == '5':
            break
        else:
            print("Choix invalide.")

# Affichage des élèves ( sous forme de tableaux c mieux :3 )

def afficher_eleves():
    print("\n=== Liste des élèves ===")
    print(f"{'Nom':<25} {'Classe':<10} {'Notes':<20} {'Emploi du temps':<30}")
    print("-" * 80)
    for nom, infos in eleves.items():
        notes = ", ".join(map(str, infos['notes'])) if infos['notes'] else "Aucune"
        emploi_temps = ", ".join([f"{jour}: {cours}" for jour, cours in infos['emploi_temps'].items()]) if infos['emploi_temps'] else "Vide"
        print(f"{nom:<25} {infos['classe']:<10} {notes:<20} {emploi_temps:<30}")
    input("\nAppuyez sur Entrée pour continuer...")

# Affichage des professeurs avec une meilleure mise en forme
def afficher_professeurs():
    print("\n=== Liste des professeurs ===")
    print(f"{'Nom':<25} {'Matière':<15} {'Classes':<20} {'Emploi du temps':<30}")
    print("-" * 80)
    for nom, infos in professeurs.items():
        classes = ", ".join(infos['classes']) if infos['classes'] else "Aucune"
        emploi_temps = ", ".join([f"{jour}: {cours}" for jour, cours in infos['emploi_temps'].items()]) if infos['emploi_temps'] else "Vide"
        print(f"{nom:<25} {infos['matière']:<15} {classes:<20} {emploi_temps:<30}")
    input("\nAppuyez sur Entrée pour continuer...")



# Consultation et modification des élèves
def modifier_eleves():
    while True:
        afficher_eleves()
        nom = input("Entrez le nom de l'élève pour modifier (ou 'q' pour quitter) : ")
        if nom == 'q':
            return  # Retourne au menu précédent ( g oublier de le mètre depuis je galerer XD )
        elif nom in eleves:
            clear_screen()
            print(faded_text)
            print(f"=== Choisisez une option pour {nom} ===")
            print("\n1. Modifier les notes")
            print("2. Modifier l'emploi du temps")
            print("3. Modifier la classe")
            print("4. Ajouter une punition")
            choix = input("\nChoisissez une option : ")
            if choix == '1':
                note = float(input("Entrez la note : "))
                eleves[nom].setdefault("notes", []).append(note)
            elif choix == '2':
                ajout_emploi_temps(nom)
            elif choix == '3':
                nouvelle_classe = input("Entrez la nouvelle classe : ")
                eleves[nom]["classe"] = nouvelle_classe
            elif choix == '4':
                punition = input("Description de la punition : ")
                punitions.setdefault(nom, []).append(punition)
            save_data(ELEVE_FILE, eleves)
            save_data(PUNITION_FILE, punitions)  # Enregistrer les punitions
            print(f"Mise à jour de {nom} effectuée.")
            clear_after_modification()  # Clear the output after modification
        else:
            clear_screen()
            print(colorama.Fore.RED + "Élève non trouvé ! Ressaisissez le nom concerné !" + colorama.Fore.WHITE)



# Consultation et modification des professeurs
def modifier_professeurs():
    while True:
        afficher_professeurs()
        nom = input("Entrez le nom du professeur pour modifier (ou 'q' pour quitter) : ")
        if nom == 'q':
            return  # Retourne au menu précédent
        elif nom in professeurs:
            clear_screen()
            print(faded_text)
            print(f"=== Choisisez une option pour {nom}  ===")
            print("\n1. Modifier l'emploi du temps")
            print("2. Modifier les classes")
            choix = input("\nChoisissez une option : ")
            if choix == '1':
                ajout_emploi_temps_prof(nom)
            elif choix == '2':
                nouvelle_classe = input("Entrez la nouvelle classe à ajouter : ")
                professeurs[nom]['classes'].append(nouvelle_classe)
            save_data(PROF_FILE, professeurs)
            print(f"Mise à jour de {nom} effectuée.")
            clear_after_modification()  # Clear the output after modification
        else:
            print("Professeur non trouvé.")

# Ajouter un emploi du temps pour un élève
def ajout_emploi_temps(nom):
    jour = input("Entrez le jour de la semaine : ")
    cours = input("Entrez le cours : ")
    eleves[nom]['emploi_temps'][jour] = cours
    save_data(ELEVE_FILE, eleves)
    print(f"Emploi du temps mis à jour pour {nom}.")

# Ajouter un emploi du temps pour un professeur
def ajout_emploi_temps_prof(nom):
    jour = input("Entrez le jour de la semaine : ")
    cours = input("Entrez le cours : ")
    professeurs[nom]['emploi_temps'][jour] = cours
    save_data(PROF_FILE, professeurs)
    print(f"Emploi du temps mis à jour pour {nom}.")

def clear_after_modification():
    clear_screen()
    print(colorama.Fore.GREEN + "[√] Modifications effectuées avec succès!" + colorama.Fore.WHITE )


###################################################  PARTIE DIRECTION  ###########################################################






###################################################  PARTIE PROFESSEUR ###########################################################


def professeur_menu():
    mdp = input("Entrez le mot de passe professeur : ")
    if mdp != "prof123":  # Mot de passe pour les professeurs
        print("Mot de passe incorrect.")
        return

    while True:
        clear_screen()
        afficher_titre()
        print("=== Menu Professeur ===")
        print("1. Visualiser la liste des élèves")
        print("2. Modifier les informations des élèves")
        print("3. Voir/Ajouter une absence")
        print("4. Voir/Ajouter un devoir")
        print("5. Déconnexion")

        choix = input("\nChoisissez une option : ")
        if choix == '1':
            afficher_eleves()
        elif choix == '2':
            modifier_eleves()
        elif choix == '3':
            ajouter_absence()
        elif choix == '4':
            ajouter_devoir()
        elif choix == '5':
            break
        else:
            print("Choix invalide.")

def ajouter_absence():
    choix = input("Voulez vous voir(1) ou ajouter(2) une absence ?: ")
    if choix == "1":
        classe = input("Entrez la classe : ")
        print("\n=== Liste des Eleves ===")
        text = ""
        for eleve in eleves:
            if eleves[eleve]['classe'] == classe:
                text += f"{eleve}\n"
        print(text)
        eleve = input("Entrez le nom de l'eleve : ")
        print("\n=== Liste des absences ===")
        text = ""
        for personne in punitions:
            if personne == eleve:
                for punition in punitions[personne]:
                    if "Absence" in punition:
                        text += f"-Absence en {punition.split()[1]} le {punition.split()[2]}\n"
        print(text)
        input("Appuyez sur Entrée pour continuer...")
        return
    if choix == "2":
        classe = input("Entrez la classe : ")
        print("\n=== Liste des Eleves ===")
        text = ""
        for eleve in eleves:
            if eleves[eleve]['classe'] == classe:
                text += f"{eleve}\n"
        print(text)
        eleve = input("Entrez le nom de l'eleve : ")
        matiere = input("Entrez la matiere : ")
        date = input("Entrez la date : ")
        if eleve in punitions:
            punitions_actuels = punitions[eleve]
        else:
            punitions_actuels = [f"Absence {matiere} {date}"]
        punitions[eleve] = punitions_actuels
        print(f"\nL'absence du {date} en {matiere} a ete attribue pour {eleve}")
        input("\nAppuyez sur Entrée pour continuer...")


def ajouter_devoir():
    choix = input("Voulez vous voir(1) ou ajouter(2) une absence ?: ")
    if choix == "1":
        classe = input('Entrez la classe : ')
        if classe not in devoirs:
            print("\nCette classe n'a pas de devoir")
            input("\nAppuyez sur Entrée pour continuer...")
            return
        print("\n=== Liste des devoirs ===")
        for devoir in devoirs[classe]:
            print(f"-{devoir}")
        input("\nAppuyez sur Entrée pour continuer...")
        return
    if choix == "2":
        classe = input('Entrez la classe : ')
        devoir = input('Entrez le devoir : ')
        if classe in devoirs:
            devoirs_actuels = devoirs[classe]
            devoirs_actuels.append(devoir)
            devoirs[classe] = devoirs_actuels
            print(f'\nLe devoir "{devoir}" a ete attribue pour la classe {classe}')
            input("\nAppuyez sur Entrée pour continuer...")
            return
        devoirs[classe] = [devoir]
        print(f'\nLe devoir "{devoir}" a ete attribue pour la classe {classe}')
        input("\nAppuyez sur Entrée pour continuer...")
        return


################################################### PARTIE DIRECTION ###########################################################




################################################### MENU PRINCIPALE  ###########################################################



def main():
    while True:
        clear_screen()
        afficher_titre()
        print("=== Menu Principal ===")
        print("1. Connexion direction")
        print("2. Connexion professeur")
        print("3. Espace élève")
        print("4. Quitter")
        
        choix = input("Choisissez une option : ")
        if choix == '1':
            direction_menu()
        elif choix == '2':
            professeur_menu()
        elif choix == '3':
            print("Espace élève non implémenté.")
            input("Appuyez sur Entrée pour continuer...")
        elif choix == '4':
            break
        else:
            print("Choix invalide.")



if __name__ == "__main__":
    main()