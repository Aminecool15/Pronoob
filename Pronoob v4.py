import os
import fade
import colorama

faded_text = fade.greenblue("""
  ____                              _             _  _   
 |  _ \ _ __ ___  _ __   ___   ___ | |__   __   _| || |  
 | |_) | '__/ _ \| '_ \ / _ \ / _ \| '_ \  \ \ / / || |_ 
 |  __/| | | (_) | | | | (_) | (_) | |_) |  \ V /|__   _|
 |_|   |_|  \___/|_| |_|\___/ \___/|_.__/    \_(_)  |_|  
                                                                                       
                             version 4.0
""") 

os.system('mode 170,30') # pour pouvoir consulter pleinement les tableaux ^^

# fonction pour effacer l'ecran
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# afficher le titre en effacant l'ecran avant
def afficher_titre():
    clear_screen()
    print(faded_text) 



###################################################  Données pour partie direction ###########################################################

# info élèves
eleves = {
    'Alice Dupont': {'classe': '1G6', 'notes': [], 'emploi_temps': {}},
    'Adrian Laporte': {'classe': '1G6', 'notes': ["Maths : 16 ", "NSI : 13 ", "Français : 17 ", "Histoire-Géographie : 14 ", "Anglais : 18  ", "Physique-Chimie : 15  ", "SVT : 16"], 'emploi_temps': {"Lundi": "Maths", "Mardi": "Français", "Mercredi": "NSI", "Jeudi": "Anglais", "Vendredi": "Histoire-Géographie"}},
    'Bob Martin': {'classe': '1G6', 'notes': [], 'emploi_temps': {}},
    'Chloé Bernard': {'classe': '1G5', 'notes': [], 'emploi_temps': {}},
    'David Moreau': {'classe': '1G5', 'notes': [], 'emploi_temps': {}},
    'Alexandre Aris': {'classe': '1G4', 'notes': ["Maths : 15 ", "NSI : 14 ", "Français : 19 ", "Histoire-Géographie : 15"], 'emploi_temps': {"Lundi": "Physique-Chimie", "Mardi": "SVT", "Mercredi": "Philosophie", "Jeudi": "Espagnol", "Vendredi": "EPS"}},
    'Emma Lefèvre': {'classe': '1G4', 'notes': [], 'emploi_temps': {}},
    'Lucas Simon': {'classe': '1G4', 'notes': [], 'emploi_temps': {}},
    'Sophie Dubois': {'classe': '1G3', 'notes': [], 'emploi_temps': {}}
}

# infos profs
professeurs = {
    'Monsieur Dupont': {'matière': 'Mathématiques', 'emploi_temps': {}, 'classes': []},
    'Madame Lefevre': {'matière': 'Français', 'emploi_temps': {}, 'classes': []},
    'Monsieur Martin': {'matière': 'Histoire', 'emploi_temps': {}, 'classes': []},
    'Madame Rousseau': {'matière': 'Mathématiques', 'emploi_temps': {}, 'classes': []},
    'Monsieur Lambert': {'matière': 'Français', 'emploi_temps': {}, 'classes': []},
    'Madame Caron': {'matière': 'Histoire', 'emploi_temps': {}, 'classes': []},
    'Monsieur Lefort': {'matière': 'Mathématiques', 'emploi_temps': {}, 'classes': []},
    'Madame Dubois': {'matière': 'Français', 'emploi_temps': {}, 'classes': []},
    'Monsieur Leclerc': {'matière': 'Histoire', 'emploi_temps': {}, 'classes': []},
    'Madame Bernard': {'matière': 'Mathématiques', 'emploi_temps': {}, 'classes': []},
    'Monsieur Simon': {'matière': 'Français', 'emploi_temps': {}, 'classes': []},
    'Madame Petit': {'matière': 'Histoire', 'emploi_temps': {}, 'classes': []},
    'Monsieur Renard': {'matière': 'Mathématiques', 'emploi_temps': {}, 'classes': []},
    'Madame Lefevre': {'matière': 'Français', 'emploi_temps': {}, 'classes': []},
    'Monsieur Caron': {'matière': 'Histoire', 'emploi_temps': {}, 'classes': []},
    'Madame Lemoine': {'matière': 'Mathématiques', 'emploi_temps': {}, 'classes': []},
    'Monsieur Fabre': {'matière': 'Français', 'emploi_temps': {}, 'classes': []},
}

