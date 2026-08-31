def run_max_sum_after_partitioning(solution_class: type, arr: list[int], k: int):
    implementation = solution_class()
    return implementation.max_sum_after_partitioning(arr, k)


def assert_max_sum_after_partitioning(result: int, expected: int) -> bool:
    assert result == expected
    return True
