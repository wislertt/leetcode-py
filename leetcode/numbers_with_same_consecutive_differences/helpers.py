def run_nums_same_consec_diff(solution_class: type, n: int, k: int):
    implementation = solution_class()
    return implementation.nums_same_consec_diff(n, k)


def assert_nums_same_consec_diff(result: list[int], expected: list[int]) -> bool:
    assert sorted(result) == sorted(expected)
    return True
