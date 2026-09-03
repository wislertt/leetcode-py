def run_odd_even_jumps(solution_class: type, arr: list[int]):
    implementation = solution_class()
    return implementation.odd_even_jumps(arr)


def assert_odd_even_jumps(result: int, expected: int) -> bool:
    assert result == expected
    return True
