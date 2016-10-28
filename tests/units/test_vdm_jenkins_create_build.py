# -*- coding: utf-8 -*-

if __name__ == '__main__':

    from minitest import *
    import vdmcli
    from vdm_jenkins import vdm_jenkins

    from mock import MagicMock

    print("\n--- début tests unitaires pour création de projet jenkins ---\n")

    # tester la création d'un nouveau dépôt avec nom
    with test("create_jenkins_build_with_correct_param"):
        vdm_jenkins_create_build_mock = vdm_jenkins.Vdm_jenkins()
        vdm_jenkins_create_build_mock.createBuild = MagicMock(return_value="success")
        result = vdm_jenkins_create_build_mock.createBuild("projettoto",
                                                           "buildtoto")
        result.must_equal("success")

    # tester la création d'un nouveau dépôt sans nom
    with test("create_jenkins_build_without_param"):
        vdm_jenkins_create_build_mock = vdm_jenkins.Vdm_jenkins()
        vdm_jenkins_create_build_mock.createBuild = MagicMock(return_value="error")
        result = vdm_jenkins_create_build_mock.createBuild()
        result.must_equal("error")
