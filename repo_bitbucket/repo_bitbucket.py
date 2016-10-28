# -*- coding: utf-8 -*-

from bitbucket.bitbucket import Bitbucket
import os


class Repo_bitbucket(object):
    def __init__(self):
        self.project_name = "reponame"

    # permet de créér des dépôts sur bitbucket
    def createRepo(self, repo_name, owner, project):
        bb = authBitbucket()
        repo = bb.repository.create(repo_name=repo_name,
                                    scm='git',
                                    private=True,
                                    owner=owner,
                                    project=project)
        print "success" if repo[0] else "error"

    # permet d'ajouter des services de type webhook sur bitbucket
    def createWebhook(self, repo_name, project, webhook_name, url):
        print "success" if repo[0] else "error"

    # permet d'ajouter un usager dans un groupe d'organisation
    def createUser(self, username):
        print "success" if repo[0] else "error"

    def authBitbucket(self):
        bba = Bitbucket(os.environ.get("BITBUCKET_USER"),
                        os.environ.get("BITBUCKET_PASS"))
        return bba
