def run_min_distance(
    solution_class: type,
    height: int,
    width: int,
    tree: list[int],
    squirrel: list[int],
    nuts: list[list[int]],
):
    implementation = solution_class()
    return implementation.min_distance(height, width, tree, squirrel, nuts)


def assert_min_distance(result: int, expected: int) -> bool:
    assert result == expected
    return True
