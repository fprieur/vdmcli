# -*- coding: utf-8 -*-

if __name__ == '__main__':

    from minitest import *
    import vdmcli

    import click
    from click.testing import CliRunner
    from mock import MagicMock
    from vdm_runtest import vdm_runtest

    print("\n--- début des tests unitaires pour lancer les tests de stress ---\n")

    # simulation que la réponse est positive
    with test("run_load_test"):
        vdm_runtest_mock = vdm_runtest.Vdm_runtest()
        vdm_runtest_mock.testsLoad = MagicMock(return_value="success")
        result = vdm_runtest_mock.testsLoad()
        result.must_equal("success")

    # simulation que la réponse est négative
    with test("run_integration_tests_without_dir"):
        vdm_runtest_mock = vdm_runtest.Vdm_runtest()
        vdm_runtest_mock.testsLoad = MagicMock(return_value="error")
        result = vdm_runtest_mock.testsLoad()
        result.must_equal("error")
