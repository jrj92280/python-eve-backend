def assert_lists_equivalent(expected, actual):
    for item in expected:
        assert item in actual

    for item in actual:
        assert item in expected
