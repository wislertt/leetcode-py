def run_peak_index_in_mountain_array(solution_class: type, arr: list[int]):
    implementation = solution_class()
    return implementation.peak_index_in_mountain_array(arr)


def assert_peak_index_in_mountain_array(result: int, expected: int) -> bool:
    assert result == expected
    return True
