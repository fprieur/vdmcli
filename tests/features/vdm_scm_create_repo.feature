Feature: Ajout depot
    Pour utiliser git
    un nouvel utilisateur
    doit avoir acces à un dépôt git

    Scenario: Ajouter un dépôt git dans le groupe test
      Given Je suis un administrateur du groupe
      When Ajoute dépôt avec le nom mondepottoto dans le groupe test
      Then Le dépôt mondepottoto doit se retrouver dans le groupe test
