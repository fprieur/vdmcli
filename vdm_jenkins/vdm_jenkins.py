# -*- coding: utf-8 -*-
import jenkins


class Vdm_jenkins(object):
    def __init__(self):
        self.jenkins_url = "http://localhost:8080"

    def createBuild(self, build_name):
        try:
            server = self.authJenkins()
            server.create_job(build_name, jenkins.EMPTY_CONFIG_XML)
            print "success"
        except Exception, e:
            print ("erreur : " + str(e))

    def createView(self, view_name):
        try:
            server = self.authJenkins()
            server.create_view(view_name, jenkins.EMPTY_VIEW_CONFIG_XML)
            print "success"
        except Exception, e:
            print ("erreur : " + str(e))

    def runBuild(self, build_name):
        #  to be implement
        print "success" if build_name else "error"


    def authJenkins(self):
        server = jenkins.Jenkins("http://localhost:8080",
                                 username="fred",
                                 password="fred")
        return server
