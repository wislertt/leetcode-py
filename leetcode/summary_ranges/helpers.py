def run_summary_ranges(solution_class: type, nums_list: list[int]):
    implementation = solution_class()
    return implementation.summary_ranges(nums_list)


def assert_summary_ranges(result: list[str], expected: list[str]) -> bool:
    assert result == expected
    return True
