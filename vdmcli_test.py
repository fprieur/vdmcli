if __name__ == '__main__':

    from minitest import *
    import vdmcli

    with test("create_repo"):
        with capture_output() as output:
            result = vdmcli.repo_webhook
        str(result).must_equal("repo create")
