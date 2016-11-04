Feature: Ajout utilisateur
    Pour utiliser bitbucket
    un nouvel utilisateur
    doit être dans un groupe

    Scenario: Ajouter un nouvel utilisateur dans le groupe test
      Given Je suis un administrateur du groupe
      When Ajoute utilisateur toto dans le groupe test
      Then Utilisateur toto se retrouve dans le groupe test
