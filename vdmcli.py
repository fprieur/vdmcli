#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from repo_bitbucket import repo_bitbucket
from vdm_jenkins import vdm_jenkins


@click.group()
def cli():
    pass


@cli.command()
@click.option('--name', help='Repo name')
@click.option('--project', default="test", help='Project name')
def repo_create(name, project):
    """Créer une dépôt git"""
    b = repo_bitbucket.Repo_bitbucket()
    return b.createRepo(name, project)


@cli.command()
def repo_webhook():
    """Créer des webhook sur un dépôt git"""
    b = repo_bitbucket.Repo_bitbucket()
    return b.createWebhook()


@cli.command()
def repo_user():
    """Créer des usagers pour des groupes à l'intérieur d'une organisation
    bitbucket"""
    b = repo_bitbucket.Repo_bitbucket()
    return b.createUser("un user")


@cli.command()
@click.option('--name', help='Project name')
def jenkins_project(name):
    """Création d'un nouveau projet dans jenkins"""
    j = vdm_jenkins.Vdm_jenkins()
    return j.createProject(name)


@cli.command()
def jenkins_build():
    """Création d'un nouveau build dans un projet jenkins"""
    print("création d'une nouvelle pipeline")


@cli.command()
def jenkins_run():
    """Lancer le build d'un projet"""
    print("le build jenkins a été lancée")


@cli.command()
def tests_units():
    """Lancer l'éxécution des tests unitaires"""
    print("L'éxécution des tests unitaires a été lancée")


@cli.command()
def tests_integration():
    """Lancer l'éxécution des tests d'intégration"""
    print("L'éxécution des tests d'intégration a été lancée")


@cli.command()
def tests_load():
    """Lancer l'éxécution des tests de charge"""
    print("L'éxécution des tests de charge a été lancée")
