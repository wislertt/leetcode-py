def run_minimum_delete_sum(solution_class: type, s1: str, s2: str):
    implementation = solution_class()
    return implementation.minimum_delete_sum(s1, s2)


def assert_minimum_delete_sum(result: int, expected: int) -> bool:
    assert result == expected
    return True
