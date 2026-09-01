def run_min_available_duration(
    solution_class: type, slots1: list[list[int]], slots2: list[list[int]], duration: int
):
    implementation = solution_class()
    return implementation.min_available_duration(slots1, slots2, duration)


def assert_min_available_duration(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
