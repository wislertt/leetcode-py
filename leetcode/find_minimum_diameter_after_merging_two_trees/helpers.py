def run_minimum_diameter_after_merge(
    solution_class: type, edges1: list[list[int]], edges2: list[list[int]]
):
    implementation = solution_class()
    return implementation.minimum_diameter_after_merge(edges1, edges2)


def assert_minimum_diameter_after_merge(result: int, expected: int) -> bool:
    assert result == expected
    return True
