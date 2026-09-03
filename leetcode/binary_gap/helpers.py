def run_binary_gap(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.binary_gap(n)


def assert_binary_gap(result: int, expected: int) -> bool:
    assert result == expected
    return True
