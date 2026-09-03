def run_min_swaps_couples(solution_class: type, row: list[int]):
    implementation = solution_class()
    return implementation.min_swaps_couples(row)


def assert_min_swaps_couples(result: int, expected: int) -> bool:
    assert result == expected
    return True
