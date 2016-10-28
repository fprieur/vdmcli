### Description
Le projet est un client de type commandline qui permet d'éxécuter plusieurs tâches redondantes dans un pipeline de déploiement d'un projet.

### Exigences fonctionnelles
* Le code du projet doit se trouver dans un repertoire /src
* Un fichier nommé vdm.yaml doit se trouver à la racine de votre projet
* pour l'utilisation de bitbucket, vous devez configurer certaines variables d'environnement

---

### Installation

#### Pré-requis d'installation
* pip
* git
* python 2.7+

#### Installer les dépendances du projet
`$ pip install -r requirements.txt`

#### Préparer l'installation du projet
`$ python setup.py install`

#### Pour installer le projet
`$ pip install --editable .`

#### Valider l'installation
`$ vdmcli --help`<br>
Vous devriez voir les commandes disponibles
<br>
Les commandes avec un astérix ne sont pas encore complétement implémentées

#### Pour l'interaction avec Bitbucket
vous devez ajouter les variables d'environnement suivante
* BITBUCKET_USER
* BITBUCKET_PASS

---

### Tests

#### Pour lancer les tests du projet
se positionner à la racine du projet <br>
`$ ./runtest.sh` <br>
(le fichier doit être exécutable)

---
