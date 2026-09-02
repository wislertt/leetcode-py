from .solution import ArrayReader


def run_guess_majority(solution_class: type, nums: list[int]):
    reader = ArrayReader(nums)
    return solution_class().guess_majority(reader)


def assert_guess_majority(result: int, expected: int, nums: list[int]) -> bool:
    # Any index of the most frequent value is valid;
    # -1 is the only valid answer on a tie
    if expected == -1:
        assert result == -1
        return True
    assert 0 <= result < len(nums)
    assert nums[result] == nums[expected]
    return True
