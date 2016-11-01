# -*- coding: utf-8 -*-

if __name__ == '__main__':

    from minitest import *
    import vdmcli

    import click
    from click.testing import CliRunner
    from mock import MagicMock
    from vdm_bitbucket import vdm_bitbucket

    print("\n--- début des tests unitaires pour creations de webhook ---\n")

    # tester la création d'un nouveau dépôt avec nom
    with test("create_webhook_with_repo_name"):
        webhook_create_mock = vdm_bitbucket.Vdm_bitbucket()
        webhook_create_mock.createWebhook = MagicMock(return_value="success")
        result = webhook_create_mock.createWebhook("nomdepot",
                                                   "nomprojet",
                                                   "unwebhook",
                                                   "http://example.com")
        result.must_equal("success")

    # tester la création d'un nouveau dépôt sans nom
    with test("create_webhook_without_repo_name"):
        repo_create_mock = vdm_bitbucket.Vdm_bitbucket()
        repo_create_mock.createRepo = MagicMock(return_value="error")
        result = repo_create_mock.createRepo()
        result.must_equal("error")
