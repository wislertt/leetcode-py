def run_can_see_persons_count(solution_class: type, heights: list[int]):
    implementation = solution_class()
    return implementation.can_see_persons_count(heights)


def assert_can_see_persons_count(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
