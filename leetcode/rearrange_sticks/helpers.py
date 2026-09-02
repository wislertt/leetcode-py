def run_rearrange_sticks(solution_class: type, n: int, k: int):
    implementation = solution_class()
    return implementation.rearrange_sticks(n, k)


def assert_rearrange_sticks(result: int, expected: int) -> bool:
    assert result == expected
    return True
