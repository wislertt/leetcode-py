def run_find_derangement(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.find_derangement(n)


def assert_find_derangement(result: int, expected: int) -> bool:
    assert result == expected
    return True
