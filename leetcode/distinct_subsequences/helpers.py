def run_num_distinct(solution_class: type, s: str, t: str):
    implementation = solution_class()
    return implementation.num_distinct(s, t)


def assert_num_distinct(result: int, expected: int) -> bool:
    assert result == expected
    return True
