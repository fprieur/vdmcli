#### Prérequis
* pip => pour la gestion des packages python
* virtualenv et virtualenvwrapper => pour l'installation et la création du projet

---

#### Installer les dépendances du projet
`$ pip install -r requirements.txt`

---

#### Pour installer le projet
`$ pip install --editable .`

---

#### Pour lancer les tests du projet
se positionner à la racine du projet 
`$ python -m vdmcli_test`

---

#### Pour lancer les tests automatiquement à chaque modification des fichiers souce
Ouvrir un autre fenetre de terminal, se positionner dans le répertoire
et lancer la commande suivante pour installer pywatch<br>
`$ pip install pywatch`
<br><br>
pywatch est un utilitaire permettant d'éxécuter une commande lorsqu'un fichier est modifié
<br>
#### Pour lancer les tests automatiquement à chaque modification des fichiers source .py
`$ pywatch "python -m vdmcli_test" *.py`


