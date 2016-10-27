# -*- coding: utf-8 -*-
import jenkins


class Vdm_jenkins(object):
    def __init__(self):
        self.jenkins_url = "http://localhost:8080"

    def createProject(self, project_name):
        #  to be implement
        print "success" if project_name else "error"

    def createBuild(self, project_name, build_name):
        #  to be implement
        print "success" if project_name else "error"

    def runBuild(self, build_name):
        #  to be implement
        print "success" if build_name else "error"
