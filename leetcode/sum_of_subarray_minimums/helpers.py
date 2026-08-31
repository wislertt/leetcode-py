def run_sum_subarray_mins(solution_class: type, arr: list[int]):
    implementation = solution_class()
    return implementation.sum_subarray_mins(arr)


def assert_sum_subarray_mins(result: int, expected: int) -> bool:
    assert result == expected
    return True