# les devoirs par classe
devoirs = {
    
    '1G6': ['[+] Devoir de Mathématiques sur les équations  ', '[+] Devoir de Français sur un livre'],
    '1G5': ['[+] Devoir d\'Histoire sur la Révolution Française'],
    '1G4': ['[+] Devoir de SVT sur les écosystèmes']
}

# les punitions par eleves 
punitions = {
    'Alice Dupont': [colorama.Fore.RED + "[X] Exclusion de cours" + colorama.Fore.WHITE],
    'Bob Martin': [colorama.Fore.RED + '[X] Parler pendant le cours' + colorama.Fore.WHITE]
}

###################################################  Données pour partie direction ###########################################################






###################################################  PARTIE DIRECTION ###########################################################

def direction_menu():
    mdp = input("Entrez le mot de passe pour accéder à la direction : ")
    if mdp != "admin123":
        print("Mot de passe incorrect.")
        return

    # menu pour la partie Direction
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

        if choix == '1': # listes d'eleves
            afficher_eleves()
        elif choix == '2': # listes de professeurs
            afficher_professeurs()
        elif choix == '3': # modifications des informations des eleves
            modifier_eleves()
        elif choix == '4': # meme chose pour les professeurs
            modifier_professeurs()
        elif choix == '5': # sortie du menu
            break
        else: # au cas ou il y a une faute de frappe
            print("Choix invalide.")

# affichage des élèves (sous forme de tableaux c mieux :3)
def afficher_eleves(pause=True):
    afficher_titre()
    print("=== Liste des élèves ===")
    print(f"{'Nom':<25} {'Classe':<10} {'Notes':<20} {'Punitions':<10} {'Emploi du temps':<30}")
    print("-" * 90)
    for nom, infos in eleves.items():
        notes = f"{len(infos['notes'])} notes" if len(infos['notes']) > 0 else "Aucune"
        emploi_temps = ", ".join([f"{jour}: {cours}" for jour, cours in infos['emploi_temps'].items()]) if infos['emploi_temps'] else "Vide"
        punition = len(punitions[nom]) if nom in punitions else "Aucune"
        print(f"{nom:<25} {infos['classe']:<10} {notes:<20} {punition:<10} {emploi_temps:<30}")
    if pause:
        input("\nAppuyez sur Entrée pour continuer...")

# la meme chose pour les profs
def afficher_professeurs(pause=True):
    afficher_titre()
    print("=== Liste des professeurs ===\n")
    print(f"{'Nom':<25} {'Matière':<15} {'Classes':<20} {'Emploi du temps':<30}")
    print("-" * 80)
    for nom, infos in professeurs.items():
        classes = ", ".join(infos['classes']) if infos['classes'] else "Aucune"
        emploi_temps = ", ".join([f"{jour}: {cours}" for jour, cours in infos['emploi_temps'].items()]) if infos['emploi_temps'] else "Vide"
        print(f"{nom:<25} {infos['matière']:<15} {classes:<20} {emploi_temps:<30}")
    if pause:
        input("\nAppuyez sur Entrée pour continuer...")

