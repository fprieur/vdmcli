Feature: Lancer les tests unitaires
    Pour maintenir la qualité du code
    Pour un projet donné
    Le cli devrait permettre de lancer des unitaires

    Scenario: Lancer des tests unitaires
      Given Que des tests unitaires existe dans le répertoire d'un projet
      When Quand je lance les tests unitaires
      Then Je devrais voir les résultats des tests unitaires
