def run_subarray_bitwise_ors(solution_class: type, arr: list[int]):
    implementation = solution_class()
    return implementation.subarray_bitwise_ors(arr)


def assert_subarray_bitwise_ors(result: int, expected: int) -> bool:
    assert result == expected
    return True
