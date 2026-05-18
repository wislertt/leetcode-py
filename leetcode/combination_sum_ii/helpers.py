def run_combination_sum2(solution_class: type, candidates: list[int], target: int):
    implementation = solution_class()
    result = implementation.combination_sum2(candidates, target)
    return sorted([sorted(combo) for combo in result])


def assert_combination_sum2(result: list[list[int]], expected: list[list[int]]) -> bool:
    expected_sorted = sorted([sorted(combo) for combo in expected])
    assert result == expected_sorted
    return True