# pour modifier les infos des eleves
def modifier_eleves():
    while True:
        afficher_eleves(False)
        nom = input("\nEntrez le nom de l'élève pour modifier (ou 'q' pour quitter) : ")
        if nom == 'q':
            return
        elif nom in eleves:
            clear_screen()
            print(faded_text)
            print(f"=== Choisisez une option pour {nom} ===\n")
            print("1. Voir/Modifier les notes")
            print("2. Modifier l'emploi du temps")
            print("3. Modifier la classe")
            print("4. Voir/Ajouter une punition")
            print("5. Déconnexion")
            choix = input("\nChoisissez une option : ")

            if choix == '1': # voir ou ajouter une note
                question = input("Appuyer sur 1 pour Consulter ou sur 2 pour Modifier : ")
                eleves_notes(question, nom)
            elif choix == '2': # modifier un jour de l'emploi du temps
                ajout_emploi_temps(nom)
            elif choix == '3': # changer la classe de l'eleve
                eleve_changer_classe(nom)
            elif choix == '4': # voir ou ajouter une punition a l'eleve
                question = input("Appuyer sur 1 pour Consulter ou sur 2 pour Modifier : ")
                eleves_punitions(question, nom)
            else:
                return
            clear_after_modification()
        else:
            clear_screen()
            print(colorama.Fore.RED + "Élève non trouvé ! Ressaisissez le nom concerné !" + colorama.Fore.WHITE )

# redirection vers les fonctions correspondantes
def eleves_notes(choix, nom):
    if choix == "1": # choix de consulter les notes
        eleves_notes_voir(nom)
    if choix == "2": #       de en ajouter une
        eleves_notes_modifier(nom)

# fonction pour voir toutes les notes d'un eleve
def eleves_notes_voir(nom):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(faded_text)
    print('=== Listes des notes ===')
    if len(eleves[nom]['notes']) > 0:
        for note in eleves[nom]['notes']:
            print(f"- {note}")
        input("\nAppuyez sur Entrée pour continuer...")
    else:
        print(colorama.Fore.YELLOW + "\n[!] Aucune note " + colorama.Style.RESET_ALL)
        input("\nAppuyez sur Entrée pour continuer...")

# fonction pour ajouter une note a un eleve
def eleves_notes_modifier(nom):
    matiere = input("Entrez la matiere : ")
    note = float(input("Entrez la note : "))
    notes = eleves[nom]['notes']
    notes.append(f"{matiere} : {note}")
    eleves[nom]['notes'] = notes

# ajouter un cours pour un élève
def ajout_emploi_temps(nom):
    jour = input("Entrez le jour de la semaine : ")
    cours = input("Entrez le cours : ")
    eleves[nom]['emploi_temps'][jour] = cours
    print(f"Emploi du temps mis à jour pour {nom}.")

# changer la classe d'un eleve
def eleve_changer_classe(nom):
    nouvelle_classe = input("Entrez la nouvelle classe : ")
    eleves[nom]["classe"] = nouvelle_classe

# redirection vers les fonctions associes au choix dans les punitions
def eleves_punitions(choix, nom):
    if choix == "1": # consulter
        eleves_punitions_voir(nom)
    if choix == "2": # ajouter
        eleves_punitions_ajouter(nom)

# fonction pour voir les punitions d'un eleve
def eleves_punitions_voir(nom):
    afficher_titre()
    print(f"=== Liste des punitions pour {nom}  ===")
    if nom in punitions:
        for punition in punitions[nom]:
            print(colorama.Fore.RED +"\n"+ punition + colorama.Fore.WHITE)
    else:
        print(colorama.Fore.GREEN + "\n[√] Aucune " + colorama.Fore.WHITE)
    input("\nAppuyez sur Entrée pour continuer...")
    return

# fonction pour attribuer une punition a un eleve
def eleves_punitions_ajouter(nom):
    punition = input("Description de la punition : ")
    if nom in punitions:
        punitions[nom].append("[X] " + punition)
    else:
        punitions[nom] = ["[X] " + punition]
    input("\nAppuyez sur Entrée pour continuer...")
    return

