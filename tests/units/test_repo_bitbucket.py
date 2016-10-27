if __name__ == '__main__':

    from minitest import *
    import vdmcli

    import click
    from click.testing import CliRunner

    @click.group()
    def cli():
        pass

    @cli.command()
    @click.option('--name', help='Repo name')
    @click.option('--project', default="test", help='Project name')
    def repo_create(name, project):
        b = repo_bitbucket.Repo_bitbucket()

        runner = CliRunner()
        result = runner.invoke(cli, ['--name', 'allotest'])
        assert result.exit_code == "success"
        assert 'Debug mode is on' in result.output
        assert 'Syncing' in result.output
