import os
import fade  # type: ignore
import colorama

faded_text = fade.greenblue("""
 ____                              _             _____ 
|  _ \ _ __ ___  _ __   ___   ___ | |__   __   _|___ / 
| |_) | '__/ _ \| '_ \ / _ \ / _ \| '_ \  \ \ / / |_ \ 
|  __/| | | (_) | | | | (_) | (_) | |_) |  \ V / ___) |
|_|   |_|  \___/|_| |_|\___/ \___/|_.__/    \_(_)____/ 
                               
                             version 3.0
""") 

os.system('mode 170,30') #pour pouvoir consulter pleinement les emplois du temps ^^

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def afficher_titre():
    clear_screen()
    print(faded_text) 



###################################################  Données pour partie direction ###########################################################

# on avait un peu la flemme de tt remplir mais l'essentiel est la
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
    'Monsieur Durand': {'matière': 'Mathématiques', 'emploi_temps': {}, 'classes': []},
    'Madame Dupuis': {'matière': 'Français', 'emploi_temps': {}, 'classes': []},
    'Monsieur Leroy': {'matière': 'Histoire', 'emploi_temps': {}, 'classes': []}
}

# les devoirs par classe
devoirs = {
    '1G6': ["[+] Devoir de Mathématiques sur les équations  ", "[+] Devoir de Français sur un livre"],
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
    if mdp != "admin123":  # <---- ptit mdp :3
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


# affichage des élèves (sous forme de tableaux c mieux :3)
def afficher_eleves(pause=True):
    print("\n=== Liste des élèves ===")
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
def afficher_professeurs():
    print("\n=== Liste des professeurs ===")
    print(f"{'Nom':<25} {'Matière':<15} {'Classes':<20} {'Emploi du temps':<30}")
    print("-" * 80)
    for nom, infos in professeurs.items():
        classes = ", ".join(infos['classes']) if infos['classes'] else "Aucune"
        emploi_temps = ", ".join([f"{jour}: {cours}" for jour, cours in infos['emploi_temps'].items()]) if infos['emploi_temps'] else "Vide"
        print(f"{nom:<25} {infos['matière']:<15} {classes:<20} {emploi_temps:<30}")
    input("\nAppuyez sur Entrée pour continuer...")


# pour modifier les infos des eleves
def modifier_eleves():
    while True:
        afficher_eleves(False)
        nom = input("\nEntrez le nom de l'élève pour modifier (ou 'q' pour quitter) : ")
        if nom == 'q':
            return  # Retourne au menu précédent j'ai oublier de le mètre depuis je galerer XD # mdrr
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
            # notes
            if choix == '1':
                question = input("Appuyer sur 1 pour Consulter ou sur 2 pour Modifier : ")
                if question == "1":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(faded_text)
                    print('=== Listes des notes ===')
                    if len(eleves[nom]['notes']) > 0:
                        for note in eleves[nom]['notes']:
                            print(f"- {note}")
                    else:
                        print(colorama.Fore.YELLOW + "\n[!] Aucune note " + colorama.Style.RESET_ALL)
                        input("\nAppuyez sur Entrée pour continuer...")
    
                if question == "2":
                    matiere = input("Entrez la matiere : ")
                    note = float(input("Entrez la note : "))
                    notes = eleves[nom]['notes']
                    notes.append(f"{matiere} : {note}")
                    eleves[nom]['notes'] = notes
            # emploi du temps
            elif choix == '2':
                ajout_emploi_temps(nom)
            # classe
            elif choix == '3':
                nouvelle_classe = input("Entrez la nouvelle classe : ")
                eleves[nom]["classe"] = nouvelle_classe
            # punitions
            elif choix == '4':
                question = input("Appuyer sur 1 pour Consulter ou sur 2 pour Modifier : ")
                if question == "1":
                    afficher_titre()
                    print(f"=== Liste des punitions pour {nom}  ===")
                    if nom in punitions:
                        for punition in punitions[nom]:
                            print(colorama.Fore.RED +"\n"+ punition + colorama.Fore.WHITE)
                    else:
                        print(colorama.Fore.GREEN + "\n[√] Aucune (Continuez Ainsi ! :D )" + colorama.Fore.WHITE)
                    input("\nAppuyez sur Entrée pour continuer...")
                    return
                if question == "2":
                    punition = input("Description de la punition : ")
                    if nom in punitions:
                        punitions[nom].append("[X] " + punition)
                    else:
                        punitions[nom] = ["[X] " + punition]
                    input("\nAppuyez sur Entrée pour continuer...")
                    return
            else:
                return
            clear_after_modification()

        else:
            clear_screen()
            print(colorama.Fore.RED + "Élève non trouvé ! Ressaisissez le nom concerné !" + colorama.Fore.GREEN )


# modifier les infos des profs
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
            os.system('cls' if os.name == 'nt' else 'clear')
            print(faded_text) 
            print(colorama.Fore.GREEN +  f"[√] Mise à jour effectuée pour {nom} "+colorama.Fore.WHITE) #
        else:
            print("Professeur non trouvé.")


# ajouter un cours pour un élève
def ajout_emploi_temps(nom):
    jour = input("Entrez le jour de la semaine : ")
    cours = input("Entrez le cours : ")
    eleves[nom]['emploi_temps'][jour] = cours
    print(f"Emploi du temps mis à jour pour {nom}.")


# ajouter un cours pour un professeur
def ajout_emploi_temps_prof(nom):
    jour = input("Entrez le jour de la semaine : ")
    cours = input("Entrez le cours : ")
    professeurs[nom]['emploi_temps'][jour] = cours
    print(colorama.Fore.GREEN + f"[√] Emploi du temps mis à jour pour {nom}." + colorama.Fore.WHITE )


# pour dire que tt est bon a la fin
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
    choix = input("Appuyer sur 1 pour Consulter ou sur 2 pour Modifier : ")
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
        text = colorama.Fore.RED
        trouver = False
        for personne in punitions:
            if personne == eleve:
                for punition in punitions[personne]:
                    if "Absence" in punition:
                        trouver = True
                        text += f"-[X]Absence en {punition.split()[1]} le {punition.split()[2]}\n"
        if not trouver:
            print(colorama.Fore.GREEN + '[√] Aucune absence ( Continuez ainsi :D !)' + colorama.Fore.WHITE)
        else:
            print(text + colorama.Fore.WHITE)
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
            punitions[eleve].append(colorama.Fore.RED + f'Absence {matiere} {date}' + colorama.Fore.WHITE)
        else:
            punitions[eleve] = [colorama.Fore.RED + f'Absence {matiere} {date}' + colorama.Fore.WHITE]
        print(colorama.Fore.GREEN + f"\nL'absence du {date} en {matiere} a ete attribue pour {eleve}" + colorama.Fore.WHITE)
        input("\nAppuyez sur Entrée pour continuer...")


def ajouter_devoir():
    choix = input("Appuyer sur 1 pour Consulter ou sur 2 pour Modifier: ")
    if choix == "1":
        classe = input('Entrez la classe : ')
        if classe not in devoirs:
            print(colorama.Fore.YELLOW + "\nCette classe n'a pas de devoir" + colorama.Fore.WHITE)
            input("\nAppuyez sur Entrée pour continuer...")
            return
        print("\n=== Liste des devoirs ===")
        for devoir in devoirs[classe]:
            print(f"-{devoir}")
        input("\nAppuyez sur Entrée pour continuer...")
        return

    if choix == "2":
        classe = input('Entrez la classe : ')
        matiere = input('Entrez la matiere : ')
        consigne = input('Entrez la consigne : ')
        devoir = f"[+] Devoir de {matiere} : {consigne}"
        if classe in devoirs:
            devoirs[classe].append(devoir)
        else:
            devoirs[classe] = [devoir]
        print(colorama.Fore.GREEN + f'\n[√] Le devoir "{devoir}" a ete attribue pour la classe {classe}' + colorama.Fore.WHITE)
        input("\nAppuyez sur Entrée pour continuer...")
        return



################################################### PARTIE PROFESSEUR ###########################################################




################################################### PARTIE ELEVE ###########################################################


# Menu élève
def eleve_menu():
    mdp = input("Entrez le mot de passe élève : ")
    if mdp != "A":
        print("Mot de passe incorrect.")
        return

    while True:
        clear_screen()
        afficher_titre()
        print("\n=== Menu Élève ===")
        print("1. Visualiser ses notes")
        print("2. Visualiser ses devoirs")
        print("3. Visualiser son emploi du temps")
        print("4. Visualiser ses punitions")
        print("5. Déconnexion")
        
        choix = input("\nChoisissez une option : ")

        # notes
        if choix == '1':
            eleve = input("Entrez votre nom : ")
            if eleve in eleves:
                notes = eleves[eleve].get("notes", [])
                clear_screen()
                afficher_titre()
                print(f"\n=== Notes de {eleve} === : ", end="")
                if len(notes) > 0:
                    print("\n")
                    for note in notes:
                        print(note)
                else:
                    print(colorama.Fore.YELLOW + '\n[+] Aucune note'+ colorama.Fore.WHITE )
            else:
                print("Élève non trouvé.")
            input("\nAppuyez sur Entrée pour continuer...")

        # devoirs
        elif choix == '2':
            eleve = input("Entrez votre nom : ")
            if eleve in eleves:
                classe = eleves[eleve]["classe"]
                afficher_titre()
                if classe in devoirs:
                    print(f"=== Devoirs pour {classe} ===\n")
                    for devoir in devoirs[classe]:
                        print(devoir)
                else:
                    print(f"=== Devoirs pour {classe} ===\n" + colorama.Fore.YELLOW + "\n[+] Vous n'avez pas de devoir :D\n" + colorama.Fore.WHITE)  
            else:
                print("Élève non trouvé.")
            input("\nAppuyez sur Entrée pour continuer...")

        # emploi du temps
        elif choix == '3':
            eleve = input("Entrez votre nom : ")
            afficher_titre()
            if eleve in eleves:
                classe = eleves[eleve].get("classe", "Classe inconnue")
                print(f"=== Emploi du temps de la classe {classe} === :")
                if eleves[eleve]['emploi_temps'] != {}:
                    emploi_temps = eleves[eleve].get("emploi_temps", {})
                    for jour, cours in emploi_temps.items():
                        print(f"\n{jour} : {cours}")
                else :
                    print(colorama.Fore.YELLOW + "\n[+] Vous n'avez pas cours !"+ colorama.Fore.WHITE)
                    
                input("\nAppuyez sur Entrée pour continuer...")   
  
        # punitions
        elif choix == '4':
            eleve = input("Entrez votre nom : ")
            afficher_titre()
            if eleve in punitions:
                print(f"=== Punitions de {eleve} === : \n")
                for punition in punitions[eleve]:
                    print(punition)
                input("\nAppuyez sur entree pour continuer...")
            else:
                print(colorama.Fore.GREEN + '[√] Aucune punition ( Continuez ainsi :D !)' + colorama.Fore.WHITE + "\n")
                input("\nAppuyez sur Entrée pour continuer...")

        # deco
        elif choix == '5':
            print("Déconnexion réussie.")
            break
        else:
            print("Choix invalide.")
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
        
        choix = input("Choisissez une option : ")
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