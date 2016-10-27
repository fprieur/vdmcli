# -*- coding: utf-8 -*-

if __name__ == '__main__':

    from minitest import *
    import vdmcli
    from vdm_jenkins import vdm_jenkins

    from mock import MagicMock

    print("\n--- début tests unitaires pour lancer des builds jenkins ---\n")

    # tester la création d'un nouveau dépôt avec nom
    with test("run_jenkins_build_with_correct_param"):
        vdm_jenkins_run_mock = vdm_jenkins.Vdm_jenkins()
        vdm_jenkins_run_mock.runBuild = MagicMock(return_value="success")
        result = vdm_jenkins_run_mock.runBuild("buildtoto")
        result.must_equal("success")

    # tester la création d'un nouveau dépôt sans nom
    with test("run_jenkins_build_without_param"):
        vdm_jenkins_run_mock = vdm_jenkins.Vdm_jenkins()
        vdm_jenkins_run_mock.runBuild = MagicMock(return_value="error")
        result = vdm_jenkins_run_mock.runBuild()
        result.must_equal("error")
