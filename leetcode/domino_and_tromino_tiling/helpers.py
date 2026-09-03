def run_num_tilings(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.num_tilings(n)


def assert_num_tilings(result: int, expected: int) -> bool:
    assert result == expected
    return True
