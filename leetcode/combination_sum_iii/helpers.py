def run_combination_sum_3(solution_class: type, k: int, n: int):
    implementation = solution_class()
    return implementation.combination_sum_3(k, n)


def assert_combination_sum_3(result: list[list[int]], expected: list[list[int]]) -> bool:
    assert sorted([tuple(p) for p in result]) == sorted([tuple(p) for p in expected])
    return True
