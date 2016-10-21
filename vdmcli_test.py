if __name__ == '__main__':
    # import the minitest
    from minitest import *

    import vdmcli

    with test("create_repo"):
        vdmcli.repo_create.must_equal("repo create")
