# -*- coding: utf-8 -*-

if __name__ == '__main__':

    from minitest import *
    import vdmcli

    import click
    from click.testing import CliRunner
    from mock import MagicMock
    from repo_bitbucket import repo_bitbucket

    # tester la création d'un nouveau dépôt avec nom
    with test("create_repo_with_repo_name"):
        repo_create_mock = repo_bitbucket.Repo_bitbucket()
        repo_create_mock.createRepo = MagicMock(return_value="success")
        result = repo_create_mock.createRepo("nomdepot")
        result.must_equal("success")

    # tester la création d'un nouveau dépôt sans nom
    with test("create_repo_without_repo_name"):
        repo_create_mock = repo_bitbucket.Repo_bitbucket()
        repo_create_mock.createRepo = MagicMock(return_value="error")
        result = repo_create_mock.createRepo()
        result.must_equal("error")
