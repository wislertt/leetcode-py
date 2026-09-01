def run_largest_combination(solution_class: type, candidates: list[int]):
    implementation = solution_class()
    return implementation.largest_combination(candidates)


def assert_largest_combination(result: int, expected: int) -> bool:
    assert result == expected
    return True
