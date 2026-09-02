def run_make_equal(solution_class: type, words: list[str]):
    implementation = solution_class()
    return implementation.make_equal(words)


def assert_make_equal(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
