def run_num_of_subarrays(solution_class: type, arr: list[int], k: int, threshold: int):
    implementation = solution_class()
    return implementation.num_of_subarrays(arr, k, threshold)


def assert_num_of_subarrays(result: int, expected: int) -> bool:
    assert result == expected
    return True
