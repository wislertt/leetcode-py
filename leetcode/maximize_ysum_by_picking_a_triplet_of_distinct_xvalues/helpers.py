def run_max_sum_distinct_triplet(solution_class: type, x: list[int], y: list[int]):
    implementation = solution_class()
    return implementation.max_sum_distinct_triplet(x, y)


def assert_max_sum_distinct_triplet(result: int, expected: int) -> bool:
    assert result == expected
    return True
