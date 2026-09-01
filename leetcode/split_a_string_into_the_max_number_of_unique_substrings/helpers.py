def run_max_unique_split(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.max_unique_split(s)


def assert_max_unique_split(result: int, expected: int) -> bool:
    assert result == expected
    return True
