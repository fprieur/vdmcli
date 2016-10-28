# -*- coding: utf-8 -*-

if __name__ == '__main__':

    from minitest import *
    import vdmcli
    from vdm_readyaml import vdm_readyaml

    from mock import MagicMock

    print("\n--- début tests unitaires pour la lecture des usager dans le fichier yaml ---\n")

    # tester la création d'un nouveau dépôt avec nom
    with test("create_jenkins_build_with_correct_param"):
        vdm_readyaml_read_users_mock = vdm_readyaml.Readyaml()
        vdm_readyaml_read_users_mock.readUsers = MagicMock(return_value=["toto"])
        result = vdm_readyaml_read_users_mock.readUsers()
        result.must_equal(["toto"])
