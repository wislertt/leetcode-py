def run_outer_trees(solution_class: type, trees: list[list[int]]):
    implementation = solution_class()
    return implementation.outer_trees(trees)


def assert_outer_trees(result: list[list[int]], expected: list[list[int]]) -> bool:
    # Trees on the fence perimeter are reported in any order
    assert sorted(result) == sorted(expected)
    return True
