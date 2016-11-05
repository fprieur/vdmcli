Feature: Lancer les tests integration
    Pour maintenir la qualité du code
    Pour un projet donné
    Le cli devrait permettre de lancer des integration

    Scenario: Lancer des tests integration
      Given Que des tests integration existe dans le répertoire du projet
      When Quand je lance les tests integration
      Then Je devrais voir les résultats des tests integration
