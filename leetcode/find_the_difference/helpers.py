def run_find_the_difference(solution_class: type, s: str, t: str):
    implementation = solution_class()
    return implementation.find_the_difference(s, t)


def assert_find_the_difference(result: str, expected: str) -> bool:
    assert result == expected
    return True
