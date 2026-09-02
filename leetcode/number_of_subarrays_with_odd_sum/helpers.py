def run_num_of_subarrays(solution_class: type, arr: list[int]):
    implementation = solution_class()
    return implementation.num_of_subarrays(arr)


def assert_num_of_subarrays(result: int, expected: int) -> bool:
    assert result == expected
    return True
