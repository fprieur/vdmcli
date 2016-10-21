if __name__ == '__main__':

    from minitest import *
    import vdmcli

    import click
    from click.testing import CliRunner

    runner = CliRunner()

    with test("create_repo"):
        result = runner.invoke(vdmcli.cli,['repo_create'])
        result.output.must_equal(u"repo create\n")

    with test("create_webhook"):
        result = runner.invoke(vdmcli.cli,['repo_webhook'])
        result.output.must_equal(u"repo webhook create\n")
