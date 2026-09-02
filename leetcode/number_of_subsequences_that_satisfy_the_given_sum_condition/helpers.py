def run_num_subseq(solution_class: type, nums: list[int], target: int):
    implementation = solution_class()
    return implementation.num_subseq(nums, target)


def assert_num_subseq(result: int, expected: int) -> bool:
    assert result == expected
    return True
