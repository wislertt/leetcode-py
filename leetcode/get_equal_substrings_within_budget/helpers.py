def run_equal_substring(solution_class: type, s: str, t: str, max_cost: int):
    implementation = solution_class()
    return implementation.equal_substring(s, t, max_cost)


def assert_equal_substring(result: int, expected: int) -> bool:
    assert result == expected
    return True
