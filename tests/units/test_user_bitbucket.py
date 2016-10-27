# -*- coding: utf-8 -*-

if __name__ == '__main__':

    from minitest import *
    import vdmcli

    import click
    from click.testing import CliRunner
    from mock import MagicMock
    from repo_bitbucket import repo_bitbucket

    print("\n--- début des tests unitaires pour ajout de user ---\n")

    # tester la création d'un nouveau user avec nom en paramètre
    with test("create_repo_with_repo_name"):
        repo_create_mock = repo_bitbucket.Repo_bitbucket()
        repo_create_mock.createUser = MagicMock(return_value="success")
        result = repo_create_mock.createUser("toto")
        result.must_equal("success")

    # tester la création d'un user sans nom en paramètre
    with test("create_repo_without_repo_name"):
        repo_create_mock = repo_bitbucket.Repo_bitbucket()
        repo_create_mock.createUser = MagicMock(return_value="error")
        result = repo_create_mock.createUser()
        result.must_equal("error")
