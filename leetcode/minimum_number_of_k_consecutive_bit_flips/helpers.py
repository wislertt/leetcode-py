def run_min_k_bit_flips(solution_class: type, nums: list[int], k: int):
    implementation = solution_class()
    return implementation.min_k_bit_flips(nums, k)


def assert_min_k_bit_flips(result: int, expected: int) -> bool:
    assert result == expected
    return True
