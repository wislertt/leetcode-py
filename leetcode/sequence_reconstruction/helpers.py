def run_sequence_reconstruction(solution_class: type, nums: list[int], sequences: list[list[int]]):
    implementation = solution_class()
    return implementation.sequence_reconstruction(nums, sequences)


def assert_sequence_reconstruction(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