# modifier les infos des profs
def modifier_professeurs():
    while True:
        afficher_titre() 
        afficher_professeurs(False)
        nom = input("\nEntrez le nom du professeur pour modifier (ou 'q' pour quitter) : ")
        if nom == 'q':
            return  # Retourne au menu précédent
        elif nom in professeurs:
            clear_screen()
            print(faded_text)
            print(f"=== Choisisez une option pour {nom}  ===")
            print("\n1. Modifier l'emploi du temps")
            print("2. Modifier les classes")
            choix = input("\nChoisissez une option : ")

            if choix == '1': # modifier un jour de l'emploi du temps du prof
                ajout_emploi_temps_prof(nom)
            elif choix == '2': # changer la classe du prof
                ajout_classe_prof(nom)
                
            afficher_titre()
            print(colorama.Fore.GREEN +  f"[√] Mise à jour effectuée pour {nom} "+colorama.Fore.WHITE) #
            input("Appuyez sur Entrée pour continuer...")
        else:
            choix = input(colorama.Fore.YELLOW + "[!] Professeur non trouvé, voulez vous en rajouter un ? (oui/non) : " + colorama.Fore.WHITE)
            ajout_prof(choix, nom)
        afficher_titre()

# ajouter un cours pour un professeur
def ajout_emploi_temps_prof(nom):
    jour = input("Entrez le jour de la semaine : ")
    cours = input("Entrez le cours : ")
    professeurs[nom]['emploi_temps'][jour] = cours
    print(colorama.Fore.GREEN + f"[√] Emploi du temps mis à jour pour {nom}." + colorama.Fore.WHITE )

# modifier la classe attribue au prof
def ajout_classe_prof(nom):
    nouvelle_classe = input("Entrez la nouvelle classe à ajouter : ")
    professeurs[nom]['classes'].append(nouvelle_classe)

# ajouter un prof s'il est pas encore dans la liste
def ajout_prof(choix, nom):
    if choix == "non":
        return
    if choix == "oui":
        afficher_titre()
        print(f"=== Informations pour Professeur {nom} ===\n")
        matiere = input("Entrez la matiere du professeur : ")
        professeurs[nom] = {'matière': matiere, 'emploi_temps': {}, 'classes': []}
        afficher_titre()
        print(colorama.Fore.GREEN + "[√] Professeur ajouté avec succès !" + colorama.Fore.WHITE)
        input("Appuyez sur Entrée pour continuer...")
    return

# pour dire que tt est bon a la fin
def clear_after_modification():
    afficher_titre()
    print(colorama.Fore.GREEN + "[√] Modifications effectuées avec succès!" + colorama.Fore.WHITE )
    input("\nAppuyez sur Entrée pour continuer...")


###################################################  PARTIE DIRECTION  ###########################################################






###################################################  PARTIE PROFESSEUR ###########################################################


def professeur_menu():
    mdp = input("Entrez le mot de passe professeur : ")
    if mdp != "prof123":  # Mot de passe pour les professeurs
        print("Mot de passe incorrect.")
        return

    # menu partie professeur
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

        if choix == '1': # voir tout les eleves
            afficher_eleves()
        elif choix == '2': # modifier les infos d'un eleve
            modifier_eleves()
        elif choix == '3': # voir ou ajouter une absence
            question = input("Appuyer sur 1 pour Consulter ou sur 2 pour Ajouter : ")
            absence_eleves_choix(question)
        elif choix == '4': # voir ou ajouter des devoirs
            question = input("Appuyer sur 1 pour Consulter ou sur 2 pour Ajouter: ")
            devoir(question)
        elif choix == '5': # sortie
            break
        else:
            print("Choix invalide.")

# redirection vers les fonctions pour les choix des absences
def absence_eleves_choix(choix):
    if choix == "1": # voir des absences
        absence_eleves_voir()
    if choix == "2": # ajouter une absence
        selection_absence()

# affichage des eleves pour choisir lequel regarder
def absence_eleves_voir():
    classe = input("Entrez la classe : ")
    afficher_titre()
    print("=== Liste des Eleves ===")
    for eleve in eleves:
        if eleves[eleve]['classe'] == classe:
            print(f"- {eleve}")
    eleve = input("\nEntrez le nom de l'eleve : ")
    afficher_absence(eleve)
    return

