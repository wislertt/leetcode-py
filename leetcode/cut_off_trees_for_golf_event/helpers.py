def run_cut_off_tree(solution_class: type, forest: list[list[int]]):
    implementation = solution_class()
    return implementation.cut_off_tree(forest)


def assert_cut_off_tree(result: int, expected: int) -> bool:
    assert result == expected
    return True
