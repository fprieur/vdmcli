Feature: Lancer les tests de stress
    Pour maintenir la qualité de performance
    Pour un projet donné
    Le cli devrait permettre de lancer de stress

    Scenario: Lancer des tests de stress
      Given Que des tests de stress existent dans le répertoire du projet
      When Quand je lance les tests de stress
      Then Je devrais voir les résultats des tests de stress
