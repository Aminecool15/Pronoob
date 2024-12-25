# 🎓 Pronoob v2.0 - Version Améliorée

Bienvenue dans la deuxième version de **Pronoob**, l'outil de gestion des notes et des emplois du temps des élèves, maintenant plus puissant et encore plus simple à utiliser. Cette mise à jour apporte de nouvelles fonctionnalités, une meilleure interface et une gestion plus fluide des données.

---

## 🌟 Fonctionnalités principales

- **Gestion des élèves** : Ajoutez, modifiez et consultez les élèves, leurs notes et leurs emplois du temps.
- **Gestion des professeurs** : Visualisez et modifiez les professeurs, leurs matières et leurs emplois du temps.
- **Suivi des absences et punitions** : Ajoutez et consultez les absences et les punitions des élèves.
- **Gestion des devoirs** : Consultez et ajoutez les devoirs des élèves par classe.
- **Sécurisation** : Des mots de passe sont désormais requis pour accéder aux menus des professeurs et de la direction.

---

## 🚀 Lancer Pronoob

Pour démarrer **Pronoob** version 2.0, lancez simplement le script Python :

```bash
python pronoob.py
```

---

## 📚 Documentation

### Exemple de code pour ajouter un élève et gérer ses informations :

```python
def modifier_notes(choix):
    # Demander la nouvelle note
    nouvelle_note = float(input("Entrez la nouvelle note : "))
    
    # Mise à jour de la note de l'élève choisi
    eleves[choix]['note'] = nouvelle_note
    
    # Confirmation de la mise à jour
    print(f"La note de l'élève {choix} a été modifiée à {nouvelle_note}.")

```

**☝️ Cette fonction permet de modifier la note d'un élève. Elle demande à l'utilisateur d'entrer une nouvelle note et met à jour l'entrée correspondante dans la liste des élèves. Une confirmation est ensuite affichée pour indiquer que la note a été modifiée avec succès.**

---

## 🏅 Crédits

Ce projet a été réalisé par :
- [Ez²](https://github.com/Aminecool15)
- [Doraj](https://github.com/D0rAj)

---

## 📷 Screenshot

![image](https://github.com/user-attachments/assets/91c7d585-29bc-4cf1-b359-9401ae111475)


---

**Pronoob** v2.0 continue d'évoluer et reste fidèle à son objectif : offrir un outil simple mais puissant pour la gestion scolaire. Profitez des nouvelles fonctionnalités et gérez vos classes avec plus de facilité que jamais !
