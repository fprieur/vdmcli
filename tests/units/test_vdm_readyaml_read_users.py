# -*- coding: utf-8 -*-

if __name__ == '__main__':

    from minitest import *
    import vdmcli
    from vdm_readfile import vdm_readfile

    from mock import MagicMock

    print("\n--- début tests unitaires pour la lecture des usager dans le fichier ---\n")

    # tester la création d'un nouveau dépôt avec nom
    with test("create_jenkins_build_with_correct_param"):
        vdm_readfile_read_users_mock = vdm_readfile.Readfile()
        vdm_readfile_read_users_mock.readUsers = MagicMock(return_value=["toto"])
        result = vdm_readfile_read_users_mock.readUsers()
        result.must_equal(["toto"])