# affichage des absences de l'eleves
def afficher_absence(eleve):
    afficher_titre()
    print("=== Liste des absences ===")
    text = colorama.Fore.RED
    trouver = False
    for personne in punitions:
        if personne == eleve:
            for punition in punitions[personne]:
                if "Absence" in punition:
                    trouver = True
                    text += f"-[X]Absence en {punition.split()[1]} le {punition.split()[2]}\n"
    if not trouver:
        print(colorama.Fore.GREEN + '[√] Aucune absence \n' + colorama.Fore.WHITE)
    else:
        print(text + colorama.Fore.WHITE)
    input("Appuyez sur Entrée pour continuer...")

# selection de l'eleve et de l'absence
def selection_absence():
    classe = input("Entrez la classe : ")
    afficher_titre()
    print("=== Liste des Eleves ===")
    for eleve in eleves:
        if eleves[eleve]['classe'] == classe:
            print(f"{eleve}")
    eleve = input("\nEntrez le nom de l'eleve : ")
    matiere = input("Entrez la matiere : ")
    date = input("Entrez la date : ")
    ajouter_absence(eleve, matiere, date)

# attribution de l'absence de l'eleve
def ajouter_absence(eleve,matiere,date):
    if eleve in punitions:
        punitions[eleve].append(colorama.Fore.RED + f'Absence {matiere} {date}' + colorama.Fore.WHITE)
    else:
        punitions[eleve] = [colorama.Fore.RED + f'Absence {matiere} {date}' + colorama.Fore.WHITE]
    afficher_titre()
    print(colorama.Fore.GREEN + f"L'absence du {date} en {matiere} a été attribué pour {eleve}" + colorama.Fore.WHITE)
    input("\nAppuyez sur Entrée pour continuer...")

# redirection vers les fonctions associes aux devoirs
def devoir(choix):
    if choix == "1": # consulter les devoirs d'un classe
        devoir_voir()
    if choix == "2": # ajouter un devoir pour une classe
        devoir_selection()

# fonction pour voir les devoirs d'une classe
def devoir_voir():
    classe = input('Entrez la classe : ')
    if classe not in devoirs:
        print(colorama.Fore.YELLOW + "\n[!] Cette classe n'a pas de devoir" + colorama.Fore.WHITE)
        input("\nAppuyez sur Entrée pour continuer...")
        return
    afficher_titre()
    print("=== Liste des devoirs ===")
    for devoir in devoirs[classe]:
        print(f"-{devoir}")
    input("\nAppuyez sur Entrée pour continuer...")
    return

# selection des informations du devoir
def devoir_selection():
    classe = input('Entrez la classe : ')
    matiere = input('Entrez la matiere : ')
    consigne = input('Entrez la consigne : ')
    devoir_ajout(classe, matiere, consigne)
    return

# attribution du devoir à la classe
def devoir_ajout(classe, matiere, consigne):
    devoir = f"[+] Devoir de {matiere} : {consigne}"
    if classe in devoirs:
        devoirs[classe].append(devoir)
    else:
        devoirs[classe] = [devoir]
    afficher_titre()
    print(colorama.Fore.GREEN + f'{devoir} a été attribué pour la classe {classe}' + colorama.Fore.WHITE)
    input("\nAppuyez sur Entrée pour continuer...")


################################################### PARTIE PROFESSEUR ###########################################################






################################################### PARTIE ELEVE ###########################################################


def eleve_menu():
    mdp = input("Entrez le mot de passe élève : ")
    if mdp != "eleve123":
        print("Mot de passe incorrect.")
        return

    # menu élève
    while True:
        clear_screen()
        afficher_titre()
        print("=== Menu Élève ===")
        print("1. Visualiser ses notes")
        print("2. Visualiser ses devoirs")
        print("3. Visualiser son emploi du temps")
        print("4. Visualiser ses punitions")
        print("5. Déconnexion")
        choix = input("\nChoisissez une option : ")

        if choix == '1': # voir ses notes
            voir_notes_eleves()
        elif choix == '2': # voir ses devoirs
            voir_devoirs_eleves()
        elif choix == '3': # voir son emploi du temps
            voir_emploidutemps_eleves()
        elif choix == '4': # voir ses punitions
            voir_punitions_eleves()
        elif choix == '5': # sortie
            print("Déconnexion réussie.")
            break
        else:
            print("Choix invalide.")
            input("\nAppuyez sur Entrée pour continuer...")

