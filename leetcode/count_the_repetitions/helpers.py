def run_get_max_repetitions(solution_class: type, s1: str, n1: int, s2: str, n2: int):
    implementation = solution_class()
    return implementation.get_max_repetitions(s1, n1, s2, n2)


def assert_get_max_repetitions(result: int, expected: int) -> bool:
    assert result == expected
    return True
