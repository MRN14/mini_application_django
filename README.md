# mini-application-python

Version **Python** du projet de gestion de magasin **mini-application** dans le cadre du recrutement en stage à la DGA

## Consigne

Réaliser une mini-application de gestion d’un petit magasin.
La technologie est libre, tant que cela reste dans l’écosystème web (Python, Node.js, React, ...).

### Fonctionnalités attendues

- [ ] Afficher la liste des produits (avec pour chaque produit : un nom, une qté, un fabricant, une référence)
- [ ] Système CRUD complet
- [ ] Sauvegarde des données (Une petite base de données relationnelles simples en SQLite)
- [ ] Rechercher un produit (par nom ou réf)
- [ ] Trie des produits

Tu es libre d’ajouter toute fonctionnalité ou amélioration que tu juges pertinente.

### Livrables attendus

Le projet doit être livré via un dépôt Github comprenant :

- Le code complet.
- un README contenant :
  - [ ] Les instructions pour lancer le projet
  - [ ] Tes choix techniques
  - [ ] Le limites connues
  - [ ] Les améliorations possibles.

#### Date limite et envoi

Le projet doit être remis 1 semaine avant le rendez-vous physique par mail avec le lien du dépôt.

## instructions

1. Assurez-vous d'avoir installé [python](https://www.python.org/downloads/)
2. Assurez-vous d'installer toutes les dépendances dans `requirement.txt` avec `pip`
3. Déplacez vous dans le dossier de l'application avec `cd mini_application_django`
4. Complétez le `.env.exemple`
5. Créez un administrateur avec `python manage.py createuser`
6. Lancez l'application sur le port `8000` avec `python manage.py runserver`
7. Ouvrez `http://localhost:8000/` dans votre navigateur
