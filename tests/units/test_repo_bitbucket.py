if __name__ == '__main__':

    from minitest import *
    import vdmcli

    import click
    from click.testing import CliRunner
    from mock import MagicMock
    from repo_bitbucket import repo_bitbucket

    runner = CliRunner()

    # tester la création d'un nouveau dépôt avec un nom correct sans nom de projet
    with test("create_repo_with_repo_name"):
        repo_create_mock = repo_bitbucket.Repo_bitbucket()
        repo_create_mock.createRepo = MagicMock(return_value="success")
        result = repo_create_mock.createRepo("nomdepot")
        #result = runner.invoke(vdmcli.cli,
        #                       ['repo_create', '--name', 'allotest'])
        if (repo_create_mock.createRepo.assert_called_once_with("nomdepot")):
            result.must_equal("success")
    print result.ppl()
