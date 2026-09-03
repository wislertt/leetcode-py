def run_find_integers(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.find_integers(n)


def assert_find_integers(result: int, expected: int) -> bool:
    assert result == expected
    return True
