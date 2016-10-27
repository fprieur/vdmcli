if __name__ == '__main__':

    from minitest import *
    import vdmcli

    import click
    from click.testing import CliRunner

    runner = CliRunner()

    with test("create_repo_with_repo_name"):
        result = runner.invoke(vdmcli.cli,
                               ['repo_create', '--name', 'allotest'])
        result.output.must_equal(u"success\n")
    print result.ppl()
