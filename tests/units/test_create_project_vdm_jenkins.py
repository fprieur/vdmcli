# -*- coding: utf-8 -*-

if __name__ == '__main__':

    from minitest import *
    import vdmcli
    from vdm_jenkins import vdm_jenkins

    from mock import MagicMock

    print("\n--- début tests unitaires pour création de projet jenkins ---\n")

    # tester la création d'un nouveau dépôt avec nom
    with test("create_jenkins_project_with_project_name"):
        vdm_jenkins_create_mock = vdm_jenkins.Vdm_jenkins()
        vdm_jenkins_create_mock.createProject = MagicMock(return_value="success")
        result = vdm_jenkins_create_mock.createProject("projettoto")
        result.must_equal("success")

    # tester la création d'un nouveau dépôt sans nom
    with test("create_repo_without_repo_name"):
        vdm_jenkins_create_mock = vdm_jenkins.Vdm_jenkins()
        vdm_jenkins_create_mock.createProject = MagicMock(return_value="error")
        result = vdm_jenkins_create_mock.createProject()
        result.must_equal("error")
