def test_pass_fail(testdir):
    testdir.makepyfile("""
        def test_pass():
            assert 1 == 1
        
        def test_fail():
            assert 1 == 2
    """)

    result = testdir.runpytest()
    # print('+++' * 8, result)
    result.stdout.fnmatch_lines([
        '*.F', # . for Pass, F for Fail
        ])

    assert result.ret == 1