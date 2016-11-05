# -*- coding: utf-8 -*-
from lettuce import step


@step(u'Given Je suis un administrateur de jenkins')
def given_je_suis_un_administrateur_de_jenkins(step):
    assert True, 'This step must be implemented'


@step(u'When Quand on ajoute un nouveau build nommé buildtoto')
def when_quand_on_ajoute_un_nouveau_build_nomme_buildtoto(step):
    assert True, 'This step must be implemented'


@step(u'Then On devrait retrouver un nouveau build nommé buildtoto')
def then_on_devrait_retrouver_un_nouveau_build_nomme_buildtoto(step):
    assert True, 'This step must be implemented'
