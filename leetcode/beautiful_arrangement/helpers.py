def run_count_arrangement(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.count_arrangement(n)


def assert_count_arrangement(result: int, expected: int) -> bool:
    assert result == expected
    return True
