# 🎓 Pronoob v4.0 – Simplifiez la gestion scolaire avec Python 

Bienvenue sur le git officiel de **Pronoob**, une version simplifiée de Pronote développée en Python. Ce projet, créé par deux élèves passionnés de NSI (Numérique et Sciences Informatiques), a pour objectif de proposer une solution facile à utiliser pour la gestion des emplois du temps, des notes et des devoirs des élèves.

<p align="center">
  <img src="https://github.com/user-attachments/assets/84c903cc-2d27-467c-83ce-449d20f8b818" alt="Pronoob Logo" width="200">
</p>

---

## **🌟** **Fonctionnalités principales**

Pronoob est conçu pour offrir trois espaces distincts, chacun adapté aux besoins spécifiques des utilisateurs :

### 🏫 **Pour l'administration**
| Fonctionnalités                 | Description                                         |
|---------------------------------|-----------------------------------------------------|
| 👥 Visualiser les listes d'élèves | Consultez la liste complète des élèves.            |
| 🧑‍🏫 Visualiser les listes de professeurs | Consultez la liste complète des professeurs.       |
| 🛠️ Consultation et modification des élèves | Gérez les informations des élèves facilement.      |
| 🔧 Consultation et modification des professeurs | Gérez les informations des professeurs facilement. |
---

### 👩‍🏫 **Pour les professeurs**
| Fonctionnalités                 | Description                                         |
|---------------------------------|-----------------------------------------------------|
| 👨‍🎓 Visualiser la liste des élèves | Consultez la liste des élèves de vos classes.      |
| ✏️ Modifier les informations des élèves | Modifiez les informations des élèves en cas de besoin. |
| 📄 Voir/Ajouter une absence      | Enregistrez ou consultez les absences des élèves.   |
| 📚 Voir/Ajouter un devoir        | Ajoutez des devoirs pour vos classes ou consultez ceux existants. |

---

### 🧑‍🎓 **Pour les élèves**
| Fonctionnalités                 | Description                                         |
|---------------------------------|-----------------------------------------------------|
| 🔍 Visualiser ses notes          | Accédez facilement à toutes vos notes.             |
| 📝 Visualiser ses devoirs        | Consultez les devoirs assignés par vos professeurs.|
| 📅 Visualiser son emploi du temps| Vérifiez votre emploi du temps détaillé.           |
| ❌ Visualiser ses punitions      | Consultez vos sanctions et remarques éventuelles.  |

---

## 🎥 Démonstration rapide
Découvrez Pronoob en action ! Voici un aperçu en GIF de son interface et de ses fonctionnalités principales :

![Pronoob Demo](path/to/demo.gif) *(Ajoutez le chemin vers votre fichier GIF)*

---

## 📚 Documentation 

### Dictionnaires principaux
Voici une description détaillée des structures de données utilisées dans **Pronoob**. Ces dictionnaires constituent l'épine dorsale du projet :

#### 1. **Élèves** **(`eleves`)**
Ce dictionnaire regroupe les informations des élèves : classe, notes, emploi du temps, etc.

```python
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
```

#### 2. **Professeurs (`professeurs`)**
Liste des enseignants avec leurs matières, emplois du temps et classes attribuées.

```python
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
```

#### 3. **Devoirs (`devoirs`)**
Devoirs à rendre par classe.

```python
devoirs = {
    '1G6': ['[+] Devoir de Mathématiques sur les équations  ', '[+] Devoir de Français sur un livre'],
    '1G5': ['[+] Devoir d\'Histoire sur la Révolution Française'],
    '1G4': ['[+] Devoir de SVT sur les écosystèmes']
}
```

#### 4. **Punitions (`punitions`)**
Enregistrement des punitions des élèves.

```python
punitions = {
    'Alice Dupont': [colorama.Fore.RED + "[X] Exclusion de cours" + colorama.Fore.WHITE],
    'Bob Martin': [colorama.Fore.RED + '[X] Parler pendant le cours' + colorama.Fore.WHITE]
}
```

---

## 🚀 Exécution
Pour exécuter **Pronoob**, il suffit de lancer le script principal :

```bash
python pronoob.py
```

Vous aurez alors accès au menu principal, où vous pourrez choisir votre espace (Direction, Professeur, ou Élève).

---

## 🛠️ Contribution
Les contributions sont les bienvenues ! Si vous avez des idées pour améliorer Pronoob, n'hésitez pas à ouvrir une *issue* ou à soumettre une *pull request*.

---

## 🏅 Crédits
Ce projet a été créé par :
- [Ez²](https://github.com/Aminecool15)
- [Doraj](https://github.com/D0rAj)


