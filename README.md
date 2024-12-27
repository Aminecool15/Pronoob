# 🎓 **Pronoob v3.0 - Nouvelle Version Améliorée**

Bienvenue dans **Pronoob v3.0**, une version avancée de notre projet. Cette mise à jour apporte des fonctionnalités encore plus puissantes, une interface améliorée, et des options de gestion simplifiées pour les élèves, les professeurs, et la direction.

---

## 🌟 **Nouvelles Fonctionnalités de la Version 3.0**

- **Gestion des élèves améliorée** : Accédez à toutes les informations des élèves, modifiez leurs notes et emplois du temps de manière fluide.
- **Suivi des devoirs et absences** : Ajoutez et consultez les devoirs et les absences des élèves par classe.
- **Sécurisation renforcée** : Des mots de passe spécifiques pour chaque utilisateur (élèves, professeurs, direction) garantissent une sécurité optimale.
- **Menu Direction** : Nouveau menu pour la direction, permettant une gestion complète des élèves et professeurs avec des options pour consulter et modifier les informations.
- **Interaction avec les professeurs** : Professeurs peuvent facilement gérer les devoirs et les absences des élèves.

---

## 🚀 **Lancer Pronoob**

Pour démarrer **Pronoob** version 3.0, exécutez simplement le script Python :

```bash
python pronoob.py
```

---

## 📚 **Documentation**

### Exemple de code pour ajouter un cours à un élève :

```python
def ajout_emploi_temps(nom):
    jour = input("Entrez le jour de la semaine : ")
    cours = input("Entrez le cours : ")
    eleves[nom]['emploi_temps'][jour] = cours
    print(f"Emploi du temps mis à jour pour {nom}.")
```

**☝️ Cette fonction permet de mettre à jour l'emploi du temps d'un élève en ajoutant un cours pour un jour spécifique. L'élève sera informé que son emploi du temps a été modifié.**

### Exemple de code pour modifier les punitions d'un élève :

```python
def ajouter_absence():
    choix = input("Appuyer sur 1 pour Consulter ou sur 2 pour Modifier: ")
    
    if choix == "1":
        classe = input("Entrez la classe : ")
        # Supposons que nous avons une liste d'absences par classe sous forme d'un dictionnaire
        absences = {
            "1A": ["John Doe", "Jane Smith"],
            "2B": ["Paul Dupont", "Marie Martin"]
        }
        
        if classe in absences:
            print(f"Absences pour la classe {classe} : {', '.join(absences[classe])}")
        else:
            print(f"Aucune absence enregistrée pour la classe {classe}.")
    
    if choix == "2":
        classe = input("Entrez la classe : ")
        eleve = input("Entrez le nom de l'élève à ajouter : ")
        
        # Liste d'absences pour chaque classe
        absences = {
            "1A": ["John Doe", "Jane Smith"],
            "2B": ["Paul Dupont", "Marie Martin"]
        }
        
        if classe in absences:
            absences[classe].append(eleve)
            print(f"Absence de {eleve} ajoutée à la classe {classe}.")
        else:
            absences[classe] = [eleve]
            print(f"La classe {classe} n'existait pas. Elle a été créée et {eleve} a été ajouté.")


```

**☝️ Cette fonction permet de gérer les absences des élèves, en offrant une option pour consulter les absences existantes ou en ajouter de nouvelles.**

---

## 🏅 **Crédits**

Ce projet a été réalisé par :
- [Ez²](https://github.com/Aminecool15)
- [Doraj](https://github.com/D0rAj)

---

## 📷 **Screenshots**

<p style="text-align: center;">
  <img src="https://github.com/user-attachments/assets/a118636a-ec91-4e18-882b-5fd7e028e6a9" alt="Image 1" width="400" />
  <br />
  <span style="display: block; font-size: 24px;">👇</span>
  <br />
  <img src="https://github.com/user-attachments/assets/eddb11e3-5a8b-4a8b-94fc-b85b2ea104da" alt="Image 2" width="400" />
</p>





---

