# 🎓 **Pronoob v3.0 - Nouvelle Version Améliorée**

Bienvenue dans **Pronoob v3.0**, la version la plus avancée de notre système de gestion des notes et emplois du temps. Cette mise à jour apporte des fonctionnalités encore plus puissantes, une interface améliorée, et des options de gestion simplifiées pour les élèves, les professeurs, et la direction.

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
        # Affichage des absences existantes
        # ...
    if choix == "2":
        classe = input("Entrez la classe : ")
        # Ajout d'une nouvelle absence
        # ...
```

**☝️ Cette fonction permet de gérer les absences des élèves, en offrant une option pour consulter les absences existantes ou en ajouter de nouvelles.**

---

## 🏅 **Crédits**

Ce projet a été réalisé par :
- [Ez²](https://github.com/Aminecool15)
- [Doraj](https://github.com/D0rAj)

---

## 📷 **Screenshots**

![image](https://github.com/user-attachments/assets/91c7d585-29bc-4cf1-b359-9401ae111475)

---

La version 3.0 de **Pronoob** vous offre plus de contrôle et de sécurité pour gérer toutes les informations liées aux élèves et aux professeurs. C'est une version encore plus complète et adaptée aux besoins de gestion scolaire.
