Feature: Ajout build
    Pour utiliser jenkins dans un projet
    pour un nouveau projet
    un nouveau build doit être créé

    Scenario: Ajouter un nouveau build dans jenkins
      Given Je suis un administrateur de jenkins
      When Quand on ajoute un nouveau build nommé buildtoto
      Then On devrait retrouver un nouveau build nommé buildtoto