# consulter ses notes
def voir_notes_eleves():
    eleve = input("Entrez votre nom : ")
    if eleve in eleves:
        notes = eleves[eleve].get("notes", [])
        clear_screen()
        afficher_titre()
        print(f"=== Notes de {eleve} ===\n")
        if len(notes) > 0:
            for note in notes:
                print(note)
        else:
            print(colorama.Fore.YELLOW + '[+] Aucune note' + colorama.Fore.WHITE)
    else:
        print("Élève non trouvé.")
    input("\nAppuyez sur Entrée pour continuer...")

# consulter ses devoirs
def voir_devoirs_eleves():
    eleve = input("Entrez votre nom : ")
    if eleve in eleves:
        classe = eleves[eleve]["classe"]
        afficher_titre()
        if classe in devoirs:
            print(f"=== Devoirs pour {classe} ===\n")
            for devoir in devoirs[classe]:
                print(devoir)
        else:
            print(f"=== Devoirs pour {classe} ===\n" + colorama.Fore.YELLOW + "\n[+] Vous n'avez pas de devoir :D" + colorama.Fore.WHITE)
    else:
        print("Élève non trouvé.")
    input("\nAppuyez sur Entrée pour continuer...")

# consulter son emploi du temps
def voir_emploidutemps_eleves():
    eleve = input("Entrez votre nom : ")
    if eleve in eleves:
        afficher_titre()
        print(f"=== Emploi du temps ===\n")
        if eleves[eleve]['emploi_temps'] != {}:
            emploi_temps = eleves[eleve]["emploi_temps"]
            for jour, cours in emploi_temps.items():
                print(f"{jour} : {cours}")
        else:
            print(colorama.Fore.YELLOW + "[+] Vous n'avez pas cours !" + colorama.Fore.WHITE)
    else:
        print('Nom inconnue')
    input("\nAppuyez sur Entrée pour continuer...")

# consulter ses punitions
def voir_punitions_eleves():
    eleve = input("Entrez votre nom : ")
    if eleve in eleves:
        afficher_titre()
        print(f"=== Punitions de {eleve} ===\n")
        if eleve in punitions:
            for punition in punitions[eleve]:
                print(punition)
        else:
            print(colorama.Fore.GREEN + '[√] Aucune punition ( Continuez ainsi :D !)' + colorama.Fore.WHITE)
    else:
        print('Eleve introuvable')
    input("\nAppuyez sur Entrée pour continuer...")

    
################################################### PARTIE ELEVE ###########################################################
       

################################################### MENU PRINCIPALE  ###########################################################


# menu d'arrivee
def main():
    while True:
        clear_screen()
        afficher_titre()
        print("=== Menu Principal ===")
        print("1. Connexion direction")
        print("2. Connexion professeur")
        print("3. Espace élève")
        print("4. Quitter")
        
        choix = input("\nChoisissez une option : ")
        if choix == '1':
            direction_menu()
        elif choix == '2':
            professeur_menu()
        elif choix == '3':
            eleve_menu()
        elif choix == '4':
            break
        else:
            print("Choix invalide.")

################################################### MENU PRINCIPALE  ###########################################################





# ligne qui dis de ne pas executer le programme s'il est importer -_-
if __name__ == "__main__":
      main()





################################################### Crédits ###########################################################



# Coded by Ez² and Doraj ^^ 

# ( La version finale apres votre retour sera posté sur : https://github.com/Aminecool15 en colab avec https://github.com/D0rAj)    