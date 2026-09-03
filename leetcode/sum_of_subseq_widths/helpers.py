def run_sum_subseq_widths(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.sum_subseq_widths(nums)


def assert_sum_subseq_widths(result: int, expected: int) -> bool:
    assert result == expected
    return True
