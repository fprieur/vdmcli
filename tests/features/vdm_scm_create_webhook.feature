Feature: Ajout webhook
    Pour utiliser bitbucket
    avec un serveur d'intégration continue
    un dépôt git bitbucket doit avoir un webhook associé

    Scenario: Ajouter un nouveau webhook dans un dépôt bitbucket
      Given Je suis un administrateur du groupe
      When Ajoute un webhook sur le dépôt bitbucket
      Then Le dépôt devrait avoir un nouveau webhook
