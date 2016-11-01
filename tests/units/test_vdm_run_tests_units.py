# -*- coding: utf-8 -*-

if __name__ == '__main__':

    from minitest import *
    import vdmcli

    import click
    from click.testing import CliRunner
    from mock import MagicMock
    from vdm_runtest import vdm_runtest

    print("\n--- début des tests unitaires pour lancer units tests ---\n")

    # tester le lancement de tests unitaires avec un nom de répertoire
    with test("run_units_tests_with_dir"):
        vdm_runtest_mock = vdm_runtest.Vdm_runtest()
        vdm_runtest_mock.testsUnits = MagicMock(return_value="success")
        result = vdm_runtest_mock.testsUnits("toto")
        result.must_equal("success")

    # tester le lancement de tests unitaires sans un nom de répertoire
    with test("run_units_tests_without_dir"):
        vdm_runtest_mock = vdm_runtest.Vdm_runtest()
        vdm_runtest_mock.testsUnits = MagicMock(return_value="success")
        result = vdm_runtest_mock.testsUnits("toto")
        result.must_equal("success")
