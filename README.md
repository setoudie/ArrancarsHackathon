# Instructions pour cloner et installer les dépendances Python

## 1. Cloner le dépôt

Pour commencer, clonez le dépôt GitHub sur votre machine locale :
```bash
git clone https://github.com/setoudie/ArrancarsHackathon.git
```

## 2. Créer un environnement virtuel

Assurez-vous d'avoir la version de Python définie dans le fichier `runtime.txt`.

Si vous utilisez **pyenv** pour gérer la version de Python, exécutez les commandes suivantes :
```bash
pyenv install $(cat runtime.txt)        # Installe la version Python spécifiée dans runtime.txt
pyenv local $(cat runtime.txt | sed 's/python-//')  # Utilise cette version pour le projet
```

Ensuite, créez un environnement virtuel et activez-le :
```bash
python -m venv env
source env/bin/activate  # Sur Windows, utilisez `.\env\Scripts\activate`
```

## 3. Installer les dépendances

Une fois l'environnement virtuel activé, installez les dépendances avec :
```bash
pip install -r requirements.txt
```

Cela installera toutes les bibliothèques nécessaires pour le projet.

## 4. Créer une branche pour travailler

Avant de commencer à développer, créez une branche dédiée pour votre tâche ou fonctionnalité :
```bash
git checkout -b <nom-de-votre-branche>
```

Par exemple, si vous travaillez sur une nouvelle fonctionnalité, vous pourriez nommer votre branche comme suit :
```bash
git checkout -b feature/ajouter-analyse-sentiment
```

## 5. Valider et pousser vos changements

Après avoir apporté vos modifications, n'oubliez pas de commettre et pousser votre branche :
```bash
git add .
git commit -m "Description des changements apportés"
git push origin <nom-de-votre-branche>
```

## 6. Créer une Pull Request (PR)

Lorsque vous avez terminé vos modifications et que vous souhaitez les intégrer dans la branche principale, ouvrez une **Pull Request** (PR) sur GitHub.

## Bonnes pratiques

- Travaillez toujours dans une branche spécifique à une tâche.
- Faites des commits fréquents avec des messages clairs.
- Avant de créer une PR, assurez-vous d'avoir récupéré les dernières modifications depuis la branche principale (par exemple, `main`) :
  ```bash
  git pull origin main
  ```

---

Si vous avez des questions ou si vous rencontrez des problèmes, n'hésitez pas à demander de l'aide dans le canal Slack (ou tout autre outil de communication de l’équipe).

Bonne chance à toute l’équipe pour la réalisation du projet !
```

---

### **Points à vérifier avant de partager :**
1. Assurez-vous de remplacer `<URL_DU_DEPOT>` par l'URL réelle du dépôt GitHub.
2. Vous pouvez ajouter des détails supplémentaires concernant les outils ou processus spécifiques si nécessaire.

Ce fichier README est conçu pour être simple et direct, pour que vos collègues puissent démarrer rapidement avec le projet.