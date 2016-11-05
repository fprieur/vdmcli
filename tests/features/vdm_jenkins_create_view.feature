Feature: Ajout view
    Pour faciliter l'affichage de jenkins
    pour un nouveau build
    un build peut être intégré à une view

    Scenario: Ajouter une nouvelle view dans jenkins
      Given Je suis un administrateur de jenkins
      When Quand on ajoute une nouvelle view nommée viewtoto
      Then On devrait retrouver la view nommée viewtoto
