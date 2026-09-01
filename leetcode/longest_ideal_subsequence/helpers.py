def run_longest_ideal_string(solution_class: type, s: str, k: int):
    implementation = solution_class()
    return implementation.longest_ideal_string(s, k)


def assert_longest_ideal_string(result: int, expected: int) -> bool:
    assert result == expected
    return True
