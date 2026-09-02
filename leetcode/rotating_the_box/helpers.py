def run_rotate_the_box(solution_class: type, box_grid: list[list[str]]):
    import copy

    box_copy = copy.deepcopy(box_grid)
    implementation = solution_class()
    return implementation.rotate_the_box(box_copy)


def assert_rotate_the_box(result: list[list[str]], expected: list[list[str]]) -> bool:
    assert result == expected
    return True
