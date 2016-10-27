import ruamel.yaml as yaml


class Readyaml(object):
    def __init__(self):
        self.file = "reponame"

    def readUsers(self):
        with open("./../vdm.yaml") as stream:
            try:
                fichier_yaml = yaml.load(stream)
                users = fichier_yaml['users']
                return users
            except yaml.YAMLError as exc:
                return ("fichier yaml manquant")

    def readScm(self):
        with open("./../vdm.yaml") as stream:
            try:
                fichier_yaml = yaml.load(stream)
                scm = fichier_yaml['scm']
                return scm
            except yaml.YAMLError as exc:
                return ("fichier yaml manquant")

    def readTestUnitsDirectory(self):
        with open("./../vdm.yaml") as stream:
            try:
                fichier_yaml = yaml.load(stream)
                unitstestdir = fichier_yaml['tests'][0]['units']
                return unitstestdir
            except yaml.YAMLError as exc:
                return ("fichier yaml manquant")

    def readTestIntegrationDirectory(self):
        with open("./../vdm.yaml") as stream:
            try:
                fichier_yaml = yaml.load(stream)
                integrationtestdir = fichier_yaml['tests'][1]['integration']
                return integrationtestdir
            except yaml.YAMLError as exc:
                return ("fichier yaml manquant")
