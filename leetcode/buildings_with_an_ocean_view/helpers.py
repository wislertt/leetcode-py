def run_find_buildings(solution_class: type, heights: list[int]):
    implementation = solution_class()
    return implementation.find_buildings(heights)


def assert_find_buildings(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
