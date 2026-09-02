def run_find_least_num_of_unique_ints(solution_class: type, arr: list[int], k: int):
    implementation = solution_class()
    return implementation.find_least_num_of_unique_ints(arr, k)


def assert_find_least_num_of_unique_ints(result: int, expected: int) -> bool:
    assert result == expected
    return True
