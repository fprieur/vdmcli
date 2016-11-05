Feature: Lancer build jenkins
    Pour faciliter l'intégration continue
    pour un projet donnée
    on doit lancer des builds pré-configuré

    Scenario: Lancer un nouveau build dans jenkins
      Given Je suis un administrateur de jenkins
      When Quand je lance le nouveau build buildtoto
      Then On devrait voir que le build buildtoto a réussit
