def run_min_bit_flips(solution_class: type, start: int, goal: int):
    implementation = solution_class()
    return implementation.min_bit_flips(start, goal)


def assert_min_bit_flips(result: int, expected: int) -> bool:
    assert result == expected
    return True
