# -*- coding: utf-8 -*-
from lettuce import step


@step(u'Given Je suis un administrateur du groupe')
def given_je_suis_un_administrateur_du_depot(step):
    assert True, 'This step must be implemented'


@step(u'When Ajoute utilisateur toto dans le groupe test')
def when_ajoute_utilisateur_toto_dans_le_groupe_test(step):
    assert True, 'This step must be implemented'


@step(u'Then Utilisateur toto se retrouve dans le groupe test')
def then_utilisateur_toto_se_retrouve_dans_le_groupe_test(step):
    assert True, 'This step must be implemented'
