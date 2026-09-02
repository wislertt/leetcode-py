def run_total_hamming_distance(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.total_hamming_distance(nums)


def assert_total_hamming_distance(result: int, expected: int) -> bool:
    assert result == expected
    return True
