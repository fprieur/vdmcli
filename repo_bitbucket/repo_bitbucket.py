from bitbucket.bitbucket import Bitbucket
import os


class Repo_bitbucket(object):
    def __init__(self):
        self.project_name = "reponame"

    def createRepo(self,repo_name, project):
        bb = Bitbucket(os.environ.get("BITBUCKET_USER"),
                       os.environ.get("BITBUCKET_PASS"))
        repo = bb.repository.create(repo_name=repo_name,
                                    scm='git',
                                    private=True,
                                    owner="testvdm",
                                    project=project)
        print "success" if repo[0] else "error"

    def createWebhook(self):
        return "self.name"

    def createUser(self, username):
        print username
