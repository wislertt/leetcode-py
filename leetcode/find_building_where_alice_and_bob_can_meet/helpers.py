def run_leftmost_building_queries(
    solution_class: type, heights: list[int], queries: list[list[int]]
):
    implementation = solution_class()
    return implementation.leftmost_building_queries(heights, queries)


def assert_leftmost_building_queries(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
